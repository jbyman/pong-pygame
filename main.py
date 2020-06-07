"""
Simple pong game built in PyGame
"""

import pygame, sys
pygame.init()
clock = pygame.time.Clock()

#
# Display 
#

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

#
# Visual objects
#

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#
# Colors
#

light_grey = (200,200,200)

#
# Speed
#

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

#
# Score
#

basic_font = pygame.font.Font('freesansbold.ttf', 32)
player_score = 0
opponent_score = 0

#
# Game loop
#

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_speed += 7
        if event.key == pygame.K_UP:
            player_speed -= 7

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            player_speed -= 7
        if event.key == pygame.K_UP:
            player_speed += 7

    #
    # Keep the ball moving
    #

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += player_speed

    #
    # Don't collide against walls
    #

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:

        #
        # Someone won a point
        #

        if ball.left <= 0:
            player_score += 1
        else:
            opponent_score += 1

        # Go back to the start
        ball.center = (screen_width / 2, screen_height / 2)

    #
    # Paddle hitting
    #

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    #
    # Restrict player movement
    #

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    
    #
    # Opponent logic
    #

    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    #
    # Redraw screen
    #

    screen.fill((0,0,255))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width/2, screen_height))
    player_text = basic_font.render(f'{player_score}', False, light_grey)
    screen.blit(player_text,(660,470))
    opponent_text = basic_font.render(f'{opponent_score}', False, light_grey)
    screen.blit(opponent_text,(600,470))
    pygame.display.flip()
    clock.tick(60)
