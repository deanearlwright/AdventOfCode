-- ======================================================================
-- Handheld Halting
--   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                      i n s t r u c t i o n . l u a
-- ======================================================================
-- Instruction for the Advent of Code 2020 Day 08 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Instruction = { part2=false, text='', 
  operation='', argument=0, visited=false}

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                            Instruction
-- ======================================================================


function Instruction:Instruction (o)
  -- Object for Handheld Halting


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.operation = ''
  o.argument = 0
  o.visited = false

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Instruction:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Break out the operation and argument
  self.operation = text:match("%a%a%a")
  self.argument = tonumber(text:match("[+-]%d+"))

end

function Instruction:execute(acc)
  -- Execute the instruction, returning the updated accumulator and pc offset
  
  -- 1. Mark instruction as visited
  self.visited = true
  
  -- 2. Handle acc operation
  if self.operation == 'acc' then
    acc = acc + self.argument
    pc = 1
    
  -- 3. Handle jmp operation  
  elseif self.operation == 'jmp' then
    pc = self.argument
    
  -- 4. Handle nop operation  
  elseif self.operation == 'nop' then
    pc = 1
  
  -- 5. Invalid operation
  else
    error("Invalid operation", self.operation)
  end
  
  -- 5. Return the updated accumulator and pc offset
  return acc, pc
end
 
  
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Instruction

-- ======================================================================
-- end                 i n s t r u c t i o n . l u a                  end
-- ======================================================================
