#meta
import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

#feluletek
bg_surface = pygame.image.load('hatter.jpg').convert()
floor_surface = pygame.image.load('padlo.jpg').convert()

bird_surface = pygame.image.load('bird1.png').convert_alpha()
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('pipe.png').convert_alpha()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 500, 600, 650, 700, 750, 800, 850]
#valtozok
fl_xpos = 0
gravity = 0.25
bird_movement = 0
game_active = True


#fuggvenyek
def draw_floor():
    screen.blit(floor_surface,(fl_xpos, 900))
    screen.blit(floor_surface,(fl_xpos + 576, 900))



def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes



def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
    
    
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):

            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False

    return True
           

#gameloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                
        if event.type == SPAWNPIPE:
            pipe_list.extend (create_pipe())
    
    screen.blit(bg_surface, (0,0))
    
    if game_active:
        #birb
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)
        
        
        #pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    
    
    
    
    
    
    
    #floor 
    fl_xpos -=5
    draw_floor()
    if fl_xpos <= -576:
        fl_xpos = 0
    
    pygame.display.update()
    clock.tick(120)