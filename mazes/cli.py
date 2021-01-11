import click
import random

@click.group()
@click.option('--seed', default='', help='PRNG initialization seed.')
@click.option('--start', default='center', help='Start position, one of '
        '`center`, `random`, `top-left`, `top-right`, `bottom-left` or '
        '`bottom-right`.')
@click.option('--width', default=50, help='Maze width.', type=int)
@click.option('--height', default=15, help='Maze height.', type=int)
@click.option('--thickness', default=10, help='Pen thickness.', type=int)
@click.option('--preview', is_flag=True, help='Preview maze, no saving.')
@click.pass_context
def cli(ctx, seed, start, width, height, thickness, preview):
    '''Maze generation program.

    This program allows generating mazes according using several algorithms.
    '''
    if seed:
        random.seed(seed)

    if start == 'random':
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
    elif start == 'center':
        x = width // 2
        y = height // 2
    elif start == 'top-left':
        x = y = 0
    elif start == 'top-right':
        x = width - 1
        y = 0
    elif start == 'bottom-left':
        x = 0
        y = height - 1
    elif start == 'bottom-left':
        x = width - 1
        y = height - 1
    else:
        if 'x' in start:
            x, y = [int(v) for v in start.split('x', 1)]
        else:
            x = y = int(start)

    ctx.obj.update({
        'start': (x, y),
        'width': width,
        'height': height,
        'thickness': thickness,
        'preview': preview
    })
