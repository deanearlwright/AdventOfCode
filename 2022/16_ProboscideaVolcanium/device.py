
# ======================================================================
# Proboscidea Volcanium
#   Advent of Code 2022 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
from collections import deque

import valves

# ----------------------------------------------------------------------
#                                                             namedtuple
# ----------------------------------------------------------------------
State = namedtuple("State", "time, loc, opened, pressure, goal")
StateDumbo = namedtuple("State", "time, loc, opened, pressure, goal, dumbo, dumbo_goal, log")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Proboscidea Volcanium"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.valves = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.valves = valves.Valves(text=text, part2=part2)

    def most_pressure_one(self, minutes):  # pylint: disable=R0914
        "What is the most pressure you can release"

        # 1. Start at the beginning
        most = 0
        states = deque()
        states.append(State(time=0, loc="AA", opened=0, pressure=0, goal=""))

        # 2. Loop while there is something to do
        while len(states) > 0:

            # 3. Grab a state (breadth first)
            time, loc, opened, pressure, goal = states.pop()

            # 4. Can we do better?
            additional = self.valves.most_additional_pressure(minutes - time, opened, loc)
            if pressure + additional <= most:
                continue

            # 5. Advance the time
            time = time + 1

            # 6. Has the time expired or all valves opened, save the most_pressure, and scene
            if time == minutes or self.valves.are_all_opened(opened):
                if pressure > most:
                    # print(f"{time} {loc} {pressure} {opened}")
                    most = pressure
                continue

            # 7. Are we where we want to be? If so, open the valve
            number, rate, tunnels = self.valves.info(loc)
            if loc == goal and rate > 0 and number & opened == 0:
                states.append(State(time=time,
                                    loc=loc,
                                    opened=opened | number,
                                    pressure=pressure + rate * (minutes - time),
                                    goal=""))
                continue

            # 8. Determine where to go
            if goal != "":
                next_loc = self.valves.next_to(tunnels, goal)
                states.append(State(time=time,
                                    loc=next_loc,
                                    opened=opened,
                                    pressure=pressure,
                                    goal=goal))
                continue
            goals = self.valves.can_open(opened).split(',')
            for goal in goals:
                next_loc = self.valves.next_to(tunnels, goal)
                states.append(State(time=time,
                                    loc=next_loc,
                                    opened=opened,
                                    pressure=pressure,
                                    goal=goal))

        # 9. When all has been explored, return the most pressure released
        return most

    def most_pressure_two(self, minutes):  # pylint: disable=R0914
        "What is the most pressure you can release"

        # 1. Start at the beginning
        minutes -= 4
        most = 0
        states = deque()
        states.append(StateDumbo(time=0, loc="AA", opened=0, pressure=0, goal="",
                                 dumbo="AA", dumbo_goal="", log=""))

        # 2. Loop while there is something to do
        while len(states) > 0:

            # 3. Grab a state (breadth first)
            time, loc, opened, pressure, goal, dumbo, dumbo_goal, log = states.pop()

            # 4. Can we do better?
            additional = self.valves.most_additional_pressure(minutes - time, opened,
                                                              loc, dumbo=dumbo)
            if pressure + additional <= most:
                continue

            # 5. Advance the time
            time = time + 1
            time_left = minutes - time

            # 6. Has the time expired or all valves opened, save the most_pressure, and scene
            if time == minutes or self.valves.are_all_opened(opened):
                if pressure > most:
                    print(f"{time} {loc} {dumbo} {pressure}")
                    most = pressure
                continue

            # 7. Are we where we want to be? If so, open the valve
            number, rate, tunnels = self.valves.info(loc)
            if loc == goal:
                if rate > 0 and number & opened == 0:
                    opened |= number
                    pressure += rate * time_left
                    # print(f"{time_left} I opened {rate} valve at {loc} pressure is {pressure}, "
                    #       f"dumbo is at {dumbo}/{dumbo_goal}")
                    new_log = log + f"\n{time} I opened {loc}"
                    dumbo_next, dumbo_goal, opened, pressure = \
                        self.what_would_dumbo_do(dumbo, dumbo_goal, time_left,
                                                 opened, pressure)
                    if dumbo_next == "Fail":
                        continue
                    states.extend(self.dumbo_states(time, loc, "", opened, pressure,
                                                    dumbo, dumbo_goal, dumbo_next, new_log))
                    continue
                continue # goal = "" # Goal not obtainable

            # 8. Determine where to go
            if goal != "":
                if self.valves.is_valve_closed(goal, opened):
                    next_loc = self.valves.next_to(tunnels, goal)
                    new_log = log + f"\n{time} I moved to {next_loc} toward {goal}"
                    dumbo_next, dumbo_goal, opened, pressure = \
                        self.what_would_dumbo_do(dumbo, dumbo_goal, time_left,
                                                 opened, pressure)
                    if dumbo_next == "Fail":
                        continue
                    states.extend(self.dumbo_states(time, next_loc, goal, opened, pressure,
                                                    dumbo, dumbo_goal, dumbo_next, new_log))
                    continue
                continue # Not obtainable
            goals = self.valves.can_open(opened).split(',')
            for goal in goals:
                next_loc = self.valves.next_to(tunnels, goal)
                new_log = log + f"\n{time} I picked {next_loc} toward {goal}"
                dumbo_next, new_dumbo_goal, new_opened, new_pressure = \
                    self.what_would_dumbo_do(dumbo, dumbo_goal, time_left,
                                             opened, pressure)
                if dumbo_next == "Fail":
                    continue
                states.extend(self.dumbo_states(time, next_loc, goal, new_opened, new_pressure,
                                                dumbo, new_dumbo_goal, dumbo_next, new_log))

        # 9. When all has been explored, return the most pressure released
        return most

    def what_would_dumbo_do(self, dumbo, goal, time_left, opened, pressure):   # pylint: disable=R0913
        "Returns the next action for dumbo"

        # 1. If dumbo is at his goal, he should open it (if he still can)
        number, rate, tunnels = self.valves.info(dumbo)
        if dumbo == goal:
            if rate > 0 and number & opened == 0:
                opened |= number
                pressure += rate * time_left
                # print(f"{time_left} Dumbo opened {rate} valve at {dumbo} pressure {pressure}"
                return dumbo, "open", opened, pressure
            return "Fail", "", opened, pressure # goal = ""

        # 2. If dumbo has a goal, he should move towards it
        if goal != "":
            if self.valves.is_valve_closed(goal, opened):
                next_loc = self.valves.next_to(tunnels, goal)
                return next_loc, goal, opened, pressure
            return "Fail", "", opened, pressure

        # 3. Dumbo needs new goals
        return "", "", opened, pressure

    def dumbo_states(self, time, loc, goal, opened, pressure,  # pylint: disable=R0913, R0914
                     dumbo, dumbo_goal, dumbo_next, log):
        "Create states expanding dumbo goals"

        # 1. If dumbo has something to do he should just do it
        if dumbo_next != "":
            if dumbo_goal == "open":
                newer_log = log + f", Dumbo opened {dumbo} p={pressure}"
                dumbo_goal = ""
            else:
                newer_log = log + f", Dumbo moves to {dumbo_next} toward {dumbo_goal} p={pressure}"
            return [StateDumbo(time=time,
                               loc=loc,
                               opened=opened,
                               pressure=pressure,
                               goal=goal,
                               dumbo=dumbo_next,
                               dumbo_goal=dumbo_goal,
                               log=newer_log)]

        # 2. Get new goals for dumbo
        goals = self.valves.can_open(opened).split(',')

        # 3. If dumbo has nothing to do, let him stay in place
        if len(goals) == 0 or goals[0] == "":
            newer_log = log + f", Dumbo rests p={pressure}"
            return [StateDumbo(time=time,
                               loc=loc,
                               opened=opened,
                               pressure=pressure,
                               goal=goal,
                               dumbo=dumbo,
                               dumbo_goal="",
                               log=newer_log)]

        # 4. Set up for multiple possible goals
        result = []
        _, _, tunnels = self.valves.info(dumbo)

        # 5. Loop for all of the goals
        for new_goal in goals:
            if new_goal == "":
                print(f"woops: dumbo={dumbo} goal={goal} goals={goals}")

            # 6. Determine dumbo's next move toward the goal
            next_dumbo = self.valves.next_to(tunnels, new_goal)
            newer_log = log + f", Dumbo goes {next_dumbo} toward {new_goal}  p={pressure}"
            result.append(StateDumbo(time=time,
                                     loc=loc,
                                     opened=opened,
                                     pressure=pressure,
                                     goal=goal,
                                     dumbo=next_dumbo,
                                     dumbo_goal=new_goal,
                                     log=newer_log))

        # 7. Return all of dumbo's possible moves
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
