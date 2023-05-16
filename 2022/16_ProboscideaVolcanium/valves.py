
# ======================================================================
# Proboscidea Volcanium
#   Advent of Code 2022 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a l v e s . p y
# ======================================================================
"Valves for the Advent of Code 2022 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import valve

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Valves
# ======================================================================


class Valves(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Proboscidea Volcanium"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.valves = {}
        self.steps = {}
        self.max_rate = 0
        self.max_number = 0
        self.numbers = {}
        self.working = []
        self.closed_mask = 0
        self.working_mask = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all lines of text
        self.max_number = 1
        for line in text:

            # 2. Create a valve
            a_valve = valve.Valve(text=line, part2=self.part2, number=self.max_number)

            # 3. Add it to the rest
            self.valves[a_valve.name] = a_valve
            self.numbers[a_valve.number] = a_valve
            self.max_number = self.max_number + self.max_number
            self.max_rate += a_valve.rate

        # 4. Identify the working valves
        self.working = sorted([name for name in list(self.valves.keys())
                               if self.valves[name].rate > 0])
        for name in self.working:
            self.working_mask |= self.valves[name].number

        # 5. Find the best paths
        for from_loc, from_valve in self.valves.items():
            self.steps[from_loc] = {from_loc: 0, }
            for to_valve in self.working:
                if from_loc != to_valve:
                    self.steps[from_loc][to_valve] = \
                        self.bfs(from_valve.tunnels, to_valve)

        # 6. Compute the closed mask
        self.closed_mask = self.max_number + self.max_number - 1

    def bfs(self, todo, end):
        "Breadth First search of locations"
        depth = 1
        while True:
            next_todo = set()
            for loc in todo:
                if loc == end:
                    return depth
                for new_loc in self.valves[loc].tunnels:
                    next_todo.add(new_loc)
            todo = next_todo
            depth += 1

    def release_pressure(self, opened):
        "Release pressure from the open valves"

        # 1. Start with nothing
        pressure = 0

        # 2. Loop for all the open valves
        for a_valve in opened:

            # 3. Add in the pressure released by this valve
            pressure += self.valves[a_valve].rate

        # 4. Return the pressure released
        return pressure

    def show_open(self, bitmap):
        "Return names of open valves and pressure rate per minute"

        # 1. Start with nothing
        open_valves = []
        rate = 0

        # 2. Loop for all the valves
        for a_valve in self.valves.values():

            # 3. Ignore closed valves
            if bitmap & a_valve.number == 0:
                continue

            # 4. Add the open valve
            open_valves.append(a_valve.name)
            rate += a_valve.rate

        # 5. Return the open valves and the combined rate (per minute)
        return ','.join(open_valves), rate

    def most_additional_pressure(self, time_left, opened, loc, dumbo=None):
        "Return the amount of pressure if all remaining valves opened ASAP"

        # 1. Start with nothing
        result = 0

        # 2. Get the valves that remain to be opened
        to_be_opened = self.can_open(opened)

        # 3. Loop for the valves that can be opened
        for valve_name in to_be_opened.split(','):

            # 4. Determine the shorted number of steps to the valve
            if valve_name == "":
                continue
            shortest = self.steps[loc][valve_name]
            if dumbo:
                shortest = min(shortest, self.steps[dumbo][valve_name])

            # 5. Can we get there in time
            if shortest >= time_left:
                continue

            # 6. Add in the pressure for this valve
            result += self.valves[valve_name].rate * (time_left - shortest)

        # 7. Return the best possiple increase in pressure
        return result

    def loc_to_number(self, loc):
        "Convert location name to valve number"
        return self.valves[loc].number

    def number_to_loc(self, number):
        "Convert valve number to location name"
        return self.numbers[number].name

    def info(self, loc):
        "Get the value information: number, rate, and tunnels"
        return self.valves[loc].info()

    def closed(self, opened):
        "Return the numbers of the closed valves"
        return self.closed_mask ^ opened

    def can_open(self, opened):
        "Return list of valves that can be opened and the combined flow rate"
        return self.show_open(self.closed(opened) & self.working_mask)[0]

    def are_all_opened(self, opened):
        "Return true if all valves are opened"
        return opened & self.working_mask == self.working_mask

    def is_valve_closed(self, loc, opened):
        "Return true if the valve at loc is closed"

        # 1. Get the valve's number
        number = self.loc_to_number(loc)

        # 2. Return True if valve is closed
        return number & opened == 0

    def next_to(self, locs, goal):
        "Return the location closest to the goal"

        # 1. Start with nothing
        best_loc = ""
        best_steps = 99999

        # 2. Loop for the possible locations
        for loc in locs:

            # 3. If that's the goal, return it
            if loc == goal:
                return loc

            # 4. Get the number of steps to the goal
            steps = self.steps[loc][goal]

            # 5. If better than want we have, save it
            if steps < best_steps:
                best_steps = steps
                best_loc = loc

        # 6. Return the best location to reach the goal
        return best_loc

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      v a l v e s . p y                     end
# ======================================================================
