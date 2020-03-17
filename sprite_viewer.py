import sys
import pygame
import asset_loader

__version__ = "v1.0 - 17.03.2020"
__author__ = "mikazz"

IMG_PATH = "player"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 900

BACKGROUND_COLOR = pygame.Color('black')  # The background colod of our window


class SpriteLoader:
    """Loads Sprites from given directory"""
    def __init__(self, sprite_directory_name, scale):
        self.sprite_directory_name = sprite_directory_name
        self.sprites_dictionary = asset_loader.get_asset(sprite_directory_name)
        self.scale = scale

    def animation_names(self):
        """return list of names of all avaiable animations (spritesheets) to load"""
        return list(self.sprites_dictionary.keys())

    def load(self, sprite_name):
        """load animation"""
        # Access only sprite paths that are available at given key
        sprites = self.sprites_dictionary.get(sprite_name, None)
        images = [pygame.image.load(sprite) for sprite in sprites]

        # Resize Sprites basing on dimensions of the biggest one
        max_size = max([image.get_rect().size for image in images])
        resized = tuple([ int(self.scale * i) for i in max_size ])
        images = [pygame.transform.scale(image, resized) for image in images]

        return images

    def __str__(self):
        return f"SpriteLoader Class. From directory: \n{self.sprite_directory_name}\nLoaded Sprites with size: {self.size}"

    def __repr__(self):
        return f"SpriteLoader{self.sprite_directory_name, self.scale}"


class MySprite(pygame.sprite.Sprite):
    def __init__(self, scale):
        super(MySprite, self).__init__()

        # --------------- Sprite Loading ---------------
        self.player_sprites_directory_path = IMG_PATH

        self.scale = scale

        self.player_sprites = SpriteLoader(sprite_directory_name=self.player_sprites_directory_path,
                                           scale=self.scale)

        self.all_animation_names = self.player_sprites.animation_names()
       
        # Default Animation state to show, load the first one -> 0
        self.images = self.player_sprites.load(self.all_animation_names[0])
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)

        # Animation name scrolling
        self.animation_index = 0

        # Stop animating
        self.stop = False

    def update(self):
        # Show sprite frames
        if not self.stop:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        reflect_v = pressed[pygame.K_v]
        reflect_h = pressed[pygame.K_h]
        rewind = pressed[pygame.K_r]
        next_frame = pressed[pygame.K_s]
        prev_frame = pressed[pygame.K_a]

        if next_frame:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        if prev_frame:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.images) - 1
            self.image = self.images[self.index]

        if left:
            self.animation_index -= 1
            if self.animation_index < 0:
                self.animation_index = len(self.all_animation_names) - 1  # list indexing starts from 0!

            animation_name = self.all_animation_names[self.animation_index]
            self.images = self.player_sprites.load(animation_name)

        if right:
            self.animation_index += 1
            if self.animation_index >= len(self.all_animation_names):
                self.animation_index = 0

            animation_name = self.all_animation_names[self.animation_index]
            self.images = self.player_sprites.load(animation_name)

        if reflect_h:
            # Transforms sprite horizontally up and down - (/\ X \/)
            self.images = [pygame.transform.flip(sprite, False, True) for sprite in self.images]

        if reflect_v:
            # Transforms sprite vertically right and left - (<- Y ->)
            self.images = [pygame.transform.flip(sprite, True, False) for sprite in self.images]

        if rewind:
            self.index = 0


def main():
    FPS = 10  # Frames per second
    FULLSCREEN = False
    pygame.init()
    pygame.font.init()

    myfont = pygame.font.SysFont('Consolas', 15)
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Sprite Viewer")

    try:
        application_icon = pygame.image.load('icon.png')
        pygame.display.set_icon(application_icon)
    except FileNotFoundError:
        pass

    scale = 5 # this needs to be redone
    my_sprite = MySprite(scale)
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    color = ""
    color_label = myfont.render(str(color), 1, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    pos = pygame.mouse.get_pos()
                    try:
                        color = str(my_sprite.image.get_at(pos)) + " (RGBA)"
                    except IndexError:
                        color = ""

                    color_label = myfont.render(color, 1, (255, 255, 255))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                if event.key == pygame.K_w:
                    FPS = FPS + 1
                    
                if event.key == pygame.K_q:
                    FPS = FPS - 1
                    if FPS < 0:
                        FPS = 0

                if event.key == pygame.K_z:
                    scale -= 1
                    if scale <= 1:
                        scale = 0

                    my_sprite = MySprite(scale)

                if event.key == pygame.K_x:
                    scale += 1
                    my_sprite = MySprite(scale)

                if event.key == pygame.K_SPACE:
                    if my_sprite.stop == False:
                        my_sprite.stop = True

                    elif my_sprite.stop == True:
                        my_sprite.stop = False

                if event.key == pygame.K_f:
                    if FULLSCREEN == False:
                        FULLSCREEN = True
                        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

                    elif FULLSCREEN == True:
                        FULLSCREEN = False
                        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        my_group.update()
        screen.fill(BACKGROUND_COLOR)

        screen.blit(color_label, (0, 75))

        text_surface1 = myfont.render(f'FPS: {FPS}', False, (255, 255, 255))
        text_surface2 = myfont.render(f'animation: {my_sprite.all_animation_names[my_sprite.animation_index]}', False, (255, 255, 255))
        text_surface3 = myfont.render(f'dest: {my_sprite.player_sprites_directory_path}', False, (255, 255, 255))
        text_surface4 = myfont.render(f'animations: {", ".join(my_sprite.all_animation_names)}', False, (255, 255, 255))
        text_surface5 = myfont.render(f'frame: {my_sprite.index + 1}  [{len(my_sprite.images) }]', False, (255, 255, 255))
        text_surface6 = myfont.render('[Q/W] (-/+) FPS [SPACE] Pause [V/H] Mirror [R] Rewind To Begin [A/S] Prev/Next Frame [L/R ARROWS] Next Anim Dir [F] FullScreen [ESC] Exit', False, (255, 255, 255))
        
        screen.blit(text_surface1, (0, 0))
        screen.blit(text_surface2, (0, 15))
        screen.blit(text_surface3, (0, 30))
        screen.blit(text_surface4, (0, 45))
        screen.blit(text_surface5, (0, 60))
        screen.blit(text_surface6, (0, WINDOW_HEIGHT-15))

        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)  # limit the runtime speed 


if __name__ == '__main__':
    main()
