# ======================================================================
# No Space Left On Device
#   Advent of Code 2022 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import directory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for No Space Left On Device"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.root = None
        self.current = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Create the root file system
        self.root = directory.Directory(part2=self.part2, name="/")
        self.root.out = self.root

        # 2. Initially at root
        self.current = self.root

        # 3. Loop for all of the lines of text
        for line in text:

            # 4. If a command, execute the command
            if line.startswith("$"):
                self._process_cmd(line[2:])
                continue

            # 5. If a directory, add it
            if line.startswith("dir"):
                new_dir = directory.Directory(part2=self.part2,
                                              name=line[4:],
                                              out=self.current)
                self.current.add_dir(new_dir)
                continue

            # 6. Else add the file
            size, name = line.split()
            self.current.add_file(name, int(size))

    def _process_cmd(self, cmd):
        "Execute a command"

        # 1. Break into command and argument
        parts = cmd.split()
        command = parts[0]
        argument = None
        if len(parts) > 1:
            argument = parts[1]

        # 2. Process cd command
        if command == "cd":
            if argument == "/":
                self.current = self.root
            elif argument == "..":
                self.current = self.current.out
            else:
                if argument in self.current.dirs:
                    self.current = self.current.dirs[argument]
                else:
                    print("Unable to navigate to %s from %s" % (argument, self.current.name))

        # 3. Process the ls command
        if command == "ls":
            pass

    def size_under(self, limit=100000):
        "Return the total size of directories uner the limit"

        if self.root:
            return sum(self.root.sizes_under(limit=limit))
        return None

    def smallest_to_delete(self, limit=70000000):
        "Find the size of the smallest directory to delete"

        # 1. Need a file system
        if not self.root:
            return None

        # 2. Determine the amount of space we need to free up
        total_size = 70000000
        total_used = self.root.size()
        total_free = total_size - total_used
        total_needed = 30000000
        to_find = total_needed - total_free
        print(total_size, total_used, total_free, total_needed, to_find)

        # 3. Get the sizes of possible directories
        sizes = self.root.sizes_over(limit=to_find)
        print(sizes)

        # 4. Return the smallest size available
        sizes.sort()
        return sizes[0]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
