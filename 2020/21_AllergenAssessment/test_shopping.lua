-- ======================================================================
-- Allergen Assessment
--   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ s h o p p i n g . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 21, Allergen Assessment

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local shopping = require('shopping')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- Break the text into trimed, non-comment lines

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch('[^\r\n]+') do

    -- 3. But ignore blank and comment lines
    line = line:gsub("%s*$", "")
    if #line > 0 and "!" ~= line:sub(1, 1) then

      -- 4. Add the line
      table.insert(result, line)
    end
  end

  -- 5. Return a table of cleaned lines
  return result
end

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = [[
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 5
local PART_TWO_RESULT = "mxmxvkd,sqjhc,fvjkl"

-- ======================================================================
--                                                           TestShopping
-- ======================================================================


function test_empty_init()
  -- Test the default Shopping creation

  -- 1. Create default Shopping object
  local myobj = shopping:Shopping()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.labels, 0)
  luaunit.assertEquals(#myobj.ingredients, 0)
  luaunit.assertEquals(#myobj.allergens, 0)
  luaunit.assertEquals(#myobj.mapping, 0)

end

function test_text_init()
  -- Test the Shopping object creation from text

  -- 1. Create Shopping object from text
  local myobj = shopping:Shopping({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 4)
  luaunit.assertEquals(#myobj.labels, 4)
  luaunit.assertEquals(#myobj.ingredients, 7)
  luaunit.assertEquals(#myobj.allergens, 3)
  luaunit.assertEquals(#myobj.mapping['soy'], 2)
  luaunit.assertEquals(myobj.mapping['soy']:has('sqjhc'), true)
  luaunit.assertEquals(myobj.mapping['soy']:has('fvjkl'), true)
  luaunit.assertEquals(#myobj.mapping['dairy'], 1)
  luaunit.assertEquals(myobj.mapping['dairy']:has('mxmxvkd'), true)
  luaunit.assertEquals(tostring(myobj.mapping['dairy']), '{mxmxvkd}')
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:count_ingredient('mxmxvkd'), 3)
  luaunit.assertEquals(#myobj:not_safe(), 3)
  luaunit.assertEquals(#myobj:safe(), 4)
  luaunit.assertEquals(myobj:count_ingredients(myobj:safe()), 5)  
  luaunit.assertEquals(myobj:resolve_allergens(), true)
  luaunit.assertEquals(#myobj.mapping['dairy'], 1)
  luaunit.assertEquals(#myobj.mapping['fish'], 1)
  luaunit.assertEquals(#myobj.mapping['soy'], 1)
  luaunit.assertEquals(myobj.mapping['dairy']:has('mxmxvkd'), true)
  luaunit.assertEquals(myobj.mapping['fish']:has('sqjhc'), true)
  luaunit.assertEquals(myobj.mapping['soy']:has('fvjkl'), true)
  luaunit.assertEquals(myobj:sorted_ingredients(), {"mxmxvkd", "sqjhc", "fvjkl"})
end

function test_part_one()
  -- Test part one example of Shopping object

  -- 1. Create Shopping object from text
  local myobj = shopping:Shopping({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Shopping object

  -- 1. Create Shopping object from text
  local myobj = shopping:Shopping({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                t e s t _ s h o p p i n g . l u a               end
-- ======================================================================
