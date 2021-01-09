-- ======================================================================
-- Handy Haversacks
--   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e . l u a
-- ======================================================================
-- Rule for the Advent of Code 2020 Day 07 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rule = { part2=false, text='', bag='', bags={} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local MATCH_BAG = "%a+ %a+"
local MATCH_REST = "%d+ %a+ %a+"
local MATCH_NUMBER = "%d+"

-- ======================================================================
--                                                                   Rule
-- ======================================================================


function Rule:Rule (o)
  -- Object for Handy Haversacks


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.bag = ''
  o.bags = {}

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
  
  -- 1. Get the bag color
  self.bag = text:match(MATCH_BAG)
  
  -- 2. Loop for all of the contained bags
  for contained in text:gmatch(MATCH_REST) do
    
    -- 3. Get number abd color of contained bag
    local number = tonumber(contained:match(MATCH_NUMBER))
    local color = contained:match(MATCH_BAG)
    
    -- 4. Save the contained bag
    self.bags[color] = number
  end
  
end

function Rule:contains(color)
  -- Returns the number of the bags that this bag contains
  
  -- 1. Loop for all the contained bags
  for bcolor, bnumber in pairs(self.bags) do
    
    -- 2. If the colors match, return the number
    if color == bcolor then
      return bnumber
    end
  end
   
  -- 3. Not found, return 0
  return 0
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Rule

-- ======================================================================
-- end                         r u l e . l u a                        end
-- ======================================================================
