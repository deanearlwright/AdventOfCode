-- ======================================================================
-- Custom Customs
--   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         g r o u p s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 06 puzzle
-- ---------------------------
-------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local group = require('group')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Groups = { part2 = false, text = {}, groups = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Groups
-- ======================================================================

-- Object for Custom Customs

function Groups:Groups (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.groups = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  o.numbers = {}
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Groups:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Start with no answers for the group
  local answers = {}
  
  -- 2. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 3. If this is a blank like save the collected answers (if any)
    if #line == 0 then
      if #answers > 0 then
        local grp = group:Group({part2=self.part2, text=answers})
        table.insert(self.groups, grp)
        answers = {}
      end
    
    -- 4. Else accumulate answers
    else
      table.insert(answers, line)
    end
  end
  
  -- 5. Add any final answers
  if #answers > 0 then
    local grp = group:Group({part2=self.part2, text=answers})
    table.insert(self.groups, grp)
  end

end

function Groups:total_yes()
  -- Total the yes count from all the groups
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all the groups
  for _, grp in ipairs(self.groups) do
    
    -- 3. Add in the could from the group
    result = result + grp:count_yes()
    
  end
  
  -- 4. Return the total count
  return result
end

    
function Groups:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:total_yes()
end


function Groups:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:total_yes()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Groups

-- ======================================================================
-- end                      g r o u p s . l u a                     end
-- ======================================================================
