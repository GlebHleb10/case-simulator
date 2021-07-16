import random
import pygame

did = "Desert Eagle | Директива"
scar = "SCAR-20 | Наемникs"
stattrackvoy1 = "StatTrak™ M4A4 | Вой"
dlor = "AWP | История о драконе"


screen = pygame.display.set_mode((800, 600))
menu = pygame.image.load("Безымянный.png")
menu = pygame.transform.scale(menu, (800, 600))
loading = pygame.image.load("thumb-1920-895715.png")
loading = pygame.transform.scale(loading, (800, 600))
fon = pygame.image.load("14160044614l.jpg")
fon = pygame.transform.scale(fon, (800, 600))
chfon = pygame.image.load("1614281824_11-p-chernii-fon-kartinka-bez-risunka-13.jpg")
chfon = pygame.transform.scale(chfon, (400, 600))
case = pygame.image.load("img-YyGw2L5PVlcBNJRQ-w1370.png")
case = pygame.transform.scale(case, (260, 230))
open = pygame.image.load("ккк.jpg")
open = pygame.transform.scale(open, (150, 30))
dragonlore = pygame.image.load("image2.png")
dragonlore = pygame.transform.scale(dragonlore, (800, 600))
stena = pygame.image.load("1593698890_6-p-kirpichnii-fon-11.jpg")
stena = pygame.transform.scale(stena, (800, 600))
directiva = pygame.image.load("s802.png")
directiva = pygame.transform.scale(directiva, (600, 400))
voy = pygame.image.load("image4.png")
voy = pygame.transform.scale(voy, (600, 400))
# choise = [directiva,dragonlore]
# drop = random.choice(choise)
pygame.init()
screen.blit(menu, (0, 0))
x1 = 255
x2 = 488
y1 = 513
y2 = 547
x3 = 319
x4 = 469
y3 = 499
y4 = 528
# screen2 =pygame.display.set_mode((800,600))
pygame.display.flip()


def randomizer():
    drop = random.randint(1, 1000)
    if 1 <= drop <= 5:
        return dlor
    elif 6 <= drop <= 300:
        return did
    elif 301 <= drop <= 304:
        return stattrackvoy1
    elif 501 <= drop <= 1000:
        return scar

def start():
    fon = pygame.image.load("14160044614l.jpg")
    fon = pygame.transform.scale(fon, (800, 600))
    screen.blit(fon, (0, 0))
    screen.blit(open, (320, 500))
    pygame.display.flip()

while True:
    pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if x3 < pos[0] < x4 and y3 < pos[1] < y4:
                screen.blit(stena, (0, 0))
                x = randomizer()
                print(x)
                if x == dlor:
                    screen.blit(dragonlore, (0, 170))
                    pygame.display.flip()
                if x == did:
                    screen.blit(directiva, (150, 170))
                    pygame.display.flip()
                if x == stattrackvoy1:
                    screen.blit(voy, (0, 170))
                    pygame.display.flip()

            if x1 < pos[0] < x2 and y1 < pos[1] < y2:
                x1 = 0
                x2 = 0
                y1 = 0
                y2 = 0
                screen.blit(loading, (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)
                screen.blit(fon, (0, 0))
                screen.blit(chfon, (200, 0))
                screen.blit(case, (280, 250))
                screen.blit(open, (320, 500))
                pygame.display.flip()

# def method_name():
#     name = print("ваше имя: ")
#     try:
#         os.chdir(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}")
#     except:
#         s = input('такого пользователя нет. создать?')
#         if s == "да":
#             os.makedirs(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}")
#             os.chdir(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}")
#             file = open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\инвентарь.txt", "w", encoding='utf-8')
#             file.close()
#             file1 = open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\деньги.txt", "w", encoding='utf-8')
#             file1.write('0')
#             file1.close()
#         if s == "нет":
#             exit()
#     v = input("читкод?")
#     while True:
#
#         if v == "give$money!":
#             money = int(input())
#             file1 = open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\деньги.txt", "r", encoding='utf-8')
#             now_money = int(file1.read())
#             file1.close()
#             file1 = open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\деньги.txt", "w", encoding='utf-8')
#             b = money + now_money
#             file1.write(str(b))
#             file1.close()
#         if v == "нет":
#             pass
#         c = input("что хотите сделать?посмотреть инвентарь\посмотреть деньги\выйти ")
#
#         if c == "посмотреть инвентарь":
#             with open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\инвентарь.txt", "r",
#                       encoding='utf-8') as file:
#                 data = file.read()
#                 if data:
#                     print(data)
#                 else:
#                     print('рюкзак пуст')
#         elif c == "посмотреть деньги":
#             with open(rf"C:\Users\Глеб\Desktop\пользоваели симулятора\{name}\деньги.txt", "r",
#                       encoding='utf-8') as file:
#                 data = file.read()
#                 print(data)
#         elif c == 'выйти':
#             method_name()
#         else:
#             print('такой команды нет')
#
#
#
# method_name()


# if 1 <= drop <= 100:
# elif 6 <= drop <= 300:
#     print(did)
# elif 301 <= drop <= 500:
#     print(dib)
# elif 501 <= drop <= 1000:
#     print(scar)
# print(drop)
