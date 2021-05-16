-- ======================================================================
-- Allergen Assessment
--   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         s h o p p i n g . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 21 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local label = require('label')
local set = require('set')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Shopping = { part2 = false, text = {}, 
  labels = {}, ingredients = {}, allergens = {}, mapping = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                               Shopping
-- ======================================================================

-- Object for Allergen Assessment

function Shopping:Shopping (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.labels = {}
  o.ingredients = set:Set()
  o.allergens = set:Set()
  o.mapping = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Shopping:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the label to the labels
    table.insert(self.labels, label:Label({part2=self.part2, text=line}))
    end

  -- 2. Get list of ingredients
  for _, lab in ipairs(self.labels) do
    for ing in pairs(lab.ingredients) do
      self.ingredients:add(ing)
    end
  end
  
  -- 3. Get list of allergens
  for _, lab in ipairs(self.labels) do
    for alg in pairs(lab.allergens) do
      self.allergens:add(alg)
    end
  end
  
  -- 4. Map the allergens to (possible) ingredients
  for _, lab in ipairs(self.labels) do
    for alg in pairs(lab.allergens) do
      if nil == self.mapping[alg] then
        self.mapping[alg] = set:Set(lab.ingredients)
      else
        self.mapping[alg] = self.mapping[alg] * lab.ingredients
      end
    end
  end
end

function Shopping:not_safe()
  -- Returns all of the not safe ingredients
  
  -- 1. Start with nothing
  local result = set:Set()
  
  -- 2. Loop for all of the allergens mapped to ingredients
  for _, ings in pairs(self.mapping) do
    
    -- 3. Loop for all of the ingredients in that alergin
    for ing, _ in pairs(ings) do
      
      -- 4. Add to the unsafe ingredients
      result:add(ing)
    end
  end
  
  -- 5. Return the suspected unsafe ingredients
  return result
end

function Shopping:safe()
  -- Returns all of the safe ingredients
  
  -- 1. Start with all the ingredients
  local result = set:Set(self.ingredients)
  
  -- 2. Remove the unsafe ones
  result = result - self:not_safe()
  
  -- 3. Return the safe ingredients
  return result
end

function Shopping:count_ingredient(ingredient)
  -- Return the number of times the ingredient appears
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the labels
  for _, lab in ipairs(self.labels) do
    
    -- 3. If the ingredient appears on the label, increment count
    if lab:has_ingredient(ingredient) then
      result = result + 1
    end
  end
  
  -- 4. Return the ingredient count
  return result
end

function Shopping:count_ingredients(ingredients)
  -- Return the number of times the ingredients in the list appear
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the ingredients
  for ing in pairs(ingredients) do
    
    -- 3. Add in the number of times this ingredient appears
    result = result + self:count_ingredient(ing)
  end
  
  -- 4. Return the total ingredient count
  return result
end

function Shopping:resolve_allergens()
  -- Returns true if we could resolve the allergens to their ingredients
  
  -- 1. Impose a limit
  for _ = 1, 10 do
    local done = true
    
    -- 2. Once we find an allergen that can be in only one ingredient
    --    we can remove that ingredient from the other allergen lists
    for _, ingredients in pairs(self.mapping) do
      if #ingredients == 1 then
        local ing = ingredients:pop()
        for _, other in pairs(self.mapping) do
          other:remove(ing)
        end
        ingredients:add(ing)
      else
        done = false
      end
      
      -- 3. If all allergens have only one ingredient, we are done
      if done then
        return true
      end
    end
  end
  
  -- 4. All that work and nothing to show for it
  return false
end

function Shopping:sorted_ingredients()
  -- Return the list of ingredients sorted by allergens
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Sort the mapping by allergen
  local algs = self.allergens:tolist()
  table.sort(algs)
      
  -- 3. Add the sorted ingredians to the result
  for _, alg in ipairs(algs) do
    table.insert(result, self.mapping[alg]:element())
  end
  
  -- 4. Return the sorted ingredients
  return result
end

function Shopping:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_ingredients(self:safe())
end


function Shopping:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  if self:resolve_allergens() then 
    return table.concat(self:sorted_ingredients(), ',')
  end
  return nil
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Shopping

-- ======================================================================
-- end                     s h o p p i n g . l u a                    end
-- ======================================================================
