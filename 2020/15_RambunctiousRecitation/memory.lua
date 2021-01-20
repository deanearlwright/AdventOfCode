-- ======================================================================
-- Rambunctious Recitation
--   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         m e m o r y . l u a
-- ======================================================================
-- Memory for the Advent of Code 2020 Day 15 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Memory = { part2=false, text='', age=nil, turn=0, numbers={} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Memory
-- ======================================================================


function Memory:Memory (o)
  -- Object for Rambunctious Recitation


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.age = nil
  o.turn = 0
  o.numbers = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Memory:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for all of the numbers given
  for number in text:gmatch("[0-9]+") do
    
    -- 2. Remember the number
    self:add(tonumber(number))
  end
  
end

function Memory:add_last_spoken()
  -- Add the last number spoken
  self:add(self.age)
end

function Memory:add(number)
  -- Add a number to the memory
  
  -- 1. Increment the turn number
  self.turn = self.turn + 1
  
  -- 2. If the number is new, the age is 0
  if nil == self.numbers[number] then
    self.age = 0
    
  -- 3. Else the age is calculated from when last seen
  else
    self.age = self.turn - self.numbers[number]
  end
  
  -- 4. Save when the number was last seen
  self.numbers[number] = self.turn
end

    
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Memory

-- ======================================================================
-- end                       m e m o r y . l u a                      end
-- ======================================================================
