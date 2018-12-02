"""
You notice that the device repeats the same frequency change
list over and over.
To calibrate the device, you need to find the first frequency it reaches twice.
"""

FILENAMES = ['tests_part_2/test_a.txt', 'tests_part_2/test_b.txt',
             'tests_part_2/test_c.txt', 'tests_part_2/test_d.txt', 'input.txt']


def get_first_dupe_frequency(filename):
    frequency = 0
    found_frequencies = {frequency, }
    is_dupe_found = False
    with open(filename) as changes:
        while not is_dupe_found:
            for change in changes:
                frequency += int(change)
                if frequency in found_frequencies:
                    return frequency
                found_frequencies.add(frequency)
            changes.seek(0)

    return frequency


for filename in FILENAMES:
    print('Frequency for changes in {}:'.format(
        filename), get_first_dupe_frequency(filename))
