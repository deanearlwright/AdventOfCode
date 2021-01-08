-- ======================================================================
-- Binary Boarding
--   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         b p a s s . l u a
-- ======================================================================
-- "Bpass for the Advent of Code 2020 Day 05 puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Bpass = { part2=false, text='', row=0, column=0, seat=0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Bpass
-- ======================================================================


function Bpass:Bpass (o)
  -- "Object for Binary Boarding"


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end
 
function Bpass:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text == 10)
  
  -- 1. Convert BF and RL to 10
  local binary = text:gsub('B', '1')
  binary = binary:gsub('F', '0')
  binary = binary:gsub('R', '1')
  binary = binary:gsub('L', '0')
  
  -- 2. Convert to a number
  self.seat = tonumber(binary, 2)
  
  -- 3. Separate into row and seat
  self.row = self.seat // 8
  self.column = self.seat % 8

end
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Bpass

-- ======================================================================
-- end                      b p a s s . l u a                     end
-- ======================================================================
