-- ======================================================================
-- Adapter Array
--   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         j o l t s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 10 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Jolts = { part2 = false, text = {}, numbers = {}, device = 0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Jolts
-- ======================================================================

-- Object for Adapter Array

function Jolts:Jolts (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.numbers = {}
  o.device = 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Jolts:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Start with a low value for the maximum
  local max = 0
  
  -- 2. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    local num = tonumber(line)
    table.insert(self.numbers, num)
    
    -- 3. Keep track of the maximum
    max = math.max(max, num)
  end

  -- 4. device is 3 + maximum of the adaptors
  self.device = max + 3
  
  -- 5. Sort the numbers
  table.sort(self.numbers)
  -- print(table.concat(self.numbers, ", ") )
  
end

function Jolts:count_diff()
  -- Returns the number of 1 and 3 differences
  
  -- 1. Start with nothing
  local one = 0
  local three = 0
  local last = 0
  
  -- 2. Loop for all the numbers (in sorted order)
  for _, jolts in ipairs(self.numbers) do
    
    -- 3. Compute and count the difference the difference
    local diff = jolts - last
    if diff == 1 then
      one = one + 1
    else
      three = three + 1
    end
    
    -- 4. The current value is now the last one
    last = jolts
  end
  
  -- 5. One for three difference to connect to the device
  three = three + 1
  
  -- 6. Return the counts
  return one, three
end

function Jolts:count_arrangements()
  -- Count the number of arrangements of adaptors from outlet to device
  
  -- 1. Start with a no arrangements
  local arrangements = {}
  -- print(table.concat(self.numbers, ", ") )
  
  -- 2. Loop for all of the adaptors
  for index = 1, #self.numbers do
    local jolts = self.numbers[index]
    
    -- 3. Get the number of the arrangements for the previous three arrangements
    local minus_three = arrangements[jolts-3] or 0
    local minus_two = arrangements[jolts-2] or 0
    local minus_one = arrangements[jolts-1] or 0
    local initial = 0
       
    -- 4. Can this adaptor reach the outlet?
    if jolts <= 3 then
      initial = 1
    end
    
    -- 5. The number of arrangements for this adaptor is the sum of those immediately below it
    -- print(jolts, minus_three, minus_two, minus_one, initial)
    arrangements[jolts] = minus_three + minus_two + minus_one + initial
    
  end  
  
  -- 6. Return the number of arrangements
  return arrangements[self.numbers[#self.numbers]]
end

    
    
function Jolts:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  local one, three = self:count_diff()
  return one * three
end


function Jolts:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:count_arrangements()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Jolts

-- ======================================================================
-- end                        j o l t s . l u a                       end
-- ======================================================================
