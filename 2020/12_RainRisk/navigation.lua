-- ======================================================================
-- Rain Risk
--   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         n a v i g a t i o n . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 12 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local ferry = require('ferry')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Navigation = { part2 = false, text = {}, ferry = nil }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                             Navigation
-- ======================================================================

-- Object for Rain Risk

function Navigation:Navigation (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.ferry = ferry:Ferry({part2=o.part2})

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  return o
end

function Navigation:execute_all()
  -- Execute all of the navigation instructions and return the manhattan distance

  -- 1. Loop for each line of the text
  for indx, line in ipairs(self.text) do

    -- 2. Execute the instruction
    self.ferry:execute(line)
    -- print(indx, line, self.ferry.loc[1], self.ferry.loc[2], 
    --  self.ferry.waypoint[1], self.ferry.waypoint[2])
  end
  
  -- 3. Return the manhattan distance
  return self.ferry:manhattan_distance()

end

function Navigation:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:execute_all()
end


function Navigation:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:execute_all()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Navigation

-- ======================================================================
-- end                   n a v i g a t i o n . l u a                  end
-- ======================================================================
