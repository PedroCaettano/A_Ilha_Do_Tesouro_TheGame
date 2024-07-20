import random
import time

# Função para imprimir mensagens de forma dramática
def print_dramatic(text):
    print("\n" + "=" * 50)
    print(text)
    print("=" * 50 + "\n")
    time.sleep(2)  # Espera para dar um efeito dramático

# Função para gerar um número aleatório entre 1 e 20
def roll_d20():
    return random.randint(1, 20)

# Função para o sistema de luta
def combat():
    print("Escolha seu ataque: A, B ou C")
    attack = input("Digite sua escolha: ").lower()
    enemy_attack = random.choice(["a", "b", "c"])
    if attack == enemy_attack:
        return "Empate! Ambos se defendem."
    elif (attack == "a" and enemy_attack == "c") or (attack == "b" and enemy_attack == "a") or (attack == "c" and enemy_attack == "b"):
        return "Você venceu o combate!"
    else:
        return "Você foi derrotado pelo inimigo..."

# Função para combate alternativo com a Ocarina
def ocarina_combat():
    print("Você pode tocar uma das 3 músicas para tentar conquistar seus adversários:")
    songs = ["Vale dos Chaguri", "Declaração além do tempo", "Sinfonia da Noite"]
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")
    song_choice = int(input("Digite o número da música que deseja tocar: ")) - 1
    effectiveness = roll_d20()
    if effectiveness > 15:
        return f"Você tocou {songs[song_choice]} e seus adversários foram conquistados!"
    elif effectiveness > 10:
        return f"Você tocou {songs[song_choice]} e conseguiu fugir dos adversários!"
    else:
        return f"Você tocou {songs[song_choice]}, mas não teve efeito e seus adversários atacaram."

# Função para utilizar a Ocarina fora do combate
def use_ocarina():
    songs = ["Vale dos Chaguri", "Declaração além do tempo", "Sinfonia da Noite"]
    print(f"Você toca a Ocarina e seus inimigos ficam encantados e dançam ao som de {random.choice(songs)}.")



# Introdução e créditos
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

# Início do jogo
print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro abandonado pela falecida Princesa dos Elfos.")
print("Tome cuidado com suas escolhas, pois elas podem determinar seu destino.\n")

# Primeira escolha - O começo de sua jornada
choice1 = input('Você está em uma encruzilhada sem destino. Para onde deseja ir? Digite "esquerda" ou "direita": ').lower()
if choice1 == "esquerda":
    # Segunda escolha - Aqui o seu destino começa!
    choice2 = input('Você encontrou um lago. Há uma ilha em um vale encantado onde pode estar o tesouro. Digite "espere" para esperar por um barco, ou "nade" para cruzar a nado: ').lower()
    if choice2 == "espere":
        print_dramatic("Você chegou à ilha. Agora enfrente um desafio!")

        # Terceira escolha - Implementando nova dinâmica com números aleatórios
        print("Você encontrou uma casa com 3 portas: vermelha, azul e amarela.")
        print("Escolha sabiamente...\n")
        
        door_colors = ["vermelha", "azul", "amarela"]
        door_color = random.choice(door_colors)
        choice3 = input(f"Qual porta você escolhe? {', '.join(door_colors)}: ").lower()

        if choice3 == door_color:
            if choice3 == "vermelha":
                print_dramatic("Você entrou em uma sala cheia de rubis brilhantes. Você encontrou um item valioso!")
                print("Ao sair da sala, você avista uma sombra escura se movendo na floresta...")
                time.sleep(1)
                print("Você decide seguir a sombra misteriosa.\n")
                print_dramatic("Você se depara com um monstro guardião! Ele ataca com fúria.")
                
                # Combate contra o monstro
                print("Escolha entre 'lutar' ou 'ocarina' para tentar usar a Ocarina:")
                combat_choice = input("Digite sua escolha: ").lower()
                if combat_choice == "lutar":
                    combat_result = combat()
                elif combat_choice == "ocarina":
                    combat_result = ocarina_combat()
                else:
                    combat_result = "Você hesitou e foi atacado. Game Over."

                print_dramatic(combat_result)
                if "derrotado" in combat_result:
                    print("Game Over.")
                    exit()

            elif choice3 == "azul":
                print_dramatic("Você encontrou uma passagem secreta para um túnel cheio de riquezas!")
                print("Dentro do túnel, você ouve um rugido profundo vindo de uma câmara adiante...")
                time.sleep(1)
                print("Você decide avançar para investigar.\n")
                print_dramatic("Você encontra um dragão adormecido guardando o tesouro!")

                # Interagir com o dragão
                dragon_choice = input('Você vai tentar "roubar" o tesouro ou "conversar" com o dragão? ').lower()

                if dragon_choice == "roubar":
                    print_dramatic("Você tenta roubar o tesouro, mas o dragão acorda e ataca!")
                    print("Game Over.")
                    exit()
                else:
                    print_dramatic("Você conversa com o dragão e descobre que ele está guardando o tesouro da princesa desaparecida.")

            elif choice3 == "amarela":
                print_dramatic("Você encontrou uma armadilha, mas conseguiu escapar por pouco!")
                print("Ao escapar, você encontra um estranho dispositivo mágico em meio às ruínas da armadilha.")
                time.sleep(1)
                print("Você decide investigar o dispositivo.\n")
                print_dramatic("O dispositivo teleporta você para um local misterioso.")

                # Desafio no local misterioso
                print("Você está em uma caverna mágica. Há três portas à sua frente.")
                choice4 = input('Escolha uma porta para prosseguir: "ouro", "prata" ou "bronze"? ').lower()

                if choice4 == "ouro":
                    print_dramatic("Você encontrou uma câmara cheia de ouro reluzente!")
                elif choice4 == "prata":
                    print_dramatic("Você encontra um espelho mágico que revela segredos ocultos.")
                elif choice4 == "bronze":
                    print_dramatic("Você enfrenta um desafio de labirinto mágico, mas consegue escapar ileso.")
                else:
                    print_dramatic("Você escolhe uma porta errada e cai em um abismo sem fim... Game Over.")
                    exit()
            else:
                print_dramatic("Você escolheu uma porta que não existe. Game Over.")
                exit()

        else:
            print_dramatic("Você foi atacado por armadilhas mágicas. Cuidado na próxima vez!")
            exit()

    elif choice2 == "nade":
        print_dramatic("Você nadou até a ilha, mas foi atacado por criaturas marinhas. Game Over.")
        exit()

