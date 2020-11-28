from classes.game import person, bcolors
from random import randint

magic = [{'name': 'Fire', 'cost': 15, 'dmg': 180},
         {'name': 'Thunder', 'cost': 20, 'dmg': 240},
         {'name': 'Blizzard', 'cost': 15, 'dmg': 180},
         {'name': 'Heal', 'cost': 15, 'dmg': 250},
         {'name': 'Taunt', 'cost': 0, 'dmg': 0}]

magic1=[{'name': 'Stun','dmg':200},
        {'name':'Ice Blast','dmg':150},
        {'name':'Bite','dmg':100}]

items1 = [{'item':'potion','description':'Heals 300HP','value':300,'quantity':2,'cost':100},
       {'item':'megapotion','description':'Heals 450HP','value':450,'quantity':1,'cost':250},
       {'item':'maxpotion','description':'Heals 700 HP','value':700, 'quantity':0,'cost':500},
       {'item':'elixir','description':'Restores 20MP','value': 20,'quantity': 2, 'cost':400 },
       {'item':'hyper elixir','description':'Restores 40MP','value': 40 ,'quantity':0},
       {'item':'nuke','description':'Dealt 600 Damage','value': 600,'quantity':0,'cost':500}]

player1 = person("Franklin: ",850, 50, 150, 80, magic, items1, 100)
player2 = person("Micheal:  ",950, 50, 180, 40, magic, items1, 100)
player3 = person("Trevor:   ",950, 50, 200, 60, magic, items1, 100)

enemy1 = person('Martin',1200, 30, 160, 25, magic1, 0, 250)
enemy2 = person('Devin ',1600, 30, 180, 50, magic1, 0, 450)
enemy3 = person('Lester',600, 30, 100, 20, magic1, 0, 100)

players=[player1,player2,player3]
enemies=[enemy1,enemy2,enemy3]
print("\n")
print(f"{bcolors.OKGREEN}  ,ad8888ba,   888888888888         db         {bcolors.ENDC}88{bcolors.FAIL}     88888888ba   88888888ba     ,ad8888ba, {bcolors.ENDC}")
print(f"{bcolors.OKGREEN} d8'    ` '8b       88             d88b        {bcolors.ENDC}88 {bcolors.FAIL}    88      '8b  88      '8b   d8'    `8b {bcolors.ENDC}")
print(f"{bcolors.OKGREEN}88                  88           d8'  `8b      {bcolors.ENDC}88   {bcolors.FAIL}  88aaaaaa8P'  88aaaaaa8P'  88             {bcolors.ENDC} ")
print(f"{bcolors.OKGREEN}88      88888       88          d8YaaaaY8b     {bcolors.ENDC}88{bcolors.FAIL}     88''''''88'  88'          88      88888{bcolors.ENDC} ")
print(f"{bcolors.OKGREEN}Y8a.     .a88       88         d8       `8b    {bcolors.ENDC}88  {bcolors.FAIL}   88     `8b   88            Y8a.    .a88 {bcolors.ENDC}")
print(f"{bcolors.OKGREEN}  Y888888P'         88        d8          8b   {bcolors.ENDC}88  {bcolors.FAIL}   88       8b  88              'Y88888P{bcolors.ENDC}")

print(f"                                                            {bcolors.OKBLUE}              _                     _             _____       _ {bcolors.ENDC}")
print(f"                                                      {bcolors.OKBLUE}             __ _  | |__     ___    ___  | |_          |___ /    __| |{bcolors.ENDC}")
print(f"                                                           {bcolors.OKBLUE}       / _` | | '_ \   / _ \  / __| | __|           |_ \   / _` |{bcolors.ENDC}")
print(f"                                                       {bcolors.OKBLUE}          | (_| | | | | | | (_) | \__ \ | |_           ___) | | (_| |{bcolors.ENDC}")
print(f"                                                         {bcolors.OKBLUE}         \__, | |_| |_|  \___/  |___/  \__|  _____  |____/   \__,_|{bcolors.ENDC}")
print(f"                                                               {bcolors.OKBLUE}   |___/                              |_____|                {bcolors.ENDC}")

x=int(input(("Press 0 to start ")))
if x== 0:
    running = True
