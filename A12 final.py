import pygame, sys, math


def pixel_collision(mask1, rect1, mask2, rect2):
    """Checks to see if two objects have overlapping pixels.

    :param mask1: Mask of first image.
    :param rect1: Rect of first image.
    :param mask2: Mask of second image.
    :param rect2: Rect of second image.
    :return: A boolean value that states whether or not the objects collided.
    """

    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]

    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap


def main():
    """Function that initializes and runs game.

    :return: None
    """

    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((1000, 1000))

    # Initialize start screen
    title_screen = pygame.image.load("title screen.png").convert_alpha()
    title_screen_rect = title_screen.get_rect()

    # Initialize start buttons
    start_button = pygame.image.load("start button.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (140, 70))
    start_button_rect = start_button.get_rect()
    start_button_mask = pygame.mask.from_surface(start_button)
    start_button_rect.center = (100, 500)
    start_button2 = pygame.image.load("start button.png").convert_alpha()
    start_button2 = pygame.transform.smoothscale(start_button2, (140, 70))
    start_button2_rect = start_button2.get_rect()
    start_button2_rect.center = (500, 50)
    start_button_mask2 = pygame.mask.from_surface(start_button2)
    start_button3 = pygame.image.load("start button.png").convert_alpha()
    start_button3 = pygame.transform.smoothscale(start_button3, (140, 70))
    start_button3_rect = start_button3.get_rect()
    start_button3_rect.center = (50, 900)
    start_button_mask3 = pygame.mask.from_surface(start_button3)

    # Initialize map
    level_1_map = pygame.image.load("level 1 map.png").convert_alpha()
    level_1_map_rect = level_1_map.get_rect()
    level_1_mask = pygame.mask.from_surface(level_1_map)

    # Initialize level 1 title decor
    level_1_title = pygame.image.load("Level 1 Title.png").convert_alpha()
    level_1_title_rect = level_1_title.get_rect()

    # Initialize fruit decor
    fruit_decor = pygame.image.load("fruit decor.png")
    fruit_decor_rect = fruit_decor.get_rect()

    # Initialize Game Over Screen
    game_over_screen = pygame.image.load("game over screen.png").convert_alpha()
    game_over_rect = game_over_screen.get_rect()

    # Initialize level 2 Start Screen
    level_2_start_screen = pygame.image.load("level 2 start screen.png").convert_alpha()
    level_2_start_screen_rect = level_2_start_screen.get_rect()

    # Initialize level 2
    level_2_map = pygame.image.load("plain mario map.png").convert_alpha()
    level_2_map_rect = level_2_map.get_rect()
    level_2_map_mask = pygame.mask.from_surface(level_2_map)

    # Level 2 decor overlay
    mario_map_overlay = pygame.image.load("mario background overlay.png").convert_alpha()
    mario_map_overlay_rect = mario_map_overlay.get_rect()

    # Initialize level 3 start screen
    level_3_start_screen = pygame.image.load("level 3 start screen.png").convert_alpha()
    level_3_start_screen_rect = level_3_start_screen.get_rect()

    # Initialize level 3 map
    level_3_map = pygame.image.load("donkey kong map.png").convert_alpha()
    level_3_map_rect = level_3_map.get_rect()
    level_3_map_mask = pygame.mask.from_surface(level_3_map)

    # Initialize end screen
    end_screen = pygame.image.load("end screen.png").convert_alpha()
    end_screen_rect = end_screen.get_rect()

    # Initialize players
    player = pygame.image.load("pacman_partial_closed.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    second_player = pygame.image.load("flying mario.png").convert_alpha()
    second_player = pygame.transform.smoothscale(second_player, (25, 25))
    second_player_rect = second_player.get_rect()
    second_player_mask = pygame.mask.from_surface(second_player)

    third_player = pygame.image.load("donkey kong mario sprite.png").convert_alpha()
    third_player = pygame.transform.smoothscale(third_player, (25, 25))
    third_player_rect = third_player.get_rect()
    third_player_mask = pygame.mask.from_surface(third_player)

    # Initialize peach
    peach = pygame.image.load("peach.png").convert_alpha()
    peach = pygame.transform.smoothscale(peach, (50, 50))
    peach_rect = peach.get_rect()
    peach_rect.center = (130, 110)
    peach_mask = pygame.mask.from_surface(peach)

    # Initialize apple
    apple = pygame.image.load("apple.png").convert_alpha()
    apple = pygame.transform.smoothscale(apple, (40, 40))
    apple_rect = apple.get_rect()
    apple_rect.center = (700, 105)
    apple_mask = pygame.mask.from_surface(apple)

    # Initialize cherry
    cherry = pygame.image.load("cherry.png").convert_alpha()
    cherry = pygame.transform.smoothscale(cherry, (40, 40))
    cherry_rect = cherry.get_rect()
    cherry_rect.center = (780, 770)
    cherry_mask = pygame.mask.from_surface(cherry)

    # Initialize ghosts
    ghost = pygame.image.load("PacmanGhost.png").convert_alpha()
    ghost = pygame.transform.smoothscale(ghost, (50, 50))
    ghost_rect = ghost.get_rect()
    ghost_rect.centerx = 570
    ghost_rect.centery = 50
    ghost_mask = pygame.mask.from_surface(ghost)

    ghost2 = pygame.image.load("mandarin ghost.png").convert_alpha()
    ghost2 = pygame.transform.smoothscale(ghost2, (50, 50))
    ghost_rect2 = ghost2.get_rect()
    ghost_rect2.centerx = 570
    ghost_rect2.centery = 760
    ghost_rect2_mask = pygame.mask.from_surface(ghost2)

    # Initialize mario enemy
    mario_enemy = pygame.image.load("flying mario enemy.png").convert_alpha()
    mario_enemy = pygame.transform.smoothscale(mario_enemy, (60, 60))
    mario_enemy_rect = mario_enemy.get_rect()
    mario_enemy_mask = pygame.mask.from_surface(mario_enemy)
    mario_enemy_rect.centerx = 500
    mario_enemy_rect.centery = 200

    # Initialize mario chomper
    mario_chomper = pygame.image.load("mario chomper.png").convert_alpha()
    mario_chomper = pygame.transform.smoothscale(mario_chomper, (40, 80))
    mario_chomper_rect = mario_chomper.get_rect()
    mario_chomper_mask = pygame.mask.from_surface(mario_chomper)
    mario_chomper_rect.centerx = 785
    mario_chomper_rect.centery = 525

    # Initialize boomba
    boomba_enemy = pygame.image.load("boomba.png").convert_alpha()
    boomba_enemy = pygame.transform.smoothscale(boomba_enemy, (50, 50))
    boomba_enemy_rect = boomba_enemy.get_rect()
    boomba_enemy_rect.centerx = 300
    boomba_enemy_rect.centery = 735
    boomba_enemy_mask = pygame.mask.from_surface(boomba_enemy)

    # Initialize Mushroom
    mushroom = pygame.image.load("mario mushroom.png").convert_alpha()
    mushroom = pygame.transform.smoothscale(mushroom, (30, 30))
    mushroom_rect = mushroom.get_rect()
    mushroom_rect.center = (400, 220)
    mushroom_mask = pygame.mask.from_surface(mushroom)

    # Initialize coins for the Mario game
    coin = pygame.image.load("mario coin.png").convert_alpha()
    coin = pygame.transform.smoothscale(coin, (30, 30))
    coin_rect = coin.get_rect()
    coin_rect.center = (380, 600)
    coin_mask = pygame.mask.from_surface(coin)

    coin2 = pygame.image.load("mario coin.png").convert_alpha()
    coin2 = pygame.transform.smoothscale(coin2, (30, 30))
    coin2_rect = coin2.get_rect()
    coin2_rect.center = (870, 460)
    coin2_mask = pygame.mask.from_surface(coin2)

    # Initialize coins for the Donkey Kong game
    coin3 = pygame.image.load("mario coin.png").convert_alpha()
    coin3 = pygame.transform.smoothscale(coin3, (30, 30))
    coin3_rect = coin3.get_rect()
    coin3_rect.center = (380, 600)
    coin3_mask = pygame.mask.from_surface(coin3)

    coin4 = pygame.image.load("mario coin.png").convert_alpha()
    coin4 = pygame.transform.smoothscale(coin4, (30, 30))
    coin4_rect = coin4.get_rect()
    coin4_rect.center = (500, 200)
    coin4_mask = pygame.mask.from_surface(coin4)

    coin5 = pygame.image.load("mario coin.png").convert_alpha()
    coin5 = pygame.transform.smoothscale(coin5, (30, 30))
    coin5_rect = coin5.get_rect()
    coin5_rect.center = (720, 720)
    coin5_mask = pygame.mask.from_surface(coin5)

    # Initialize Star
    star = pygame.image.load("mario star sprite.png").convert_alpha()
    star = pygame.transform.smoothscale(star, (30, 30))
    star_rect = coin.get_rect()
    star_rect.center = (640, 740)
    star_mask = pygame.mask.from_surface(star)

    # Initialize donkey kong sprite
    donkey_kong = pygame.image.load("donkey kong sprite.png").convert_alpha()
    donkey_kong = pygame.transform.smoothscale(donkey_kong, (80, 80))
    donkey_kong_rect = donkey_kong.get_rect()
    donkey_kong_rect.center = (70, 110)
    donkey_kong_mask = pygame.mask.from_surface(donkey_kong)

    # Initialize barrels
    barrel_1 = pygame.image.load("barrel sprite.png").convert_alpha()
    barrel_1 = pygame.transform.smoothscale(barrel_1, (110, 110))
    barrel_1_rect = barrel_1.get_rect()
    barrel_1_rect.center = (130, 120)
    barrel_1_mask = pygame.mask.from_surface(barrel_1)

    barrel_2 = pygame.image.load("barrel sprite.png").convert_alpha()
    barrel_2 = pygame.transform.smoothscale(barrel_2, (110, 110))
    barrel_2_rect = barrel_2.get_rect()
    barrel_2_rect.center = (900, 220)
    barrel_2_mask = pygame.mask.from_surface(barrel_2)

    barrel_3 = pygame.image.load("barrel sprite.png").convert_alpha()
    barrel_3 = pygame.transform.smoothscale(barrel_3, (110, 110))
    barrel_3_rect = barrel_3.get_rect()
    barrel_3_rect.center = (320, 440)
    barrel_3_mask = pygame.mask.from_surface(barrel_3)

    barrel_4 = pygame.image.load("barrel sprite.png").convert_alpha()
    barrel_4 = pygame.transform.smoothscale(barrel_4, (110, 110))
    barrel_4_rect = barrel_4.get_rect()
    barrel_4_rect.center = (980, 620)
    barrel_4_mask = pygame.mask.from_surface(barrel_4)

    barrel_5 = pygame.image.load("barrel sprite.png").convert_alpha()
    barrel_5 = pygame.transform.smoothscale(barrel_5, (110, 110))
    barrel_5_rect = barrel_5.get_rect()
    barrel_5_rect.center = (320, 750)
    barrel_5_mask = pygame.mask.from_surface(barrel_5)

    # Initialize ball
    goal_ball = pygame.image.load("white ball sprite.png").convert_alpha()
    goal_ball = pygame.transform.smoothscale(goal_ball, (50, 50))
    goal_ball_rect = goal_ball.get_rect()
    goal_ball_rect.center = (493, 50)
    goal_ball_mask = pygame.mask.from_surface(ghost)

    # Initialize mario tube
    mario_tube = pygame.image.load("mario tube.png").convert_alpha()
    mario_tube = pygame.transform.smoothscale(mario_tube, (90, 100))
    mario_tube_rect = mario_tube.get_rect()
    mario_tube_rect.center = (70, 880)
    mario_tube_mask = pygame.mask.from_surface(mario_tube)

    # Initialize frame as 0
    frame_count = 0

    # The clock helps manage frames per second to animate
    clock = pygame.time.Clock()

    # Initialize boolean values for objects
    apple_touched = False
    cherry_touched = False
    orb_touched = True
    star_touched = False
    mushroom_touched = False
    coin_touched = False
    coin_touched2 = False
    coin_touched3 = False
    coin_touched4 = False
    coin_touched5 = False
    tube_touched = True
    moving_down = True
    moving_left = True
    moving_up = True
    moving_right = True
    moving_right2 = True
    barrel_moving1 = True
    barrel_moving2 = True
    barrel_moving3 = True
    barrel_moving4 = True
    barrel_moving5 = True
    peach_touched = False

    # Initialize starting the game by being alive
    is_alive = True

    # Initializes game by starting at level 0
    game_level = 0

    # Hides cursor
    pygame.mouse.set_visible(False)

    # Main game loop
    while is_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        # Position player to mouse location
        position = pygame.mouse.get_pos()
        player_rect.center = position

        # Draws white backgroundgv
        if game_level == 0:
            # Draws title screen
            screen.blit(title_screen, title_screen_rect)
            # Draws start button
            screen.blit(start_button, start_button_rect)
            # Draws player
            screen.blit(player, player_rect)
            # If the user presses the start button the game = 1
            if pixel_collision(player_mask, player_rect, start_button_mask, start_button_rect):
                if event.type == pygame.MOUSEBUTTONUP:
                    game_level = 1x

        # Game level 1
        if game_level == 1:
            # Draws pacman player
            screen.blit(player, player_rect)
            # Draws the level 1 map
            screen.blit(level_1_map, level_1_map_rect)
            # Draws level 1 title
            screen.blit(level_1_title, level_1_title_rect)
            # Draws fruit decor at the bottom
            screen.blit(fruit_decor, fruit_decor_rect)
            # Draws the first pink ghost
            screen.blit(ghost, ghost_rect)
            # Draws the orange ghost
            screen.blit(ghost2, ghost_rect2)
            # Programs the first ghost to move back and forth
            if moving_down:
                if ghost_rect.centery > 419:
                    moving_down = False
                ghost_rect = ghost_rect.move((0, 3))
            else:
                if ghost_rect.centery < 50:
                    moving_down = True
                ghost_rect = ghost_rect.move((0, -3))
            # Programs the second ghost to move back and forth
            if moving_right2:
                if ghost_rect2.centerx > 960:
                    moving_right2 = False
                ghost_rect2 = ghost_rect2.move((3, 0))
            else:
                if ghost_rect2.centerx < 570:
                    moving_right2 = True
                ghost_rect2 = ghost_rect2.move((-3, 0))
            # If the cherry isn't collected it'll be displayed on the screen
            if not cherry_touched:
                screen.blit(cherry, cherry_rect)
            # If the apple isn't touched it'll be displayed on the screen
            if not apple_touched:
                screen.blit(apple, apple_rect)
            # If the player collides with the apple fruit
            if pixel_collision(player_mask, player_rect, apple_mask, apple_rect):
                apple_touched = True
            # If the player collides with the cherry fruit
            if pixel_collision(player_mask, player_rect, cherry_mask, cherry_rect):
                cherry_touched = True
            # If both apple and cherry are eaten, then draw the goal ball
            if apple_touched == True and cherry_touched == True:
                screen.blit(goal_ball, goal_ball_rect)
                orb_touched = False
            # If the orb isn't collected, it is drawn
            if not orb_touched:
                screen.blit(goal_ball, goal_ball_rect)
            # If the player touches the goal ball, moves to next level
            if pixel_collision(player_mask, player_rect, goal_ball_mask, goal_ball_rect):
                orb_touched = True
                game_level = 2
            # If the player touches the walls of the maze, the game is over
            if pixel_collision(player_mask, player_rect, level_1_mask, level_1_map_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True

            # If the player touches the first ghost, game is over
            if pixel_collision(player_mask, player_rect, ghost_mask, ghost_rect):
                apple_touched = False
                cherry_touched = False
                orb_touched = True

            # If the player touches the second ghost, the game is over
            if pixel_collision(player_mask, player_rect, ghost_rect2_mask, ghost_rect2):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True

        # Start screen 2
        if game_level == 2:
            # Draws the second level start screen
            screen.blit(level_2_start_screen, level_2_start_screen_rect)
            # Draws the start button for the second level
            screen.blit(start_button2, start_button2_rect)
            # Draws the second player
            screen.blit(second_player, second_player_rect)
            # Sets the second player to follow the mouse
            position = pygame.mouse.get_pos()
            second_player_rect.center = position
            # If the start button is clicked, then the second level begins
            if pixel_collision(second_player_mask, second_player_rect, start_button_mask2, start_button2_rect):
                if event.type == pygame.MOUSEBUTTONUP:
                    game_level = 3

        # Game level 2
        if game_level == 3:

            # Draws the level 2 map
            screen.blit(level_2_map, level_2_map_rect)

            # Draws the mario map overlay with the decorations
            screen.blit(mario_map_overlay, mario_map_overlay_rect)

            # Draws the second player
            screen.blit(second_player, second_player_rect)

            # Draws mario's cloud enemy
            screen.blit(mario_enemy, mario_enemy_rect)

            # Draws the vine chomper
            screen.blit(mario_chomper, mario_chomper_rect)

            # Draws the boomba
            screen.blit(boomba_enemy, boomba_enemy_rect)

            # Sets the player sprite to the mouse location
            position = pygame.mouse.get_pos()
            second_player_rect.center = position

            # Programs the chomper to move up and down
            if moving_up:
                if mario_chomper_rect.centery > 525:
                    moving_up = False
                mario_chomper_rect = mario_chomper_rect.move((0, 1))
            else:
                if mario_chomper_rect.centery < 500:
                    moving_up = True
                mario_chomper_rect = mario_chomper_rect.move((0, -1))

            # Programs the sky mario enemy to move back and forth
            if moving_left:
                if mario_enemy_rect.centerx > 950:
                    moving_left = False
                mario_enemy_rect = mario_enemy_rect.move(3, 0)
            else:
                if mario_enemy_rect.centerx < 370:
                    moving_left = True
                mario_enemy_rect = mario_enemy_rect.move(-3, 0)

            # Programs the boomba to move left and right
            if moving_right:
                if boomba_enemy_rect.centerx > 630:
                    moving_right = False
                boomba_enemy_rect = boomba_enemy_rect.move(3, 0)
            else:
                if boomba_enemy_rect.centerx < 400:
                    moving_right = True
                boomba_enemy_rect = boomba_enemy_rect.move(-3, 0)

            # If the star is not collected, it's displayed on the screen.
            if not star_touched:
                screen.blit(star, star_rect)

            # If the coin isn't collected, it is displayed on the screen.
            if not coin_touched:
                screen.blit(coin, coin_rect)

            # If the second coin isn't collected, it is displayed on the screen.
            if not coin_touched2:
                screen.blit(coin2, coin2_rect)

            # If the mushroom is not collected, it's displayed on the screen.
            if not mushroom_touched:
                screen.blit(mushroom, mushroom_rect)

            # If the player collects the star, the collection bool is True.
            if pixel_collision(second_player_mask, second_player_rect, star_mask, star_rect):
                star_touched = True

            # If the second player touches the first coin, the collection bool is True.
            if pixel_collision(second_player_mask, second_player_rect, coin_mask, coin_rect):
                coin_touched = True

            # If the player collides with the second coin, the collection bool True.
            if pixel_collision(second_player_mask, second_player_rect, coin2_mask, coin2_rect):
                coin_touched2 = True

            # If the second player touches or "eats" the mushroom, mushroom disappears from screen.
            if pixel_collision(second_player_mask, second_player_rect, mushroom_mask, mushroom_rect):
                mushroom_touched = True

            # If the second player touches the star, coins, AND the mushroom, then draw the tube
            if star_touched == True and coin_touched == True and mushroom_touched == True and coin_touched2 == True:
                screen.blit(mario_tube, mario_tube_rect)
                tube_touched = False

            # If the tube hasn't yet been touched, it'll be shown on the screen once everything else is drawn.
            if not tube_touched:
                screen.blit(mario_tube, mario_tube_rect)

            # If the second player touches the green tube, then it is true
            if pixel_collision(second_player_mask, second_player_rect, mario_tube_mask, mario_tube_rect):
                tube_touched = True

            # If the second player touches the level 2 map, then game is over and displays game over screen
            if pixel_collision(second_player_mask, second_player_rect, level_2_map_mask, level_2_map_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True

            # If the second player touches the green tube, then move to next level
            if pixel_collision(second_player_mask, second_player_rect, mario_tube_mask, mario_tube_rect):
                game_level = 4

            # If the second player touches the sky mario enemy, then game is over and displays game over screen
            if pixel_collision(second_player_mask, second_player_rect, mario_enemy_mask, mario_enemy_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True

            # If the second player touches the mario chomper, then game is over and displays game over screen
            if pixel_collision(second_player_mask, second_player_rect, mario_chomper_mask, mario_chomper_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True

            # If the second player touches the boomba, then game is over and displays game over screen
            if pixel_collision(second_player_mask, second_player_rect, boomba_enemy_mask, boomba_enemy_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True

        # Start screen 3
        if game_level == 4:
            # Draws the level 3 start screen
            screen.blit(level_3_start_screen, level_3_start_screen_rect)
            # Draws the start button for level 3
            screen.blit(start_button3, start_button3_rect)
            # Draws the third player
            screen.blit(third_player, third_player_rect)
            # Sets third player's position with wherever the mouse moves
            position = pygame.mouse.get_pos()
            third_player_rect.center = position
            # If the level 3 start button is clicked, then move to level 3
            if pixel_collision(third_player_mask, third_player_rect, start_button_mask3, start_button3_rect):
                if event.type == pygame.MOUSEBUTTONUP:
                    game_level = 5

        # Game level 3
        if game_level == 5:
            # Fills the background with black color
            screen.fill((0, 0, 0))
            # Draws the level 3 map
            screen.blit(level_3_map, level_3_map_rect)
            # Draws the third player
            screen.blit(third_player, third_player_rect)
            # Draws donkey kong
            screen.blit(donkey_kong, donkey_kong_rect)
            # Draws all the barrels for each line on map
            screen.blit(barrel_1, barrel_1_rect)
            screen.blit(barrel_2, barrel_2_rect)
            screen.blit(barrel_3, barrel_3_rect)
            screen.blit(barrel_4, barrel_4_rect)
            screen.blit(barrel_5, barrel_5_rect)
            # Draws princess peach
            screen.blit(peach, peach_rect)

            # Sets the position of the third player wherever the mouse moves
            position = pygame.mouse.get_pos()
            third_player_rect.center = position

            # Programs each of the barrels to move back and fourth
            if barrel_moving1:
                if barrel_1_rect.centerx > 990:
                    barrel_moving1 = False
                barrel_1_rect = barrel_1_rect.move((3, 0))
            else:
                if barrel_1_rect.centerx < 40:
                    barrel_moving1 = True
                barrel_1_rect = barrel_1_rect.move((-3, 0))

            if barrel_moving2:
                if barrel_2_rect.centerx > 990:
                    barrel_moving2 = False
                barrel_2_rect = barrel_2_rect.move((3, 0))
            else:
                if barrel_2_rect.centerx < 100:
                    barrel_moving2 = True
                barrel_2_rect = barrel_2_rect.move((-3, 0))

            if barrel_moving3:
                if barrel_3_rect.centerx > 990:
                    barrel_moving3 = False
                barrel_3_rect = barrel_3_rect.move((3, 0))
            else:
                if barrel_3_rect.centerx < 200:
                    barrel_moving3 = True
                barrel_3_rect = barrel_3_rect.move((-3, 0))

            if barrel_moving4:
                if barrel_4_rect.centerx > 990:
                    barrel_moving4 = False
                barrel_4_rect = barrel_4_rect.move((3, 0))
            else:
                if barrel_4_rect.centerx < 200:
                    barrel_moving4 = True
                barrel_4_rect = barrel_4_rect.move((-3, 0))

            if barrel_moving5:
                if barrel_5_rect.centerx > 990:
                    barrel_moving5 = False
                barrel_5_rect = barrel_5_rect.move((3, 0))
            else:
                if barrel_5_rect.centerx < 200:
                    barrel_moving5 = True
                barrel_5_rect = barrel_5_rect.move((-3, 0))

            # If the player collides with the walls of the map, the game is over
            if pixel_collision(third_player_mask, third_player_rect, level_3_map_mask, level_3_map_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False

            # If the player collides with Donkey Kong, the game is over
            if pixel_collision(third_player_mask, third_player_rect, donkey_kong_mask, donkey_kong_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False

            # If the player collides with any of the barrels, the game is over
            if pixel_collision(third_player_mask, third_player_rect, barrel_1_mask, barrel_1_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False
            if pixel_collision(third_player_mask, third_player_rect, barrel_2_mask, barrel_2_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False
            if pixel_collision(third_player_mask, third_player_rect, barrel_3_mask, barrel_3_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False
            if pixel_collision(third_player_mask, third_player_rect, barrel_4_mask, barrel_4_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False
            if pixel_collision(third_player_mask, third_player_rect, barrel_5_mask, barrel_5_rect):
                game_level = -1
                apple_touched = False
                cherry_touched = False
                orb_touched = True
                star_touched = False
                mushroom_touched = False
                coin_touched = False
                coin_touched2 = False
                coin_touched3 = False
                coin_touched4 = False
                coin_touched5 = False
                tube_touched = True
                moving_down = True
                moving_left = True
                moving_up = True
                moving_right = True
                moving_right2 = True
                barrel_moving1 = True
                barrel_moving2 = True
                barrel_moving3 = True
                barrel_moving4 = True
                barrel_moving5 = True
                peach_touched = False

            # If the third player touches princess peach, she disappears from the screen
            if pixel_collision(third_player_mask, third_player_rect, peach_mask, peach_rect):
                peach_touched = True

            # if player touches coin, coin is collected and disappears
            if pixel_collision(third_player_mask, third_player_rect, coin3_mask, coin3_rect):
                coin_touched3 = True

            # if player touches coin, coin is collected and disappears
            if pixel_collision(third_player_mask, third_player_rect, coin4_mask, coin4_rect):
                coin_touched4 = True

            # if player touches coin, coin is collected and disappears
            if pixel_collision(third_player_mask, third_player_rect, coin5_mask, coin5_rect):
                coin_touched5 = True

            # if coin is not collected, the draw the coin
            if not coin_touched3:
                screen.blit(coin3, coin3_rect)

            # if coin is not collected, the draw the coin
            if not coin_touched4:
                screen.blit(coin4, coin4_rect)

            # if coin is not collected, the draw the coin
            if not coin_touched5:
                screen.blit(coin5, coin5_rect)

            # If the coins and princess peach are all collected, then you win and game is complete!
            if peach_touched == True and coin_touched3 == True and coin_touched4 == True and coin_touched5 == True:
                game_level = 6

        # End congratulatory screen
        if game_level == 6:
            screen.blit(end_screen, end_screen_rect)

        # Failed game screen
        if game_level == -1:
            screen.blit(game_over_screen, game_over_rect)
            if event.type == pygame.MOUSEBUTTONUP:
                game_level = 0

        # Initializes increasing frame count by updating the display each frame
        frame_count += 1
        pygame.display.update()

        # Sets frame rate to 30
        clock.tick(30)

    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
