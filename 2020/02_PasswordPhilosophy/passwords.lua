-- ======================================================================
-- Password Philosophy
--   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p a s s w o r d s . l u a
-- ======================================================================
-- "A solver for the Advent of Code 2020 Day 02 puzzle"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
policy = require('policy')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Passwords = { part2 = false, text = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                              Passwords
-- ======================================================================

-- "Object for Password Philosophy"

function Passwords:Passwords (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  
  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  o.policies = {}
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Passwords:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Create a policy from that line and add it
    table.insert(self.policies, policy:Policy({part2=self.part2, text=line}))
  end
end

function Passwords:count_valid()
  
  -- 1. Start with nothing
  result = 0
  
  -- 2. Loop for all of the password policies
  for _, pol in ipairs(self.policies) do
    
    -- 3. Does this policy have a valid password?
    valid = pol:check_password()
    
    -- 4. If so, increment the cound
    if valid then
      result = result + 1
    end
  end
  
  -- 5. Return the cound of valid passwords
  return result
end

function Passwords:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_valid()
end


function Passwords:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_valid()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Passwords

-- ======================================================================
-- end                    p a s s w o r d s . l u a                   end
-- ======================================================================
