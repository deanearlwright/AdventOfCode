-- ======================================================================
-- Binary Boarding
--   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p h o n e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 05 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local bpass = require('bpass')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Phone = { part2 = false, text = {}, passes = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Phone
-- ======================================================================

function Phone:Phone (o)
  -- Object for Binary Boarding 
  
  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.passes = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Phone:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    local pass = bpass:Bpass({part2=self.part2, text=line})
    self.passes[pass.seat] = pass
    end

end

function Phone:highest_seat()
  -- Return the ID of the highest seat
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all the boarding passes
  for seat, _ in pairs(self.passes) do
    
    -- 3. If this pass has a higher seat number, save it
    if seat > result then
      result = seat
    end
  end
  
  -- 4. Return the highest seat number
  return result
end

function Phone:lowest_seat()
  -- Return the ID of the lowest seat
  
  -- 1. Start with a very high seat number indeed
  local result = 99999
  
  -- 2. Loop for all the boarding passes
  for seat, _ in pairs(self.passes) do
    
    -- 3. If this pass has a lower seat number, save it
    if seat < result then
      result = seat
    end
  end
  
  -- 4. Return the highest seat number
  return result
end
  
function Phone:find_empty()
  -- Returns an empty seat number
  
  -- 1. Get the high and low seat numbers
  local high = self:highest_seat()
  local low = self:lowest_seat()
  
  -- 2. Loop for the seat numbers between them
  for seat = low, high do
    
    -- 3. If we have no record of this seat number, return it
    if nil == self.passes[seat] then
      return seat
    end
  end
  
  -- 4. Every seat is full
  return nil
end
  
  
function Phone:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:highest_seat()
end


function Phone:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:find_empty()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Phone

-- ======================================================================
-- end                      p h o n e . l u a                     end
-- ======================================================================
