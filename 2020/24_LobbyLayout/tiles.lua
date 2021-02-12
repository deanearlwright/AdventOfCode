-- ======================================================================
-- Lobby Layout
--   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         t i l e s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 24 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Tiles = { part2 = false, text = {}, tiles = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local NUMBER_OF_DAYS = 100

local DELTA = {
  E = {10, 0},
  W = {-10, 0},
  NE = {5, -5},
  SE = {5, 5},
  NW = {-5, -5},
  SW = {-5, 5}
}

local BLACK = true
local WHITE = false

local ROWMULT = 100000
-- ======================================================================
--                                                                  Tiles
-- ======================================================================

-- Object for Lobby Layout

function Tiles:Tiles (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.tiles = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:process_text(o.text)
  end

  return o
end

function Tiles:process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Determine the location of this tile
    local loc = self:location(line)
    -- print(loc, line)
    -- 3. Set (or reset) the tile
    if nil == self.tiles[loc] then
      self.tiles[loc] = BLACK
    else
      self.tiles[loc] = nil
    end
  end
end

function Tiles:location(line)
  -- Determine the location of the tile by following the direction instructions
  
  -- 1. Isolate the instructions
  local instructions = string.gsub(line, "nw", "NW,")
  instructions = string.gsub(instructions, "ne", "NE,")  
  instructions = string.gsub(instructions, "sw", "SW,")  
  instructions = string.gsub(instructions, "se", "SE,")  
  instructions = string.gsub(instructions, "w", "W,")  
  instructions = string.gsub(instructions, "e", "E,")  
  
  -- 2. Start at the reference tile
  local loc = {10000, 10000}
  
  -- 3. Loop for all of the instructions
  for inst in instructions:gmatch("%a+") do
    
    -- 4. Adjust the location
    loc[1] = loc[1] + DELTA[inst][1]
    loc[2] = loc[2] + DELTA[inst][2]
  end
  
  -- 5. Return the final location as a single number
  return loc[2] * ROWMULT + loc[1]
end
  
function Tiles:how_many_black()
  -- Return count of black tiles
  
  -- 1. Start with none
  local result = 0
  
  -- 2. Loop through all the tiles
  for _, side in pairs(self.tiles) do
    -- print(loc, side)
    
    -- 3. If the black side is up, increment count
    if side then
      result = result + 1
    end
  end
  
  -- 4. Return the number of tiles with the black side showing
  return result
end

function Tiles:tile(row, col)
  -- Return the status (BLACK or WHITE) of a tile
  
  -- 1. Convert the row and column to an index
  local index = row * ROWMULT + col 
  
  -- 2. If no tile saved, then it is white
  if nil == self.tiles[index] then
    return WHITE
  end
  
  -- 3. Return the status of the tile
  return self.tiles[index]
end


function Tiles:neighbors(row, col)
  -- Return the tiles next to the specified tile
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Loop for all of the neighbors
  for _, delta in pairs(DELTA) do
    
    -- 3. Get the location of the nearby tile
    local loc = (row + delta[2]) * ROWMULT + delta[1] + col
    
    -- 4. Add the locations
    table.insert(result, loc)
  end
  
  -- 5. Return the nearby tile locations
  return result
end
  
function Tiles:black_neighbors(nearby)
  -- Return the number of neighboring black tiles
  
  -- 0. Precondition axions
  assert(#nearby == 6)
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the neighbors
  for _, loc in ipairs(nearby) do
    
    -- 3. Get the status of the nearby tile
    -- print(loc, self.tiles[loc])
    local side = self.tiles[loc]
    
    -- 4. If the tile is black, increment the count
    if side == BLACK then
      result = result + 1
    end
  end
  
  -- 5. Return the number of nearby black tiles
  return result
end

function Tiles:next_day()
  -- Advance tiles, returns true is something changed
  
  -- 1. Start with nothing
  local future = {}
  local changed = false
  local checked = {}
  
  -- 2. Loop for all of the current tiles (should all be black)
  for loc, side in pairs(self.tiles) do
    
    -- 3. Split the localtion into column and row
    local col = loc % ROWMULT
    local row = loc // ROWMULT
    -- print("next_day", loc, side, row, col)
      
    -- 3. Get the locations of nearby tiles
    local black_neighbors = self:neighbors(row, col)
    
    -- 4. Get the count of nearby black tiles
    local black_count = self:black_neighbors(black_neighbors)
            
    -- 5. we keep black tiles if it has exactly one or two neighbors
    if side == BLACK then
      if black_count == 1 or black_count == 2 then
        future[loc] = BLACK
        -- print("keeping black", loc)
      else  
        -- print("black to white", loc)
        changed = true
      end
      
      -- 6. Check the white tiles near the black one
      for _, nearby in ipairs(black_neighbors) do
        if self.tiles[nearby] ~= BLACK and nil == checked[nearby] then
          
          local white_col = nearby % ROWMULT
          local white_row = nearby // ROWMULT
          local white_neighbors = self:neighbors(white_row, white_col)
          local white_count = self:black_neighbors(white_neighbors)
          
          -- 7. A while tile changes to black if there are exactly two black tiles nearby
          if white_count == 2 then
            -- print("Setting to black", nearby)
            future[nearby] = true
            changed = true
          end
        end
        checked[nearby] = true
      end
        
    else  
      -- 8. A while tile changes to black if there are exactly two black tiles nearby 
      if black_count == 2 then
        future[loc] = BLACK
        changed = true
      end
    end
  end
  
  -- 9. The future is now
  self.tiles = future
  
  -- 10. Return true if any tile changed
  return changed
end

function Tiles:multiple_days(days)
  -- Advance the floor many times
  
  -- 1. Loop for the number of days
  for _ = 1, days do
    
    -- 2. Advance one day
    self:next_day()
  end
  
  -- 3. Return the number of black files
  return self:how_many_black()
end

function Tiles:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:how_many_black()
end


function Tiles:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:multiple_days(NUMBER_OF_DAYS)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Tiles

-- ======================================================================
-- end                        t i l e s . l u a                       end
-- ======================================================================
