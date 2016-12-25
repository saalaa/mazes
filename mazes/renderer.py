import tempfile

from PIL import Image, ImageDraw
from directions import NORTH, SOUTH, WEST, EAST


BACKGROUND_COLOR = (0, 190, 220, 0)
PATH_COLOR = 'white'
START_COLOR = 'green'

def renderer(ctx, moves):
    width = ctx.obj.get('width')
    height = ctx.obj.get('height')
    thickness = ctx.obj.get('thickness')

    size = (width * thickness * 2 + thickness, height * thickness * 2 +
            thickness)

    image = Image.new('RGB', size, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    for move in moves:
        x, y, direction = move

        # Pointing to the top-left corner of the source cell
        x = x * thickness + x * thickness + thickness
        y = y * thickness + y * thickness + thickness

        if direction == NORTH:
            x1, y1 = x, y - thickness * 2
            x2, y2 = x + thickness, y + thickness

        if direction == SOUTH:
            x1, y1 = x, y
            x2, y2 = x + thickness, y + thickness * 3

        if direction == WEST:
            x1, y1 = x - thickness * 2, y
            x2, y2 = x + thickness, y + thickness

        if direction == EAST:
            x1, y1 = x, y
            x2, y2 = x + thickness * 3, y + thickness

        draw.rectangle((x1, y1, x2 - 1, y2 - 1), fill=PATH_COLOR)

    x, y = ctx.obj.get('start')

    x = x * thickness + x * thickness + thickness
    y = y * thickness + y * thickness + thickness

    draw.rectangle((x, y, x + thickness - 1, y + thickness - 1),
            fill=START_COLOR)

    if ctx.obj.get('preview'):
        image.show()
    else:
        fd, filename = tempfile.mkstemp(dir='.', prefix='maze-', suffix='.png')

        print('Writing ' + filename)

        image.save(filename)
