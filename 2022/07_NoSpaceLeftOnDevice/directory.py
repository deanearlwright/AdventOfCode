# ======================================================================
# No Space Left On Device
#   Advent of Code 2022 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i r e c t o r y . p y
# ======================================================================
"Directory for the Advent of Code 2022 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Directory
# ======================================================================


class Directory(object):   # pylint: disable=R0902, R0205
    "Object for No Space Left On Device"

    def __init__(self, part2=False, name=None, out=None):

        # 1. Set the initial values
        self.part2 = part2
        self.name = name
        self.out = out
        self.dirs = {}
        self.files = {}

    def add_file(self, name, size):
        "Add a file to the directory"

        self.files[name] = size

    def add_dir(self, sdir):
        "Add a sub-directory to the directory"

        self.dirs[sdir.name] = sdir

    def size(self):
        "Return the size of the files in this directory and sub-directories"

        # 1. Start with nothing
        result = 0

        # 2. Add in the sizes of the files in this directory
        for fsize in self.files.values():
            result += fsize

        # 3. Add in the sizes of the files in the sub-directories
        for sdir in self.dirs.values():
            result += sdir.size()

        # 4. Return the total size
        return result

    def sizes_under(self, limit=100000):
        "Return the sizes of directories under the limit"

        # 1. Start with nothing
        result = []

        # 2. If my size under the limit, if so add it
        my_size = self.size()
        if my_size <= limit:
            result.append(my_size)

        # 3. If any of my sub-directories are under the limit, Add those in
        for sdir in self.dirs.values():
            sdir_size = sdir.sizes_under(limit)
            result.extend(sdir_size)

        # 4. Return the total sizes under the limit
        print("sizes_under", self.full_path(), result)
        return result

    def sizes_over(self, limit=30000000):
        "Return the names and sizes of directories over the limit"

        # 1. Start with nothing
        result = []

        # 2. If my size under the limit, if so add it
        my_size = self.size()
        if my_size >= limit:
            result.append(my_size)

        # 3. If any of my sub-directories are under the limit, Add those in
        for sdir in self.dirs.values():
            sdir_size = sdir.sizes_over(limit)
            result.extend(sdir_size)

        # 4. Return the total sizes under the limit
        print("sizes_over", self.full_path(), result)
        return result

    def full_path(self):
        "Return the full path of this directory"

        # 1. if root, full path is just us
        if self.name == "/":
            return "/"

        # 2. Else add our name to the outer directories
        return "/".join([self.out.full_path(), self.name]).replace("//", "/")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     d i r e c t o r y . p y                    end
# ======================================================================
