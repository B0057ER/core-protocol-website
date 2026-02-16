import pygame
import random
import time
import math
import os
import hashlib

pygame.init()

# Change screen dimensions to match the user's desktop
pygame.display.init()
display_info = pygame.display.Info()
SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h

# Create a resizable window sized to the desktop (use RESIZABLE to allow manual resizing)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

#Give pygame window a name
pygame.display.set_caption("Reactor Core Demo")
print("Pygame display initialized")

# UI font for buttons
font = pygame.font.SysFont(None, 24)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Assets", "CG2.png")
print(f"Looking for image at: {image_path}")
print(f"File exists: {os.path.exists(image_path)}")

def file_hash(path):
    try:
        with open(path, "rb") as f:
            h = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def scale_to_fit(img, max_w, max_h, allow_upscale=False):
    iw, ih = img.get_size()
    if iw == 0 or ih == 0:
        return img
    scale = min(max_w / iw, max_h / ih)
    if not allow_upscale and scale > 1:
        scale = 1
    new_size = (max(1, int(iw * scale)), max(1, int(ih * scale)))
    return pygame.transform.smoothscale(img, new_size)


def load_image(path):
    try:
        img = pygame.image.load(path)
        # Scale image to fit the current window while preserving aspect ratio
        img = scale_to_fit(img, screen.get_width(), screen.get_height())
        img = img.convert_alpha() if img.get_alpha() else img.convert()
        print(f"Loaded image: {os.path.basename(path)} (size {img.get_size()})")
        return img, file_hash(path)
    except Exception as e:
        print(f"Error loading image (using placeholder): {e}")
        placeholder = pygame.Surface((min(400, SCREEN_WIDTH), min(300, SCREEN_HEIGHT)))
        placeholder.fill((180, 50, 50))
        pygame.draw.line(placeholder, (255, 255, 255), (0, 0), (placeholder.get_width(), placeholder.get_height()), 5)
        pygame.draw.line(placeholder, (255, 255, 255), (placeholder.get_width(), 0), (0, placeholder.get_height()), 5)
        return placeholder, None

# initial load
Test, last_hash = load_image(image_path)

# slideshow state
images_list = [
    os.path.join(script_dir, "Assets", "CG1.png"),
    os.path.join(script_dir, "Assets", "CG2.png"),
    os.path.join(script_dir, "Assets", "CG3.png"),
]
current_index = 1  # points to CG2 by default
playing = False
slide_interval_ms = 1500
last_slide_time = pygame.time.get_ticks()

# Game loop with auto/manual reload
running = True

# keep loop responsive and limit FPS
clock = pygame.time.Clock()
first_loop = True

while running:
    # compute UI element positions each frame
    btn_w, btn_h = 120, 44
    # Exit stays top-right
    btn_x = max(10, screen.get_width() - btn_w - 10)
    btn_y = 10
    exit_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
    # Play button centered on screen
    play_x = (screen.get_width() - btn_w) // 2
    play_y = (screen.get_height() - btn_h) // 2
    play_rect = pygame.Rect(play_x, play_y, btn_w, btn_h)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Manual reload
            if event.key == pygame.K_r:
                Test, last_hash = load_image(image_path)
                print("Image reloaded (manual)")
            # Quick-switch between example images in Assets
            elif event.key == pygame.K_1:
                image_path = os.path.join(script_dir, "Assets", "CG1.png")
                current_index = 0
                playing = False
                Test, last_hash = load_image(image_path)
            elif event.key == pygame.K_2:
                image_path = os.path.join(script_dir, "Assets", "CG2.png")
                current_index = 1
                playing = False
                Test, last_hash = load_image(image_path)
            elif event.key == pygame.K_3:
                image_path = os.path.join(script_dir, "Assets", "CG3.png")
                current_index = 2
                playing = False
                Test, last_hash = load_image(image_path)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Exit if the exit button is clicked
            if exit_rect.collidepoint(event.pos):
                print("Exit button clicked")
                running = False
            # Play toggle (only clickable when not playing)
            elif play_rect.collidepoint(event.pos) and not playing:
                playing = True
                current_index = 0
                image_path = images_list[current_index]
                Test, last_hash = load_image(image_path)
                last_slide_time = pygame.time.get_ticks()
                print("Playing")

    # Auto-reload when the file contents change (hash comparison)
    try:
        cur_hash = file_hash(image_path)
        if cur_hash is not None and cur_hash != last_hash:
            Test, last_hash = load_image(image_path)
            print("Image reloaded (file change)")
    except Exception as e:
        print(f"Error checking/reloading image: {e}")

    # slideshow advance when playing
    if playing and (pygame.time.get_ticks() - last_slide_time) >= slide_interval_ms:
        last_slide_time = pygame.time.get_ticks()
        current_index = (current_index + 1) % len(images_list)
        image_path = images_list[current_index]
        Test, last_hash = load_image(image_path)

    # Clear screen, draw image centered on the screen
    screen.fill((0, 0, 0))
    img_w, img_h = Test.get_size()
    img_x = (screen.get_width() - img_w) // 2
    img_y = (screen.get_height() - img_h) // 2
    screen.blit(Test, (img_x, img_y))

    # Draw Play (only when not playing) and Exit buttons (hover effect)
    mouse_pos = pygame.mouse.get_pos()
    if not playing:
        play_hover = play_rect.collidepoint(mouse_pos)
        play_color = (40, 200, 40) if play_hover else (30, 150, 30)
        pygame.draw.rect(screen, play_color, play_rect, border_radius=8)
        play_surf = font.render("Play", True, (255, 255, 255))
        px = play_rect.x + (play_rect.width - play_surf.get_width()) // 2
        py = play_rect.y + (play_rect.height - play_surf.get_height()) // 2
        screen.blit(play_surf, (px, py))

    exit_hover = exit_rect.collidepoint(mouse_pos)
    exit_color = (200, 40, 40) if exit_hover else (150, 30, 30)
    pygame.draw.rect(screen, exit_color, exit_rect, border_radius=6)
    exit_surf = font.render("Exit", True, (255, 255, 255))
    tx = exit_rect.x + (exit_rect.width - exit_surf.get_width()) // 2
    ty = exit_rect.y + (exit_rect.height - exit_surf.get_height()) // 2
    screen.blit(exit_surf, (tx, ty))
    pygame.display.flip()

    if first_loop:
        print("Main loop running — window should be visible now")
        first_loop = False

    # limit to 60 FPS and keep events responsive
    clock.tick(60)

pygame.quit()