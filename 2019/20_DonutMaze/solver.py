# ======================================================================
# Donut Maze
#   Advent of Code 2019 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           s o l v e r . p y
# ======================================================================
"Donut Maze solver for Advent of Code 2019 Day 20"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import donut

import graph

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

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver():
    """Object representing a donut maze solver"""

    def __init__(self, text=None, verbose=False, part2=False):

        # 1. Set the initial values
        self.donut = donut.Donut(text=text, part2=part2)
        self.part2 = part2

        # 2. Find the paths to all of the portals
        self.portal_paths = self.get_direct_paths_between_portals()
        self.graph = self.portal_paths_to_graph()
        self.path = None
        self.cost = None

    def get_direct_paths_between_portals(self, verbose=False):
        "Get paths between portals"

        # 1. Start with nothing
        paths = {portal: Paths() for portal in self.donut.portals}

        # 2. Loop for all of the portals
        for from_portal, from_plocs in self.donut.portals.items():
            if verbose:
                print("Portal %s locs=%s" % (from_portal, str(from_plocs)))

            # 3. It only takes one step to go from one end of the portal to the other
            if len(from_plocs) > 1:
                list_plocs = list(from_plocs)
                if verbose:
                    print("Adding portal path for %s between %s and %s" %
                          (from_portal, list_plocs[0], list_plocs[1]))

                paths[from_portal].append(Path(from_loc=list_plocs[0], to_loc=list_plocs[1],
                                               steps=1, used=[from_portal]))
                paths[from_portal].append(Path(from_loc=list_plocs[1], to_loc=list_plocs[0],
                                               steps=1, used=[from_portal]))

            # 4. Loop for the (one or two) end of this portal
            for from_ploc in from_plocs:

                # 5. Explore from here, collecting portal locations and path length
                portal_locs = self.explore_from(from_ploc)
                if verbose:
                    print("From portal %s %s there are %s locations/steps" %
                          (from_portal, from_ploc, str(portal_locs)))

                # 6. Record the portal ends found
                if portal_locs:
                    for to_loc, steps in portal_locs.items():
                        to_portal = self.donut.portals_at[to_loc]
                        if verbose:
                            print("Adding direct path from portal %s at %s to portal %s at %s for %d steps" %
                                  (from_portal, from_ploc, to_portal, to_loc, steps))
                        paths[from_portal].append(Path(from_loc=from_ploc, to_loc=to_loc,
                                                       steps=steps, used=[]))
                elif verbose:
                    print("No portals found from portal %s at %s" %
                          (from_portal, from_ploc))

        # 4. Return the direct paths beteeen different portals
        if verbose:
            for portal, p_paths in paths.items():
                print("Portal %s: paths = %s" %
                      (portal, ', '.join(str(one_path) for one_path in p_paths)))
        return paths

    def explore_from(self, from_loc, visited=None, steps=0):
        "Explore the local maze from the specificed location without using portals"

        # 1. Start with nothing
        results = {}
        if visited is None:
            visited = set()

        # 2. Record being here
        visited.add(from_loc)
        steps += 1

        # 3. Oh, the places you'll go (that we have't been before)
        locs_to_visit = [loc for loc in self.donut.exit_locs(from_loc[0], from_loc[1])
                         if loc not in visited]

        # 4. Loop for the locations
        for loc in locs_to_visit:

            # 5. If this is a portal, record it
            if loc in self.donut.portals_at:
                if loc not in results or steps < results[loc]:
                    results[loc] = steps

            # 6. Else explore from here
            exp_results = self.explore_from(loc, visited, steps)

            # 7. Add in those results (if any)
            for exp_loc, exp_steps in exp_results.items():
                if exp_loc not in results or exp_steps < results[exp_loc]:
                    results[exp_loc] = exp_steps

        # 8. Return the results
        return results

    def portal_paths_to_graph(self, verbose=False):
        "Rework portal paths in to a graph of locations suitable for find_shortest_path"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the entries in the portal paths
        for portal, paths in self.portal_paths.items():
            if verbose:
                print("PP2G: portal %s paths %s" % (portal, paths))

            # 3. Loop for all the paths
            for path in paths:

                # 4. Add this path
                result.append((path.from_loc, path.to_loc, path.steps))

        # 5. return the graph
        if verbose:
            for edge in result:
                print("PP2G: Edge(s=%s, e=%s, c=%d)" %
                      (edge[0], edge[1], edge[2]))
        return graph.Graph(result)

    def solve_donut_maze(self):
        "Solve the donut maze"

        # 1. Get the locations of the start and finish
        start = list(self.donut.portals[self.donut.start])[0]
        finish = list(self.donut.portals[self.donut.finish])[0]

        # 2. Find the path
        result = self.graph.dijkstra(start, finish)

        # 3. If you found it, save the results
        if result is not None:
            self.path = result
            self.cost = self.graph.cost(result)


# ======================================================================
#                                                                   Path
# ======================================================================


class Path():
    """Object representing a path in the Neptune donut maze"""

    def __init__(self, from_loc=(0, 0), to_loc=(0, 0), steps=0, used=None):

        # 1. Set the initial values
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.steps = steps
        if used is None:
            self.used = set()
        else:
            self.used = set(used)

    def __str__(self):
        if self.used:
            using = ' using ' + ','.join(self.used)
        else:
            using = ''
        if self.steps == 1:
            steps = 'step'
        else:
            steps = 'steps'
        return "%s to %s takes %d %s%s" % \
               (self.from_loc, self.to_loc, self.steps, steps, using)

# ======================================================================
#                                                                  Paths
# ======================================================================


class Paths():
    """Object representing multiple paths in the Neptune donut maze"""

    def __init__(self):

        # 1. Set the initial values
        self.paths = []

    def __str__(self):
        return ', '.join(str(path) for path in self.paths)

    def __len__(self):
        return len(self.paths)

    def __iter__(self):
        return iter(self.paths)

    def append(self, path):
        "Append a path"
        self.paths.append(path)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
