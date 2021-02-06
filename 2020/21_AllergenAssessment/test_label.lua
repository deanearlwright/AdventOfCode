-- ======================================================================
-- Allergen Assessment
--   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ l a b e l . l u a
-- ======================================================================
-- Test Label for Advent of Code 2020 day 21, Allergen Assessment

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local label = require('label')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"

-- ======================================================================
--                                                              TestLabel
-- ======================================================================

function test_empty_init()
  -- Test the default Label creation

  -- 1. Create default Label object
  local myobj = label:Label()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.ingredients, 0)
  luaunit.assertEquals(#myobj.allergens, 0)

end

function test_text_init()
  -- Test the Label object creation from text

  -- 1. Create Shopping object from text
  local myobj = label:Label({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  luaunit.assertEquals(#myobj.ingredients, 4)
  luaunit.assertEquals(#myobj.allergens, 2)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:has_ingredient('mxmxvkd'), true)
  luaunit.assertEquals(myobj:has_ingredient('kfcds'), true)
  luaunit.assertEquals(myobj:has_ingredient('dairy'), false)
  luaunit.assertEquals(myobj:has_allergen('dairy'), true)
  luaunit.assertEquals(myobj:has_allergen('fish'), true)
  luaunit.assertEquals(myobj:has_allergen('soy'), false)
  luaunit.assertEquals(myobj:has_allergen('kfcds'), false)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                    t e s t _ l a b e l . p y                   end
-- ======================================================================
