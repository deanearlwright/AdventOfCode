# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c . p y
# ======================================================================
"Generates base programming source files for Advent of Code"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import datetime
import glob
import os
import shutil
import subprocess
import sys

from collections import namedtuple

import aoc_javascript as js
import aoc_python as py
import aoc_rust as rust
import aoc_typescript as ts
import aoc_lua as lua
import aoc_go as go

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Lang = namedtuple("Lang", "files, extra, before, after")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INPUT_FILE_NAME = 'input.txt'

# ----- languages


LANGUAGES = {
    'python': Lang(py.PYTHON_FILES, py.PYTHON_EXTRA,
                   py.python_before, py.python_after),
    'javascript': Lang(js.JAVASCRIPT_FILES, js.JAVASCRIPT_EXTRA,
                       js.js_before, js.js_after),
    'typescript': Lang(ts.TYPESCRIPT_FILES, ts.TYPESCRIPT_EXTRA,
                       ts.ts_before, ts.ts_after),
    'lua': Lang(lua.LUA_FILES, lua.LUA_EXTRA,
                lua.lua_before, lua.lua_after),
    'go': Lang(go.GO_FILES, go.GO_EXTRA,
               go.go_before, go.go_after),
    'rust': Lang(rust.RUST_FILES, rust.RUST_EXTRA,
                 rust.rust_before, rust.rust_after)
}

# ----- Substitions

SUBSTITUTIONS = {
    'DD': 'DD',
    'D D': 'D D',
    'DIR': 'DIR',
    'DIRLOWER': 'DIRLOWER',
    'YYYY': 'YYYY',
    'TITLE': 'TITLE',
    'CLASS': 'CLASS',
    'MODULE': 'MODULE',
    'M O D U L E': 'M O D U L E',
    'RESULT': 'RESULT',
    'RCHECK': 'RCHECK',
    'NOTCHK': 'NOTCHK'
}

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Determine defaults for year and day
    today = datetime.date.today()
    if today.month == 12:
        default_year = today.year
        default_day = today.day
    else:
        default_year = None
        default_day = None
    default_dir = os.getcwd()

    # 2. Create the command line parser
    desc = 'Advent of Code source file generator'
    sample = 'sample: python aoc.py --py -d 17 My Little Programs'
    parser = argparse.ArgumentParser(description=desc, epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, dest='verbose',
                        help='Print status messages to stdout')
    parser.add_argument('-l', '--language',
                        choices=['python', 'javascript', 'typescript'],
                        help='Programming language (python or javascript)')
    parser.add_argument('-i', '--input', action='store',
                        default="", dest='inval',
                        help='Puzzle input from web page')
    parser.add_argument('-c', '--class', action='store',
                        default="Solver", dest='cname',
                        help='Name of class')
    parser.add_argument('-r', '--result', action='store',
                        default="int", dest='rtype',
                        choices=['str', 'int'], help='Name of class')
    parser.add_argument('-y', '--year', action='store', default=default_year,
                        help="Year of puzzle", dest='year', type=int)
    parser.add_argument('-d', '--day', action='store', default=default_day,
                        help="Day of puzzle", dest='day', type=int)
    parser.add_argument('-b', '--base', action='store',
                        default=default_dir, dest='base',
                        help="base direcotory of Advent of Code")
    parser.add_argument('title', action='store', type=str, nargs='*',
                        help="Title of puzzle")
    parser.add_argument('-a', '--add', action='store_true', default=False,
                        dest='add', help='Add files to existing directory')
    parser.add_argument('-t', '--text', action='store_true', default=False,
                        dest='aocd', help='Download input.txt using aocd')
    parser.add_argument('-e', '--extra', action='append',
                        dest='enames', help='Extra class file')
    parser.add_argument('--py', dest='language',
                        action='store_const', const='python',
                        help='Programming language is python')
    parser.add_argument('--js', dest='language',
                        action='store_const', const='javascript',
                        help='Programming language is javascript')
    parser.add_argument('--ts', dest='language',
                        action='store_const', const='typescript',
                        help='Programming language is typescript')
    parser.add_argument('--lua', dest='language',
                        action='store_const', const='lua',
                        help='Programming language is lua')
    parser.add_argument('--go', dest='language',
                        action='store_const', const='go',
                        help='Programming language is go')
    parser.add_argument('--rust', dest='language',
                        action='store_const', const='rust',
                        help='Programming language is rust')
    parser.add_argument('--clean', dest='language',
                        action='store_const', const='clean',
                        help='Clean non-executables from year')
    parser.add_argument('--update', dest='language',
                        action='store_const', const='update',
                        help='Update node_modules and package[-lock].json')

    # 3. Get the options and arguments
    args = parser.parse_args()

    # 4. Check for required arguments
    check_args(args, parser)

    # 5. Ensure base and year directories exist but not the day
    if not os.path.isdir(args.base):
        parser.error(f"Base directory ({args.base}) does not exist")
    base_year = os.path.join(args.base, str(args.year))
    if not os.path.isdir(base_year):
        parser.error("Year directory ({base.year}) does not exist")
    if args.language not in ['clean', 'update']:
        day_begins = f"{args.day:02d}_"
        with os.scandir(base_year) as scan_dir:
            for entry in scan_dir:
                if entry.name.startswith(day_begins) and \
                        entry.is_dir() and not args.add:
                    parser.error(f"Day directory ({entry.name})"
                                 f" already exists")

    # 6. If there is no class name, use last word in title
    if not args.cname:
        args.cname = args.title[-1]
    args.ename = ''

    # 7. Return the arguments
    return args

