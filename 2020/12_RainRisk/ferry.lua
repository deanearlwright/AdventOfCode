-- ======================================================================
-- Rain Risk
--   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         f e r r y . l u a
-- ======================================================================
-- Ferry for the Advent of Code 2020 Day 12 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Ferry = { part2=false, start = {0, 0}, loc = {0, 0}, 
                facing = 1, waypoint = {10, -1} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local FACING = { 'N', 'E', 'S', 'W' }
local TURNING = { L = -1, R = 1 }
local DELTA = { N = {0, -1}, S = {0, 1}, E = {1, 0}, W = {-1, 0} }

-- ======================================================================
--                                                                  Ferry
-- ======================================================================


function Ferry:Ferry (o)
  -- Object for Rain Risk


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.start = {0, 0}
  o.loc = {0, 0}
  o.facing = 1 -- east
  o.waypoint = {10, -1} -- 10 east, 1 north

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)
  return o
end

function Ferry:manhattan_distance()
  -- Return manhattan distance from start

  return math.abs(self.start[1] - self.loc[1]) + math.abs(self.start[2] - self.loc[2])

end

function Ferry:execute(inst)
  -- Execute a navigation instruction
  
  -- 1. Break instruction into parts
  local letter = inst:sub(1,1)
  local amount = tonumber(inst:sub(2))
  
  -- 2. Execute moves
  if letter == 'N' or letter == 'S' or letter == 'E' or letter == 'W' then
    self:execute_move(letter, amount)
  elseif letter == 'F' then
    self:execute_forward(amount)
  -- 3. Execute turns
  elseif letter == 'L' or letter == 'R' then
    self:execute_turn(letter, amount)
  else
    print("Unexpected Navigation", inst)
  end
end

function Ferry:execute_move(dir, amount)
  -- More the ferry (or the waypoint)
  
  -- 1. Get the delta for the direction
  local delta = DELTA[dir]
  
  -- 2. For part 2, move the waypoint; for part 1, move the ferry
  if self.part2 then
    self.waypoint[1] = self.waypoint[1] + amount * delta[1]
    self.waypoint[2] = self.waypoint[2] + amount * delta[2]
  else
    self.loc[1] = self.loc[1] + amount * delta[1]
    self.loc[2] = self.loc[2] + amount * delta[2]
  end
  
end

function Ferry:execute_forward(amount)
  -- Move the ferry
  
  -- 1. For part2, the delta is the waypoint; for part1, the direction of the ferry
  local delta = {}
  if self.part2 then
    delta = self.waypoint
  else
    delta = DELTA[FACING[self.facing + 1]]
  end
  
  -- 2. Move the ferry
  self.loc[1] = self.loc[1] + amount * delta[1]
  self.loc[2] = self.loc[2] + amount * delta[2]
end

function Ferry:execute_turn(way, degrees)
  -- Turn the ferry (or the waypoint)
  
  -- 1. If part 2, turn the waypoint
  if self.part2 then
    local new_wp = {}
    if way == 'R' then
      if degrees == 90 then
        new_wp = {-self.waypoint[2], self.waypoint[1] }
      elseif degrees == 180 then
        new_wp = {-self.waypoint[1], -self.waypoint[2] }
      else
        new_wp = {self.waypoint[2], -self.waypoint[1] }
      end  
    else
      if degrees == 90 then
        new_wp = {self.waypoint[2], -self.waypoint[1] }
      elseif degrees == 180 then 
        new_wp = {-self.waypoint[1], -self.waypoint[2] }
      else
        new_wp = {-self.waypoint[2], self.waypoint[1] }
      end
    end
    self.waypoint = new_wp

  -- 2. Else true the ferry
  else
    -- 2a. Get the turning values 
    local amount = degrees // 90
    local plus_minus = TURNING[way]
  
    -- 2b. Do it
    self.facing = (4 +  self.facing + amount * plus_minus ) % 4
  end  
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Ferry

-- ======================================================================
-- end                        f e r r y . l u a                       end
-- ======================================================================
