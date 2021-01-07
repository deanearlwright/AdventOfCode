-- ======================================================================
-- Passport Processing
--   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p a s s p o r t s . l u a
-- ======================================================================
-- "A solver for the Advent of Code 2020 Day 04 puzzle"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local passport = require('passport')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Passports = { part2 = false, text = {}, passports = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                              Passports
-- ======================================================================

-- "Object for Passport Processing"

function Passports:Passports (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  o.passports = {}
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Passports:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Start with nothing
  self.passports = {}
  local combined = ''
  
  -- 2. Loop for each line of the text
  for _, line in ipairs(text) do
    
    -- 3. There is a blank line between passports
    if #line == 0 then
      -- 4. If we have collected passport fields add them to the list
      if #combined > 0 then
        table.insert(self.passports, passport:Passport({part2=self.part2, text=combined}))
        combined = ''
      end
    else -- 5. Not a blank line, accumulate the fields
      if #combined == 0 then
        combined = line
      else
        combined = combined .. ' ' .. line
      end
    end
  end 

  -- 6. Add the final passport (if any)
  if #combined > 0 then
    table.insert(self.passports, passport:Passport({part2=self.part2, text=combined}))
  end

end

function Passports:count_valid()
  -- Returns the number of valid passports
  
  -- 1. Start with none
  local result = 0
  
  -- 2. Loop for all of the passports
  for _, pspt in ipairs(self.passports) do
    
    -- 3. Increment count of valid ones
    if pspt:is_valid() then
      result = result + 1
    end
  end
  
  -- 4. Return the number of valid passports
  return result
end


function Passports:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_valid()
end


function Passports:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:count_valid()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Passports

-- ======================================================================
-- end                    p a s s p o r t s . l u a                   end
-- ======================================================================
