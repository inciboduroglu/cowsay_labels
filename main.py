from PIL import Image, ImageFont, ImageDraw
import textwrap


def get_pixel_coord_x(x):
    return x * width / max_x


def get_pixel_coord_y(y):
    return y * height / max_y


def generate_image():
    text = "You are only young once, but you can stay immature indefinitely."
    text = textwrap.fill(text, 24)
    rows = text.split('\n')
    result = []
    for row in rows:
        result.append(row.center(24))

    join = '\n'.join(result)
    print(join)
    draw.text((get_pixel_coord_x(minXcm) + 55, get_pixel_coord_y(minYcm) + 40), join, (50, 90, 70), font=font)
    image.save('sample-out' + '.png')


max_x = 18
max_y = 8

image = Image.open('label.png')
width, height = image.size

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("VCR_OSD_MONO_1.001.ttf", 48, encoding="unic")

minXcm = 1.41
maxXcm = 7.95
minYcm = .82
maxYcm = 3.17

generate_image()
