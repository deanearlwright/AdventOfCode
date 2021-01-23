-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e . l u a
-- ======================================================================
-- Rule for the Advent of Code 2020 Day 16 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rule = { part2=false, text='', name='', numbers = {}, positions= {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Rule
-- ======================================================================


function Rule:Rule (o)
  -- Object for Ticket Translation


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.name = '???'
  o.numbers = {}
  o.positions = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Rule:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. The name is one or more words
  self.name = text:match("[a-z ]+")
  
  -- 2. Get and save the numbers 
  for number in text:gmatch("[0-9]+") do
    table.insert(self.numbers, tonumber(number))
  end 
end

function Rule:is_valid(number)
  -- Returns true if the number matches the rule
  
  -- 1. Loop for the ranges in the rule
  for indx = 1, #self.numbers, 2 do
    
    -- 2. If the number is in this range, return true
    if self.numbers[indx] <= number and self.numbers[indx+1] >= number then
      return true
    end
  end
  
  -- 3. Return false as this number is not in any range for this rule
  return false
end

function Rule:are_all_valid(numbers)
  -- Returns true if all of the numbers match the rule
  
  -- 1. Loop for all of the numbers
  for _, number in ipairs(numbers) do
    
    -- 2. If the number is not valid, return false
    if not self:is_valid(number) then
      return false
    end
  end
  
  -- 3. Return true as all numbers are the range for this rule
  return true
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Rule

-- ======================================================================
-- end                         r u l e . l u a                        end
-- ======================================================================
