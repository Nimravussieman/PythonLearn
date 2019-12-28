import sys, pygame, random,time,threading
pygame.init()
pygame.font.init()

class Blok(pygame.Rect):
    def __init__(self,color,x, y, width,height):
        self.color = color
        super(Blok, self).__init__(x, y, width,height)
class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    colors = {0:(255, 255, 255),1:(0, 255, 0),2:(125, 125, 0),3:(0,0,255),4:(120,120,120),5:(120,0,0)}
    def __init__(self):
        self.size = self.width, self.height = 750, 400
        self.speed = [random.randint(0, 8), -3]
        self.sleep = 0.007
        self.screen = pygame.display.set_mode(self.size)
        self.rectwidth = 100
        self.radius = 5
        self.rect = None
        self.circle = None
        self.begin_pos()
        self.main_rect = pygame.Rect(50,40,450,500)
        self.turn = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 40)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
        self.heart = pygame.image.load("image.png")
        self.heartrect = self.heart.get_rect()
        self.heartrect.top = self.main_rect.top+50
        self.heartrect.left = self.main_rect.right+50
        self.step = 10
        self.bloks_leaft = None
        self.bloks = self.bloks_create()

    def begin_pos(self):
        self.rect = pygame.Rect(500/2-50,self.height-30, self.rectwidth, 5)
        self.circle = pygame.Rect(self.rect.x+self.rect.width//2, self.rect.y-10,5,5)

    def otskok(self):
        x = random.randint(0,6)
        self.speed[0] = x if self.speed[0] > 0 else -x
        self.speed[1] = -self.speed[1]# if random.randint(1) else -y
        self.set_sleep()
    def set_sleep(self):
        # sleep = 0.005
        temp3 = abs(self.speed[1])-abs(self.speed[0])
        # temp3=(self.speed[0]+temp3)//2
        self.sleep = 0.007 if not temp3 else 0.007*abs(temp3)
    def keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 50:
            self.rect.move_ip(-4, 0)
            self.turn = -1
        elif key[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.move_ip(4, 0)
            self.turn = 1
        else:
            self.turn = 0
    def bloks_create(self):
        temp = []
        # kord = 55
        height = 10
        width = (500-55)/height
        for y in range(0,5):
            for x in range(1,11):
                temp.append(Blok(Game.colors[y],x*width+9,y*height+55+1,width-1,height-1))
        self.bloks_leaft = len(temp)
        return temp
    def heart_round_show(self,lives,round,bloks_leaft):
        self.screen.blit(self.heart, self.heartrect)
        textsurface = self.myfont.render(str(lives), False, Game.RED)
        self.screen.blit(textsurface, (self.main_rect.right + 150, self.main_rect.top + 65))
        textsurface = self.myfont.render("Round  "+str(round), False, Game.GREEN)
        self.screen.blit(textsurface, (self.main_rect.right + 50, self.main_rect.top + 150))
        textsurface = self.myfont2.render("Bloks leaft  "+str(bloks_leaft), False, Game.GREEN)
        self.screen.blit(textsurface, (self.main_rect.right + 15, self.main_rect.top + 250))

    def fild_show(self,color):
        pygame.draw.line(self.screen, Game.RED, (50, 40), (50, self.height), 5)
        pygame.draw.line(self.screen, Game.RED, (50, 40), (500, 40), 5)
        pygame.draw.line(self.screen, Game.RED, (500, 40), (500, 400), 5)
        pygame.draw.rect(self.screen, color, self.main_rect)
        pygame.draw.rect(self.screen, Game.WHITE, self.rect)
        pygame.draw.circle(self.screen, Game.WHITE, (self.circle.x, self.circle.y), 5)
    def bloks_show(self):
        for each in self.bloks:
            if each.colliderect(self.circle):
                self.otskok()
                self.bloks.remove(each)
                self.bloks_leaft -= 1
                continue
                # if not bloks_leaft:#len(self.bloks) and round != 3:
                #     round+=1
                #     self.bloks = self.bloks_create()
            pygame.draw.rect(self.screen, each.color, each)
        return Game.BLACK
    def finish(self,text):
        textsurface = self.myfont.render(text, False, Game.GREEN)
        self.screen.blit(textsurface, (self.width / 2 - 100, self.height / 2 - 50))
        pygame.display.update()
        time.sleep(2)
    def play(self):
        lives = 5
        round = 1
        color = Game.BLACK
        # bloks_leaft = len(self.bloks)
        thread = threading.Thread(target=self.bloks_show)
        while lives and round < 4 :
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
            self.keys()
            # self.circle = self.circle.move(self.speed)
            self.heart_round_show(lives,round,self.bloks_leaft)
            self.fild_show(color)

            if self.circle.colliderect(self.rect):
                #self.speed[0] = self.speed[0] if self.speed[0]<0 else -self.speed[0] #-self.speed[1]
                self.speed[1]= self.speed[1] if self.speed[1]<0 else -self.speed[1]
                if self.turn<0:
                    if self.speed[0]<=0:    self.speed[0]-=1
                    else:   self.speed[0] //= 2
                elif self.turn>0:
                    if self.speed[0] >= 0:  self.speed[0] += 1
                    else:   self.speed[0] //=2
                color = Game.BLACK
                self.set_sleep()
                if not self.bloks_leaft:
                    round += 1
                    self.bloks = self.bloks_create()

            elif self.circle.right >= 500 or self.circle.left <= 55:
                self.speed[0]=-self.speed[0]
                color = Game.BLACK
            elif self.circle.bottom >= self.height:
                lives -= 1
                self.begin_pos()
                self.speed[1] = -self.speed[1]
                self.speed[0] = random.randint(0,2)
                color = Game.RED
            elif self.circle.top <= 45:
                self.speed[1] = self.speed[1] if self.speed[1]>0 else -self.speed[1]
                color = Game.BLACK
            self.circle = self.circle.move(self.speed)

            time.sleep(0.005)

            for each in self.bloks:
                if each.colliderect(self.circle):
                    color = Game.BLACK
                    self.otskok()
                    self.bloks.remove(each)
                    self.bloks_leaft-=1
                    continue
                    # if not bloks_leaft:#len(self.bloks) and round != 3:
                    #     round+=1
                    #     self.bloks = self.bloks_create()
                pygame.draw.rect(self.screen, each.color, each)





            pygame.display.update()
            self.screen.fill(Game.BLACK)
            time.sleep(self.sleep)
        else:
            if not lives:
                self.finish(text='Game over')
            else:
                self.finish(text='Peremoga')
Game().play()

