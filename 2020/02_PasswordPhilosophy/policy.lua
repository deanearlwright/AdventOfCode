-- ======================================================================
-- Password Philosophy
--   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p o l i c y . l u a
-- ======================================================================
-- "Policy for the Advent of Code 2020 Day 02 puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Policy = {}
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
CAPTURE = "(%d+)-(%d+) (%a): (%a+)"

-- ======================================================================
--                                                                 Policy
-- ======================================================================


function Policy:Policy (o)
  -- "Object for Password Philosophy"


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or ''
  o.low = 0
  o.high = 0
  o.letter = '?'
  o.password = '?'

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Policy:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Break down the policy
  low, high, letter, password = string.match(text, CAPTURE)
  
  -- 2. Save the parts
  self.text = text
  self.low = tonumber(low)
  self.high = tonumber(high)
  self.letter = letter
  self.password = password

end

function Policy:check_password()
  -- Check that the password is valid per the policy in effect
  
  if self.part2 then
    return self:check_password_two()
  end  
  return self:check_password_one()
  
end

function Policy:check_password_one()
  -- Check that the password is valid per the policy in part one
  
  -- 1. Get count of the specified character
  count = select(2, string.gsub(self.password, self.letter, ""))
  
  -- 2. Return true if the count if the character in the password is valid
  return count >= self.low and count <= self.high
  
end

function Policy:check_password_two()
  -- Check that the password is valid per the policy in part two
  
  -- 1. Get count of the specified character at the specified locations
  count = 0
  if self.letter == self.password:sub(self.low, self.low) then
    count = count + 1
  end  
  if self.letter == self.password:sub(self.high, self.high) then
    count = count + 1
  end  
  
  -- 2. Return true if the count if the character in the password is valid
  return count == 1
  
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Policy

-- ======================================================================
-- end                       p o l i c y . l u a                      end
-- ======================================================================
