-- ======================================================================
-- Jurassic Jigsaw
--   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ t i l e . l u a
-- ======================================================================
-- Test Tile for Advent of Code 2020 day 20, Jurassic Jigsaw

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

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
]]

local EXAMPLE_DISPLAY = [[..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###]]

local EXAMPLE_ROTATED = [[.#..#####.
.#.####.#.
###...#..#
#..#.##..#
#....#.##.
...##.##.#
.#...#....
#.#.##....
##.###.#.#
#..##.#...]]

local EXAMPLE_FLIP_HOR = [[#..##.#...
##.###.#.#
#.#.##....
.#...#....
...##.##.#
#....#.##.
#..#.##..#
###...#..#
.#.####.#.
.#..#####.]]

local BORDERS = "#..##.#...,.#..#.##..,.#..#####.,###..###.."

local EXAMPLE_IMAGE = [[#.###.#.
.#.##...
#...#...
..##.##.
....#.##
..#.##..
##...#..
#.####.#]]

local EXAMPLE_FLIP_VER = [[...#.##..#
#.#.###.##
....##.#.#
....#...#.
#.##.##...
.##.#....#
#..##.#..#
#..#...###
.#.####.#.
.#####..#.]]

local BORDERSV = "...#.##..#,###..###..,.#####..#.,.#..#.##.."

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

local MONSTER_IMAGE = [[.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#]]



-- ======================================================================
--                                                               TestTile
-- ======================================================================

function test_empty_init()
  -- Test the default Tile creation

  -- 1. Create default Tile object
  local myobj = tile:Tile()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.number, 0)
  luaunit.assertEquals(#myobj.rows, 0)
  luaunit.assertEquals(#myobj.flip, 0)
  luaunit.assertEquals(#myobj.alt, 0)

end

function test_text_init()
  -- Test the Tile object creation from text

  -- 1. Create Image object from text
  local myobj = tile:Tile({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.number, 2311)
  luaunit.assertEquals(#myobj.rows, 10)
  luaunit.assertEquals(myobj.rows[1]:len(), 10)
  luaunit.assertEquals(myobj.rows[1], "..##.#..#.")
  luaunit.assertEquals(myobj.rows[10]:len(), 10)
  luaunit.assertEquals(myobj.rows[10], "..###..###")
  luaunit.assertEquals(#myobj.flip, 10)
  luaunit.assertEquals(table.concat(myobj.alt[BORDERS],'\n'), EXAMPLE_IMAGE)
  luaunit.assertEquals(myobj:count_alt(), 8)
    
  -- 3. Check methods
  luaunit.assertEquals(myobj:display(), EXAMPLE_DISPLAY)
  myobj:_initial_rotation()
  luaunit.assertEquals(myobj:display_rot(), EXAMPLE_DISPLAY)
  myobj:rotate()
  luaunit.assertEquals(myobj:display_rot(), EXAMPLE_ROTATED)
  myobj:_initial_flip()
  luaunit.assertEquals(myobj:display_flip(), EXAMPLE_ROTATED)
  myobj:flip_hor()
  luaunit.assertEquals(myobj:display_flip(), EXAMPLE_FLIP_HOR)
  local top, right, bottom, left, image = myobj:borders_and_image()
  luaunit.assertEquals(table.concat({top, right, bottom, left}, ','), BORDERS)
  luaunit.assertEquals(table.concat(image,'\n'), EXAMPLE_IMAGE)
  myobj:flip_ver()
  luaunit.assertEquals(myobj:display_flip(), EXAMPLE_FLIP_VER)
  top, right, bottom, left, image = myobj:borders_and_image()
  luaunit.assertEquals(table.concat({top, right, bottom, left}, ','), BORDERSV)
  luaunit.assertEquals(myobj:border(BORDERS, 'T'), "#..##.#...")
  luaunit.assertEquals(myobj:border(BORDERS, 'R'), ".#..#.##..")
  luaunit.assertEquals(myobj:border(BORDERS, 'B'), ".#..#####.")
  luaunit.assertEquals(myobj:border(BORDERS, 'L'), "###..###..")
end

function test_image()
  -- Test the default Tile creation

  -- 1. Create default Tile object
  local myobj = tile:Tile()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.number, 0)
  luaunit.assertEquals(#myobj.rows, 0)

  -- 3. Set the image
  myobj.rows = IMAGE
  
  -- 4. Methods
  luaunit.assertEquals(myobj:display(), table.concat(myobj.rows, '\n'))
  myobj:construct_alternatives(true)
  luaunit.assertEquals(#myobj.alt, 16)
  local found = false
  for _, altimg in ipairs(myobj.alt) do
    if table.concat(altimg,'\n') == MONSTER_IMAGE then
      found = true
      end
  end
  luaunit.assertEquals(found, true)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                     t e s t _ t i l e . p y                    end
-- ======================================================================
