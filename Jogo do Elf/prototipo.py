# Estou desenvolvendo o protótipo de um jogo simples de aventura chamado "A ilha do Tesouro"

# Enredo: Em um mundo mágico, você é um jovem elfo que descobre a existência de um tesouro incrível abandonado pela 
# princesa dos elfos antes de morrer. Não sabendo o valor desse tesouro, você decide ir atrás dele antes que seja tarde demais
# Você, através do personagem principal. passará por uma longa aventura, onde uma escolha errada pode levá-lo ao su fim ou lhe trazer para o seu tesouro tão aguardado

print("A Game by Pedro Caetano")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem Vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro abandonado da falecida princesa dos elfos\n. Tome cuidado com suas escolhas, se não será seu fim.") 



choice1 = input('Você\' foi parar em uma encruzilhada sem destino, para onde deseja ir? Digite "esquerda" ou "direita" \n').lower()
if choice1 == "esquerda":
  
  choice2 = input('Você\' encontrou um lago. Lá há uma ilha em um vale encantado e neste vale talvez você encontre esse tesouro. Digite "espere" para esperar por um barco. ou digite "nade" para cruzar o mar no peito" \n').lower()

if choice2 == "espere":


    choice3 = input("Você foi parar em uma ilha completamete desarmado. Há uma casa com 3 portas. A porta vermelha, a porta azul e a porta amarela. Escolha sabiamente \n \n").lower()
    if choice3 == "vermelha":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "azul":
      print("Você encontrou o tesouro perdido da Princesa dos Elfos! Parabéns!")
    elif choice3 == "amarela":
      
      print("Você entrou em uma sala cheia de feras e monstros horríveis \n. Elas eram mais fortes que você e você morreu")
    else:
      print("Você escolheu uma porta que não existe, você morreu")
  else:
    print("Você foi atacado pelo devorador de corações. Você morreu.")
else:
  print("Você caiu no buraco, você morreu")