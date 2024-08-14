import os

questions = [
    {
        'Question': 'What is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
    {
        'Question': 'What is 100/10?',
        'Options': ['4', '5', '2', '10'],
        'Answer': '10',
    },
]

question_number = 0
list_of_index = []

while True:
  print('Question: ', questions[question_number]['Question'])
  for index, options in enumerate(questions[question_number]['Options']):
    list_of_index.append(index)
    print(f'{index})', options)
  
  selected_question  = input('Select an option: ')
  
  try:
    selected_question = int(selected_question)
    if selected_question not in list_of_index:
      print('Insert number of index correct!')
      continue
  except TypeError:
    print('Insert integer!')
  except ValueError:
    print('Insert number of index correct!')
    continue
  
  list_of_options = questions[question_number]['Options']
  answer_correct = questions[question_number]['Answer']
  
  if answer_correct == list_of_options[selected_question]:
    print('You got it right!')
  else:
    print('You made a mistake!')
    
  if len(questions) - 1 == question_number:
    question_number = 0
    os.system('cls')
    continue
  question_number += 1