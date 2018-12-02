"""
To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter.
You can multiply those two counts together to get a rudimentary checksum and
compare it to what your device predicts.
"""
from collections import Counter

FILENAMES = ['tests_part_1/test_a.txt', 'input.txt']


def get_checksum(filename):
    count_letter_freq_two = 0
    count_letter_freq_three = 0
    with open(filename) as container_ids:

        for container_id in container_ids:
            container_id_clean = container_id.strip()
            count_letter_freq_two += 1 if has_x_dupes(
                container_id_clean, 2) else 0
            count_letter_freq_three += 1 if has_x_dupes(
                container_id_clean, 3) else 0

    return count_letter_freq_two * count_letter_freq_three


def has_x_dupes(iterable, x):
    iterable_counter = Counter(iterable)
    if x in iterable_counter.values():
        return True
    return False


for filename in FILENAMES:
    print('Checksum result for {}:'.format(
        filename), get_checksum(filename))
