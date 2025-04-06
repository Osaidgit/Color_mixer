import pygame as pg
import random

pg.init()
win = pg.display.set_mode((500, 450))
pg.display.set_caption("RGB Color Mixer")

# Fonts
font = pg.font.SysFont("Arial", 24, bold=True)

# Colors
white = (240, 240, 240)
gray = (200, 200, 200)
black = (30, 30, 30)
slider_color = (50, 50, 255)
button_color = (0, 180, 60)

# Scrollbar settings
bar_x = 50
bar_y = [50, 120, 190]
bar_width = 300
bar_height = 10
handle_width = 15
handle_height = 25

# Initial RGB values (0-255)
r, g, b = 0, 0, 0
handle_pos = [bar_x, bar_x, bar_x]
dragging = [False, False, False]

# Color Picker Button
button_rect = pg.Rect(180, 360, 140, 40)

def draw_slider(index, value):
    y = bar_y[index]
    pg.draw.rect(win, gray, (bar_x, y, bar_width, bar_height), border_radius=5)
    handle_x = bar_x + int((value / 255) * bar_width)
    pg.draw.rect(win, slider_color, (handle_x, y - 7, handle_width, handle_height), border_radius=8)

def draw_ui():
    win.fill(white)

    # Labels
    labels = ['Red', 'Green', 'Blue']
    values = [r, g, b]
    for i in range(3):
        text = font.render(f"{labels[i]}: {values[i]}", True, black)
        win.blit(text, (370, bar_y[i] - 5))
        draw_slider(i, values[i])

    # Color preview box
    pg.draw.rect(win, (r, g, b), (100, 240, 500, 600), border_radius=15)

    # RGB & HEX text
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    color_text = font.render(f"RGB: {r}, {g}, {b}", True, black)
    hex_text = font.render(f"HEX: {hex_code}", True, black)
    pg.draw.rect(win,gray,(160,870,250,90),border_radius = 15)
    win.blit(color_text, (180, 880))
    win.blit(hex_text, (180, 910))
    

    # Color Picker Button
    #pg.draw.rect(win, button_color, button_rect, border_radius=10)
    #button_text = font.render("Random Color", True, white)
   # win.blit(button_text, (button_rect.x + 18, button_rect.y + 8))

    pg.display.update()

def get_value_from_mouse(x):
    return min(max(0, int((x - bar_x) / bar_width * 255)), 255)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = pg.mouse.get_pos()
            # Check if clicking on sliders
            for i in range(3):
                if bar_y[i] - 7 <= my <= bar_y[i] + handle_height - 7:
                    dragging[i] = True
            # Check if clicking button
            if button_rect.collidepoint(mx, my):
                r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        elif event.type == pg.MOUSEBUTTONUP:
            dragging = [False, False, False]

    mx, my = pg.mouse.get_pos()
    for i in range(3):
        if dragging[i]:
            value = get_value_from_mouse(mx)
            if i == 0:
                r = value
            elif i == 1:
                g = value
            elif i == 2:
                b = value

    draw_ui()

pg.quit()
