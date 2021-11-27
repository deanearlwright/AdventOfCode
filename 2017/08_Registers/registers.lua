-- ======================================================================
-- Registers
--   Advent of Code 2017 Day 08 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r e g i s t e r s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 08 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Registers = { part2 = false, text = {}, regs = {}, highest = 0 }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local DECODE_INST = "(%l+) ([id][ne]c) (-?%d+) if (%l+) ([<>!=]+) (-?%d+)"

-- ======================================================================
--                                                              Registers
-- ======================================================================

-- Object for Registers

function Registers:Registers(o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.regs = {}
  o.highest = 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  return o
end

function Registers:decode_inst(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Find the parts of the instruction
  beg, _, r1, incdec, by, r2, cmp, value = string.find(text, DECODE_INST)
  
  -- 2. Were we able to decode it?
  if beg ~= 1 then
    print("Unable to decode", text)
    return {"?", 0, "?", "?", "?"}
  end
  if incdec ~= "inc" and incdec ~= "dec" then
    print("Unable to decode inc/dec", incdec, text)
    return {"?", 0, "?", "?", "?"}
  end  
  
  -- 3. Make the numbers numbers
  by = tonumber(by)
  value = tonumber(value)
  if incdec == "dec" then
    by = -by
  end
  
  -- 4. Return the parts of the instruction
  return {r1, by, r2, cmp, value}
end

function Registers:get_register(reg)
  -- Return the value of the register
  
  -- 1. Retrieve the current value
  local value = self.regs[reg]
  
  -- 2. If no current value, use zero
  if value == nil then 
    value = 0
  end
  
  -- 3. Return the value of the specified register
  return value
end

function Registers:set_register(reg, value)
  -- Set register to the specified value
  
  -- 1. Get the existing value
  local old_value = self:get_register(reg)
  
  -- 2. Set the value in the register
  self.regs[reg] = value
  
  -- 3. If this is a new high value, save it
  if value > self.highest then
    self.highest = value
  end
    
  -- 4. Return the old value
  return old_value
end

function Registers:one_inst(number)
  -- Execute one instruction
  
  -- 1. Get the instruction
  local inst_text = self.text[number]
  
  -- 2. Decode the instruction
  local r1, by, r2, cmp, value  = table.unpack(self:decode_inst(inst_text))
  
  
  -- 3. Get the registers values
  local r1_value = self:get_register(r1)
  local r2_value = self:get_register(r2)
  -- print(self.pc, inst_text, r1, r1_value, by, r2, r2_value, cmp, value)
  
  -- 4. Test conditional
  local cond = false
  if cmp == "==" and r2_value == value then
    cond = true
  elseif cmp == "<" and r2_value < value then  
    cond = true
  elseif cmp == ">" and r2_value > value then  
    cond = true
  elseif cmp == "<=" and r2_value <= value then  
    cond = true
  elseif cmp == ">=" and r2_value >= value then  
    cond = true
  elseif cmp == "!=" and r2_value ~= value then  
    cond = true
  end
  
  -- 5. If conditional is true inc/dec register
  if cond then
    self:set_register(r1, r1_value + by)
  end
  
  -- 6. Return value of conditional
  return cond
end  
  
function Registers:all_inst()
  -- Run all instructions
  
  -- 1. Loop for all of the instructions
  for number = 1, #self.text do
  
    -- 2. Execute the instruction
    self:one_inst(number)
  end
end
  
function Registers:largest()
  -- Return the value of the largest register
  
  -- 1. Start with a very very negative number
  local result = -99999999
  
  -- 2. Loop for all of the registers
  for _, value in pairs(self.regs) do
    
    -- 3. Keep the largest value
    if value > result then
      result = value
    end
  end
  
  -- 4. Return the largest value
  return result
end

  
function Registers:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Run all the instructions
  self:all_inst()
  
  -- 2. Return the solution for part one
  return self:largest()
end


function Registers:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Run all the instructions
  self:all_inst()
  
  -- 2. Return the solution for part two
  return self.highest
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Registers

-- ======================================================================
-- end                    r e g i s t e r s . l u a                   end
-- ======================================================================
