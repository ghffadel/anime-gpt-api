def get_train_data ():
  train_data = [
      {
          "context": "\"Naruto\" é uma série de anime e mangá japonesa criada por Masashi Kishimoto. A história gira em torno de Naruto Uzumaki, um jovem ninja que busca reconhecimento de sua vila, a Vila da Folha, enquanto enfrenta desafios, inimigos e desenvolve habilidades ninja extraordinárias. Naruto é host de Kurama, a Raposa de Nove Caudas, uma criatura lendária que foi selada em seu corpo quando ele era um bebê. Ao longo da narrativa, Naruto forma laços de amizade com outros ninjas, como Sasuke Uchiha e Sakura Haruno, sob a orientação do sensei Kakashi Hatake. A série explora temas de amizade, superação de obstáculos, e a busca pelo significado do verdadeiro heroísmo. A trama se desenrola com a ameaça de organizações poderosas, como a Akatsuki, e revelações sobre o passado de personagens importantes. O objetivo final de Naruto é se tornar o Hokage, o líder de sua vila, e proteger aqueles que ele ama. A narrativa também aborda questões mais profundas, como o ciclo de ódio e a busca pela paz em um mundo ninja repleto de conflitos. \"Naruto\" é conhecido por sua rica mitologia, personagens cativantes e cenas de luta emocionantes. A série foi um fenômeno global e teve uma continuação direta chamada \"Naruto: Shippuden\", que acompanha Naruto em sua jornada adulta.",
          "qas": [
              {
                  "id": "00001",
                  "is_impossible": False,
                  "question": "Quem é o autor de Naruto?",
                  "answers": [
                      {
                          "text": "Masashi Kishimoto",
                          "answer_start": 71,
                      },
                  ],
              },
              {
                  "id": "00002",
                  "is_impossible": False,
                  "question": "Quem é o protagonista de Naruto?",
                  "answers": [
                      {
                          "text": "Naruto Uzumaki",
                          "answer_start": 124,
                      },
                  ],
              },
              {
                  "id": "00003",
                  "is_impossible": False,
                  "question": "Qual é a vila onde Naruto mora?",
                  "answers": [
                      {
                          "text": "Vila de Folha",
                          "answer_start": 149,
                      },
                  ],
              },
              {
                  "id": "00004",
                  "is_impossible": False,
                  "question": "O que é Kurama?",
                  "answers": [
                      {
                          "text": "A Raposa de Nove Caudas, uma criatura lendária que foi selada no corpo de Naruto quando ele era um bebê.",
                          "answer_start": 170,
                      },
                  ],
              },
              {
                  "id": "00005",
                  "is_impossible": False,
                  "question": "Com quem Naruto forma laços de amizade?",
                  "answers": [
                      {
                          "text": "Com outros ninjas, como Sasuke Uchiha e Sakura Haruno.",
                          "answer_start": 245,
                      },
                  ],
              },
              {
                  "id": "00006",
                  "is_impossible": False,
                  "question": "Quem é o sensei de Naruto?",
                  "answers": [
                      {
                          "text": "Kakashi Hatake.",
                          "answer_start": 311,
                      },
                  ],
              },
              {
                  "id": "00007",
                  "is_impossible": False,
                  "question": "Como a trama de Naruto se desenrola?",
                  "answers": [
                      {
                          "text": "A trama se desenrola com a ameaça de organizações poderosas, como a Akatsuki, e revelações sobre o passado de personagens importantes.",
                          "answer_start": 346,
                      },
                  ],
              },
              {
                  "id": "00008",
                  "is_impossible": False,
                  "question": "Qual é o objetivo final de Naruto?",
                  "answers": [
                      {
                          "text": "O objetivo final de Naruto é se tornar o Hokage, o líder de sua vila, e proteger aqueles que ele ama.",
                          "answer_start": 458,
                      },
                  ],
              },
              {
                  "id": "00009",
                  "is_impossible": False,
                  "question": "Qual é a continuação de \"Naruto\"?",
                  "answers": [
                      {
                          "text": "A série foi um fenômeno global e teve uma continuação direta chamada \"Naruto: Shippuden\", que acompanha Naruto em sua jornada adulta.",
                          "answer_start": 548,
                      },
                  ],
              },
              {
                  "id": "00010",
                  "is_impossible": True,
                  "question": "Quem é Itachi Uchiha?",
                  "answers": [],
              },
          ]
      },
  ]
  train_data += [
      {
          "context": "\"One Piece\" é uma série de anime e mangá japonesa criada por Eiichiro Oda. A história gira em torno de Monkey D. Luffy, um jovem pirata com o objetivo de encontrar o tesouro supremo conhecido como One Piece e se tornar o Rei dos Piratas. Luffy adquire poderes de uma fruta do diabo, a Gomu Gomu no Mi, que o transforma em um homem borracha. Ao longo de sua jornada, ele forma uma tripulação chamada Chapéu de Palha, composta por membros leais e habilidosos. A série explora temas de amizade, liberdade, aventura e justiça, enquanto os Chapéus de Palha enfrentam desafios, inimigos poderosos e descobrem segredos sobre o mundo. A narrativa também aborda a busca pelos Poneglyphs, artefatos que levam à localização de One Piece, e a existência dos Yonkou, os quatro imperadores dos mares. \"One Piece\" é conhecido por sua vasta mitologia, personagens carismáticos e reviravoltas emocionantes.",
          "qas": [
              {
                  "id": "00011",
                  "is_impossible": False,
                  "question": "Quem é o autor de One Piece?",
                  "answers": [
                      {
                          "text": "Eiichiro Oda",
                          "answer_start": 61
                      }
                  ]
              },
              {
                  "id": "00012",
                  "is_impossible": False,
                  "question": "Quem é o protagonista de One Piece?",
                  "answers": [
                      {
                          "text": "Monkey D. Luffy",
                          "answer_start": 103
                      }
                  ]
              },
              {
                  "id": "00013",
                  "is_impossible": False,
                  "question": "Qual é o objetivo de Luffy em One Piece?",
                  "answers": [
                      {
                          "text": "Encontrar o tesouro supremo conhecido como One Piece e se tornar o Rei dos Piratas",
                          "answer_start": 154
                      }
                  ]
              },
              {
                  "id": "00014",
                  "is_impossible": False,
                  "question": "Quais poderes Luffy adquire?",
                  "answers": [
                      {
                          "text": "Luffy adquire poderes de uma fruta do diabo, a Gomu Gomu no Mi, que o transforma em um homem borracha",
                          "answer_start": 238
                      }
                  ]
              },
              {
                  "id": "00015",
                  "is_impossible": False,
                  "question": "Como é chamada a tripulação de Luffy?",
                  "answers": [
                      {
                          "text": "Chapéu de Palha",
                          "answer_start": 399
                      }
                  ]
              },
              {
                  "id": "00016",
                  "is_impossible": False,
                  "question": "O que os Chapéus de Palha procuram em One Piece?",
                  "answers": [
                      {
                          "text": "Eles procuram pelos Poneglyphs, artefatos que levam à localização de One Piece",
                          "answer_start": 667
                      }
                  ]
              },
              {
                  "id": "00017",
                  "is_impossible": False,
                  "question": "Quem são os Yonkou em One Piece?",
                  "answers": [
                      {
                          "text": "Os Yonkou são os quatro imperadores dos mares",
                          "answer_start": 746
                      }
                  ]
              },
              {
                  "id": "00018",
                  "is_impossible": False,
                  "question": "Quais temas a série explora?",
                  "answers": [
                      {
                          "text": "A série explora temas de amizade, liberdade, aventura e justiça",
                          "answer_start": 458
                      }
                  ]
              },
              {
                  "id": "00019",
                  "is_impossible": False,
                  "question": "Por que One Piece é conhecido?",
                  "answers": [
                      {
                          "text": "\"One Piece\" é conhecido por sua vasta mitologia, personagens carismáticos e reviravoltas emocionantes.",
                          "answer_start": 787
                      }
                  ]
              },
              {
                  "id": "00020",
                  "is_impossible": True,
                  "question": "Qual é a habilidade especial da fruta do diabo de Buggy em One Piece?",
                  "answers": []
              }
          ]
      },
  ]
  
  return train_data

