-- ======================================================================
-- Report Repair
--   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r e p o r t . l u a
-- ======================================================================
-- "A solver for the Advent of Code 2020 Day 01 puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Report = {}
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Report
-- ======================================================================

-- "Object for Report Repair"

function Report:Report (o)

  -- 1. Set the initial values
  o = o or {}
  if o.part2 == nil then
    o.part2 = false
  end
  if o.text == nil then
    o.text = {}
  end
  o.numbers = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  -- 4. Return the populated object
  return o
end

function Report:_process_text(text)
  -- "Assign values from text
  
  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do
    
    -- 2. Add the number to the entries
    table.insert(self.numbers, tonumber(line))
    end  
    
end

function Report:get_pair(total)
  -- "Get a pair of numbers that add to the total"
  for _, num in ipairs(self.numbers) do
    need = total - num
    for _, other in ipairs(self.numbers) do
      if other == need and other ~= num then
        return num, other
      end
    end
  end  
  return nil, nil
end  

function Report:get_trio(total)
  -- "Get a trio of numbers that add to the total"
  for _, num in ipairs(self.numbers) do
    need = total - num
    p1, p2 = self:get_pair(need)
    if p1 ~= nil then
      return num, p1, p2
    end
  end  
  return nil, nil, nil
end  
  
function Report:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  n1, n2 = self:get_pair(2020)
  if n1 == nil then 
    return nil
  end  
  return n1 * n2
end


function Report:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  n1, n2, n3 = self:get_trio(2020)
  if n1 == nil then 
    return nil
  end  
  return n1 * n2 * n3
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Report

-- ======================================================================
-- end                      r e p o r t . l u a                     end
-- ======================================================================
