-- ======================================================================
-- Handheld Halting
--   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                        c o n s o l e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 08 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local instruction = require('instruction')
-- ----------------------------------------------------------------------

--                                                                  local
-- ----------------------------------------------------------------------
local Console = { part2 = false, text = {}, 
  instructions = {}, pc=0, acc=0 }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                Console
-- ======================================================================

-- Object for Handheld Halting

function Console:Console (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.instructions = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Console:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Create an instruction from the line of text
    local inst = instruction:Instruction({part2=self.part2, text=line}) 
    
    -- 3. Add the instruction to the console
    table.insert(self.instructions, inst)
    end

end

function Console:infinite_loop()
  -- Return the accumulator before the program would run any instruction a second time
  
  -- 1. Reset the console
  self.pc = 1
  self.acc = 0
  
  -- 2. Loop until stopped
  while self.pc > 0 and self.pc <= #self.instructions do
    
    -- 3. Exit with accumulator if we have executed this instruction before
    local inst = self.instructions[self.pc]
    if inst.visited then
      return self.acc
    end
    
    -- 4. Execute the instruction
    -- print("execution instruction @", self.pc, ":", inst.operation, inst.argument)
    local acc, delta_pc = inst:execute(self.acc)
    self.acc = acc
    self.pc = self.pc + delta_pc
  end
  
  -- 5. Broke the Infinite Loop
  return nil
end

function Console:reset_visited()
  -- Set all visited flags to false
  
  -- 1. Loop for all the instructions
  for _, inst in ipairs(self.instructions) do
    
    -- 2. Reset the visited flag
    inst.visited = false
  end
end

function Console:fix_the_program()
  -- Change a single instruction to avoid the infinate loop
  
  -- 1. Loop for every instruction
  for _, inst in ipairs(self.instructions) do
    
    -- 2. Modify and test if it is not an acc instruction
    if inst.operation ~= 'acc' then
      
      -- 3. Replace the instrunction jmp <--> nop
      local original = inst.operation
      if original == 'jmp' then
        inst.operation = 'nop'
      else
        inst.operation = 'jmp'
      end
      
      -- 4. Execute the new program
      local result = self:infinite_loop()
      
      -- 5. If we corrected the program, return the accumulator
      if result == nil then
        return self.acc
      end
      
      -- 5. Reset the instruction
      inst.operation = original
      
      -- 6. And the visited flags
      self:reset_visited()
    end
  end
  
  -- 7. We tried every instruction but had no luck
  return nil
end


function Console:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:infinite_loop()
end


function Console:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:fix_the_program()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Console

-- ======================================================================
-- end                      c o n s o l e . l u a                     end
-- ======================================================================
