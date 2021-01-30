-- ======================================================================
-- Monster Messages
--   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e . l u a
-- ======================================================================
-- Rule for the Advent of Code 2020 Day 19 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rule = { part2=false, text='', number = nil, definition = nil }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Rule
-- ======================================================================


function Rule:Rule (o)
  -- Object for Monster Messages


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.number = nil
  o.definition = nil

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
  assert(nil ~= string.find(text, ':'))
    
  -- 1. Match the rule
  local _
  _, _, self.number, self.definition = string.find(text, '(%d+): ([0-9a-z"| ]+)')
end

function Rule:is_constant()
  -- Returns true id the rule is for a constant
  return '"' == self.definition:sub(1,1)
end

function Rule:letter()
  -- Returns the letter for a constant rule
  
  -- 0. Precondition axiom
  assert(self:is_constant())
  
  -- 1. Return the letter
  return self.definition:sub(2,2)
end

function Rule:alternatives()
  -- Returns the subrules of the rule
  
  -- 0. Precondition axiom
  assert(not self:is_constant())
  
  -- 1. Return the whole definition if there are no alternatives
  if nil == string.find(self.definition, '|') then
    return {self.definition}
  end
  
  -- 2. Otherwise return the sub rules
  local _, _, left, right = string.find(self.definition, '([0-9 ]+) | ([0-9 ]+)')
  return {left, right}
end
    
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Rule

-- ======================================================================
-- end                         r u l e . l u a                        end
-- ======================================================================
