-- ======================================================================
-- Encoding Error
--   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         c y p h e r . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 09 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Cypher = { part2 = false, text = {}, numbers = {}, preamble = 25 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Cypher
-- ======================================================================

-- Object for Encoding Error

function Cypher:Cypher (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.preable = o.preamble or 25
  o.numbers = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Cypher:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    table.insert(self.numbers, tonumber(line))
    end

end

function Cypher:rule_breaker()
  -- Finds a number that does match the summary rule
  
  -- 1. Set index based on size of preamble
  local test_start = 1 + self.preamble
  local test_end = #self.numbers
  local found = nil
  
  -- 2. Loop for all of the numbers to test
  for tindex = test_start, test_end do
    local test = self.numbers[tindex]
    found = test
    
    -- 3. Loop for all of the previous numbers
    for pindex = tindex - self.preamble, tindex - 2 do
      local previous = self.numbers[pindex]
      
      -- 4. Loop for the remaining previous numbers
      for rindex = pindex + 1, tindex - 1 do
        local remaining = self.numbers[rindex]
        
        -- 5. Check if this pair of previous numbers is equal to the test number
        if previous + remaining == test then
          
          -- 6. This test number is fine, we will need another
          found = nil
        end
      end
    end
    
    -- 7. If this number did not satisify, return it
    if found ~= nil then
      return found
    end  
    
    -- 8. Try another number
  end
  
  -- 9. Every number satisified
  return nil
end

function Cypher:weakness()
  -- Find the weakness in the XMAS code
  
  -- 1. Need the rule breaker from part 1
  local rule_breaker = self:rule_breaker()
  local knt_numbers = #self.numbers
  -- print(rule_breaker, knt_numbers)
  
  -- 2. Loop for all of the numbers (except the last)
  for bindex = 1, knt_numbers -1 do
    local bnumber = self.numbers[bindex]
    local sum = bnumber
    local min = bnumber
    local max = bnumber
      
    -- 3. Loop for the remainin numbers
    for rindex = bindex + 1, knt_numbers do
      local rnumber = self.numbers[rindex]
      sum = sum + rnumber
      min = math.min(min, rnumber)
      max = math.max(max, rnumber)
      -- print(bindex, rindex, sum, min, max, rule_breaker)
        
      -- 4. So these number sum to the rule_breaker?
      if sum == rule_breaker then
          
        -- 5. If so return the minimum and maximum numbers
        return min + max
      end
        
      -- 6. If the sum is greater than the rule_breaker we need a new beginning
      if sum > rule_breaker then
        goto continue
      end
        
    end
    :: continue ::
  end
  
  -- 7. Never found a string of numbers which added up to the rule_breaker
  return nil
end

    
function Cypher:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:rule_breaker()
end


function Cypher:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:weakness()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Cypher

-- ======================================================================
-- end                       c y p h e r . l u a                      end
-- ======================================================================
