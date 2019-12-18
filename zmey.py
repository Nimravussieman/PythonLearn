import sys, pygame, random,time
pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = 5

class MyRect:#(pygame.Rect):
    def __init__(self,x,y,speed = (0,0),color = WHITE):
        #super(MyRect, self).__init__()
        self.speed = speed
        self.rect = pygame.Rect(x, y, SIZE,SIZE)
        self.color = color
    def move(self):#,speed):
        self.rect.move_ip(self.speed[0],self.speed[1])

class MyRectColl:
    def __init__(self,x,y,speed,color=GREEN):
        self.rects=[self.new(x, y,speed,color)]#[pygame.Rect(width/2, height/2, SIZE,SIZE)]
        self.count = 1
    def add_new(self):#,my_rect):
        self.first().color = WHITE
        temp = self.new(self.first().rect.x + self.first().speed[0],
                        self.first().rect.y + self.first().speed[1],
                        self.first().speed,
                        RED)
        self.rects.insert(0,temp)
        self.count+=1
    def new(self,x,y,speed,color = WHITE):
        return MyRect(x,y,speed,color)
    def first(self):
        return self.rects[0]
    def get_len(self):
        return self.count
class Game:

    def __init__(self):
        self.size = self.width, self.height = 500, 500
        self.dots = self.new_fild()
        self.step = [0.05,0.001]
        self.speed = (0, SIZE)
        self.screen = pygame.display.set_mode(self.size)
        # self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        # self.loop = True
        self.collection = MyRectColl(self.width/2,self.height/2,self.speed)

    def new_fild(self):
        temp = []
        i = 10
        while i < self.width-10:
            if not random.randint(0, 17):
                j = 10
                while j < self.height-10:
                    if not random.randint(0, 45):
                        temp.append(MyRect(i, j, color=RED))
                    j += 5
            i += 5
        return temp

    def new_step(self):
        if self.step[0] - self.step[1] <= 0:  # not speed - step:
            self.step[1] /= 10
        self.step[0] -= self.step[1]

    def keys(self,i):
        if i.key == pygame.K_UP : self.speed = (0, -SIZE)
        elif i.key == pygame.K_DOWN : self.speed = (0, SIZE)
        elif i.key == pygame.K_RIGHT : self.speed = (SIZE, 0)
        elif i.key == pygame.K_LEFT : self.speed = (-SIZE, 0)
        # if i.key == pygame.K_SPACE :
        #     self.collection.add_new()
    def zmey_move(self):
        i = self.collection.get_len() - 1
        j = i - 1
        while i != 0:
            self.collection.rects[i].rect.x = self.collection.rects[j].rect.x
            self.collection.rects[i].rect.y = self.collection.rects[j].rect.y
            i -= 1
            j -= 1

    def final(self,text,color):
        self.screen.fill(color)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(text, False, BLACK)
        self.screen.blit(textsurface, (self.height / 2 - 60, self.width / 2))
        pygame.display.update()
        time.sleep(2)


    def play(self):
        color = BLACK
        # textsurface = self.myfont.render(str(count), False, Game.GREEN)

        while len(self.dots):
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
                if i.type == pygame.KEYDOWN:
                    self.keys(i)

            for dot in self.dots:
                pygame.draw.rect(self.screen, dot.color, dot.rect)
                if self.collection.first().rect.colliderect(dot.rect):
                    self.collection.add_new()
                    self.dots.remove(dot)
                    self.new_step()

            self.collection.first().speed = self.speed

            self.zmey_move()

            self.collection.first().move()
            for each in self.collection.rects:
                pygame.draw.rect(self.screen, each.color, each.rect)

            if self.collection.first().rect.left <= 0 or self.collection.first().rect.right >= self.width or self.collection.first().rect.top <= 0 or self.collection.first().rect.bottom >= self.height:
                break


            pygame.display.update()
            time.sleep(self.step[0])
            self.screen.fill(color)
        else:
            self.final("peremoga", GREEN)
            return
        self.final("Game over",RED)


Game().play()

