-- ======================================================================
-- Toboggan Trajectory
--   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         t r e e s . l u a
-- ======================================================================
-- "A solver for the Advent of Code 2020 Day 03 puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Trees = { part2 = false, text = {}, rows = 0, cols = 0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local TREE = '#'

-- ======================================================================
--                                                                  Trees
-- ======================================================================

-- "Object for Toboggan Trajectory"

function Trees:Trees (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rows = o.rows or 0
  o.cols = o.cols or 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Trees:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Set the number of rows and columns
  self.rows = #text
  self.cols = #text[1]

end

function Trees:is_tree(col, row)
  -- Returns true if there is a tree at (col, row)
  
  -- 1. There are no trees below the forest
  if self:is_below(row) then
    return false
  end
  
  -- 2. Check the forest square
  mcol = 1 + (col - 1) % self.cols
  if TREE == self.text[row]:sub(mcol, mcol) then
    return true
  end
  return false
end

function Trees:is_below(row)
  -- Returns true if beyond forest
  return row > self.rows
end

function Trees:count_trees(delta_col, delta_row)
  -- Returns number of trees hit in toboggen ride

  -- 1. Start at the very beginning
  col, row, count = 1, 1, 0
  
  -- 2. Loop until we are out of the forest
  repeat
    
    -- 3. If this is a tree, count it
    if self:is_tree(col, row) then
      count = count + 1
    end
    
    -- 4. Advance to next location
    col = col + delta_col
    row = row + delta_row
    
  until self:is_below(row)
  
  -- 5. Return the number of tree hit
  return count
end

  
function Trees:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_trees(3, 1)
end


function Trees:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Get counts for multiple paths
  knt_1_1 = self:count_trees(1, 1)
  knt_3_1 = self:count_trees(3, 1)
  knt_5_1 = self:count_trees(5, 1)
  knt_7_1 = self:count_trees(7, 1)
  knt_1_2 = self:count_trees(1, 2)
  
  -- 1. Return the solution for part two
  return knt_1_1 * knt_3_1 * knt_5_1 * knt_7_1 * knt_1_2
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Trees

-- ======================================================================
-- end                      t r e e s . l u a                     end
-- ======================================================================