print(bcolors.FAIL+"ENEMIES APPEARED!!"+bcolors.ENDC)
while running:
    print("====================================================================")
    print("Name               HP                                    MP")
    for player in players:
        player_blocks = ""
        no = int(player.hp/45)
        player_blocks+='█'*no
        while no<int(player.maxhp/45):
            player_blocks+=' '*(int(player.maxhp/45)-no)
            break
        mp_blocks=""
        nos=int(player.mp/5)
        mp_blocks+='█'*nos
        while nos<int(player.maxmp/5):
            mp_blocks += ' '*(int(player.maxmp/5)-nos)
            break
        spaces = ''
        no_of_spaces = 10
        spaces += ' '*10
        if no < 23:
            spaces += ' ' *(23-no)
            if len(spaces) >13:
                spaces = 13*' '
        print(f"                  {'_'*int(player.maxhp/45)}  {spaces}{' '*7}{'_'*int(player.maxmp/5)}")
        print(
            f"{player.name}       |{bcolors.OKGREEN}{player_blocks}{bcolors.ENDC}|{player.hp}/{player.maxhp}{spaces}|{bcolors.OKBLUE}{mp_blocks}{bcolors.ENDC}|{player.mp}/{player.maxmp}")
    print("\n")
    print("Name            HP")
    for enemy in enemies:
        enemy_blocks=""
        no2=int(enemy.hp/40)
        enemy_blocks+='█'*no2
        while no2<int(enemy.maxhp/40):
            enemy_blocks+=' '*(int(enemy.maxhp/40)-no2)
            break
        print(f"                 {'_'*int(enemy.maxhp/40)}")
        print(f"{enemy.name}:         |{bcolors.FAIL}{enemy_blocks}{bcolors.ENDC}|{enemy.hp}/{enemy.maxhp}")
    for player in players:
        print(f"{bcolors.OKBLUE}   What would you do?{bcolors.ENDC}")
        player.choose()
        choice = int(input(f"{bcolors.OKBLUE}    Choose what will you do: {bcolors.ENDC}"))
        print(f"   {player.name} choose to use {player1.choice[choice-1]}")
        if choice == 1:
            print("   Whom you want to Attack?")
            print(f"     1: {enemy1.name}")
            print(f"     2: {enemy2.name}")
            print(f"     3: {enemy3.name}")
            enemy_choice=int(input("   Choose the enemy: "))
            dmg = player.attack()
            print(f"You did {dmg} damage to {enemies[enemy_choice-1].name}")
            print(f"{enemies[enemy_choice-1].name} Has {enemies[enemy_choice-1].reduce_hp(dmg)} HP")
        elif choice == 2:
            player1.choose_magic()
            choice2 = int(input("What will you use? "))
            if player.get_mp() >= player.magic[choice2-1]['cost']:
                print(f"You chose {magic[choice2-1]['name']}")
                print("   Whom you want to Attack?")
                print(f"     1: {enemy1.name}")
                print(f"     2: {enemy2.name}")
                print(f"     3: {enemy3.name}")
                enemy_choice = int(input("   Choose the enemy: "))
                if magic[choice2-1]['name'] == 'Heal':
                    player.reduce_mp(choice2 - 1)
                    player.hp += magic[choice2-1]['dmg']
                    print(f"Your HP increased by {bcolors.OKGREEN}{magic[choice2-1]['dmg']}{bcolors.ENDC}")
                    if player.hp >= player.maxhp:
                        player.hp = player.maxhp
                else:
                    dmg2 = player.use_magic(choice2-1)
                    player.reduce_mp(choice2-1)
                    print(f"You did {dmg2} damage to {enemies[enemy_choice-1].name}")
                    print(f"Enemy Has {enemies[enemy_choice-1].reduce_hp(dmg2)} HP")
                    for enemy in enemies:
                        if enemy.hp <= 0:
                            enemy.hp = 0
            else:
                print(bcolors.OKBLUE+"You don't have enough MP"+bcolors.ENDC)
                print(f"Your current MP is {player.get_mp()}")
                continue
        elif choice == 3:
            print(bcolors.OKBLUE + "Choose Item: " + bcolors.ENDC)
            player.choose_items()
            choice3 = int(input("Choose an item to use: "))
            if choice3 == 1 or choice3 == 2 or choice3 == 3:
                player.hp += player.items[choice3-1]['value']
                print(f"HP increased by{bcolors.OKGREEN} {player.items[choice3-1]['value']}{bcolors.ENDC}")
                if player.hp >= player.maxhp:
                    player.hp = player.maxhp
            elif choice3 == 4 or choice3 == 5:
                player.mp += player.items[choice3-1]['value']
                print(f"MP increased by{bcolors.OKBLUE} {player.items[choice3 - 1]['value']}{bcolors.ENDC}")
            elif choice3 == 6:
                print("   Whom you want to Attack?")
                print(f"     1: {enemy1.name}")
                print(f"     2: {enemy2.name}")
                print(f"     3: {enemy3.name}")
                enemy_choice = int(input("   Choose the enemy: "))
                enemies[enemy_choice-1].hp -= player.items[choice3-1]['value']
                print(f"{enemies[enemy_choice-1].name}'s HP decreased by{bcolors.FAIL} {player.items[choice3 - 1]['value']}{bcolors.ENDC}")
                for enemy in enemies:
                    if enemy.hp <= 0:
                        enemy.hp = 0
    print("Enemies Attacked")
    for enemy in enemies:
        if enemy.hp<enemy.maxhp*0.3:
            if enemy.mp>20:
                print(f"{enemy.name} used heal")
                enemy.hp+=250
                enemy.mp-=20
        else:
            style=randint(0,1)
            if style==0:
                dmg1 = enemy.attack()
                enemy_attacked=randint(0,2)
                print(f"{enemy.name} did {dmg1} damage to {players[enemy_attacked].name}")
                players[enemy_attacked].hp-=dmg1
            else:
                magic_style=randint(0,2)
                dmg2=enemy.magic[magic_style]['dmg']
                enemy_attacked = randint(0, 2)
                players[enemy_attacked].hp -= dmg2
                print(f"{enemy.name} did {dmg2} damage to {players[enemy_attacked].name} using {enemy.magic[magic_style]['name']}")
        if player1.hp<0:
            player1.hp=0
        if player2.hp<0:
            player2.hp=0
        if player3.hp<0:
            player3.hp=0
        if enemy.hp<=0:
            enemy.hp=0
    if player1.hp == 0 and player2.hp==0 and player3.hp==0:
        print(bcolors.FAIL+"You have been defeated"+bcolors.ENDC)
        running = False
    elif enemy1.hp == 0 and enemy2.hp == 0 and enemy3.hp == 0:
        print(bcolors.OKGREEN+"You've killed the enemy"+bcolors.ENDC)
        running = False
        print(bcolors.OKGREEN + "You received 50HP, 15MP, 30coins")
        for player in players:
            player.hp += 50
            player.mp += 15
            player.coins += 30
            print(bcolors.WARNING + player.name," Have", player.coins, 'coins' + bcolors.ENDC)
