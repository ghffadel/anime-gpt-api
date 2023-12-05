from data import get_eval_data, get_train_data, parse_input
from simpletransformers.question_answering import QuestionAnsweringModel
import torch

OUTPUT_DIR = './AnimeGPT'

train_data = get_train_data()
eval_data = get_eval_data()

train_arguments = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "use_cached_eval_features": True,
    "output_dir": f"{OUTPUT_DIR}/outputs/",
    "best_model_dir": f"{OUTPUT_DIR}/outputs/best_model",
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

if __name__ == "__main__":
    torch.multiprocessing.freeze_support()

    model = QuestionAnsweringModel(
        "bert",
        "bert-base-multilingual-cased",
        use_cuda = False,
        args = train_arguments
    )

    model.train_model(train_data, eval_data = eval_data)

    print("\nFinished training!\n")

    while True:
        question = parse_input(input())
        answers, probabilities = model.predict(question, n_best_size = None)
        print(answers)
