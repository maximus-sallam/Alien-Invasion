import sys
import os
from time import sleep
import pygame
from bullet import BulletUp, BulletDown, BulletLeft, BulletRight
from alien import Alien
import math

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)

        # Play background music.
        play_music()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to the keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_w:
        fire_bullet_up(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_s:
        fire_bullet_down(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_a:
        fire_bullet_left(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_d:
        fire_bullet_right(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def fire_bullet_up(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit nor reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = BulletUp(ai_settings, screen, ship)
        bullets.add(new_bullet)
        BulletUp.bullet_sound()

def fire_bullet_down(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit nor reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = BulletDown(ai_settings, screen, ship)
        bullets.add(new_bullet)
        BulletDown.bullet_sound()

def fire_bullet_left(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit nor reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = BulletLeft(ai_settings, screen, ship)
        bullets.add(new_bullet)
        BulletLeft.bullet_sound()

def fire_bullet_right(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit nor reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = BulletRight(ai_settings, screen, ship)
        bullets.add(new_bullet)
        BulletRight.bullet_sound()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.

    # With background image
    screen.blit(ai_settings.bg_image, (0, 0))

    # With background color
    # screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        if bullet.rect.bottom >= 800:
            bullets.remove(bullet)
        if bullet.rect.left <= 0:
            bullets.remove(bullet)
        if bullet.rect.right >= 1200:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        ship.center_ship()
        play_level_up_sound()
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        # Pause.
        sleep(1.0)

        create_fleet(ai_settings, screen, ship, aliens)
    remove_bullets(ai_settings, stats, sb, aliens, bullets)

def remove_bullets(ai_settings, stats, sb, aliens, bullets):
    """Remove any bullets and aliens that have collided."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        alien_hit_sound()
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.y = alien.rect.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by aliens"""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Play sound
        hit_sound()

        # Pause.
        sleep(1.5)

    else:
        stop_music()
        play_end()
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship for hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for the aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        alien.rect.x 
    ai_settings.fleet_direction *= -1

def hit_sound():
    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound('sound/explosion.wav')
    pygame.mixer.Sound.play(hit_sound)

def alien_hit_sound():
    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound('sound/hit.wav')
    pygame.mixer.Sound.play(hit_sound)

def play_music():
    """Play background music."""
    #pygame.mixer.init()

    # All the stars are closer
    #pygame.mixer.music.load("sound/stars.wav")

    # Star wars main theme
    # pygame.mixer.music.load("sound/starwars.wav")

    #pygame.mixer.music.play(-1, 0)

def stop_music():
    """Stop background music."""
    pygame.mixer.init()
    pygame.mixer.music.stop()

def play_end():
    """Final sound after you lose."""
    pygame.mixer.init()
    pygame.mixer.music.load("sound/sad.wav")
    pygame.mixer.music.play(1, 0)

def play_level_up_sound():
    """The sound that plays every time you clear a fleet."""
    pygame.mixer.init()
    level_up_sound = pygame.mixer.Sound("sound/level_up.wav")
    pygame.mixer.Sound.play(level_up_sound)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
