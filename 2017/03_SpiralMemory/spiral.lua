-- ======================================================================
-- SpiralMemory
--   Advent of Code 2017 Day 03 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         s p i r a l . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 03 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Spiral = { part2 = false, text = {}, grid = {}, 
                 value = 0, x = 0, y = 0, dir = "E",
                 steps = 1}

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

local DELTA = {
  E = {x = 1, y = 0},
  W = {x = -1, y = 0},
  N = {x = 0, y = 1},
  S = {x = 0, y = -1},
  NE = {x = 1, y = 1},
  SE = {x = 1, y = -1},
  NW = {x = -1, y = 1},
  SW = {x = -1, y = -1},
}

local TURN = {
  E = "N",
  N = "W",
  W = "S",
  S = "E",
}


-- ======================================================================
--                                                                 Spiral
-- ======================================================================

-- Object for SpiralMemory

function Spiral:Spiral (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.grid = {["0,0"] = 1}
  o.value = 0
  o.x = 0
  o.y = 0
  o.dir = "E"
  o.steps = 1

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o.value = tonumber(o.text[1])
  end

  return o
end

function Spiral:distance()
  -- Determine distance back to the center
  return math.abs(self.x) + math.abs(self.y)
end
  
function Spiral:location()
  -- Return the location as a string
  return string.format("%d,%d", self.x, self.y)
end

function Spiral:neighbor(dir)
  -- Return the value of the neighbor in the specified directions
  
  -- 1. Get the neighbor's location
  local nx = self.x + DELTA[dir]["x"]
  local ny = self.y + DELTA[dir]["y"]
  local nloc = string.format("%d,%d", nx, ny)
  
  -- 2. Return the value
  return self.grid[nloc]
end
  
function Spiral:sum_neighbors()
  -- Return the sum of the neighbors
  
  -- 1. Start with nothing
  local result = 0
  
  -- 1. Loop for all of the neighbors
  for dir, delta in pairs(DELTA) do
    
    -- 2. Get the neighbor's location
    local nx = self.x + delta.x
    local ny = self.y + delta.y
    local nloc = string.format("%d,%d", nx, ny)
    
    -- 3. Add the neighbor's value to the total
    local value = self.grid[nloc]
    if value then
      -- print(self.x, self.y, dir, delta.x, delta.y, nloc, result, value)
      result = result + value
    end
    
  end
  
  -- 4. Return the value of the neighbors
  return result
end
    
function Spiral:grow()
  -- Advance the spiral grid one step
  
  -- 1. Advance one step
  self.x = self.x + DELTA[self.dir]["x"]
  self.y = self.y + DELTA[self.dir]["y"]
  
  -- 2. Increment number of steps
  self.steps = self.steps + 1
  
  -- 3. Determine the value to store at the location
  local value = self.steps
  if self.part2 then
    value = self:sum_neighbors()
  end
  
  -- 4. Save value at new location
  self.grid[self:location()] = value
  
  -- 5. If there is no neighbor to the right, turn
  -- print(self.x, self.y, self:location(), self.dir, TURN[self.dir], self.grid[self:location()], self:neighbor(TURN[self.dir]), value)
  if nil == self:neighbor(TURN[self.dir]) then
    self.dir = TURN[self.dir]
  end
  
  -- 7. Return the last value stored
  return value
end

function Spiral:grow_until(limit)
  -- grow the spiral unit the limit is reached
  
  -- 1. Start with nothing
  local value = 0
  
  -- 1. Loop until the limit reached
  while value < limit do
    
    -- 2. Grow another step
    value = self:grow()
    
  end 
  
  -- 3. Return the distance to the center or last value written
  if self.part2 then
    return value
  end
  
  return self:distance()
end

function Spiral:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:grow_until(self.value)
end


function Spiral:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return  self:grow_until(self.value)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Spiral

-- ======================================================================
-- end                       s p i r a l . l u a                      end
-- ======================================================================
