import pygame
class ball:
    def __init__(self, position, color):
        self.velocity = [0.0, 0.0]
        self.__position = position
        self.__startPosition = position
        self.__color = color
        self.__size = [30,30] 

    def getPosition(self):
        return self.__position
    def getSize(self):
        return self.__size
    def getColor(self):
        return self.__color
    def resetToStartPosition(self):
        self.__position = self.__startPosition
    def drawToScreen(self,surface):
        pygame.draw.rect(surface, self.__color, pygame.Rect(self.__position[0], self.__position[1], self.__size[0], self.__size[1]), 0)



def main():
    colorWhite = (255,255,255)
    colorMagenta = (255,0,255)
    colorRed = (255,0,0)
    colorBlue = (0,0,255)
    screenWidth = 800
    screenHeight = 600

    #setup pygame
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    FPS = 60
    deltaTime = 1.0/FPS
    clock = pygame.time.Clock()
    running = True

    theBall = ball([800/2 - 30/2, 600/2 - 30/2],colorMagenta)
    theBall.velocity[0] = 100
    theBall.velocity[1] = 100

    paddles = [Paddle([40, screenHeight/2 - 120/2],colorRed),
              Paddle([760, screenHeight/2 - 120/2],colorBlue)]  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        theBall.move(deltaTime)
        for paddle in paddles:
            paddle.move(deltaTime)
            if paddle.getPosition()[1] < 0:
                paddle.getPosition()[1] = 0
            elif paddle.getPosition()[1] > (screenHeight - 120):
                paddle.getPosition()[1] = screenHeight - 120

        #code to bounce
        if(theBall.getPosition()[1] < 0):
            theBall.velocity[1] = -theBall.velocity[1]
        elif(theBall.getPosition()[1] > + theBall.getSize()[1] > screenHeight):
            theBall.velocity[1] = -theBall.velocity[1]
        
        screen.fill(colorWhite)
        theBall.drawToScreen(screen)
        pygame.display.flip()
        clock.tick(FPS)


# class Wall:
#     def __init__(self,xCor ,yCor, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#         self.xCor = xCor
#         self.yCor = yCor

    

    