elif choice1 == "direita":
    # Novo desafio adicionado - Escolha entre portais mágicos
    print_dramatic("Você encontrou uma clareira com três portais mágicos: verde, roxo e dourado.")
    print("Cada portal leva a um destino desconhecido...\n")
    
    portal_colors = ["verde", "roxo", "dourado"]
    portal_choice = input(f"Qual portal você escolhe? {', '.join(portal_colors)}: ").lower()

    if portal_choice == "verde":
        print_dramatic("Você foi transportado para uma floresta mágica cheia de criaturas encantadas!")
        print("Na floresta, você encontra uma fada que oferece ajuda para encontrar o tesouro.")
        
        # Novo aliado adicionado
        choice_fairy = input('Você aceita a ajuda da fada? Digite "sim" ou "não": ').lower()
        
        if choice_fairy == "sim":
            print_dramatic("A fada guia você até um campo onde está escondido o tesouro da Princesa dos Elfos!")
        else:
            print_dramatic("Você recusa a ajuda da fada e fica perdido na floresta. Game Over.")
            exit()

    elif portal_choice == "roxo":
        print_dramatic("Você foi transportado para um castelo sombrio cheio de enigmas e desafios!")
        print("Dentro do castelo, você encontra uma biblioteca mágica com um livro antigo.")
        
        # Desafio de resolver enigmas
        print("O livro contém um enigma. Resolva o enigma para encontrar o tesouro.")
        enigma = input('Eu sou leve como uma pena, mas ninguém pode me segurar por muito tempo. O que sou eu? ').lower()
        
        if enigma == "respiração":
            print_dramatic("Você resolveu o enigma e o livro revela a localização do tesouro!")
        else:
            print_dramatic("Você não conseguiu resolver o enigma e fica preso no castelo. Game Over.")
            exit()

    elif portal_choice == "dourado":
        print_dramatic("Você foi transportado para um reino celestial cheio de luz e harmonia!")
        print("No reino, você encontra um sábio ancião que oferece um desafio final para encontrar o tesouro.")
        
        # Desafio final - Luta contra o guardião do tesouro
        print("Você deve enfrentar o guardião celestial do tesouro.")
        print("Escolha entre 'lutar' ou 'ocarina' para tentar usar a Ocarina:")
        combat_choice = input("Digite sua escolha: ").lower()
        if combat_choice == "lutar":
            combat_result = combat()
        elif combat_choice == "ocarina":
            combat_result = ocarina_combat()
        else:
            combat_result = "Você hesitou e foi atacado. Game Over."

        print_dramatic(combat_result)
        if "derrotado" in combat_result:
            print("Game Over.")
            exit()

    else:
        print_dramatic("Você escolheu um portal inexistente e foi transportado para um vazio infinito. Game Over.")
        exit()

else:
    print_dramatic("Você não tomou uma decisão e foi capturado por piratas. Game Over.")
    exit()

# Final do jogo - Parabéns!
print_dramatic("Parabéns! Você encontrou o tesouro da Princesa dos Elfos e completou sua missão com sucesso!")
print_dramatic("Mas ao abrir o baú do tesouro, você encontra um diário revelando que a Princesa dos Elfos não morreu.")
print_dramatic("Você descobre que a princesa está viva em um reino distante e que muitos segredos ainda o aguardam!")
print("Obrigado por jogar 'A Ilha do Tesouro'!")
