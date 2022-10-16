import colorsys
import time
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


class Text():

    def __init__(self, lines) -> None:
        self.lines = lines

    def display(self):    
        colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x / float(len(self.lines)), 1.0, 1.0)]) for x in range(len(self.lines))]


        ANIMATION_TIME = 0.02

        unicorn.rotation(270)
        unicorn.brightness(0.6)


        width, height = unicorn.get_shape()

        text_x = width
        text_y = 2


        #font = ImageFont.truetype(font_file, font_size)
        font = ImageFont.load_default()

        text_width, text_height = width, 0


        for line in self.lines:
            w, h = font.getsize(line)
            text_width += w + width
            text_height = max(text_height, h)

        text_width += width + text_x + 1

        image = Image.new('RGB', (text_width, max(16, text_height)), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        offset_left = 0

        for index, line in enumerate(self.lines):
            draw.text((text_x + offset_left, text_y), line, colours[index], font=font)

            offset_left += font.getsize(line)[0] + width

        for scroll in range(text_width - width):
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x + scroll, y))
                    r, g, b = [int(n) for n in pixel]
                    unicorn.set_pixel(width - 1 - x, y, r, g, b)

            unicorn.show()
            time.sleep(ANIMATION_TIME)