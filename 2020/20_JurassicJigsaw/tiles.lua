-- ======================================================================
-- Jurassic Jigsaw
--   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                          t i l e s . l u a
-- ======================================================================
-- Tiles for the Advent of Code 2020 Day 20 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local tile = require('tile')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Tiles = { part2=false, text={}, tiles={}, size=0, grid={} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local TILE_SIZE = 10

-- ======================================================================
--                                                                  Tiles
-- ======================================================================


function Tiles:Tiles (o)
  -- Object for Jurassic Jigsaw


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.tiles = {}
  o.size = 0
  o.grid = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Tiles:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Start with nothing
  local tile_text = {}
  
  -- 2. Loop for all the lines in the text
  for _, line in ipairs(text) do
    
    -- 3. Add this line to the tile_text
    table.insert(tile_text, line)
    
    -- 4. Do we have enough lines for a tile?
    if #tile_text == TILE_SIZE + 1 then
      
      -- 5. Yes, Create a tile and add it to the collection
      table.insert(self.tiles, tile:Tile({part2=self.part2, text=tile_text}))
      tile_text = {}
    end
  end
  
  -- 6. Determine the image size
  self.size = math.sqrt(#self.tiles)
end

function Tiles:position_tiles()
  -- Position oriented tiles in a nice grid
  
  -- 1. Create an empty grid
  local grid = {}
  
  -- 2. Fill it with nothing
  for _ = 1, self.size do
    local row = {}
    for _ = 1, self.size do
      table.insert(row, {})
    end
    table.insert(grid, row)
  end
  
  -- 3. Find (hopefully) a workable solution
  self.grid = self:_position_tiles(grid, 1, 1)
end

function Tiles:number_at(row, col)
  -- Return the tile number at the grid location
  if #self.grid == 0 then 
    return 0
  end
  if row < 1 or row > #self.grid then
    return 0
  end
  if col < 1 or col > #self.grid then
    return 0
  end
  if #self.grid[row][col] == 0 then
    return 0
  end
  return self.grid[row][col][1].number
end

function Tiles:corners()
  -- Return the product of the tiles in the corners
  return self:number_at(1,1) * self:number_at(1,self.size) * self:number_at(self.size,1) * self:number_at(self.size, self.size)
end

function Tiles:is_placed(grid, the_tile)
  -- Return true of the tile is already in the grid
  
  -- 1. Loop for the rows and columns of the grid
  for _, row in ipairs(grid) do
    for _, col in ipairs(row) do
      
      -- 2. If the tile is here, return true
      if #col > 0 and col[1].number == the_tile.number then
        return true
      end
    end
  end
  
  -- 3. The tile was not found in the grid
  return false
end

function Tiles:_position_tiles(grid, row, col)
  -- Recursively position the oriented tiles in a nice grid
  -- print("_position_tiles", row, col, self.size)
  
  -- 1. Are we done yet?
  if row > self.size then
    return grid
  end
  
  -- 2. Loop for all of the tiles that aren't already in the grid
  for _, the_tile in ipairs(self.tiles) do
    if not self:is_placed(grid, the_tile) then
      
      -- 3. Try placing the tile so that it lines up
      local rest = self:_position_tile(grid, row, col, the_tile) 
      if #rest > 0 then
        return rest
      end
    end
  end
  
  -- 4. Nothing to see here
  return {}
end

function Tiles:_position_tile(grid, row, col, the_tile)
  -- Try to orient the tile at the row and column of the grid
  -- print("_position_tile", row, col, the_tile.number)
  
  -- 1. Loop for all possible orientions of the tile
  for borders, image in pairs(the_tile.alt) do
    
    -- 2. If placed here, would the borders match? 
    local match = true
    if col > 1 then
      local other_borders = grid[row][col-1][2]
      if the_tile:border(other_borders, 'R') ~= the_tile:border(borders, 'L') then
        match = false
      end
    end
    if row > 1 then
      local other_borders = grid[row-1][col][2]
      if the_tile:border(other_borders, 'B') ~= the_tile:border(borders, 'T') then
        match = false
      end
    end
    
    -- 3. If the borders match, save tile in the grid
    if match then
      grid[row][col] = {the_tile, borders, image}
      
      -- 4. Where does the next tile go?
      local next_col = col + 1
      local next_row = row
      if next_col > self.size then
        next_col = 1
        next_row = next_row + 1
      end
      
      -- 5. Now try to fill in the rest of the tiles
      local rest = self:_position_tiles(grid, next_row, next_col)
      if #rest > 0 then
        return rest
      end
    end
    
    -- 6. Try another orientation
  end
  
  -- 7. Couldn't put the tile there
  grid[row][col] = {}
  return {}
end

function Tiles:image()
  -- Return the image as rows of characters
  
  -- 0. Precondition axioms
  assert(#self.grid == self.size)
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Loop for the grid rows
  for _, row in ipairs(self.grid) do
  
    
    -- 3. Loop for the rows of the image segment
    for indx = 1, 8 do
      local image_row = {}
      
      -- 4. Loop for the grid columns of the 
      for _, col in ipairs(row) do
        
        -- 5. Add in this part of the image row
        print("image", col[1].number, col[2], indx, col[3][indx])
        table.insert(image_row, col[3][indx])
      end
      
      -- 6. Add this row to the collected image
      table.insert(result, table.concat(image_row, ''))
    end
  end
  
  -- 7. Return the rows of the image
  return result
end
  
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Tiles

-- ======================================================================
-- end                        t i l e s . l u a                       end
-- ======================================================================
