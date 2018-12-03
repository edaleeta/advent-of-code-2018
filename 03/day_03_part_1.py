"""
Each Elf has made a claim about which area of fabric would be ideal for
Santa's suit. All claims have an ID and consist of a single rectangle with
edges parallel to the edges of the fabric. Each claim's rectangle
is defined as follows:

The number of inches between the left edge of the fabric and the left
 edge of the rectangle.
The number of inches between the top edge of the fabric and the top
 edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a
rectangle 3 inches from the left edge,
2 inches from the top edge, 5 inches wide, and 4 inches tall.

If the Elves all proceed with their own plans,
none of them will have enough fabric.
How many square inches of fabric are within two or more claims?
"""
import re
CLAIM_MARKER = 'o'
OVERLAP_MARKER = 'X'
FILENAMES = ['tests_part_1/test_a.txt', 'input.txt']


def create_grid(width, height):
    grid = []
    for _ in range(height):
        row = [None] * width
        grid.append(row)
    return grid


def plot_claim(grid, left, top, width, height):
    for i in range(height):
        for j in range(width):
            grid[top+i][left+j] = 'o' if grid[top+i][left+j] is None else 'X'
    return


def get_count_overlap(grid, marker):
    count_overlap = 0
    for row in grid:
        for char in row:
            count_overlap += 1 if char == marker else 0
    return count_overlap


def parse_claim(claim):
    pattern = re.compile(r'^#\d+\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)')
    result = pattern.match(claim)
    return {'left': int(result.group(1)), 'top': int(result.group(2)),
            'width': int(result.group(3)), 'height': int(result.group(4))}


def get_overlap(filename):
    grid = create_grid(1000, 1000)
    with open(filename) as claims:
        for claim in claims:
            claim_details = parse_claim(claim.strip())
            plot_claim(grid, claim_details['left'], claim_details['top'],
                       claim_details['width'], claim_details['height'])
    return get_count_overlap(grid, OVERLAP_MARKER)


for filename in FILENAMES:
    print('Overlapping square inches in {}:'.format(
        filename), get_overlap(filename))
