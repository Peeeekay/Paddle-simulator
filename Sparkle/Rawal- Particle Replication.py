
import pygame, sys, random
from pygame.locals import *
pygame.init()

WINDOW_X = 800
WINDOW_Y = 600
K=0

d=0
NUM_PARTICLES = 75
t=0
LEFT_PADDLE = []
RIGHT_PADDLE=[]

for x in range(5):
    LEFT_PADDLE.append(pygame.image.load("LeftPaddle-"+str(x+1)+".png"))
for x in range(5):
    RIGHT_PADDLE.append(pygame.image.load("RightPaddle-"+str(x+1)+".png"))

#Particle Class. We will be instantiating many of these!
class Particle(object):
    def __init__(self, image, dir_x, dir_y, emit_x, emit_y,  countdown, type, LIFETIME, sc):
        self.type = type
        self.x = dir_x
        self.y = dir_y
        self.image = image
        self.alive = True
        self.countdown = countdown
        self.pos=image.get_rect().move(emit_x, emit_y)
        self.lifetime= LIFETIME
        self.steps=0
        self.sc=sc
    def move(self):
        if self.countdown>0:self.countdown -= 1
        else:
            self.steps += 1
            if self.steps == self.lifetime: self.alive = False
            self.pos = self.pos.move(self.x, self.y)


screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))     #set up PyGame Window
black = 0,0,0                                             #black is 0 red, 0 green, 0 blue




def getImage():
    particle_image= pygame.image.load("large.png").convert_alpha()
    particle_image2= pygame.image.load("medium.png").convert_alpha()
    particle_image3= pygame.image.load("small.png").convert_alpha()
    particle_image4= pygame.image.load("tiny.png").convert_alpha()

    C= random.randint(0,100)
    if C>=94 :
        return(particle_image,x,4,50)
    elif 94>C>=59:
        return(particle_image2,x,16,27)
    elif 59> C>=24: return(particle_image3,x,30,24)
    else: return(particle_image4,x,30,15)

particlesL=[]

for x in range(NUM_PARTICLES): 		#create objects
    EMIT_LX= random.randint(232,239)
    EMIT_LY= random.randint(318,325)
    EMIT_RX= random.randint(534,541)
    EMIT_RY= random.randint(318,325)

    image, type, LIFETIME,sc = getImage()
    p = Particle(image,random.uniform(-8,3),random.uniform(1,15),EMIT_LX,EMIT_LY,random.randint(0,50),type,LIFETIME,sc)
    image, type, LIFETIME,sc = getImage()
    a= Particle(image,random.uniform(-3,8),random.uniform(1,15), EMIT_RX,EMIT_RY,random.randint(0,50),type, LIFETIME,sc)
    particlesL.append(p)
    particlesL.append(a)






mouse_x = 0
mouse_y = 0

paddle_image = 2
running = True



while running:
    d=d+1
    pygame.mouse.set_visible(1)

    # -- Check for User closing the window, and QUIT in that event ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

    screen.fill(black)  # Clear the screen by filling black

    for p in particlesL:
        p.move()
        if p.countdown == 0:
            if p.steps <= 2:
                draw= pygame.transform.scale(p.image,(p.sc,p.sc))
            elif 2<p.steps<16:
                V= random.randint(5,9)
                VV=random.randint(13,17)
                N=p.sc-VV
                if N<=0:
                    draw=pygame.transform.scale(p.image,(V,V))
                else:
                    draw=pygame.transform.scale(p.image,(N,N))
            elif p.steps>=16 :
                v=random.randint(3,7)
                draw=pygame.transform.scale(p.image,(v,v))



            screen.blit(draw, p.pos)
            if p.alive==False:

                image, type,LIFETIME,sc= getImage()

                particlesL.remove(p)

                if K==0:
                    o= Particle(image,random.uniform(-8,3),random.uniform(1,15), EMIT_LX,EMIT_LY,random.randint(0,50),type, LIFETIME,sc)
                    K=K+1
                else:
                    o=Particle(image,random.uniform(-3,8),random.uniform(1,15), EMIT_RX,EMIT_RY,random.randint(0,50),type, LIFETIME,sc)
                    K=K-1
                particlesL.append(o)






    if d%5==0:
        t=random.randint(0,4)
    screen.blit((LEFT_PADDLE[t]),(100,200))
    screen.blit((RIGHT_PADDLE[t]),(500,200))

    pygame.display.update()
    pygame.time.delay(15)


pygame.quit()

