-- ======================================================================
-- Corruption Checksum
--   Advent of Code 2017 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         c h e c k s u m . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 02 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Checksum = { part2 = false, text = {}, rows = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                               Checksum
-- ======================================================================

-- Object for Corruption Checksum

function Checksum:Checksum (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rows = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Checksum:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do
    
    -- 2. Start a new row 
    row = {}
    
    -- 3. Split up the row
    for num in string.gmatch(line, "[0-9]+") do
      
      -- 4. Add number to the row
      table.insert(row, tonumber(num))
    end
    
    -- 5. Add the row of numbers
    table.insert(self.rows, row)
    end
end

function Checksum:row_min_max_diff(num)
  -- Returns the minimum and maximum of the specified row
  
  -- 1. Get the specified row
  row = self.rows[num]
  
  -- 2. Start with first value
  row_min = row[1]
  row_max = row[1]
  
  -- 3. Loop for the values in the row
  for indx = 2, #row do
    value = row[indx]
    
    -- 4. If higher or lower than saved values, set new value
    if value < row_min then
      row_min = value
    end  
    if value > row_max then
      row_max = value
    end
  end
  
  -- 4 Return the difference between the minimum and maximum values of the row
  return row_max - row_min
end

function Checksum:row_div_even(num)
  -- Returns the result of dividing two numbers in the row evenly
  
  -- 1. Get the specified row
  row = self.rows[num]
  
  -- 2. Loop for all of the numbers in the row
  for indx, value in ipairs(row) do
    
    -- 3. Loop for all of the rest of the numbers in the row
    for indx2 = indx + 1, #row do
      value2 = row[indx2]
      
      -- 4. If they divide evenly, return the result
      if value > value2 and value % value2 == 0 then
        return value // value2
      end
      if value2 > value and value2 % value == 0 then
        return value2 // value
      end
    end
  end
  
  -- 5. I was told that this wouldn't happen
  return nil
end
      
  
function Checksum:total()
  -- Returns the total of the row checksums
  
  -- 1. Start with nothing
  result = 0
  
  -- 2. Loop for all of the rows
  for indx = 1, #self.rows do
    
    -- 3. Get the checksum for the row
    if self.part2 then
      chk = self:row_div_even(indx)
    else  
      chk = self:row_min_max_diff(indx)
    end  
    
    -- 4. Add it to the running total
    result = result + chk
  end
  
  -- 5. Return the total checksum
  return result
end

  
function Checksum:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:total()
end


function Checksum:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:total()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Checksum

-- ======================================================================
-- end                     c h e c k s u m . l u a                    end
-- ======================================================================