# ----------------------------------------------------------------------
#                                                             check_args
# ----------------------------------------------------------------------


def check_args(args, parser):
    "Ensure we have required arguments (year, day, title, and language)"

    # 1. We have to have a language
    if not args.language:
        parser.error("Programming language is required")
    # 2. And most certainly a year
    if not args.year:
        parser.error("Puzzle year is required")
    if args.year > 2049 or args.year < 2015:
        parser.error("Year must be 2015-2049")
    # 3. Really want a title as well
    if not args.title or len(''.join(args.title)) < 3:
        parser.error("Puzzle title is required")
    # 4. If cleaning, we want a title of clean (just to be sure)
    if args.language == 'clean':
        if ''.join(args.title) != 'clean':
            parser.error("Use title of 'clean' with --clean")
    elif args.language == 'update':
        if ''.join(args.title) != 'update':
            parser.error("Use title of 'update' with --update")
    else:
        if not args.day:
            parser.error("Puzzle day is required")
        if args.day > 25 or args.day < 1:
            parser.error("Day must be 1-25")


# ----------------------------------------------------------------------
#                                                             copy_files
# ----------------------------------------------------------------------


def copy_files(args, day_directory):
    """Copy language files to day directory"""

    # 1. Get list of language specific files and pre and post converters
    lang = LANGUAGES[args.language]

    # 2. Execute the build converter function for this language
    text_converters = lang.before(args)

    # 3. Loop for all the files
    for file_info in lang.files.items():

        # 4. Process this single file
        copy_file(args, day_directory, text_converters,
                  lang.after, file_info)

    # 5. Loop for any extra files
    if args.enames:
        for ename in args.enames:

            # 6. Get the converters
            args.ename = ename
            text_converters = lang.before(args)

            # 7. Loop for the extra files
            for file_info in lang.extra.items():

                # 8. Process this single file
                copy_file(args, day_directory, text_converters,
                          lang.after, file_info)

# ----------------------------------------------------------------------
#                                                              copy_file
# ----------------------------------------------------------------------


def copy_file(args, day_directory,   # pylint: disable=R0913
              text_converters, after, file_info,
              overwrite=False):
    """Copy a single language file to day directory"""

    # 1. Get full path of output file
    raw_file_name, raw_file_text = file_info
    out_file_name = get_file_name(day_directory,
                                  raw_file_name, text_converters)

    # 2. Don't write if the file already exists
    if os.path.isfile(out_file_name) and not overwrite:
        print(f"File {out_file_name} already exists, skipping")
        return

    # 3. Convert the text for this file
    converted_text = convert_text(text_converters, raw_file_text)

    # 4. Do any final conversion
    final_text = after(args, text_converters, converted_text)

    # 5. Write file
    with open(out_file_name, 'w', encoding="utf8") as output_file:
        output_file.write(final_text)

# ----------------------------------------------------------------------
#                                                          get_file_name
# ----------------------------------------------------------------------


def get_file_name(day_directory, raw_file_name, converters):
    "Get full path name of file"

    # 1. Convert the raw file name
    converted_file_name = convert_text(converters, raw_file_name)

    # 2. Return the complete file name
    return os.path.join(day_directory, converted_file_name)

