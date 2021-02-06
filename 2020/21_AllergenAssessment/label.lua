-- ======================================================================
-- Allergen Assessment
--   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         l a b e l . l u a
-- ======================================================================
-- Label for the Advent of Code 2020 Day 21 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local set = require('set')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Label = { part2=false, text='', ingredients = {}, allergens = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Label
-- ======================================================================

function Label:Label(o)
  -- Object for Allergen Assessment


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.ingredients = set:Set()
  o.allergens = set:Set()
  
  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Label:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Divide the at string "contains"
  local contains_beg, contains_end = text:find("contains")
  local ingredients = text:sub(1, contains_beg-1)
  local allergens = text:sub(contains_end+1)
  
  -- 2. Add the ingredents
  for ingredient in ingredients:gmatch("%a+") do
    self.ingredients:add(ingredient)
  end
  
  -- 3. Add the allergens
  for allergen in allergens:gmatch("%a+") do
    self.allergens:add(allergen)
  end
end

function Label:has_ingredient(ingredient)
  -- Return true of the label lists the ingredient
  return self.ingredients:has(ingredient)
end

function Label:has_allergen(allergen)
  -- Return true of the label lists the allergen
  return self.allergens:has(allergen)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Label

-- ======================================================================
-- end                        l a b e l . l u a                       end
-- ======================================================================
