import os
import re
import sys

multiple = 1

def repl(mo):
    global multiple

    mo = str(int(mo.group()) * multiple)

    return mo

del sys.argv[0]

if len(sys.argv) > 0:
    for argv in sys.argv:
        if os.path.isfile(argv) and '.atlas' in argv and '.atlas_' not in argv:
            with open(argv, 'r') as f:
                data = f.read()

            multiple = 2048 // int(re.search(r'size: ([0-9]+)', data).group(1))
            data = re.sub(r'(?<=[, ])([0-9]+)', repl, data)

            with open(argv.replace('.atlas', f'_{multiple}x.atlas'), 'w') as f:
                f.write(data)
