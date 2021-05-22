-- ======================================================================
-- Crab Combat
--   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p l a y e r . l u a
-- ======================================================================
-- Test Player for Advent of Code 2020 day 22, Crab Combat

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local player = require('player')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                             TestPlayer
-- ======================================================================

function test_empty_init()
  -- Test the default Player creation

  -- 1. Create default Player object
  local myobj = player:Player()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.number, 0)
  luaunit.assertEquals(#myobj.cards, 0)
  luaunit.assertEquals(tostring(myobj), '0: ')

end

function test_text_init()
  -- Test the Player object creation from text

  -- 1. Create Game object from text
  local myobj = player:Player({number=1})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.number, 1)
  luaunit.assertEquals(#myobj.cards, 0)
  
  -- 3. Test methods
  myobj:add_cards({9, 2, 6, 3, 1})
  luaunit.assertEquals(#myobj.cards, 5)
  luaunit.assertEquals(tostring(myobj), '1: 9, 2, 6, 3, 1')
  luaunit.assertEquals(myobj:score(), 45 + 8 + 18 + 6 + 1)
  luaunit.assertEquals(myobj:get_top_card(), 9)
  luaunit.assertEquals(#myobj.cards, 4)
  myobj:keep(9, 5)
  luaunit.assertEquals(#myobj.cards, 6)
  luaunit.assertEquals(myobj:score(), 12 + 30 + 12 + 3 + 18 + 5)
  luaunit.assertEquals(myobj:is_deck_empty(), false)  
  luaunit.assertEquals(myobj:get_top_card(), 2)
  luaunit.assertEquals(myobj:get_top_card(), 6)
  luaunit.assertEquals(myobj:get_top_card(), 3)
  luaunit.assertEquals(myobj:get_top_card(), 1)
  luaunit.assertEquals(myobj:get_top_card(), 9)
  luaunit.assertEquals(myobj:get_top_card(), 5)
  luaunit.assertEquals(myobj:is_deck_empty(), true)  
end

function test_clone()
  -- Test the cloning a player

  -- 1. Create Game object from text
  local myobj = player:Player({number=1})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.number, 1)
  luaunit.assertEquals(#myobj.cards, 0)
  
  -- 3. Test methods
  myobj:add_cards({9, 2, 6, 3, 1})
  luaunit.assertEquals(#myobj.cards, 5)
  luaunit.assertEquals(tostring(myobj), '1: 9, 2, 6, 3, 1')
  
  local newobj = myobj:clone(3)
  luaunit.assertEquals(newobj.part2, false)
  luaunit.assertEquals(newobj.number, 1)
  luaunit.assertEquals(#newobj.cards, 3)
  luaunit.assertEquals(tostring(newobj), '1: 9, 2, 6')
end

  
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ p l a y e r . p y                end
-- ======================================================================
