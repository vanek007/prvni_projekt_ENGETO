
import pygame
import random


pygame.init()

sirka=500
vyska=400

dis=pygame.display.set_mode((sirka,vyska))
x,y=sirka/2,vyska/2

hodinky=pygame.time.Clock()
had=[]
delka_hada=1
delta_x,delta_y=0,0
konec_hry=False
jidlo_pozice=(
                round(random.randrange(0,sirka-10)/10.0)*10.0,
                round(random.randrange(0,vyska-10)/10.0)*10.0
)
while not konec_hry:
    dis.fill([0,0,0])
    for event in pygame.event.get() :
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                delta_x=-10
                delta_y=0
            elif event.key == pygame.K_RIGHT:
                delta_x = 10
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -10
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = 10

    x+=delta_x
    y+=delta_y


    if x>= sirka or x<=0 or y>=vyska or y<=0:
        print("Konec hry")
        konec_hry=True

    hlava=(x,y)
    had.append(hlava)


    for pozice in had[:-1]:
        pygame.draw.rect(dis,[0,255,0],[pozice[0],pozice[1],10,10])
    pygame.draw.rect(dis, [0, 0, 255], [jidlo_pozice[0], jidlo_pozice[1], 10, 10])
    pygame.display.update()

    if hlava== jidlo_pozice:
        jidlo_pozice = (
            round(random.randrange(0, sirka - 10) / 10.0) * 10.0,
            round(random.randrange(0, vyska - 10) / 10.0) * 10.0
        )
        delka_hada+=1
        print(f"delka haha{delka_hada}")
        print(f"len(had){len(had)}")
    if len(had) > delka_hada:
        del had[0]

    for pozice in had[:-1]:
        if pozice == hlava:
            konec_hry = True
    hodinky.tick(5)