def get_eval_data ():
  eval_data = [
      {
          "context": "\"Naruto Shippuden\" é a continuação direta da série original \"Naruto\". A narrativa se desenrola com Naruto Uzumaki retornando à Vila da Folha após um treinamento rigoroso de dois anos. O enredo aprofunda os desafios enfrentados por Naruto e seus amigos enquanto confrontam ameaças ainda mais formidáveis, como a Akatsuki e inimigos poderosos. Ao longo da série, os personagens amadurecem, revelações impactantes sobre o passado são desvendadas, e a busca de Naruto pelo reconhecimento e o significado da verdadeira força atinge novos patamares. \"Naruto Shippuden\" é marcado por intensas batalhas, desenvolvimento de personagens e exploração de temas profundos, culminando na realização dos ideais do protagonista e na busca pela paz em um mundo ninja tumultuado.",
          "qas": [
              {
                  "id": "00001",
                  "is_impossible": False,
                  "question": "Para onde Naruto Uzumaki retornou?",
                  "answers": [
                      {
                          "text": "À Vila da Folha",
                          "answer_start": 95,
                      },
                  ],
              },
              {
                  "id": "00002",
                  "is_impossible": False,
                  "question": "Quanto tempo durou seu treinamento rigoroso?",
                  "answers": [
                      {
                          "text": "Dois anos",
                          "answer_start": 111,
                      },
                  ],
              },
              {
                  "id": "00003",
                  "is_impossible": False,
                  "question": "Pelo quê Naruto Shippuden é marcado?",
                  "answers": [
                      {
                          "text": "É marcado por intensas batalhas, desenvolvimento de personagens e exploração de temas profundos, culminando na realização dos ideais do protagonista e na busca pela paz em um mundo ninja tumultuado.",
                          "answer_start": 214,
                      },
                  ],
              },
          ]
      },
  ]

  eval_data += [
      {
          "context": "\"One Piece\" segue a jornada de Monkey D. Luffy em busca do tesouro supremo, conhecido como One Piece. Ele forma uma tripulação pirata diversificada e enfrenta desafios, incluindo outros piratas e o Governo Mundial. O mundo é vasto e cheio de ilhas perigosas. Luffy possui a habilidade única de esticar seu corpo como borracha após comer uma fruta do diabo. A narrativa explora amizade, aventura e a busca pelo sonho.",
          "qas": [
              {
                  "id": "00004",
                  "is_impossible": False,
                  "question": "Quem é o protagonista de One Piece?",
                  "answers": [
                      {
                          "text": "Monkey D. Luffy",
                          "answer_start": 39,
                      },
                  ],
              },
              {
                  "id": "00005",
                  "is_impossible": False,
                  "question": "O que Luffy procura?",
                  "answers": [
                      {
                          "text": "O tesouro supremo, conhecido como One Piece",
                          "answer_start": 65,
                      },
                  ],
              },
              {
                  "id": "00006",
                  "is_impossible": False,
                  "question": "Quais são os poderes especiais de Luffy?",
                  "answers": [
                      {
                          "text": "Esticar seu corpo como borracha após comer uma fruta do diabo",
                          "answer_start": 156,
                      },
                  ],
              },
          ]
      },
  ]

  return eval_data

