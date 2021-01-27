-- ======================================================================
-- Operation Order
--   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         h o m e w o r k . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 18 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local expression = require('expression')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Homework = { part2 = false, text = {}, expressions = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                               Homework
-- ======================================================================

-- Object for Operation Order

function Homework:Homework (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.expressions = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Homework:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for all of the text
  for _, line in ipairs(text) do
    
    -- 2. Create an expression
    local exp = expression:Expression({part2=self.part2, text=line})
    
    -- 3. Save it 
    table.insert(self.expressions, exp)
  end
end

function Homework:evaluate_all()
  -- Returns the sum of evaluating all of the experssions
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all the expressions
  for _, exp in ipairs(self.expressions) do
    
    -- 3. Evaluate the expression
    local value = exp:evaluate()
    
    -- 4. Accumulate the value of the expressions
    result = result + value
  end
  
  -- 5. Return the accumulated expressions
  return result
end

function Homework:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:evaluate_all()
end


function Homework:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:evaluate_all()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Homework

-- ======================================================================
-- end                     h o m e w o r k . l u a                    end
-- ======================================================================
