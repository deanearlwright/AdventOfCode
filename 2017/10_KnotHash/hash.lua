-- ======================================================================
-- Knot Hash
--   Advent of Code 2017 Day 10 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         h a s h . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 10 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Hash = { part2 = false, text = {}, length = 0, numbers = {}, lengths = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
ADDITIONAL_LENGTHS = "17, 31, 73, 47, 23"
DEFAULT_LENGTH = 256

-- ======================================================================
--                                                                   Hash
-- ======================================================================

-- Object for KnotHash

function Hash:Hash(o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.length = o.length or DEFAULT_LENGTH
  o.current = 0
  o.skip = 0
  o.numbers = {}
  o.lengths = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text[1])
  end

  -- 4. Fill in the numbers
  if o.length > 0 then
    for number = 0, o.length - 1 do
      table.insert(o.numbers, number)
    end
  end
  
  -- 5. Return the Hash object
  return o
end

function Hash:_process_text(line)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(line ~= nil and #line > 0)

  -- 1. Loop for each number in the line
  for number in string.gmatch(line, "%d+") do

    -- 2. Add the number to the lengths
    table.insert(self.lengths, tonumber(number))
    end
end

function Hash:process_one_knot(3, verbose=False)

function Hash:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return nil
end


function Hash:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return nil
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Hash

-- ======================================================================
-- end                         h a s h . l u a                        end
-- ======================================================================