def parse_input (question):
  naruto_context = "\"Naruto\" é uma série de anime e mangá japonesa criada por Masashi Kishimoto. A história gira em torno de Naruto Uzumaki, um jovem ninja que busca reconhecimento de sua vila, a Vila da Folha, enquanto enfrenta desafios, inimigos e desenvolve habilidades ninja extraordinárias. Naruto é host de Kurama, a Raposa de Nove Caudas, uma criatura lendária que foi selada em seu corpo quando ele era um bebê. Ao longo da narrativa, Naruto forma laços de amizade com outros ninjas, como Sasuke Uchiha e Sakura Haruno, sob a orientação do sensei Kakashi Hatake. A série explora temas de amizade, superação de obstáculos, e a busca pelo significado do verdadeiro heroísmo. A trama se desenrola com a ameaça de organizações poderosas, como a Akatsuki, e revelações sobre o passado de personagens importantes. O objetivo final de Naruto é se tornar o Hokage, o líder de sua vila, e proteger aqueles que ele ama. A narrativa também aborda questões mais profundas, como o ciclo de ódio e a busca pela paz em um mundo ninja repleto de conflitos. \"Naruto\" é conhecido por sua rica mitologia, personagens cativantes e cenas de luta emocionantes. A série foi um fenômeno global e teve uma continuação direta chamada \"Naruto: Shippuden\", que acompanha Naruto em sua jornada adulta."
  one_piece_context = "\"One Piece\" é uma série de anime e mangá japonesa criada por Eiichiro Oda. A história gira em torno de Monkey D. Luffy, um jovem pirata com o objetivo de encontrar o tesouro supremo conhecido como One Piece e se tornar o Rei dos Piratas. Luffy adquire poderes de uma fruta do diabo, a Gomu Gomu no Mi, que o transforma em um homem borracha. Ao longo de sua jornada, ele forma uma tripulação chamada Chapéu de Palha, composta por membros leais e habilidosos. A série explora temas de amizade, liberdade, aventura e justiça, enquanto os Chapéus de Palha enfrentam desafios, inimigos poderosos e descobrem segredos sobre o mundo. A narrativa também aborda a busca pelos Poneglyphs, artefatos que levam à localização de One Piece, e a existência dos Yonkou, os quatro imperadores dos mares. \"One Piece\" é conhecido por sua vasta mitologia, personagens carismáticos e reviravoltas emocionantes."
  naruto_count = one_piece_count = 0

  for word in question.split(" "):
    if word in naruto_context:
      naruto_count += 1

    if word in one_piece_context:
      one_piece_count += 1

  return [
    {
      "context": naruto_context if naruto_count > one_piece_count else one_piece_context,
      "qas": [
        {
          "question": question,
          "id": "0",
        }
      ],
    },
  ]