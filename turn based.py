import pygame
import random
import math
import time
import sys
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
RED = (255,0,0)
PURPLE = (128,0,128)


## -- Define the class Button which is a sprite 
class Button(pygame.sprite.Sprite): 
    def __init__(self, color, width, height): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 1000
        self.rect.y = 1000
    
    def button_setx_val(self, x):
        self.rect.x = x
    
    def button_sety_val(self, y):
        self.rect.y = y

## -- Define the class NPC which is a sprite 
class NPC(pygame.sprite.Sprite): 
    def __init__(self, color, width, height): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 340
        self.rect.y = 70

## -- Define the class Enemy which is a sprite 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self, color, width, height, HP): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 640
        self.rect.y = 240
        self.HP = 5

    def enemy_setx_val(self, x):
        self.rect.x = x
    
    def enemy_sety_val(self, y):
        self.rect.y = y

    def enemy_attacked(self, damage):
        self.HP = self.HP - damage
    
    def set_enemy_hp(self, health):
        self.HP = health

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite): 
    def __init__(self, color, width, height, HP, MP, Burst): 
        super().__init__()
        self.image = pygame.Surface([width, height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = 340
        self.rect.y = 500
        self.movex = 0
        self.movey = 0
        self.HP = 50
        self.MaxHP = 50
        self.MP = 5
        self.MaxMP = 5
        self.Burst = 5
        self.MaxBurst = 5
        self.Defend = False
        self.Flee = 0 
        self.escaped = False
        self.money = 0
        self.exp = 0

    def player_set_movement(self, x, y):
        self.movex += x
        self.movey += y

    def player_end_movement(self):
        self.movex = 0
        self.movey = 0

    def player_x_val(self):
        return self.rect.x
    
    def player_setx_val(self, x):
        self.rect.x = x
    
    def player_sety_val(self, y):
        self.rect.y = y
    
    def set_player_hp(self, health, Max):
        self.HP = health
        self.MaxHP = Max
    
    def set_player_mp(self, magic, Max):
        self.MP = magic
        self.MaxMP = Max
    
    def use_mp(self, magic):
        self.MP = self.MP - magic
    
    def player_heal(self, heal):
        self.HP = self.HP + heal

    def set_defending(self):
        self.Defend = isdefending
        self.HP = self.HP + 5

    def runaway(self):
        self.Flee = get_flee_chance()
        if self.Flee > 7 and enemy_type != 0:
            self.escaped = True

    def player_attacked(self, damage):
        self.HP = self.HP - damage

    def update(self): 
        self.rect.x += self.movex
        self.rect.y += self.movey

        if self.rect.x > 690:
            self.rect.x = 690
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 510:
            self.rect.y = 510
        if self.rect.y < 0:
            self.rect.y = 0

        # Check collision with NPC sprite
        if self.rect.colliderect(NPCr.rect):
            # Adjust player position to prevent overlap
            if self.movex > 0:
                self.rect.right = NPCr.rect.left
            elif self.movex < 0:
                self.rect.left = NPCr.rect.right
            if self.movey > 0:
                self.rect.bottom = NPCr.rect.top
            elif self.movey < 0:
                self.rect.top = NPCr.rect.bottom
        
        # Check collision with Enemy sprite
        if self.rect.colliderect(Enemeyr.rect):
            # Adjust player position to prevent overlap
            if self.movex > 0:
                self.rect.right = Enemeyr.rect.left
            elif self.movex < 0:
                self.rect.left = Enemeyr.rect.right
            if self.movey > 0:
                self.rect.bottom = Enemeyr.rect.top
            elif self.movey < 0:
                self.rect.top = Enemeyr.rect.bottom


# -- Initialise PyGame
pygame.init()
pygame.font.init()
my_fontbig = pygame.font.SysFont('Comic Sans MS', 25)
my_font = pygame.font.SysFont('Comic Sans MS', 18)

# Create a clock object to track time
clock = pygame.time.Clock()

# -- Blank Screen
size = (720, 540)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Turn Based")
# -- Exit game flag set to false
done = False 
# Create a list of all sprites#
enemy_group = pygame.sprite.Group()  # Create a separate group for enemies 
npc_group = pygame.sprite.Group()  # Create a separate group for NPCs
fight_group = pygame.sprite.Group() # Create a separate group for the fighting sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 

# Create the enemies 
Enemeyr = Enemy(RED, 30, 30, 50)
all_sprites_group.add(Enemeyr) 
enemy_group.add(Enemeyr)
fight_group.add(Enemeyr)

# Create the NPC 
NPCr = NPC(YELLOW, 30, 30)
all_sprites_group.add(NPCr) 
npc_group.add(NPCr)

# Create the player
Player = Player(BLUE, 30, 30, 50, 5, 0)
all_sprites_group.add(Player)
fight_group.add(Player) 

# Buttons
BackdropButton = Button(BLUE, 720, 200)
fight_group.add(BackdropButton)

BackdropButton2 = Button(BLACK, 720, 400)
fight_group.add(BackdropButton2)

Buttonf = Button(WHITE, 120, 32)
fight_group.add(Buttonf)

Buttonh = Button(WHITE, 120, 32)
fight_group.add(Buttonh)

Buttond = Button(WHITE, 120, 32)
fight_group.add(Buttond)

Buttonr = Button(WHITE, 120, 32)
fight_group.add(Buttonr)


click_detector = False
click_detector2 = False

click_detectorf = False
click_detectorh = False
click_detectord = False
click_detectorr = False
isdefending = False

# Initialize variables for cooldowns and last click times
last_click_time_f = 0
last_click_time_h = 0
last_click_time_d = 0
last_click_time_r = 0
pause_time = 0
damage_flag= 0
heal_flag = 0
defend_flag = 0
flee_flag = 0
burst_flag = 0
enemy_flag = 0
enemy_type = 0
turnflag = 1
full_health = 0
max_health = 0
healed = 0


# Define cooldown duration (5 seconds)
cooldown_duration = 5


def get_damage():
    return random.randint(1,10)

def get_flee_chance():
    return random.randint(1,10)


# sets gamestate to open world, open world = 1 fight = 2
gamestate = 1

### -- Game Loop
while not done:
    if gamestate == 1:
        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and NPCr.rect.collidepoint(event.pos):
                    click_detector = True
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and Enemeyr.rect.collidepoint(event.pos):
                    click_detector2 = True
            elif event.type == pygame.KEYDOWN:  # - a key is down
                if event.key == pygame.K_a:  # - if the left key is pressed
                    Player.player_set_movement(-4, 0)  # speed set to -3
                elif event.key == pygame.K_d:  # - if the right key is pressed
                    Player.player_set_movement(4, 0)  # speed set to 3
                elif event.key == pygame.K_w:
                    Player.player_set_movement(0, -4)
                elif event.key == pygame.K_s:
                    Player.player_set_movement(0, 4)
            elif event.type == pygame.KEYUP:  # - a key released
                if event.key in (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s):
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
                        Player.player_end_movement()  # speed set to 0

        all_sprites_group.update()

        # Clear the screen if no collision
        screen.fill(GREEN)

        all_sprites_group.draw(screen)
        Area1 = my_fontbig.render('Grasslands', False, (255, 255, 255))
        screen.blit(Area1, (5, 5))

        Hint1 = my_font.render('Hint: Click on the yellow sprite', False, (255, 255, 255))
        screen.blit(Hint1, (5, 510))

        # Display "Success" if NPC sprite is clicked
        if click_detector:
            n_txt = my_font.render('Welcome, walk over to the enemy', False, (255, 255, 255))
            n_txt2 = my_font.render('and click to intiate a fight', False, (255, 255, 255))
            screen.blit(n_txt, (230, 20))
            screen.blit(n_txt2, (260, 40))

        if click_detector2:
            e_txt = my_font.render('Fight initated', False, (255, 255, 255))
            screen.blit(e_txt, (600, 200))
            gamestate = 2
        
    if gamestate == 2:
        #variable used for checking for cooldowns
        current_time = pygame.time.get_ticks()  # Get current time in milliseconds
        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(GREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            #variable used for checking for cooldowns
            current_time = time.time()
            # Check if the mouse button was clicked on the NPC sprite
            if event.button == 1 and Buttonf.rect.collidepoint(event.pos):
                if current_time - last_click_time_f >= cooldown_duration:
                    click_detectorf = True
                    last_click_time_f = current_time
               

            if event.button == 1 and Buttonh.rect.collidepoint(event.pos):
                if current_time - last_click_time_h >= cooldown_duration:
                    click_detectorh = True
                    last_click_time_h = current_time
        

            if event.button == 1 and Buttond.rect.collidepoint(event.pos):
                if current_time - last_click_time_d >= cooldown_duration:
                    click_detectord = True
                    last_click_time_d = current_time

            if event.button == 1 and Buttonr.rect.collidepoint(event.pos):
                if current_time - last_click_time_r >= cooldown_duration:
                    click_detectorr = True
                    last_click_time_r = current_time


        if click_detectorf:
            turnflag = 1
            if damage_flag == 0:
                damage = get_damage()
                Enemeyr.enemy_attacked(damage)
                damage_flag = 1
            if Player.Burst == 5:
               damage = get_damage()
               Enemeyr.enemy_attacked(damage * 2)
               Player.Burst = 0
               burst_flag = 1 
               damage_flag = 1 
            # end if

            # while i < 10000:
            #     f_txt = my_font.render('You attacked the Test Dummy', False, (255, 255, 255))
            #     f_txt2 = my_font.render('You dealt ' + str((damage)) + ' damage', False, (255, 255, 255))
            #     screen.blit(f_txt, (230, 20))
            #     #screen.blit(f_txt2, (260, 40))
            #     print (i)
            #     i = i + 1
            # #end while

            if burst_flag == 1:
                burst_txt = my_font.render('You unleashed a burst attack!', False, (255, 255, 255))
                burst_txt2 = my_font.render('You dealt ' + str((damage*2)) + ' damage', False, (255, 255, 255))
                screen.blit(burst_txt, (230, 20))
                screen.blit(burst_txt2, (260, 40))
            else:
                f_txt = my_font.render('You attacked the Test Dummy', False, (255, 255, 255))
                f_txt2 = my_font.render('You dealt ' + str((damage)) + ' damage', False, (255, 255, 255))
                screen.blit(f_txt, (230, 20))
                screen.blit(f_txt2, (260, 40))


            if Enemeyr.HP <= 0:
             end_txt = my_font.render('You killed the Test Dummy', False, (255, 255, 255))
             screen.blit(end_txt, (230, 60))

            if pause_time > 180:
                click_detectorf = False
                if Enemeyr.HP <= 0:
                    turnflag = 3
                else:
                    turnflag = 2  
                pause_time = 0
                damage_flag = 0
                if burst_flag == 1:
                    burst_flag = 0
                else: 
                    Player.Burst = Player.Burst + 1
            else:
                pause_time+=1
            # end if  
             
        
        if click_detectorh:
            turnflag = 1
            if heal_flag == 0 and Player.MP > 0:
                if  Player.HP < 45:
                    Player.use_mp(1)
                    Player.player_heal(5)
                    heal_flag = 1
                    healed = 1
                elif Player.HP >= 45 and Player.HP < 50:
                    Player.use_mp(1)
                    Player.HP = 50
                    heal_flag = 1
                    max_health = 1
                elif Player.HP == Player.MaxHP:
                    full_health = 1
            if Player.MP == 0:
                h3_txt = my_font.render('You have no mana', False, (255, 255, 255))
                screen.blit(h3_txt, (230, 20)) 
            #end if

            if full_health == 1:
                hf_txt = my_font.render('You can not heal over max HP', False, (255, 255, 255))
                screen.blit(hf_txt, (230, 20))
                    
             
            if max_health == 1:
                h_txt = my_font.render('You have healed to full', False, (255, 255, 255))
                screen.blit(h_txt, (230, 20))

            if healed == 1:
                h2_txt = my_font.render('You have successfully healed', False, (255, 255, 255))
                screen.blit(h2_txt, (230, 20)) 
                     
            if Player.MP <= 0:
                Player.MP = 0

            if pause_time > 180:
                click_detectorh = False
                turnflag = 2  
                pause_time = 0
                heal_flag = 0
                full_health = 0
                max_health = 0
                healed = 0
            else:
                pause_time+=1
            # end if 
        
        if click_detectord:
            turnflag = 1
            if defend_flag == 0:
                isdefending = True
                defend_flag = 1
            #end if

            d_txt = my_font.render('You have successfully defended', False, (255, 255, 255))
            screen.blit(d_txt, (230, 20))
            d2_txt = my_font.render('you take reduced damage', False, (255, 255, 255))
            screen.blit(d2_txt, (250, 40))

            if pause_time > 180:
                click_detectord = False
                turnflag = 2  
                pause_time = 0
                defend_flag = 0
            else:
                pause_time+=1
            # end if   
        
        if click_detectorr:
            turnflag = 1
            if flee_flag == 0:
                Player.runaway()
                flee_flag = 1
            #end if

            if enemy_type == 0:
                r_txt = my_font.render('You can not flee from this battle', False, (255, 255, 255))
                screen.blit(r_txt, (230, 20))
            elif enemy_type != 0 and Player.escaped == True:
                rs_txt = my_font.render('You have successfully escaped', False, (255, 255, 255))
                screen.blit(rs_txt, (230, 20))
            elif enemy_type != 0 and Player.escaped == False:
                rf_txt = my_font.render('You have failed to escaped', False, (255, 255, 255))
                screen.blit(rf_txt, (230, 20))
            
            
            if pause_time > 180:
                click_detectorr = False
                turnflag = 2  
                pause_time = 0
                flee_flag = 0
            else:
                pause_time+=1
            # end if  
            

        if turnflag == 2:
            cooldown_duration == 99999
            if enemy_flag == 0:
                damage = get_damage()
                if isdefending == True:
                    damage = damage // 2
                    Player.player_attacked(damage)
                else:
                    Player.player_attacked(damage)
                enemy_flag = 1
                #end if
            #end if
    
            e_txt = my_font.render('You have been attacked', False, (255, 255, 255))
            e_txt2 = my_font.render('You took ' + str((damage)) + ' damage', False, (255, 255, 255))
            screen.blit(e_txt, (240, 20))
            screen.blit(e_txt2, (260, 40))
            if Player.HP <= 0:
                lose_txt = my_font.render('You have perished', False, (255, 255, 255))
                screen.blit(lose_txt, (262, 60))
            
            if pause_time > 180:
                turnflag = 1
                pause_time = 0
                enemy_flag = 0
            else:
                pause_time+=1
            # end if   
        
        if turnflag == 3:
            t_txt = my_font.render('You have gained 5 EXP and 10 Gold', False, (255, 255, 255))
            t2_txt = my_font.render('You have finished the tutorial', False, (255, 255, 255))
            t3_txt = my_font.render('you will be taken back the open world', False, (255, 255, 255))
            screen.blit(t_txt, (220, 20))
            screen.blit(t2_txt, (240, 40))
            screen.blit(t3_txt, (210, 60))
            if pause_time > 180:
                pause_time = 0
                gamestate = 3
            else:
                pause_time+=1
            #end if
        #end if


        #set player pos
        Player.player_setx_val(240)
        Player.player_sety_val(175)
        if Player.HP <= 0:
            Player.enemy_setx_val(999)
            Player.enemy_sety_val(999)

        #set enemy pos
        Enemeyr.enemy_setx_val(450)
        Enemeyr.enemy_sety_val(175)
        if Enemeyr.HP <= 0:
            Enemeyr.enemy_setx_val(999)
            Enemeyr.enemy_sety_val(999)

        #set fight button pos
        Buttonf.button_setx_val(40)
        Buttonf.button_sety_val(365)

        #set heal button pos
        Buttonh.button_setx_val(40)
        Buttonh.button_sety_val(410)
                
        #set defend button pos
        Buttond.button_setx_val(40)
        Buttond.button_sety_val(455)
                
        #set flee button pos
        Buttonr.button_setx_val(40)
        Buttonr.button_sety_val(500)

        #set backdropbutton pos
        BackdropButton.button_setx_val(0)
        BackdropButton.button_sety_val(350)

        #set backdrop2button pos
        BackdropButton2.button_setx_val(200)
        BackdropButton2.button_sety_val(550)

        #draw the fighting sprites and buttons
        fight_group.update()
        fight_group.draw(screen)

        #draw the hp bar
        pygame.draw.rect(screen, BLACK, (335, 374, Player.MaxHP*3 + 3, 24))
        pygame.draw.rect(screen, RED, (335, 374, Player.MaxHP*3, 20))
        pygame.draw.rect(screen, GREEN, (335, 374, Player.HP*3, 20))

        #draw the magic bar
        pygame.draw.rect(screen, BLACK, (335, 409, Player.MaxMP*30 + 3, 24))
        pygame.draw.rect(screen, RED, (335, 409, Player.MaxMP*30, 20))
        pygame.draw.rect(screen, PURPLE, (335, 409, Player.MP*30, 20))

        #draw the burst bar
        pygame.draw.rect(screen, BLACK, (335, 444, Player.MaxBurst*30 + 3, 24))
        pygame.draw.rect(screen, RED, (335, 444, Player.MaxBurst*30, 20))
        pygame.draw.rect(screen, WHITE, (335, 444, Player.Burst*30, 20))

        #set area text
        Area2 = my_fontbig.render('Grasslands: Fight', False, (255, 255, 255))
        screen.blit(Area2, (5, 5))
        #if turnflag == 1:
            #Turn = my_fontbig.render('Your Turn: Choose an action ', False, (255, 255, 255))
            #screen.blit(Turn, (5, 50))
        #if turnflag == 2:
            #screen.blit(Turn, (999, 999))
            #Turn2 = my_fontbig.render('Enemy Turn: Prepare for the worst ', False, (255, 255, 255))
            #screen.blit(Turn, (5, 50))

        #set button texts
        Button1 = my_fontbig.render('Fight', False, (0, 0, 0))
        screen.blit(Button1, (45, 361))
        Button2 = my_fontbig.render('Heal', False, (0, 0, 0))
        screen.blit(Button2, (45, 410))
        Button3 = my_fontbig.render('Defend', False, (0, 0, 0))
        screen.blit(Button3, (45, 455))
        Button4 = my_fontbig.render('Flee', False, (0, 0, 0))
        screen.blit(Button4, (45, 500))
        Health = my_fontbig.render('HP:' + str(Player.HP) + "/" + str(Player.MaxHP), False, (0, 0, 0))
        screen.blit(Health, (200, 365))
        MagicP = my_fontbig.render('MP:' + str(Player.MP) + "/" + str(Player.MaxMP), False, (0, 0, 0))
        screen.blit(MagicP, (200, 400))
        Burst = my_fontbig.render('Burst:' + str(Player.Burst) + "/" + str(Player.MaxBurst), False, (0, 0, 0))
        screen.blit(Burst, (200, 435))

        #draw button backdrops
        #fight backdrop
        pygame.draw.rect(screen, BLACK, (160, 365, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 397, 123, 6))

        #heal backdrop
        pygame.draw.rect(screen, BLACK, (160, 410, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 442, 123, 6))

        #defend backdrop
        pygame.draw.rect(screen, BLACK, (160, 455, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 487, 123, 6))

        #flee backdrop
        pygame.draw.rect(screen, BLACK, (160, 500, 3, 35))
        pygame.draw.rect(screen, BLACK, (40, 532, 123, 6))

        #draw bar encasing
        pygame.draw.rect(screen, BLACK, (180, 365, 4, 170))
        pygame.draw.rect(screen, BLACK, (526, 365, 4, 170))
        pygame.draw.rect(screen, BLACK, (180, 532, 350, 4))
        pygame.draw.rect(screen, BLACK, (180, 365, 350, 4))
    
    if gamestate == 3:
        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and NPCr.rect.collidepoint(event.pos):
                    click_detector = True
                # Check if the mouse button was clicked on the NPC sprite
                if event.button == 1 and Enemeyr.rect.collidepoint(event.pos):
                    click_detector2 = True
            elif event.type == pygame.KEYDOWN:  # - a key is down
                if event.key == pygame.K_a:  # - if the left key is pressed
                    Player.player_set_movement(-4, 0)  # speed set to -3
                elif event.key == pygame.K_d:  # - if the right key is pressed
                    Player.player_set_movement(4, 0)  # speed set to 3
                elif event.key == pygame.K_w:
                    Player.player_set_movement(0, -4)
                elif event.key == pygame.K_s:
                    Player.player_set_movement(0, 4)
            elif event.type == pygame.KEYUP:  # - a key released
                if event.key in (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s):
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
                        Player.player_end_movement()  # speed set to 0

        all_sprites_group.update()

        # Clear the screen if no collision
        screen.fill(GREEN)

        all_sprites_group.draw(screen)

        # Display text if NPC sprite is clicked
        if click_detector:
            af_txt = my_font.render('Well done on defeating the enemy', False, (255, 255, 255))
            af_txt2 = my_font.render('more fights await you', False, (255, 255, 255))
            screen.blit(af_txt, (230, 20))
            screen.blit(af_txt2, (260, 40))


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

# End While
pygame.quit()
