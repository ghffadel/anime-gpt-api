from data import get_eval_data, get_train_data, parse_input
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from os import scandir
from simpletransformers.question_answering import QuestionAnsweringModel
import torch

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = './AnimeGPT'
BEST_MODEL_DIR = f"{OUTPUT_DIR}/outputs/best_model"

def train_model ():
    torch.multiprocessing.freeze_support()

    train_data = get_train_data()
    eval_data = get_eval_data()

    train_arguments = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "use_cached_eval_features": True,
        "output_dir": f"{OUTPUT_DIR}/outputs/",
        "best_model_dir": BEST_MODEL_DIR,
        "evaluate_during_training": True,
        "max_seq_length": 128,
        "num_train_epochs": 10,
        "evaluate_during_training_steps": 1000,
        "save_model_every_epoch": False,
        "save_eval_checkpoints": False,
        "n_best_size": 8,
        "train_batch_size": 16,
        "eval_batch_size": 16,
        "learning_rate": 1e-4, 
        "weight_decay": 0.01,
        "fp16": False,
        "dropout": 0.1,
        "early_stopping_patience": 3, 
    }

    model = QuestionAnsweringModel(
        "bert",
        "bert-base-multilingual-cased",
        use_cuda = False,
        args = train_arguments
    )

    model.train_model(train_data, eval_data = eval_data)

def has_trained_model ():
    return any(scandir(f"{OUTPUT_DIR}/outputs/best_model"))

@app.route('/ask-question', methods = ['POST'])
@cross_origin()
def ask_question():
    try:
        model = QuestionAnsweringModel("bert", BEST_MODEL_DIR, use_cuda = False)

        data = request.get_json()
        question = parse_input(data["question"])
        answers, _ = model.predict(question, n_best_size = None)

        response = { "answer": answers[0] }
        return jsonify(response)

    except Exception as e:
        error_message = str(e)
        return jsonify({ "error": error_message }), 500

if __name__ == "__main__":
    if not has_trained_model():
        train_model()
    
    app.run()