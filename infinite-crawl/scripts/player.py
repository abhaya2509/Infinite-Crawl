import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, start_pos):
        self.mode = "arcade"
        self.velocity = Vector2(0,0)
        self.friction = 0.15
        self.pos = Vector2(start_pos)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 32, 32)
        self.speed = 300.0
        self.dash_speed = 1200
        self.dash_duration = 0.15
        self.dash_timer = 0
        self.is_dashing = False
        self.facing_direction = (1,0)


    def update(self, dt, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # 1. Check for P Key (Mode Toggle)
                if event.key == pygame.K_p:  
                    if self.mode == "arcade":
                        self.mode = "realistic"
                    else:
                        self.mode = "arcade"
                
                # 2. Check for Shift Key (Dash)
                # This is now OUTSIDE the P-key block, but still inside KEYDOWN
                if event.key == pygame.K_LSHIFT: # Changed .type to .key
                    if not self.is_dashing:
                        self.is_dashing = True
                        self.dash_timer = self.dash_duration
        

        keys = pygame.key.get_pressed()
        direction = Vector2(0,0)        
        if keys[pygame.K_w] or keys[pygame.K_UP]: direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: direction.y += 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: direction.x += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: direction.x -= 1
            
        if direction.length() > 0:
            direction = direction.normalize()
            self.facing_direction = direction
        
        if self.is_dashing:
            self.dash_timer -= dt
            self.pos += self.facing_direction * self.dash_speed * dt
            if self.dash_timer <= 0:
                self.is_dashing = False
                self.velocity = Vector2(0,0)
        else:
            if self.mode == "arcade":
                self.pos += direction * self.speed * dt
                self.velocity = direction * self.speed
            elif self.mode == "realistic":
                target_vel = direction * self.speed
                self.velocity = self.velocity.lerp(target_vel, self.friction)
                self.pos += self.velocity * dt




        self.rect.topleft = (round(self.pos.x), round(self.pos.y))


    def draw(self, surface):
        if self.mode == "arcade":
            pygame.draw.rect(surface, "dodgerblue", self.rect)
        elif self.mode == "realistic":
            pygame.draw.rect(surface, "hotpink", self.rect)