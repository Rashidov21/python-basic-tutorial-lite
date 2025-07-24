import pygame
import sys

# O'yin oynasi o'lchami
WIDTH, HEIGHT = 800, 600

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# ==== Player Klass ====
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)
        self.speed = 7

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        elif not up and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)


# ==== Ball Klass ====
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ekran yuqori/pastki chegarasidan qaytish
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x *= -1  # X yo'nalishini o'zgartiradi


# ==== Ob'ektlar ====
player1 = Player(50, HEIGHT//2 - 50)
player2 = Player(WIDTH - 70, HEIGHT//2 - 50)
ball = Ball()

# ==== O'yin sikli ====
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Klaviatura boshqaruvlari
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move(up=True)
    if keys[pygame.K_s]:
        player1.move(up=False)
    if keys[pygame.K_UP]:
        player2.move(up=True)
    if keys[pygame.K_DOWN]:
        player2.move(up=False)

    # Harakatlar
    ball.move()

    # To‘p raketkalarga tegsa yo'nalishni o'zgartiradi
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.speed_x *= -1

    # To‘p chap yoki o‘ng tomondan chiqib ketsa, qayta markazga qaytadi
    if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
        ball.reset()

    # Chizish
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

    # O'yin oynasini yangilash
    pygame.display.flip()
    clock.tick(60)