# ----------------------------------------------------------------------
#                                                           convert_text
# ----------------------------------------------------------------------


def convert_text(converters, raw_text):
    "Get processed text by successively applying converters"

    # 1. Start with the initial text
    result = raw_text

    # 2. Loop for all of the converters
    for conv_from, conv_to in converters.items():

        # 3. Make this replacement
        result = result.replace(conv_from, conv_to)

    # 4. Return the converted text
    return result

# ----------------------------------------------------------------------
#                                                              clean_day
# ----------------------------------------------------------------------


def clean_day(year_dir, day_dir):
    "Remove non-source files from the year"

    # 1. Remove node_modules if it exists
    node_modules_dir = os.path.join(year_dir, day_dir, 'node_modules')
    if os.path.isdir(node_modules_dir):
        print(f"Deleting {node_modules_dir}", flush=True)
        shutil.rmtree(node_modules_dir)

    # 2. Remove __pycache__ if it exists
    pycache_dir = os.path.join(year_dir, day_dir, '__pycache__')
    if os.path.isdir(pycache_dir):
        print(f"Deleting {pycache_dir}", flush=True)
        shutil.rmtree(pycache_dir)

    # 3. Remove test/__pycache__ if it exists
    pycache_dir = os.path.join(year_dir, day_dir, 'test/__pycache__')
    if os.path.isdir(pycache_dir):
        print(f"Deleting {pycache_dir}", flush=True)
        shutil.rmtree(pycache_dir)

    # 4. Remove .mypy_pycache if it exists
    mypycache_dir = os.path.join(year_dir, day_dir, '.mypy_pycache')
    if os.path.isdir(mypycache_dir):
        print(f"Deleting {mypycache_dir}", flush=True)
        shutil.rmtree(mypycache_dir)

    # 5. Remove any exe files
    for exe_file in glob.glob(os.path.join(year_dir, day_dir, '*.exe')):
        print(f"Deleting {exe_file}", flush=True)
        os.remove(exe_file)


# ----------------------------------------------------------------------
#                                                             clean_year
# ----------------------------------------------------------------------


def clean_year(args):
    """Remove non-source files from the year"""
    print(f"Cleaning year {args.year}", flush=True)
    # 1. Get the directory for the year
    year_dir = os.path.join(args.base, str(args.year))
    # 2. Loop for all of the days in the year
    for day_dir in os.listdir(year_dir):
        clean_day(year_dir, day_dir)

    # 3 Return success
    return 0

# ----------------------------------------------------------------------
#                                                    update_package_json
# ----------------------------------------------------------------------


def update_package_json(args, day_directory):
    "Rebuild package.json file for a single day"

    # 1. Insure that there is a package.json file
    json_file = os.path.join(day_directory, 'package.json')
    if not os.path.isfile(json_file):
        print(f"No package.json ({json_file})", flush=True)
        return 1
    print(f"Updating package json file {json_file}", flush=True)

    # 2. Determine if javascript or typescript
    language = 'javascript'
    if len(glob.glob(os.path.join(day_directory, '*.ts'))) > 0:
        language = 'typescript'

    # 3. Get list of language specific files and pre and post converters
    lang = LANGUAGES[language]

    # 4. Execute the build converter function for this language
    text_converters = lang.before(args)

    # 5. Get this languages file_info javascript
    file_info = ('package.json', lang.files['package.json'])

    # 6. Process this single file
    copy_file(args, day_directory, text_converters,
              lang.after, file_info, overwrite=True)

    # 7 Return success
    return 0

# ----------------------------------------------------------------------
#                                                             update_day
# ----------------------------------------------------------------------


