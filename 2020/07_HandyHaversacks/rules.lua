-- ======================================================================
-- Handy Haversacks
--   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 07 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rules = { part2 = false, text = {}, rules = {}, known = {} }

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local THE_BAG = 'shiny gold'

-- ======================================================================
--                                                                  Rules
-- ======================================================================

-- Object for Handy Haversacks

function Rules:Rules (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rules = {}
  o.known = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Rules:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    local new_rule = rule:Rule({part2=self.part2, text=line})
    self.rules[new_rule.bag] = new_rule
    end

end

function Rules:can_contain(color)
  -- How many bags can contain the specified bag
  
  -- 1. Start with the bags that can directly contain the specified bag
  local bags = {}
  for _, rul in pairs(self.rules) do
    if rul:contains(color) > 0 then
      bags[rul.bag] = color
    end
  end
    
  -- 2. Loop until there are no new bags
  local new_bags = {}
  repeat
    local done = true
    
    -- 3. Add the new bags to bags
    for outside, inside in pairs(new_bags) do
      bags[outside] = inside 
    end
    
    -- 4. No new bags in this round
    new_bags = {}
    
    -- 5. Loop for all the bags so far
    for color, _ in pairs(bags) do
      -- 6. Loop for all of the rules
      for rcolor, rul in pairs(self.rules) do
        -- 7. If the rule is for a bag we don't have that contains a bag we do have, save it
        if nil == bags[rcolor] and rul:contains(color) > 0 then
          new_bags[rcolor] = color
          done = false
        end
      end
    end
    
    -- 8. Stop when we have no more to add
  until done
  
  -- 9. Return the total number of bags
  local result = 0
  for _, _ in pairs(bags) do
    result = result + 1
  end  
  return result
end

function Rules:required_inside(color)
  -- print("required_inside", color)
  -- How many bags are required within the specified bag
  
  -- 1. Do we know the answer already, just return it
  if nil ~= self.known[color] then
    -- print("returning known answer of", self.known[color], "for", color)
    return self.known[color]
  end
  
  -- 2. If there is no rule for this color, return 0
  if nil == self.rules[color] then
    -- print("Setting zero for", color)
    self.known[color] = 0
    return 0
  end
  
  -- 3. Otherwise accumulate the number of needed bags
  local result = 0
  
  -- 4. Loop for all of the inner bags
  for icolor, inumber in pairs(self.rules[color].bags) do
    -- print("looping",icolor, inumber)
      
      -- 5. Add number number of bags for this color
    result = result + inumber + inumber * self:required_inside(icolor)
    
  end
  
  -- 6. Remember the number of bags
  -- print("Setting number for", color, "to", result)
  self.known[color] = result
  
  -- 7. Return the number of bags
  return result
end

function Rules:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:can_contain(THE_BAG)
end


function Rules:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:required_inside(THE_BAG)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Rules

-- ======================================================================
-- end                        r u l e s . l u a                       end
-- ======================================================================
