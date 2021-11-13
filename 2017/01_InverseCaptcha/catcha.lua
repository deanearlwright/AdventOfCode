-- ======================================================================
-- InverseCaptcha
--   Advent of Code 2017 Day 01 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         c a t c h a . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 01 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Catcha = { part2 = false, text = {}, numbers = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Catcha
-- ======================================================================

-- Object for InverseCaptcha

function Catcha:Catcha (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.numbers = {}
  o.count = 0
  o.offset = 1

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text[1])
  end
  
  -- 4. Compute the offset
  if o.count > 0 then
    if o.part2 then
      o.offset = o.count // 2
    else
      o.offset = 1
    end
  end

  -- 5. Return the object
  return o
end

function Catcha:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Start with a clean table
  result = {}

  -- 2. Save the count of the numbers
  self.count = string.len(text)
  
  -- 3. Loop for each character of the first line text
  for indx = 1, self.count do

    -- 4. Add the number to the entries
    table.insert(result, tonumber(string.sub(text, indx, indx)))
  end

  -- 5. Copy the result to the numbers
  for indx = 1, self.count do
    table.insert(self.numbers, result[indx])
  end
  
  -- 6. Part two needs a second copy to deal with the greater offset, part 1 just a single number
  if self.part2 then
    for indx = 1, self.count do
      table.insert(self.numbers, result[indx])
    end
  else
    table.insert(self.numbers, result[1])
  end
end

function Catcha:solve()
  -- Determine the Captcha solution
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for the numbers
  for indx = 1, self.count do
  
    -- 3. Get this number and the next
    local number = self.numbers[indx]
    local following = self.numbers[indx + self.offset]
      
    -- 4. If they match, increment the result
    if number == following then
      result = result + number
    end
  end    
  
  -- 5. Return the sum of matching numbers
  return result  
end

function Catcha:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:solve()
end


function Catcha:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:solve()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Catcha

-- ======================================================================
-- end                      c a t c h a . l u a                     end
-- ======================================================================
