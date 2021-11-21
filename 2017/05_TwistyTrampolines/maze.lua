-- ======================================================================
-- TwistyTrampolines
--   Advent of Code 2017 Day 05 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         m a z e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 05 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Maze = { part2 = false, text = {}, numbers = {}, index = 0 }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Maze
-- ======================================================================

-- Object for TwistyTrampolines

function Maze:Maze (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.numbers = {}
  o.index = 1

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Maze:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    table.insert(self.numbers, tonumber(line))
    end

end

function Maze:escaped()
  -- Return true if we have escaped from the maze
  return nil == self.numbers[self.index]
end

function Maze:step()
  -- One step in the maze of branches
  
  -- 1. Determine new location
  local offset = self.numbers[self.index]
  local index = self.index + offset
  
  -- 2. Update the branch location
  local branch = self:update()
  
  -- 3. Set the new branch location
  self.index = index
end

function Maze:update()
  -- Update the branch
  
  -- 1. Increment the location
  local branch = 1 + self.numbers[self.index]
  
  -- 2. For part 2 do something else
  if self.part2 and branch >= 4 then
    branch = branch - 2
  end
  
  -- 3. Set the new branch value
  self.numbers[self.index] = branch
end

function Maze:steps()
  -- Return the number of steps to exit the maze
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop until we escape
  while not self:escaped() do
    
    -- 3. Take a step
    self:step()
    
    -- 4. Increment the number of steps
    result = result + 1
  end
  
  -- 4. Return the number of steps
  return result
end 

function Maze:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:steps()
end


function Maze:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:steps()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Maze

-- ======================================================================
-- end                         m a z e . l u a                        end
-- ======================================================================
