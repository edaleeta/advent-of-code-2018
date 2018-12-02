"""
What letters are common between the two correct box IDs?
(In the example above, this is found by removing the differing character
from either ID, producing fgij.)
"""
from collections import Counter

FILENAMES = ['tests_part_2/test_a.txt', 'input.txt']


def create_container_id_list(filename):
    with open(filename) as container_ids:
        return [container_id.strip() for container_id in container_ids]


def get_dupes(iterable):
    iterable_counter = Counter(iterable)
    return [key for key, value in iterable_counter.items() if value > 1]


def check_omit_char_at_index(i, strings):
    strings_with_missing_char = [
        string[0:i] + string[i+1:] for string in strings
    ]
    return get_dupes(strings_with_missing_char)


def get_common_letters_target_containers(filename):
    container_ids = create_container_id_list(filename)
    for i in range(len(container_ids[0])):
        dupes_found_removing_i = check_omit_char_at_index(i, container_ids)
        if dupes_found_removing_i:
            return dupes_found_removing_i[0]


for filename in FILENAMES:
    print('Common letters for target containers in {}:'.format(
        filename), get_common_letters_target_containers(filename))
