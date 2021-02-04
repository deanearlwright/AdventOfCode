-- ======================================================================
-- Jurassic Jigsaw
--   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         i m a g e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 20 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local tile = require('tile')
local tiles = require('tiles')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Image = { part2 = false, text = {}, tiles = nil, image = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- local MONSTER_PATTERN1 = '..................#.'
local MONSTER_PATTERN2 = '#....##....##....###'
local MONSTER_PATTERN3 = '.#..#..#..#..#..#...'

local MONSTER_POUNDS = 1 + 8 + 6
    
-- ======================================================================
--                                                                  Image
-- ======================================================================

-- Object for Jurassic Jigsaw

function Image:Image (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.tiles = nil
  o.image = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o.tiles = tiles:Tiles({part2=o.part2, text=o.text})
  end

  -- 4. Put tiles in the correct orientations
  if o.tiles ~= nil then
    o.tiles:position_tiles()
  end
  
  return o
end

function Image:corners()
  if self.tiles == nil then
    return nil
  end
  return self.tiles:corners()
end

function Image:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:corners()
end

function Image:rough_seas()
  -- Returns the rough the waters are in the sea monsters' habitat
  
  -- 1. Get the combined image
  if self.tiles == nil then
    return nil
  end
  local image = self.tiles:image()
  
  -- 2. Get the total number of pound signs
  local total_pound_signs = self:count_pound_signs(image)
  print("Total pounds signs =", total_pound_signs)
  
  -- 3. Create tile with image
  local image_tile = tile:Tile()
  image_tile.rows = image
  -- print(image_tile:display())
  
  -- 4. Create the alternative images
  image_tile:construct_alternatives(true)
  -- print("alternatives", #image_tile.alt)
  
  -- 5. Loop through the alternative images
  local most_monsters = 0
  for inum, alt_image in ipairs(image_tile.alt) do
    -- print("image", inum, "rows", #alt_image)
  
    -- 6. Get count of monsters in the image
    local monsters = self:count_monsters(alt_image)
    print("image", inum, monsters, most_monsters)
  
    -- 7. If monster count > 0, return non-monster pound signs
    if monsters > most_monsters then
      most_monsters = monsters
    end
  end  
  
  -- 8. No monsters found anywhere
  if most_monsters > 0 then 
    return total_pound_signs - most_monsters * MONSTER_POUNDS
  end
  
  return nil
end

function Image:find_all_starts(pattern, row)
  -- Find all (could be over lapping) starting location of the partern

  -- 1. Start with nothing
  local result = {}
  local pos = 1

  -- 2. Loop for every search hit
  local where, _ = row:find(pattern, pos)
  while where do

    -- 3. Record this match
    table.insert(result, where)

    -- 4. Advance and try again
    pos = where + 1
    where = row:find(pattern, pos)
  end
  
  -- 5. Return all starting locations
  return result
end

function Image:count_pound_signs(text)
  -- Count the number of pound signs in the text
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the rows of the test
  for _, row in ipairs(text) do
    
    -- 3. Get the number of pound signs in the row
    local _, row_knt = row:gsub("#", "+")
    
    -- 4. Increment the count
    result = result + row_knt
  end
  
  --5. Return the total number of pound signs in all the rows
  return result
end

function Image:count_monsters(image)
  -- Return the number of monsters found in the image
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the rows
  for rnum, row in ipairs(image) do
    
    -- 3. Only look at row three or higher
    if rnum >= 3 then
      
      -- 4. Find the starts
      local start2 = self:find_all_starts(MONSTER_PATTERN2, image[rnum-1])
      local start3 = self:find_all_starts(MONSTER_PATTERN3, row)
      
      -- 4. Loop for all of the possible sightings
      for _, in3 in ipairs(start3) do
          
        -- 5. Found the bottom of the monster, how about the middle?
        for _, in2 in ipairs(start2) do
          if in2 == in3 then
            
          -- 6. That looks good, increment count
            result = result + 1
          end
        end
      end
    end
  end
  
  -- 7. Return the count of sea monsters found in this image
  return result
end


function Image:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:rough_seas()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Image

-- ======================================================================
-- end                        i m a g e . l u a                       end
-- ======================================================================
