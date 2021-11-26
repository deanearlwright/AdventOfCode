-- ======================================================================
-- Recursive Circus
--   Advent of Code 2017 Day 07 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         t o w e r . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 07 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Tower = { part2 = false, text = {}, 
                weights = {}, supporting = {}, supported = {},
                heights = {}, combined = {}, unbalanced = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Tower
-- ======================================================================

-- Object for Recursive Circus

function Tower:Tower (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {} -- table of input.txt lines
  o.weights = {} -- weights[disc] = weight as integer
  o.supporting = {} -- supporting[disc] = table of the discs that the disc supports
  o.supported = {} -- supported[disc] = the disc that supports that disc
  o.heights = {} -- heights[disc] = height as integer (1 is the bottom)
  o.combined = {} -- combined[disc] = combined weight of disc plus any it supports
  o.unbalanced = {} -- unbalanced[disc] = height of unbalanced supporting disc

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Tower:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do
    local disc = ""
    local weight = 0
    local supporting = {}

    -- 2. loop for the items on the line
    for what in line:gmatch("%w+") do
      
      -- 3. Set disc or weight if not already set
      if disc == "" then
        disc = what
      elseif weight == 0 then
        weight = tonumber(what)
        
      -- 4. Else add to supporting
      else
        table.insert(supporting, what)
      end
    end
    
    -- 5. Add the information from this line to the object
    self.weights[disc] = weight
    if #supporting > 0 then
      self.supporting[disc] = supporting
      for _, supported in ipairs(supporting) do
        self.supported[supported] = disc
      end
    end
  end
end

function Tower:bottom()
  -- Return the name of the bottom disc
  
  -- 1. Loop for all of the disc that support others
  for disc, supporting in pairs(self.supporting) do
    
    -- 2. But it can't be supported by others
    if self.supported[disc] == nil then
      return disc
    end
  end
  
  -- 3. How wierd, must be an Esher tower
  return nil
end

function Tower:set_all_heights()
  -- Set the heights
  
  -- 1. Reset the heights
  self.heights = {}
  
  -- 2. Start at the bottom and work your way up
  self:set_height(self:bottom(), 1)
end

function Tower:set_height(disc, height)
  -- Recursively set height
  
  -- 1. Set the height of this disc
  self.heights[disc] = height
  
  -- 2. If this is a supporting disc, set the heights of the supported discs
  local supported = self.supporting[disc]
  if supported then
    
    -- 3. Loop for all of the supported disks
    for _, sdisc in ipairs(supported) do
      
      -- 4. Set the height of the supported disc
      self:set_height(sdisc, height + 1)
      
    end
  end
end

function Tower:set_all_combined()
  -- Set the combined weights
  
  -- 1. Reset the combined weights
  self.combined = {}
  
  -- 2. Start at the bottom and work your way up
  self:set_combined(self:bottom())
end

function Tower:set_combined(disc)
  -- Recursively set combined weight
  
  -- 1. Start with the weight of the disc itself
  local total = self.weights[disc]
  
  -- 2. If this is a supporting disc, get/set the weights of the supported discs
  local supported = self.supporting[disc]
  if supported then
    
    -- 3. Loop for all of the supported disks
    for _, sdisc in ipairs(supported) do
      
      -- 4. Set/Get the combined weight of the supported disc
      local sweight = self:set_combined(sdisc)
      
      -- 5. Add that weight to the total
      total = total + sweight
      
    end
  end
  
  -- 6. Set the combined weight of the disc
  self.combined[disc] = total
  
  -- 7. And return it
  return total
end

function Tower:find_unbalanced()
  -- Populated unbalanced with the height of the unbalanced nodes
  
  -- 1. Reset unbalanced
  self.unbalanced = {}
  
  -- 2. Loop for all of the supporting nodes
  for disc, supporting in pairs(self.supporting) do
    
    -- 3. Get the combined weights
    local combined = {}
    for _, disc in ipairs(supporting) do
      table.insert(combined, self.combined[disc])
    end
    
    -- 4. Get the minimum and maximum weights
    table.sort(combined)
    local min_weight = combined[1]
    local max_weight = combined[#combined]
    
    -- 5. If unbalanced, save the height
    if min_weight < max_weight then
      self.unbalanced[disc] = self.heights[disc]
    end
  end
end

function Tower:highest_unbalanced()
  -- Return the highest unbalanced disc
  
  -- 1. Start with none
  local highest = nil
  local max_height = 0
  
  -- 2. Loop for all the unbalanced discs
  for disc, height in pairs(self.unbalanced) do
    
    -- 3. Keep the highest one
    if height > max_height then
      highest = disc
      max_height = height
    end
  end
  
  -- 4. Return the highest unbalanced disc
  return highest
end

function Tower:balance(unbalanced)
  -- Return weight needed to balance the unbalanced
  
  -- 1. Need to get the weights of the towers and the bases
  local combined = {}
  local towers = {}
  local supported = {}
  
  -- 2. Loop for all of the supported discs
  for _, disc in ipairs(self.supporting[unbalanced]) do
    
    -- 3. Set the combined and supported weights
    table.insert(combined, self.combined[disc])
    table.insert(supported, self.weights[disc])
    
    -- 4. Set the weight of the tower above the sported disc
    table.insert(supported, self.combined[disc] - self.weights[disc])
  end
  
  -- 5. Find the odd weight
  local weights = {}
  for _, weight in ipairs(combined) do
    if weights[weight] == nil then
      weights[weight] =  1
    else
      weights[weight] = weights[weight] + 1
    end
  end
  local odd_weight
  local even_weight
  for weight, number in pairs(weights) do
    if number == 1 then
      odd_weight = weight
    else
      even_weight = weight
    end
  end
  
  -- 6. Who has the odd weight?
  local odd_man = nil
  for _, disc in ipairs(self.supporting[unbalanced]) do
    if self.combined[disc] == odd_weight then
      odd_man = disc
    end
  end
  local old_weight = self.weights[odd_man]
  local new_weight = old_weight - (odd_weight - even_weight)
  print(unbalanced, odd_man, odd_weight, even_weight, old_weight, new_weight)
  
  -- 7. Return the repaired weight
  return new_weight
end

function Tower:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:bottom()
end


function Tower:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Set additional tables
  self:set_all_heights()
  self:set_all_combined()
  self:find_unbalanced()
  
  -- 2. Get the node that needs balancing
  local disc = self:highest_unbalanced()
  
  -- 1. Return the solution for part two
  return self:balance(disc)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Tower

-- ======================================================================
-- end                        t o w e r . l u a                       end
-- ======================================================================
