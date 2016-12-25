import click
import random
import numpy

from cli import cli
from renderer import renderer
from directions import NORTH, SOUTH, WEST, EAST

def depth_first(width, height, start, bias=None):
    maze = numpy.zeros((width, height), dtype=numpy.bool)

    moves = []

    x, y = start
    stack = [start]

    while stack:
        maze[x, y] = True

        valid_moves = []

        if y > 0 and not maze[x, y - 1]:
            valid_moves.append(NORTH)
            if bias == 'vertical':
                valid_moves.append(NORTH)
                valid_moves.append(NORTH)
        if y < height - 1 and not maze[x, y + 1]:
            valid_moves.append(SOUTH)
            if bias == 'vertical':
                valid_moves.append(SOUTH)
                valid_moves.append(SOUTH)
        if x > 0 and not maze[x - 1, y]:
            valid_moves.append(WEST)
            if bias == 'horizontal':
                valid_moves.append(WEST)
                valid_moves.append(WEST)
        if x < width - 1 and not maze[x + 1, y]:
            valid_moves.append(EAST)
            if bias == 'horizontal':
                valid_moves.append(EAST)
                valid_moves.append(EAST)

        if not valid_moves:
            x, y = stack.pop()
        else:
            move = random.choice(valid_moves)

            stack.append((x, y))
            moves.append((x, y, move))

            if move == NORTH:
                y -= 1

            if move == SOUTH:
                y += 1

            if move == WEST:
                x -= 1

            if move == EAST:
                x += 1

    return moves

@cli.command('depth-first')
@click.option('--bias', help='Branching bias, one of `horizontal` or '
        '`vertical`.')
@click.pass_context
def depth_first_cli(ctx, bias):
    '''Generate a maze using the Depth-first modified search algorithm.

    This algorithm allows setting a bias which produces vastly different mazes.
    '''
    moves = depth_first(ctx.obj.get('width'), ctx.obj.get('height'),
            ctx.obj.get('start'), bias)

    renderer(ctx, moves)
