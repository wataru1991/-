import pygame
import sys
import random
from pygame.locals import *
import time

# 画像の読み込み
img_op = pygame.image.load("image_gl/スタート.png")
img_main = pygame.image.load("image_gl/問題.png")
img_choice = pygame.image.load("image_gl/選択.png")
img_yes = pygame.image.load("image_gl/正解.png")
img_no = pygame.image.load("image_gl/不正解.png")
img_ed = pygame.image.load("image_gl/正解発表.png")

# SEを読み込む変数
se_pato = None
se_heri = None
se_kyu = None
se_syo = None
se_densya = None
se_yes = None
se_no = None
se_yes1 = None
se_no2 = None
se_op = None

idx = 0
score = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0


def sound1():
    se_heri.play()
def sound2():
    se_pato.play()
def sound3():
    se_kyu.play()
def sound4():
    se_syo.play()
def sound5():
    se_densya.play()

    
def main(): # メインループ
    global idx,q1,q2,q3,q4,q5,score
    global se_pato, se_heri, se_kyu, se_syo, se_densya, se_yes, se_no,se_yes1,se_no2,se_op

    pygame.init()
    pygame.display.set_caption("音当てゲーム")
    screen =    pygame.display.set_mode((600, 600))
    clock =     pygame.time.Clock()
    fnt = pygame.font.SysFont("hg正楷書体pro", 30)
    fnt2 = pygame.font.SysFont("hg正楷書体pro", 35)
    fnt3 = pygame.font.SysFont("hg正楷書体pro", 50)
    se_pato =   pygame.mixer.Sound("sound_gl/パトカー.mp3")
    se_heri =   pygame.mixer.Sound("sound_gl/ヘリコプター.mp3")
    se_kyu =    pygame.mixer.Sound("sound_gl/救急車.mp3")
    se_syo =    pygame.mixer.Sound("sound_gl/消防車.mp3")
    se_densya = pygame.mixer.Sound("sound_gl/電車.mp3")
    se_yes =    pygame.mixer.Sound("sound_gl/正解.mp3")
    se_no =     pygame.mixer.Sound("sound_gl/不正解.mp3")
    se_yes1 =   pygame.mixer.Sound("sound_gl/正解(2).mp3")
    se_no2 =    pygame.mixer.Sound("sound_gl/不正解(2).mp3")
    se_op =     pygame.mixer.Sound("sound_gl/スタート.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((600, 600), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((600, 600))
                if event.key == K_SPACE:
                    if idx == 0:
                        se_op.play()
                        idx += 1
                    else:
                        idx += 1
                if event.key == K_z:
                    idx *= 0
                    score *= 0
                if event.key == K_b:
                    idx = idx - 1
                if event.key == K_a:
                    if idx == 1:
                        sound1()
                    elif idx == 3:
                        sound2()
                    elif idx == 5:
                        sound3()
                    elif idx == 7:
                        sound4()
                    elif idx == 9:
                        sound5()
                if event.key == K_1:
                    if q1 == 1:
                        screen.blit(img_yes,(0,0))
                        se_yes1.play()
                        se_yes.play()
                        time.sleep(2)
                        idx += 1
                        score += 1
                    else:
                        screen.blit(img_no,(0,0))
                        se_no2.play()
                        se_no.play()
                        time.sleep(2)
                        idx += 1
                if event.key == K_2:
                    if q2 == 1:
                        screen.blit(img_yes,(0,0))
                        se_yes1.play()
                        se_yes.play()
                        time.sleep(2)
                        idx += 1
                        score += 1
                    else:
                        screen.blit(img_no,(0,0))
                        se_no2.play()
                        se_no.play()
                        time.sleep(2)
                        idx += 1
                if event.key == K_3:
                    if q3 == 1:
                        screen.blit(img_yes,(0,0))
                        se_yes1.play()
                        se_yes.play()
                        time.sleep(2)
                        idx += 1
                        score += 1
                    else:
                        screen.blit(img_no,(0,0))
                        se_no2.play()
                        se_no.play()
                        time.sleep(2)
                        idx += 1
                if event.key == K_4:
                    if q4 == 1:
                        screen.blit(img_yes,(0,0))
                        se_yes1.play()
                        se_yes.play()
                        time.sleep(2)
                        idx += 1
                        score += 1
                    else:
                        screen.blit(img_no,(0,0))
                        se_no2.play()
                        se_no.play()
                        time.sleep(2)
                        idx += 1
                if event.key == K_5:
                    if q5 == 1:
                        screen.blit(img_yes,(0,0))
                        se_yes1.play()
                        se_yes.play()
                        time.sleep(2)
                        idx += 1
                        score += 1
                    else:
                        screen.blit(img_no,(0,0))
                        se_no2.play()
                        se_no.play()
                        time.sleep(2)
                        idx += 1
            
        if idx == 0: # タイトル
            screen.blit(img_op,(0,0))
            fnt.render("press to space",True,(255,255,0))                

        if idx == 1: # 第一問
            screen.blit(img_main,(0,0))
            next1_image = fnt3.render("だい１もん",True,(0,0,0))
            screen.blit(next1_image,(30,10))

        
        if idx == 2: # 選択1
            screen.blit(img_choice,(0,0))
            #next_image = fnt2.render("２もんめへいく→スペースキー",True,(255,255,255))
            #screen.blit(next_image,(60,565))

            se_heri.stop()
            q2 = 1

        
        if idx == 3: # 第二問
            screen.blit(img_main,(0,0))
            next1_image = fnt3.render("だい２もん",True,(0,0,0))
            screen.blit(next1_image,(30,10))
        
        if idx == 4: # 選択2
            screen.blit(img_choice,(0,0))
            #next_image = fnt2.render("３もんめへいく→スペースキー",True,(255,255,255))
            #screen.blit(next_image,(60,565))
            se_pato.stop()
            q2 = 0
            q4 = 1

        if idx == 5: # 第3問
            screen.blit(img_main,(0,0))
            next1_image = fnt3.render("だい３もん",True,(0,0,0))
            screen.blit(next1_image,(30,10))
        
        if idx == 6: # 選択３
            screen.blit(img_choice,(0,0))
            #next_image = fnt2.render("４もんめへいく→スペースキー",True,(255,255,255))
            #screen.blit(next_image,(60,565))
            se_kyu.stop()
            q4 = 0
            q5 = 1
        
        if idx == 7: # 第4問
            screen.blit(img_main,(0,0))
            next1_image = fnt3.render("だい４もん",True,(0,0,0))
            screen.blit(next1_image,(30,10))

        if idx == 8: # 選択4
            screen.blit(img_choice,(0,0))
            #next_image = fnt2.render("５もんめへいく→スペースキー",True,(255,255,255))
            #screen.blit(next_image,(60,565))
            se_syo.stop()
            q5 = 0
            q3 = 1

        if idx == 9: # 第5問
            screen.blit(img_main,(0,0))
            next1_image = fnt3.render("だい５もん",True,(0,0,0))
            screen.blit(next1_image,(30,10))

        if idx == 10: # 選択5
            screen.blit(img_choice,(0,0))
            #next_image = fnt2.render("けっかをみる→スペースキー",True,(255,255,255))
            #screen.blit(next_image,(60,565))
            se_densya.stop()
            q3 = 0
            q1 = 1

        if idx == 11: # 結果
            screen.blit(img_ed,(0,0))
            score_image = fnt.render("5問中{}問正解！".format(score),True,(0,0,255))
            screen.blit(score_image,(100,250))

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
