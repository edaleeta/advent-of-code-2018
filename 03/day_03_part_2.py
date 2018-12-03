"""
Amidst the chaos, you notice that exactly one claim doesn't overlap by
even a single square inch of fabric with any other claim.
If you can somehow draw attention to it, maybe the Elves will
be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact
after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""
# Instead of using generic markers, add the int of the claim
# Fill in the grid with the int of the claim
# When collision occurs, discard the ints from a set.
# There should only be one claim left in the set.

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


def plot_claim(grid, left, top, width, height, claim_num, uncollided_claims):
    for i in range(height):
        for j in range(width):
            current_grid_value = grid[top+i][left+j]
            if current_grid_value is not None:
                uncollided_claims.discard(current_grid_value)
                uncollided_claims.discard(claim_num)
            grid[top+i][left+j] = claim_num
    return


def parse_claim(claim):
    pattern = re.compile(r'^#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)')
    result = pattern.match(claim)
    return {'claim_num': int(result.group(1)), 'left': int(result.group(2)),
            'top': int(result.group(3)), 'width': int(result.group(4)),
            'height': int(result.group(5))}


def get_intact_claim(filename):
    uncollided_claims = set()
    grid = create_grid(1000, 1000)
    with open(filename) as claims:
        for claim in claims:
            claim_details = parse_claim(claim.strip())
            uncollided_claims.add(claim_details['claim_num'])
            plot_claim(grid, claim_details['left'], claim_details['top'],
                       claim_details['width'], claim_details['height'],
                       claim_details['claim_num'], uncollided_claims)
    return uncollided_claims.pop()


for filename in FILENAMES:
    print('Intact claim in {}:'.format(
        filename), get_intact_claim(filename))
