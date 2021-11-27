-- ======================================================================
-- StreamProcessing
--   Advent of Code 2017 Day 09 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         g r o u p s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 09 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Groups = { part2 = false, text = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local state_table = {
  [1] = {["{"] = 7, ["<"] = 9, [">"] = 9, ["}"] = 9, [","] = 9, ["!"] = 9, ["?"] = 9 }, -- 1 Initial
  [2] = {["{"] = 7, ["<"] = 3, [">"] = 9, ["}"] = 8, [","] = 2, ["!"] = 9, ["?"] = 9 }, -- 2 In Brace
  [3] = {["{"] = 6, ["<"] = 6, [">"] = 2, ["}"] = 6, [","] = 6, ["!"] = 4, ["?"] = 6 }, -- 3 In Garbage
  [4] = {["{"] = 3, ["<"] = 3, [">"] = 3, ["}"] = 3, [","] = 3, ["!"] = 3, ["?"] = 3 }, -- 4 In Shriek
}  
  
-- ======================================================================
--                                                                 Groups
-- ======================================================================

-- Object for StreamProcessing

function Groups:Groups(o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  return o
end

function Groups:next_state(state, character)
  -- Return the next state
  
  -- 1. Get the current row in the state table
  local row = state_table[state]
  
  -- 2. Get the next state
  local next_state = row[character]
  if next_state == nil then
    next_state = row["?"]
  end
  
  -- 3. Return the next state
  return next_state
end

function Groups:score_braces(line)
  -- Score the braces
  
  -- 1. Initial state
  local score = 0
  local state = 1
  local depth = 0
  
  -- 2. Loop for all characters of the string
  for indx = 1, #line do
    local character = line:sub(indx, indx)
    
    -- 3. Get the next state
    local new_state = self:next_state(state, character)
    -- print("score_braces", state, character, new_state, state, depth, indx)
    
    -- 4. Process special states
    if new_state == 9 then
      print("Unexpected character", character, score, state, depth, indx)
      return -1
    elseif new_state == 8 then
      score = score + depth
      depth = depth - 1
      if depth == 0 then
        new_state = 1
      else
        new_state = 2
      end
    elseif new_state == 7 then
      depth = depth + 1
      new_state = 2
    elseif new_state == 6 then
      new_state = 3
    end
    
    -- 5. Set the state
    state = new_state
  end
  
  -- 6. Return the score
  return score
end

function Groups:score_garbage(line)
  -- Score the braces
  
  -- 1. Initial state
  local score = 0
  local state = 1
  local depth = 0
  
  -- 2. Loop for all characters of the string
  for indx = 1, #line do
    local character = line:sub(indx, indx)
    
    -- 3. Get the next state
    local new_state = self:next_state(state, character)
    -- print("score_braces", state, character, new_state, state, depth, indx)
    
    -- 4. Process special states
    if new_state == 9 then
      print("Unexpected character", character, score, state, depth, indx)
      return -1
    elseif new_state == 8 then
      depth = depth - 1
      if depth == 0 then
        new_state = 1
      else
        new_state = 2
      end
    elseif new_state == 7 then
      depth = depth + 1
      new_state = 2
    elseif new_state == 6 then
      score = score + 1
      new_state = 3
    end
    
    -- 5. Set the state
    state = new_state
  end
  
  -- 6. Return the score
  return score
end
  
function Groups:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:score_braces(self.text[1])
end


function Groups:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:score_garbage(self.text[1])
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Groups

-- ======================================================================
-- end                       g r o u p s . l u a                      end
-- ======================================================================
