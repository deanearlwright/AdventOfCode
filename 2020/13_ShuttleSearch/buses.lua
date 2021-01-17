-- ======================================================================
-- Shuttle Search
--   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         b u s e s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 13 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local bus = require('bus')
local crt = require('crt')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Buses = { part2 = false, text = {}, earliest = 0, buses = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Buses
-- ======================================================================

-- Object for Shuttle Search

function Buses:Buses (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.earliest = o.earliest or 0
  o.buses = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Buses:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text == 2)

  -- 1. Earliest timestamp is the first line of text
  self.earliest = tonumber(text[1])
  
  -- 2. Second line is bus ids
  local offset = 0
  for bid in text[2]:gmatch("[0-9x]+") do

    -- 3. Ignore buses that are out of service
    if bid ~= 'x' then
      
      -- 4. Greate a bus
      local abus = bus:Bus({part2=self.part2, bid=tonumber(bid), offset=offset})
        
      -- 2. Add the bus to the entries
      table.insert(self.buses, abus)
    end
    offset = offset + 1
  end
end

function Buses:waiting()
  -- Return the ID of the next bus time the number of minutes waiting
  
  -- 1. Start with nothing
  local best_bus = 0
  local best_time = self.earliest + 99999999
  
  -- 2. Loop for all of the busses
  for _, bus in ipairs(self.buses) do
    
    -- 3. When is the earlist this bus will depart?
    local bus_depart = bus:next_departure(self.earliest)
    
    -- 4. If this is earlier than the best time, use this bus
    if bus_depart < best_time then
      best_time = bus_depart
      best_bus = bus.bid
    end
  end
  
  -- 5. Return the best bus id times the minutes waiting
  return best_bus * (best_time - self.earliest)
end

function Buses:contest()
  -- Return the time that the first bus departs and all the rest in succession

  -- 1. Start with nothing
  local mods = {}
  local offsets = {}
  
  -- 2. Loop for all of the buses
  for _, bus in ipairs(self.buses) do
    
    -- 3. Add to the mods and offset tables
    table.insert(mods, bus.bid)
    table.insert(offsets, -bus.offset)
  end
  
  -- 4. And then CRT does the magic
  return crt.chineseRemainder(mods, offsets)end

function Buses:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:waiting()
end


function Buses:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:contest()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Buses

-- ======================================================================
-- end                        b u s e s . l u a                       end
-- ======================================================================
