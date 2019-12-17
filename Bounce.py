import sys, pygame, random,time
pygame.init()
pygame.font.init()

class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self):
        self.size = self.width, self.height = 500, 500
        self.speed = [random.randint(1, 2), random.randint(1, 2)]
        self.screen = pygame.display.set_mode(self.size)
        self.rectheight = 100
        self.rect = pygame.Rect((self.width-5, (self.height/2)-self.rectheight, 5, self.rectheight))
        self.ball = pygame.image.load("intro_ball.gif")
        self.ballrect = self.ball.get_rect()
        self.ballrect.top = self.height/2
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.step = 10
    def otskok(self):
        temp1 = random.randint(1, 2)
        temp2 = random.randint(1, 2)
        self.speed[0] = temp1 if self.speed[0] < 0 else -temp1  # -self.speed[0]
        self.speed[1] = temp2 if self.speed[1] <= 0 else -temp2
    def keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > 0: self.rect.move_ip(0, -3)  # rect.top = rect.top-1
        if key[pygame.K_DOWN] and self.rect.bottom < self.height: self.rect.move_ip(0, 3)  # rect.bottom = rect.bottom+1

    def play(self):
        #angle = 90
        count = 5
        color = Game.BLACK
        textsurface = self.myfont.render(str(count), False, Game.GREEN)

        while count:
            for i in pygame.event.get():
                if i.type == pygame.QUIT: exit()
            self.keys()
            self.ballrect = self.ballrect.move(self.speed)

            if self.ballrect.left < 3:
                self.otskok()
                color = Game.BLACK
            elif self.ballrect.right > self.width-5:
                if not (self.ballrect.center[1] > self.rect.top and self.ballrect.center[1] < self.rect.bottom):
                    color = Game.RED
                    count -=1
                    textsurface = self.myfont.render(str(count), False, Game.GREEN)
                self.otskok()
            if self.ballrect.top < 10 or self.ballrect.bottom > self.height-10:
                self.speed[1] = -self.speed[1]# random.randint(1, 2) if self.speed[1] < 0 else -random.randint(1, 2)

            # angle += self.speed[0]
            # angle %= 360
            # screen = pygame.transform.rotate(self.ball, angle)
            pygame.draw.rect(self.screen, Game.WHITE, self.rect)
            self.screen.blit(self.ball, self.ballrect)
            #self.screen.blit(screen, self.ballrect)
            self.screen.blit(textsurface, (10, 5))

            #pygame.display.flip()

            pygame.display.update()
            self.screen.fill(color)
            time.sleep(0.001)
        else:
            textsurface = self.myfont.render("Game over", False, Game.GREEN)
            self.screen.blit(textsurface, (self.height/2-60, self.width/2))
            pygame.display.update()
            time.sleep(2)
Game().play()