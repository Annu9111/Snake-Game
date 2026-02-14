import pygame
import random
import sys

pygame.init()

#Screen setting
WIDTH,HEIGHT = 500,800
screen = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Snake Game")

#colors
WHITE=(255,255,255)
GREEN=(0,200,0)
RED=(200,0,0)
BLACK=(0,0,0)

#clock and speed
clock = pygame.time.Clock()
snake_block=20
snake_speed=6

#fonts
font_style=pygame.font.SysFont("arial",30)
score_font=pygame.font.SysFont("arial",25)

def show_score(score):
    value = score_font.render("Score: "+ str(score),True,WHITE)
    screen.blit(value,[10,10])
    
def message(text,color):
    mesg=font_style.render(text,True,color)
    screen.blit(mesg,[WIDTH /6,HEIGHT / 3])
    
def game():
    snake = [(100,100)]
    direction="RIGHT"
    score=0
    
    food_x=random.randrange(0,WIDTH,snake_block)
    food_y=random.randrange(0,HEIGHT,snake_block)
    
    game_over = False
    
    while not game_over:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction !="DOWN":
                    direction="UP"
                elif event.key ==pygame.K_DOWN and direction!="UP":
                    direction="DOWN"
                    
        head_x,head_y = snake[0]
        
        if direction == "LEFT":
            head_x-=snake_block
        elif direction == "RIGHT":
            head_x+=snake_block
        elif direction =="UP":
            head_y-=snake_block
        elif direction=="DOWN":
            head_y+=snake_block
            
        #wall collision
        if head_x<0 or head_x>=WIDTH or head_y<0 or head_y>=HEIGHT:
            game_over=True
            
        new_head = (head_x,head_y)
        
        #self collision
        if new_head in snake:
            game_over = True
            
        snake.insert(0,new_head)
        
        #food collision
        if head_x ==food_x and head_y==food_y:
            score+=1
            food_x = random.randrange(0,WIDTH,snake_block)
            food_y =random.randrange(0,HEIGHT,snake_block) 
        else:
            snake.pop()
            
        #Draw food
        pygame.draw.rect(screen,RED,[food_x,food_y,snake_block,snake_block])
        
        #Draw snake
        for block in snake:
            pygame.draw.rect(screen,GREEN,[block[0],block[1],snake_block,snake_block]) 
            
        show_score(score)
        pygame.display.update()
        clock.tick(snake_speed)
        
    #game over screen
    

                                                                         
                                        