
# ======================================================================
# Disk Fragmenter
#   Advent of Code 2024 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i s k m a p . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
File = namedtuple('File', "fid, floc, flen")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FREE = -1

# ======================================================================
#                                                                Diskmap
# ======================================================================


class Diskmap(object):   # pylint: disable=R0902, R0205
    "Object for Disk Fragmenter"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.free = []
        self.files = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. There is only one line
        assert len(self.text) == 1
        line = self.text[0]

        # 2. Let's start at the very beginning
        file_id = 0
        file_loc = 0
        is_file = True

        # 3. Loop for every number in the line
        for char in line:
            number = int(char)

            # 4. Save file or free space
            if is_file:
                if number == 0:
                    print(f"Zero length file: id={file_id} loc={file_loc}")
                self.files.append(File(fid=file_id, floc=file_loc, flen=number))
                file_id += 1
            else:
                if number > 0:
                    self.free.append(File(fid=FREE, floc=file_loc, flen=number))

            # 5. Advance to the next location
            file_loc += number
            is_file = not is_file

    def compact(self):
        "compact the file system"

        # 1. Start with (almost) nothing
        new_files = [self.files[0]]
        del self.files[0]
        use_free = 0

        # 2. Loop until all the free space is used up (or no more files)
        while use_free < len(self.free) and len(self.files) > 0:

            # 3. Will all of the last file fit in the first free location
            free = self.free[use_free]
            file = self.files[-1]
            if free.flen >= file.flen:

                # 4. Yes, use the free space and eliminate the file
                new_files.append(File(fid=file.fid, floc=free.floc, flen=file.flen))
                left_free = free.flen - file.flen
                if left_free > 0:
                    self.free[use_free] = \
                        File(fid=free.fid, floc=free.floc + file.flen, flen=left_free)
                else:
                    use_free += 1
                del self.files[-1]

            else:
                # 5. Use what we can
                new_files.append(File(fid=file.fid, floc=free.floc, flen=free.flen))
                self.files[-1] = File(fid=file.fid, floc=file.floc, flen=file.flen - free.flen)
                use_free += 1

            # 6. Left in place file below free space
            if (use_free < len(self.free) and len(self.files) > 0 and
                    self.files[0].floc < self.free[use_free].floc):
                new_files.append(self.files[0])
                del self.files[0]

        # 6. Keep what ever is left of the free space
        self.free = self.free[use_free:]

        # 7. New compacted files
        self.files = new_files
        # print(self.files)

    def compact_two(self):
        "compact the file system"

        # 1. Start with (almost) nothing
        new_files = [self.files[0]]
        del self.files[0]

        # 2. We process files right to left
        self.files.reverse()
        for file in self.files:

            # 3. Find the first free space for this file
            use_free = None
            use_index = -1
            for indx, free in enumerate(self.free):
                if free.flen >= file.flen and free.floc < file.floc:
                    use_free = free
                    use_index = indx
                    break

            # 4. If no space for this file, leave it in position
            if use_free is None:
                new_files.append(file)
                continue

            # 5. Insert the file here
            new_file = File(fid=file.fid, floc=use_free.floc, flen=file.flen)
            new_files.append(new_file)

            # 6. If we use all of the free space, eliminate it
            if file.flen == use_free.flen:
                del self.free[use_index]

            # 7. Else decrease the free space we used for the file
            else:
                self.free[use_index] = File(fid=use_free.fid,
                                            floc=use_free.floc + file.flen,
                                            flen=use_free.flen - file.flen)

        # 8. Put the files in order
        new_files.sort(key=lambda x: x.floc)

        # 9. These are the new files
        self.files = new_files
        # print(self.free)
        # print(self.files)

    def checksum(self):
        "Compute the filesystem checksum"

        # 1. Start with nothing
        result = 0

        # 2. Loop for every file
        for file in self.files:

            # 3. Loop for every file location
            for offset in range(file.flen):

                # 4. Add it the checksum for this location
                result += file.fid * (file.floc + offset)

        # 5. Return the total checksum
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.compact()
        return self.checksum()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.compact_two()
        return self.checksum()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      d i s k m a p . p y                     end
# ======================================================================
