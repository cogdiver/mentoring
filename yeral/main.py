import random

options = ('piedra','papel', 'tijera')
computer_wins = 0
user_wins = 0 
round = 1

combination = {
  ('piedra', 'tijera'): (1, 0),
  ('piedra', 'papel'): (0, 1),
  ('papel', 'piedra'): (1, 0),
  ('papel', 'tijera'): (0, 1),
  ('tijera', 'papel'): (1, 0),
  ('tijera', 'piedra'): (0, 1),
}

def winner(user_option, computer_option):
  if user_option == computer_option:
    print('Empate!')
    return 0, 0

  u, c = combination[(user_option, computer_option)]

  if u:
    print(f'{user_option} gana a {computer_option}')
    print('user gano!')
    return 1, 0
  else:
    print(f'{computer_option} gana a {user_option}')
    print('computer gano!')
    return 0, 1


while True:
  print('*' * 10)
  print('ROUND', round)
  print('*' * 10)
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)
    
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)

  if not user_option in options:
    print('esa opcion no es valida')
    continue

  round += 1
  u, c = winner(user_option, computer_option)
  computer_wins += c
  user_wins += u

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  if computer_wins == 2:
    print('El ganador es la computadora')
    break 

  if user_wins == 2:
    print('El ganador es el usuario')
    break 
