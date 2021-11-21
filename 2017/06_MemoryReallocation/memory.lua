-- ======================================================================
-- MemoryReallocation
--   Advent of Code 2017 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         m e m o r y . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 06 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Memory = { part2 = false, text = {}, banks = {}, history = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Memory
-- ======================================================================

-- Object for MemoryReallocation

function Memory:Memory (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.banks = {}
  o.history = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text[1])
  end

  return o
end

function Memory:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Start with nothing
  self.banks = {}
  
  -- 2. Loop for the number on the line of the text
  for num in text:gmatch("%d+") do

    -- 3. Add the number to the entries
    table.insert(self.banks, tonumber(num))
    end

  -- 4. Remember the initial value in the history
  self:to_history()
end

function Memory:to_history()
  -- Save the current memory block count to history
  table.insert(self.history, table.concat(self.banks, ","))
end

  
function Memory:most_blocks()
  -- Return the index to the bank with the most blocks
  
  -- 1. Assume the first bank
  local result = 1
  local highest = self.banks[1]
  
  -- 2. Loop through the banks
  for index = 1, #self.banks do
    
    -- 3. If this bank has more blocks, remember it
    if self.banks[index] > highest then
      result = index
      highest = self.banks[index]
    end
  end
  
  -- 4. Return the number of the bank with the most blocks
  return result
end

function Memory:redistribute(bank)
  -- Redistribute the memory blocks from the specified bank
  
  -- 1. Get the number of blocks from the bank and clear it
  local blocks = self.banks[bank]
  self.banks[bank] = 0
  
  -- 2. Give one block to the banks until we run out of blocks to give
  while blocks > 0 do
    
    -- 2a. Determine the next bank
    bank = self:next_bank(bank)
    
    -- 2b. Give the next bank one more memory block
    self.banks[bank] = 1 + self.banks[bank]
    
    -- 2c. Decrement the number of memory blocks to distribute
    blocks = blocks - 1
  end
  
  -- 3. Remember the new distribution in the history
  self:to_history()
  
end

function Memory:next_bank(bank)
  -- Return the number of the next bank to the right, looping back to the first one
  
  -- 1. Increment the bank number
  bank = bank + 1
  
  -- 2. If off the end, bring it bank around
  if bank > #self.banks then
    bank = 1
  end
  
  -- 2. Return the next bank number
  return bank
end

function Memory:deja_vu()
  -- Return where the latest history was seen before
  
  -- 1. Get the latest history
  local latest = self.history[#self.history]
  
  -- 2. Loop for all of the older history
  for index = 1, #self.history do
    
    -- 3. If there is is a match return the index
    if latest == self.history[index] then
      return index
    end
  end
  
  -- 4. Didn't find it
  return #self.history
end

function Memory:loop_until_repeat()
  -- Reallocate memory until we get to a configuration we have seen before
  
  -- 1. loop until there is a repeat
  while self:deja_vu() == #self.history do
    
    -- 2. Select the largest bank
    local bank = self:most_blocks()
    
    -- 3. Redistribute the banks
    self:redistribute(bank)
  end
  
  -- 4. Return the total number of steps
  return #self.history - 1
end

function Memory:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:loop_until_repeat()
end


function Memory:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  local steps = self:loop_until_repeat()
  local start = self:deja_vu()
  return 1 + steps - start
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Memory

-- ======================================================================
-- end                       m e m o r y . l u a                      end
-- ======================================================================
