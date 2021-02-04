-- ======================================================================
-- Jurassic Jigsaw
--   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ i m a g e . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 20, Jurassic Jigsaw

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local image = require('image')
local tile = require('tile')

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
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TEXT

local PART_ONE_RESULT = 20899048083289
local PART_TWO_RESULT = 273

local IMAGE = {
  ".#.#..#.##...#.##..#####",
  "###....#.#....#..#......", 
  "##.##.###.#.#..######...",
  "###.#####...#.#####.#..#",
  "##.#....#.##.####...#.##",
  "...########.#....#####.#",
  "....#..#...##..#.#.###..",
  ".####...#..#.....#......",
  "#..#.##..#..###.#.##....",
  "#.####..#.####.#.#.###..",
  "###.#.#...#.######.#..##",
  "#.####....##..########.#",
  "##..##.#...#...#.#.#.#..",
  "...#..#..#.#.##..###.###",
  ".#.#....#.##.#...###.##.",
  "###.#...#..#.##.######..",
  ".#.#.###.##.##.#..#.##..",
  ".####.###.#...###.#..#.#",
  "..#.#..#..#.#.#.####.###",
  "#..####...#.#.#.###.###.",
  "#####..#####...###....##",
  "#.##..#..#...#..####...#",
  ".#.###..##..##..####.##.",
  "...###...##...#...#..###"
}

local MONSTER_ROWS = {
  ".####...#####..#...###..",
  "#####..#..#.#.####..#.#.",
  ".#.#...#.###...#.##.##..",
  "#.#.##.###.#.##.##.#####",
  "..##.###.####..#.####.##",
  "...#.#..##.##...#..#..##",
  "#.##.#..#.#..#..##.#.#..",
  ".###.##.....#...###.#...",
  "#.####.#.#....##.#..#.#.",
  "##...#..#....#..#...####",
  "..#.##...###..#.#####..#",
  "....#.##.#.#####....#...",
  "..##.##.###.....#.##..#.",
  "#...#...###..####....##.",
  ".#.##...#.##.#.#.###...#",
  "#.###.#..####...##..#...",
  "#.###...#.##...#.######.",
  ".###.###.#######..#####.",
  "..##.#..#..#.#######.###",
  "#.#..##.########..#..##.",
  "#.#####..#.#...##..#....",
  "#....##..#.#########..##",
  "#...#.....#..##...###.##",
  "#..###....##.#...##.##.#"
}


local MONSTER_PATTERN2 = '#....##....##....###'

-- ======================================================================
--                                                              TestImage
-- ======================================================================


function test_empty_init()
  -- Test the default Image creation

  -- 1. Create default Image object
  local myobj = image:Image()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.tiles, nil)
  luaunit.assertEquals(#myobj.image, 0)

end

function test_text_init()
  -- Test the Image object creation from text

  -- 1. Create Image object from text
  local myobj = image:Image({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 99)
  luaunit.assertNotEquals(myobj.tiles, nil)
  luaunit.assertEquals(#myobj.image, 0)
  luaunit.assertEquals(#myobj.tiles.tiles, 9)
  luaunit.assertEquals(myobj.tiles.size, 3)
  luaunit.assertEquals(myobj.tiles.tiles[1].number, 2311)
  luaunit.assertEquals(myobj.tiles.tiles[9].number, 3079)

  -- 3. Check methodes
  luaunit.assertEquals(myobj:corners(), 20899048083289)
  luaunit.assertEquals(myobj:count_pound_signs(IMAGE), 273 + 2*15)
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[1]), {})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[2]), {})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[3]), {})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[4]), {3})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[5]), {})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[17]), {})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[18]), {2})
  luaunit.assertEquals(myobj:find_all_starts(MONSTER_PATTERN2, MONSTER_ROWS[19]), {})
  
  luaunit.assertEquals(myobj:count_monsters(MONSTER_ROWS), 2)
  luaunit.assertEquals(myobj:rough_seas(), 273)
end

function test_image()
  -- Test working with the alternative images
  
  -- 1. Create Image object from text
  local myobj = image:Image({text=from_text(EXAMPLE_TEXT)})
  luaunit.assertEquals(myobj:corners(), 20899048083289)
  
  -- 2. Built a tile with that image and construct alternatives
  local image_tile = tile:Tile()
  image_tile.rows = myobj.tiles:image()
  
  -- 4. Create the alternative images
  image_tile:construct_alternatives(true)
end

  
function test_part_one()
  -- Test part one example of Image object

  -- 1. Create Image object from text
  local myobj = image:Image({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Image object

  -- 1. Create Image object from text
  local myobj = image:Image({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ i m a g e . l u a                  end
-- ======================================================================