def update_day(args, year_dir, day_dir):
    "Rebuild package[-lock].json and node_modules for a single day"

    # 1. Insure that there is a package.json file
    day_directory = os.path.join(year_dir, day_dir)
    json_file = os.path.join(day_directory, 'package.json')
    if not os.path.isfile(json_file):
        print(f"No package.json ({json_file})", flush=True)
        return 1

    # 2. Remove node_modules if it exists
    node_modules_dir = os.path.join(day_directory, 'node_modules')
    if os.path.isdir(node_modules_dir):
        print(f"Deleting {node_modules_dir}", flush=True)
        shutil.rmtree(node_modules_dir)
    if os.path.isdir(node_modules_dir):
        print(f"Unable to Delete {node_modules_dir}", flush=True)
        return 2

    # 3. Create empty node_module directory
    os.mkdir(node_modules_dir)
    if not os.path.isdir(node_modules_dir):
        print(f"Unable to create {node_modules_dir}", flush=True)
        return 3

    # 4. Remove package-lock.json if it exists
    lock_file = os.path.join(day_directory, 'package-lock.json')
    if os.path.isfile(lock_file):
        print(f"Deleting {lock_file}", flush=True)
        os.remove(lock_file)
    if os.path.isfile(lock_file):
        print(f"Unable to delete {lock_file}", flush=True)
        return 4

    # 5. Verify the npm cache
    print("Verifying the npm cache", flush=True)
    os.system('npm cache verify')

    # 6. Regenerate package.json
    update_package_json(args, day_directory)

    # 7. Update packages to node_modules
    print("Updating packages to node_modules", flush=True)
    current_dir = os.getcwd()
    os.chdir(day_directory)
    os.system('npm update -include=dev')
    os.chdir(current_dir)

    # 8. Check that the package-lock file was created
    if not os.path.isfile(lock_file):
        print(f"Unable to create {lock_file}", flush=True)
        return 8

    # 9. Return success
    return 0

# ----------------------------------------------------------------------
#                                                            update_year
# ----------------------------------------------------------------------


def update_year(args):
    """Do npm install (creating package-lock.json) from the year"""
    print(f"npm update year {args.year}", flush=True)

    # 1. Get the directory for the year
    year_dir = os.path.join(args.base, str(args.year))

    # 2. Assume that all will go well
    problem = 0

    # 3. Loop for all of the days in the year
    for day_dir in os.listdir(year_dir):

        # 4. Determine day from day_dir
        if day_dir[2] != '_':
            print(f"Invalid day {day_dir}")
            return 4
        args.day = int(day_dir[:2])

        # 5. Install the day
        problem = update_day(args, year_dir, day_dir)
        if problem != 0:
            return 500 + problem

    # 5. Return success (or failure)
    return problem


# ----------------------------------------------------------------------
#                                                             aocd_input
# ----------------------------------------------------------------------
def aocd_input(args):
    "Download input.txt using aocd"

    # 1. Get the directory of the input.txt file
    base_year_day = os.path.join(args.base, str(args.year),
                                 f"{args.day:02d}_{''.join(args.title)}")

    # 2. Get the compilete input.txt path
    input_txt_path = os.path.join(base_year_day, INPUT_FILE_NAME)

    # 3. Create the input.txt file
    input_txt_file = open(input_txt_path, "w", encoding="utf8")

    # 4. Create the aocd command
    aocd_cmd = f"aocd {args.day} {args.year}"

    # 5. Use aocd to populate the file
    subprocess.Popen(aocd_cmd, stdout=input_txt_file)


# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Generate base programming files for Advent of Code solver"""

    # 1. Get the command line options
    args = parse_command_line()

    # 2. If cleaning or update, go do it
    if args.language == 'clean':
        return_code = clean_year(args)
        sys.exit(return_code)
    elif args.language == 'update':
        return_code = update_year(args)
        sys.exit(return_code)

    # 3. Create the day directory (if needed)
    base_year_day = os.path.join(args.base, str(args.year),
                                 f"{args.day:02d}_{''.join(args.title)}")
    if args.add:
        if not os.path.isdir(base_year_day):
            print(f"Missing day directory {base_year_day}")
            sys.exit(1)
    else:
        os.mkdir(base_year_day)

    # 4. Copy files to the day directory
    copy_files(args, base_year_day)

    # 5. Create input file for sepecified input (if any)
    if args.inval:
        with open(os.path.join(base_year_day, INPUT_FILE_NAME),
                  "w", encoding="utf8") as input_txt:
            input_txt.write(args.inval)
            input_txt.write('\n')

    # 6. Use aocd to create input.txt (if requested)
    if args.aocd:
        aocd_input(args)

    # 7. Check for input.txt file (if we should have built it)
    if args.inval or args.aocd:
        input_txt_file = os.path.join(base_year_day, INPUT_FILE_NAME)
        if not os.path.isfile(input_txt_file):
            print(f"Unable to create {input_txt_file}")
            sys.exit(1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ======================================================================
# end                            a o c . p y                         end
# ======================================================================
