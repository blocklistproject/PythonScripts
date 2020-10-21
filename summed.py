import glob
from typing import Generator

OUTPUT_FILE = 'everything.txt'


def read_files(files: Generator[str, None, None]) -> str:
    for f in files:
        # Skip output file
        if f != OUTPUT_FILE:
            for line in open(f, 'r'):
                # Skip comments and empty lines
                if line[0] not in ['#', '\n']:
                    yield line


def get_header(line_count: int) -> str:
    # Info text to go on top, format at "Total number of network filters"
    return ('#------------------------------------[UPDATE]--------------------------------------\n'
            '# Title: The Block List Project\n'
            '# Expires: 1 day\n'
            '# Homepage: https://blocklist.site\n'
            '# Help: https://github.com/blocklistproject/lists/wiki/\n'
            '# License: https://unlicense.org\n'
            f'# Total number of network filters: {line_count}\n'
            '#------------------------------------[SUPPORT]-------------------------------------\n'
            '# You can support by:\n'
            '# - reporting false positives\n'
            '# - making a donation: https://paypal.me/blocklistproject\n'
            '#-------------------------------------[INFO]---------------------------------------\n'
            '#\n'
            '# Summed list\n'
            '#------------------------------------[FILTERS]-------------------------------------\n')


# Get every .txt file in folder
txt_files = (f for f in glob.glob('*.txt'))

# Read all .txt-files and save non-duplicate lines
lines_set = set(read_files(txt_files))

with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(get_header(len(lines_set)))
    output_file.write(''.join(lines_set))
