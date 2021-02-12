-- ======================================================================
-- Lobby Layout
--   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t i l e s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 24, Lobby Layout

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local tiles = require('tiles')

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
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 10
local PART_TWO_RESULT = 2208

NEXT_DAY = {15, 12, 25, 14, 23, 28, 41, 37, 49, 37}

-- ======================================================================
--                                                              TestTiles
-- ======================================================================


function test_empty_init()
  -- Test the default Tiles creation

  -- 1. Create default Tiles object
  local myobj = tiles:Tiles()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:how_many_black(), 0)
  

end

function test_text_init()
  -- Test the Tiles object creation from text

  -- 1. Create Tiles object from text
  local myobj = tiles:Tiles({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 20)
  
  -- 3. Test methods
  luaunit.assertEquals(myobj:how_many_black(), 10)
  luaunit.assertEquals(myobj:tile(10000, 10000), true)
  luaunit.assertEquals(myobj:tile(10500, 10500), false)
  luaunit.assertEquals(myobj:tile(10010, 9980), true)
  local neighbors = myobj:neighbors(10000, 10000)
  luaunit.assertEquals(#neighbors, 6)
  luaunit.assertItemsEquals(neighbors, {999509995, 999510005, 1000510005, 1000009990, 1000010010, 1000509995})
  luaunit.assertItemsEquals(myobj:black_neighbors(neighbors), 1)
  
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[1])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[2])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[3])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[4])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[5])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[6])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[7])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[8])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[9])
  luaunit.assertEquals(myobj:next_day(), true)
  luaunit.assertEquals(myobj:how_many_black(), NEXT_DAY[10])

end

function test_part_one()
  -- Test part one example of Tiles object

  -- 1. Create Tiles object from text
  local myobj = tiles:Tiles({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Tiles object

  -- 1. Create Tiles object from text
  local myobj = tiles:Tiles({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ t i l e s . l u a                  end
-- ======================================================================
