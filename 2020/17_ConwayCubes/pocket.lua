-- ======================================================================
-- Conway Cubes
--   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p o c k e t . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 17 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Pocket = { part2 = false, text = {}, cycle = 0, active = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local ACTIVE = '#'
 
-- ======================================================================
--                                                                 Pocket
-- ======================================================================

-- Object for Conway Cubes

function Pocket:Pocket (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.cycle = 0
  o.active = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Pocket:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for y, cells in ipairs(text) do

    -- 2. Loop for each cube on the line of cells
    for x = 1, #cells do
      
      -- 3. Add the active cells (ignoring the inactive ones)
      if cells:sub(x,x) == ACTIVE then
        if self.part2 then
          self.active[string.format("%d,%d,0,0", x, y)] = true
        else  
          self.active[string.format("%d,%d,0", x, y)] = true
        end
      end
    end
  end
end

function Pocket:is_active(index)
  -- Return true if specified conway cube is active
  
  -- 1. Return status of cube
  if true == self.active[index] then
    return true
  end
  
  -- 2. Not found in active table, return false
  return false
end

function Pocket:count_active()
  -- Count the number of active cells
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the active cells
  for _, state in pairs(self.active) do
    
    -- 3. If active add to the count
    if state then
      result = result + 1
    end
  end
  
  -- 4. Return the count of active cells
  return result
end

function Pocket:nearby(index)
  -- Return a table of the nearby locations
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Convert index to table location
  local loc = {}
  for x in index:gmatch("[0-9-]+") do
    table.insert(loc, x)
  end
    
  -- 3. Loop for three or four dimensions
  for x = -1, 1 do
    for y = -1, 1 do
      for z = -1, 1 do
        
        -- 4. If part 1, three dimension is enough
        if not self.part2 then
          
          -- 4a. Don't include the center location
          if x ~= 0 or y ~=0 or z ~=0 then
            table.insert(result, string.format("%d,%d,%d", loc[1]+x, loc[2]+y, loc[3]+z))
          end
        else
          -- 5. Part 2 needs four dimentions
          for w = -1, 1 do
            if x ~= 0 or y ~=0 or z ~=0 or w ~= 0 then
              table.insert(result, string.format("%d,%d,%d,%d", loc[1]+x, loc[2]+y, loc[3]+z, loc[4]+w))
            end
          end
        end
      end
    end
  end
  
  -- 5. Return the nearby locations
  return result
end

function Pocket:count_nearby(loc)
  -- Return count of nearby active conway cubes
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the nearby locations
  for _, near in ipairs(self:nearby(loc)) do
    
    -- 3. If the nearby cube is active, increment count
    if self:is_active(near) then
      result = result + 1
    end
  end
  
  -- 4. Return the count of nearby active cubes
  return result
end

function Pocket:one_cycle()
  -- Simulate the conway cubes for one cycle
  
  -- 1. Start with nothing
  local next_active = {}
  local next_checked = {}
  
  -- 2. Loop for all of the active cells
  for act_loc, _ in pairs(self.active) do
    
    -- 3. Determine if it will remain active
    local act_count = self:count_nearby(act_loc)
    if act_count == 2 or act_count == 3 then
      next_active[act_loc] = true
    end
    
    -- 4. Loop for all of the neighbors of the active cell
    for _, act_nearby in ipairs(self:nearby(act_loc)) do
      
      -- 5. Ignore neighbors that are active or we have already checked
      if not self:is_active(act_nearby) and nil == next_checked[act_nearby] then
        
        -- 6. Determine if the neighbor will become active
        if self:count_nearby(act_nearby) == 3 then
          next_active[act_nearby] = true
        end
        
        -- 7. Remember we checked this nearby location
        next_checked[act_nearby] = true
      end
    end
  end
  
  -- 8. The future is now
  self.active = next_active
  
  -- 9. Update the cycle count
  self.cycle = self.cycle + 1
end
  
function Pocket:run_until(cycle)
  -- Return count of active cubes after the specified cycle
  
  -- 1. Loop until we react the specified cycle
  while self.cycle < cycle do
    
    -- 2. Execute the next cycle
    self:one_cycle()
  end
  
  -- 3. Return the count of active cubes
  return self:count_active()
end

    
function Pocket:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:run_until(6)
end


function Pocket:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:run_until(6)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Pocket

-- ======================================================================
-- end                       p o c k e t . l u a                      end
-- ======================================================================
