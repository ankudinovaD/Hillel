import pygame
import random

# Ініціалізація pygame
pygame.init()

# Налаштування вікна
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Магічна Куля")

# Колір фону та тексту
background_color = (0, 0, 0)  # Чорний фон
text_color = (255, 255, 255)  # Білий текст

# Шрифт
font = pygame.font.Font(None, 36)

# Відповіді магічної кулі
responses = [
    "Так!",
    "Ні!",
    "Можливо.",
    "Я не впевнений.",
    "Зачекай, я ще не готовий відповісти.",
    "Не схоже, що це буде."
]

def magic_ball():
    screen.fill(background_color)  # Очищаємо екран
    title = font.render("Запитай у магічної кулі!", True, text_color)
    screen.blit(title, (50, 50))  # Виводимо текст на екран

    # Оновлюємо екран
    pygame.display.flip()

    # Чекати натискання клавіші для отримання відповіді
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_input = False

    # Вивести випадкову відповідь
    response = random.choice(responses)
    screen.fill(background_color)  # Очищаємо екран
    response_text = font.render(response, True, text_color)
    screen.blit(response_text, (100, 150))  # Виводимо відповідь на екран

    # Оновлюємо екран
    pygame.display.flip()

    # Затримка перед закриттям
    pygame.time.wait(2000)  # Зачекати 2 секунди

# Виклик функції магічної кулі
magic_ball()

# Закриття pygame
pygame.quit()