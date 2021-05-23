import json

from PIL import Image, ImageFont, ImageDraw
import textwrap


def get_pixel_coord_x(x):
    return x * width / max_x


def get_pixel_coord_y(y):
    return y * height / max_y


def format_text(text_line):
    text = textwrap.fill(text_line, max_char)
    rows = text.split('\n')
    result = []
    for row in rows:
        result.append(row.center(max_char))

    join = '\n'.join(result)
    print(join)
    return join


def get_text_pos(draw, text, font):
    w, h = draw.textsize(text, font=font)

    coord_x_right = get_pixel_coord_x(maxXcm)
    coord_x_left = get_pixel_coord_x(minXcm)
    coord_y_down = get_pixel_coord_y(maxYcm)
    coord_y_up = get_pixel_coord_y(minYcm)

    x = ((coord_x_right - coord_x_left - w) / 2) + coord_x_left
    y = ((coord_y_down - coord_y_up - h) / 2) + coord_y_up
    return {'x': x + left_margin, 'y': y + top_margin}


def generate_image(textLine, lineCount, image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("VCR_OSD_MONO_1.001.ttf", 48, encoding="unic")
    text = format_text(textLine)
    text_pos = get_text_pos(draw, text, font)

    draw.text((text_pos['x'], text_pos['y']), text, (50, 90, 70), font=font)
    image.save('sample-out-' + str(lineCount) + '.png')


label_prop_file = 'label250prop.json'
with open(label_prop_file) as f:
    label_props = json.load(f)

max_x = label_props['max_x']
max_y = label_props['max_y']

label_file = label_props['label_file']
image = Image.open(label_file)
width, height = image.size

minXcm = label_props['minXcm']
maxXcm = label_props['maxXcm']
minYcm = label_props['minYcm']
maxYcm = label_props['maxYcm']

top_margin = label_props['top_margin']
left_margin = label_props['left_margin']

max_char = label_props['max_char']


def main():
    from sys import stdin

    count = 0
    for line in stdin:
        image = Image.open(label_file)

        print(">>> line: {}".format(line))
        generate_image(line, count, image)
        count += 1


if __name__ == "__main__":
    main()
