from random import randint
kubik = 0
player = 1
while player <= 100:
    kubik = randint(1,6)
    for i in range(1,101,1):
        if i == player:
            print(f'[{i}] - вы здесь')
        else:
            print(f"[{i}]")
    player = kubik + player
