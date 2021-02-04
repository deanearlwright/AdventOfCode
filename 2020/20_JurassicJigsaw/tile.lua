-- ======================================================================
-- Jurassic Jigsaw
--   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                           t i l e . l u a
-- ======================================================================
-- Tile for the Advent of Code 2020 Day 20 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Tile = { part2=false, text={}, 
               number=0, rows={}, rot = {}, flip = {}, alt = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Tile
-- ======================================================================


function Tile:Tile (o)
  -- Object for Jurassic Jigsaw

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.number = 0
  o.rows = {}
  o.rot = {}
  o.flip = {}
  o.alt = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
    o:_process_text(o.text)
  end

  -- 4. Construct alternatives
  if #o.rows > 0 then
    o:construct_alternatives(false)
  end
  
  -- 5. Return the tile
  return o
end

function Tile:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for all the text 
  for _, row in ipairs(self.text) do
    
    -- 2. The first row contains the number
    if row:sub(1,5) == "Tile " then
      self.number = tonumber(row:sub(6,9))
    else
      -- 3. Add the row to the rows
      table.insert(self.rows, row)
    end
  end
end

function Tile:construct_alternatives(combined)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(#self.rows > 0 and #self.rows == string.len(self.rows[1]))
  
  -- 1. Set initial rotation (not actually rotated) and save it
  self:_initial_rotation(combined)
  
  -- 2. Add the four flips
  self:add_four_flips(combined)
  
  -- 3. Rotate and add
  self:rotate()
  self:add_four_flips(combined)
  
  -- 4. Rotate and add
  self:rotate()
  self:add_four_flips(combined)
  
  -- 5. Rotate and add
  self:rotate()
  self:add_four_flips(combined)
  
end
 
function Tile:_initial_rotation()
  -- Convert rows of character version of tile to rows of columns
  
  -- 0. Precondition axioms
  assert(#self.rows > 0 and #self.rows == string.len(self.rows[1]))
  
  -- 1. Start with nothing
  self.rot = {}
  
  -- 2. Loop for all the rows
  for _, row in ipairs(self.rows) do
    
    -- 3. Collect the columns
    local cols = {}
    for col in row:gmatch(".") do
      table.insert(cols, col)
    end
    
    -- 4. Add columns to the rotation rows
    table.insert(self.rot, cols)
  end
end

function Tile:rotate()
  -- Rotate the tile one position 
  
  -- 0. Precondition axioms
  assert(#self.rot > 0 and #self.rot == #self.rot[1])
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Loop for the columns 
  for col_indx = 1, #self.rows do
    -- 3. Start the new row  
    local new_row = {}
    -- 4. Loop for the old reversed rows
    for row_indx = #self.rows, 1, -1 do
      -- 5. Add a character to the new row
      table.insert(new_row, self.rot[row_indx][col_indx])
    end
    -- 6. Add the new row to the result
    table.insert(result, new_row)
  end
  -- 7. Save the new rotation
  self.rot = result
end

function Tile:_initial_flip()
  -- Set the flipped tiles from the current rotation
  
  -- 0. Precondition axioms
  assert(#self.rot > 0 and #self.rot == #self.rot[1])
  
  -- 1. Start with nothing
  self.flip = {}
  
  -- 2. Loop for the rows in the rotated image
  for _, row in ipairs(self.rot) do
    
    -- 3. Added to the flipped tile row
    table.insert(self.flip, row)
  end
end

function Tile:borders_and_image()
  -- Get the top, right, bottom, and left borders and the internal image
  
  -- 0. Precondition axioms
  assert(#self.flip > 0 and #self.rot == #self.flip[1])
  
  -- 1. Start with nothing
  local image = {}
  
  -- 2. Get the image as rows of characters
  for row_indx = 2, 9 do
    local row = self.flip[row_indx]
    local image_row = {}
    for col_indx = 2, 9 do
      table.insert(image_row, row[col_indx])
    end
    table.insert(image, table.concat(image_row, ''))
  end
  
  -- 3. Get the top and bottom borders
  local top = table.concat(self.flip[1], '')
  local bottom  = table.concat(self.flip[10], '')
  
  -- 4. Get the right and left borders
  local right = {}
  local left = {}
  for _, row in ipairs(self.flip) do
    table.insert(right, row[10])
    table.insert(left, row[1])
  end
  right = table.concat(right, '')
  left = table.concat(left, '')
  
  -- 5. Return the top, right, bottom, and left borders and the internal image
  return top, right, bottom, left, image
end

function Tile:flip_hor()
  -- Flip tile top to bottom
  
  -- 0. Precondition axioms
  assert(#self.flip > 0 and #self.rot == #self.flip[1])
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Loop for all rows, bottom to top
  for row_indx = #self.rows, 1, -1 do
    
    -- 3. Add row to result
    table.insert(result, self.flip[row_indx])
  end
  
  -- 4. Set the new flipped tile
  self.flip = result
end

function Tile:flip_ver()
  -- Flip tile left to right
  
  -- 0. Precondition axioms
  assert(#self.flip > 0 and #self.rot == #self.flip[1])
  
  -- 1. Start with nothing
  local result = {}
  
  -- 2. Loop for all rows, top to bottom
  for _, row in ipairs(self.flip) do
    
    -- 3. Loop for all columns, right to left
    local new_row = {}
    for col_indx = #self.rows, 1, -1 do
      table.insert(new_row, row[col_indx])
    end
    
    -- 4. Add the reversed row to the result
    table.insert(result, new_row)
  end
  
  -- 5. Set the new flipped tile
  self.flip = result
end
  
function Tile:add_four_flips(combined)
  -- Add the four flipsL none, hor, ver, hor and ver

  -- 0. Precondition axioms
  assert(#self.rot > 0 and #self.rot == #self.rot[1])

  -- 1. Set the initial flip
  self:_initial_flip()
  -- 2. Add the initial (non-flipped) version to alternatives
  self:add_alternative(combined)
  -- 3. Flip it top to bottom and add it
  self:flip_hor()
  self:add_alternative(combined)
  -- 4. And then flip that left to right and add it
  self:flip_ver()
  self:add_alternative(combined)
  -- 5. Flip it again top to bottom to get just the left to right flip
  self:flip_hor()
  self:add_alternative(combined)
end

function Tile:add_alternative(combined)  
  -- Add the alternative image
  
  -- 0. Precondition axioms
  assert(#self.flip > 0 and #self.rot == #self.flip[1])
  
  -- 1. If processing the combined image, just add it
  if combined then
    local image = {}
    for _, row in ipairs(self.flip) do
      table.insert(image, table.concat(row, ''))
    end
    table.insert(self.alt, image) 
  else    
  
    -- 1. Get the borders and image 
    local top, right, bottom, left, image = self:borders_and_image()
  
    -- 2. Add it to the alternatives 
    self.alt[table.concat({top, right, bottom, left}, ',')] = image
  end
end

function Tile:display()
  -- Display a tile
  return table.concat(self.rows, '\n')
end

function Tile:display_rot()
  -- Display a rotated tile
  local rows = {}
  for _, row in ipairs(self.rot) do
    table.insert(rows, table.concat(row, ''))
  end
  return table.concat(rows, '\n')
end

function Tile:display_flip()
  -- Display a flipped tile
  local rows = {}
  for _, row in ipairs(self.flip) do
    table.insert(rows, table.concat(row, ''))
  end
  return table.concat(rows, '\n')
end

function Tile:border(border, letter)
  -- Return the Top, Right, Bottom, or Left section of the border
  
  -- 0. Precondition axioms
  assert(border:len() == 43)
  assert(letter == 'T' or letter == 'R' or letter == 'B' or letter == 'L')
  
  -- 1. Return a section of border based on the letter
  if letter == 'T' then
    return border:sub(1,10)
  end
  if letter == 'R' then
    return border:sub(12,21)
  end
  if letter == 'B' then
    return border:sub(23,32)
  end
  return border:sub(34,43)
end

function Tile:count_alt()
  -- Return the number of alternatives
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all the alternatives
  for _, _ in pairs(self.alt) do
     -- 3. Increment the count
     result = result + 1
   end
   
   -- 4. Return the number of alternatives
   return result
 end
 
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Tile

-- ======================================================================
-- end                          t i l e . l u a                       end
-- ======================================================================
