# ======================================================================
# Many-Worlds Interpretation
#   Advent of Code 2019 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           s o l v e r . p y
# ======================================================================
"Many-Worlds Interpretation Maze solver for Advent of Code 2019 Day 18"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import heapq

import vault

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

REVERSE = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W'
}

DIRS = ['?', 'N', 'S', 'W', 'E']
RDIR = ['?', 'S', 'N', 'E', 'W']

ORIGIN_KEY = '@0'

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver():
    """Object representing a vault maze solver"""

    def __init__(self, text=None, verbose=False, part2=False):

        # 1. Set the initial values
        self.vault = vault.Vault(text=text, part2=part2)
        self.part2 = part2

        # 2. Find the path to all of the keys
        self.key_paths = self.get_key_paths(verbose=verbose)


    def get_shortest_path(self, from_loc, to_loc):
        "Get the short path that collects all the keys"

        # 1. Start with no path found, no doors to unlock, and nothing in the path
        path_steps = None
        doors = set()
        path = set()

        # 2. Start the queue from where we are
        priority_queue = []
        heapq.heappush(priority_queue, (0, from_loc, set()))

        # 3. Loop while there is somewhere to explore
        while priority_queue:

            # 4. Take the minimum (steps) item from the queue
            steps, here, doors = heapq.heappop(priority_queue)

            # 5. We are here
            path.add(here)

            # 6. If here is there, we are done
            if here == to_loc:
                path_steps = steps
                break

            # 7. If there is a door, we have more to unlock
            if here in self.vault.door_at:
                doors = doors.copy()
                doors.add(self.vault.door_at[here])

            # 8. We need to explore all exits from here
            for direction in self.vault.locs[here].exits_at():
                delta = vault.DELTA[direction]
                nxt = (here[0] + delta[0], here[1] + delta[1])
                if nxt not in path:
                    heapq.heappush(priority_queue, (steps + 1, nxt, doors))

        # 9. Return the number if steps in path (or None if no path found) and keys needed
        return path_steps, doors

    def get_key_paths(self, verbose=False):
        "Get paths to and between keys"

        # 1. Start with nothing
        paths = {key: {} for key in self.vault.keys}

        # 2. Loop for all of the keys
        for key, kloc in self.vault.keys.items():

            # 3. Add the shortest path to that key from the origin (if any)
            if self.part2:
                self.get_key_origin_paths_part2(paths, key, kloc, verbose=verbose)
            else:
                self.get_key_origin_paths(paths, key, kloc, verbose=verbose)

            # 5. Add the shortest path to each key from that key (if any)
            self.get_key_to_key_paths(paths, key, kloc)

        # 5. Return the paths to the keys and from keys to keys
        return paths

    def get_key_origin_paths(self, paths, key, kloc, verbose=False):
        "Get path from origin to the specified key"

        # 1. Get the shortest path to that key from the origin
        steps, doors = self.get_shortest_path(self.vault.origin, kloc)
        if verbose:
            print("Shortest path to key %s %s from single origin %s: steps=%s, doors=%s" %
                  (key, kloc, self.vault.origin, steps, doors))

        # 2. If there is a path, Add it to the paths
        if steps is not None:
            if ORIGIN_KEY not in paths:
                paths[ORIGIN_KEY] = {}
            paths[ORIGIN_KEY][key] = Path(loc=kloc, steps=steps, doors=doors)

    def get_key_origin_paths_part2(self, paths, key, kloc, verbose=False):
        "Get path from origin to the specified key"

        # 1. Loop for the four origins
        for onum, origin in enumerate(self.vault.origins):
            if verbose:
                print("origin %d = %s" % (onum, origin))

            # 2. Get the shortest path to the key from this origin
            steps, doors = self.get_shortest_path(origin, kloc)
            if verbose:
                print("Shortest path to key %s %s from origin %s: steps=%s, doors=%s" %
                      (key, kloc, origin, steps, doors))

            # 3. If there is a path, Add it to the paths
            if steps is not None:
                okey = '@%d' % onum
                if okey not in paths:
                    paths[okey] = {}
                paths[okey][key] = Path(loc=kloc, steps=steps, doors=doors)

    def get_key_to_key_paths(self, paths, key, kloc):
        "Get path from origin to the specified key"

        # 1. Find a path from the key to every other key
        for okey, oloc in self.vault.keys.items():

            # 2. Don't need to find ourselves or previous keys
            if okey != key and (oloc not in paths or key not in paths[oloc]):

                # 3. Find the shortest path
                steps, doors = self.get_shortest_path(kloc, oloc)

                # 4. If there is a way, save it
                if steps is not None:
                    if key not in paths:
                        paths[key] = {}
                    if okey not in paths:
                        paths[okey] = {}
                    paths[key][okey] = Path(loc=oloc, steps=steps, doors=doors)
                    paths[okey][key] = Path(loc=kloc, steps=steps, doors=doors)

    #
    def get_all_keys(self, verbose=False):
        "Return the number of steps to find all key recursively"

        # 1. If part2, Use multiple origins
        if self.part2:
            start_from = {'@%d' % _: '@%d' % _ for _ in range(len(self.vault.origins))}
        else:
            start_from = {ORIGIN_KEY: ORIGIN_KEY}
        if verbose:
            print("get_all_keys starting with %s" % start_from)

        # 2. Solve with maze (maybe from multiple origins)
        return self.get_keys(start_from, robot=ORIGIN_KEY, key=ORIGIN_KEY,
                             found=None, cache=None, verbose=verbose)

    def get_keys(self, at_key, robot, key, found=None, cache=None, verbose=False):
        "Get the keys (recursive)"

        # 1. If nothing found, get the keys obtainable from the origin
        if found is None:
            found = set(_ for _ in self.key_paths if _[0] == ORIGIN_KEY[0])
            if verbose:
                print("Setting found to %s" % found)
                print(self.key_paths)

        # 2. Start a cache if there is none
        if cache is None:
            if verbose:
                print("Setting cache to empty")
            cache = {}

        # 3. Start with the initial key (origin)
        at_key[robot] = key
        if verbose:
            print("Setting at_key[%s] to %s" % (robot, key))

        # 4. If we have what we want, we are done
        if len(found) == len(self.key_paths):
            if verbose:
                print("length of found (%d) == length of key_paths, returning 0,%s" %
                      (len(found), key))
            return 0, [key]

        # 5. If we haven't done this before, so much to explore
        ckey = "".join(sorted(at_key.values())) + '|' + \
            "".join(sorted(set(self.key_paths.keys()) - found))
        if verbose:
            print("Checking cache for %s" % (ckey))
        if ckey not in cache:

            # 6. Start with no paths from here
            paths = []

            # 7. Loop for all the runners and all the possible paths
            for bot, bot_key in at_key.items():
                for pkey in self.key_paths[bot]:

                    # 8. Ignore if we already explored this path or don't have the keys for it
                    if pkey in found or self.key_paths[bot_key][pkey].doors - found != set():
                        continue

                    #  9. Explore this path and remember it
                    ksteps, kpaths = self.get_keys(at_key.copy(), bot, pkey, found | {pkey}, cache, verbose=verbose)
                    paths.append((self.key_paths[bot_key][pkey].steps + ksteps, [key] + kpaths))

            # 10. Remember only the best
            cache[ckey] = min(paths)
            if verbose:
                print("Setting cache for %s to %s" % (ckey, min(paths)))

        # 11. Return the best from here
        return cache[ckey]


# ======================================================================
#                                                                   Path
# ======================================================================
class Path():
    """Object representing a path to an item in the Neptune vault"""

    def __init__(self, loc=(0, 0), steps=0, doors=None):

        # 1. Set the initial values
        self.loc = loc
        self.steps = steps
        if doors is None:
            self.doors = set()
        else:
            self.doors = set(doors)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
