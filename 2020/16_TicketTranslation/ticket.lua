-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         t i c k e t . l u a
-- ======================================================================
-- Ticket for the Advent of Code 2020 Day 16 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Ticket = { part2=false, text='', numbers = {}, valid=true }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Ticket
-- ======================================================================

function Ticket:Ticket (o)
  -- Object for Ticket Translation


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.numbers = {}
  o.valid = true

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Ticket:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Get and save the numbers
  for number in text:gmatch("[0-9]+") do
    table.insert(self.numbers, tonumber(number))
  end
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Ticket

-- ======================================================================
-- end                       t i c k e t . l u a                      end
-- ======================================================================
