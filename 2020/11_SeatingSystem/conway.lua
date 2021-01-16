-- ======================================================================
-- Seating System
--   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         c o n w a y . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 11 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Conway = { part2 = false, text = {}, seats = {}, leave = 4 }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local SEAT_FLOOR = "."
local SEAT_EMPTY = "L"
local SEAT_OCCUPIED = '#'
local SEAT_BEYOND = ' '

local NEIGHBORS = { {-1, -1}, {-1, 0}, {-1, 1},
                    { 0, -1},          { 0, 1},
                    { 1, -1}, { 1, 0}, { 1, 1} }

-- ======================================================================
--                                                                 Conway
-- ======================================================================

-- Object for Seating System

function Conway:Conway (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.seats = {}
  if o.part2 then
    o.leave = 5
  else  
    o.leave = 4
  end
  
  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Conway:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Split the line into individual characters (seats and floors)
    local row = {}
    line:gsub(".", function(c) table.insert(row, c) end)
  
    -- 3. Add the row to the current status
    table.insert(self.seats, row)
  end

end

function Conway:count_occupied() 
  -- Count the currently occupied seats
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the rows
  for _, row in ipairs(self.seats) do
    
    -- 3. Loop for all of the seats (and some floors) in the row
    for _, seat in ipairs(row) do
      
      -- 4. If the seat is occupied, increment the count
      if seat == SEAT_OCCUPIED then
        result = result + 1
      end
    end
  end
  
  -- 5. Return the count of occupied seats
  return result
end

function Conway:seat(row, col)
  -- Return the status of a single seat
  return self.seats[row][col]
end

function Conway:neighbor(row, col, delta)
  -- Return the status of a seat near the specified seat
  
  -- 1. Compute the seat number
  local delta_row = row + delta[1]
  local delta_col = col + delta[2]
  
  -- 2. If off the seating plan, return floor
  if delta_row < 1 or delta_col < 1 or delta_row > #self.seats or delta_col > #self.seats then
    return SEAT_BEYOND
  end
  
  -- 3. Return the seat status
  return self:seat(delta_row, delta_col)
end

  
function Conway:neighbors(row, col)
  -- Return the number of occupied seats near the specified seat
  
  -- 1. Start with nothing
  local num_occupied = 0
  
  -- 2. Loop for all of the neighbors
  for _, delta in ipairs(NEIGHBORS) do
    
    -- 3. Get the status of the nearby seat
    local nbor = self:neighbor(row, col, delta)
    -- print(row, col, delta[1], delta[2], nbor)
    
    -- 4. If the seat is occupied, increment occupied count
    if nbor == SEAT_OCCUPIED then
      num_occupied = num_occupied + 1
      
    -- 5. If part2 we look until the next seat  
    elseif self.part2 and nbor == SEAT_FLOOR then
      nbor = self:sight_line_neighbor(row, col, delta)
      if nbor == SEAT_OCCUPIED then
        num_occupied = num_occupied + 1
      end
    end
  end
  
  -- 6. Return the number of nearby occupied seats
  return num_occupied
end

function Conway:sight_line_neighbor(row, col, delta)
  -- Returns the next seat in the sight line
  
  -- 1. Start with with floor
  local nbor = SEAT_FLOOR
  local delta_row = row + delta[1]
  local delta_col = col + delta[2]
  
  -- 2. Loop until we are not at a a floor space
  while nbor == SEAT_FLOOR do
    
    -- 3. Check the next space
    nbor = self:neighbor(delta_row, delta_col, delta)
    
    -- 4. Advance
    delta_row = delta_row + delta[1]
    delta_col = delta_col + delta[2]
  end
  
  -- 5. Return the non-Floor value
  return nbor
end
   
  
function Conway:next_round()
  -- Advance seats occupation, returns True is something changed
  
  -- 1. Start with nothing
  local future = {}
  local changed = false
  
  -- 2. Loop for all of the rows and seats in the row
  for rnum, row in ipairs(self.seats) do
    local future_row = {}
    for cnum, seat in ipairs(row) do
      local future_seat = seat
      
      -- 3. Get the number of occupied seats
      local num_occupied = 0
      if seat ~= SEAT_FLOOR then 
        num_occupied = self:neighbors(rnum, cnum)
      end
            
      -- 4. An empty seat becomes occupied if there are no nearby occupied seats
      if seat == SEAT_EMPTY and num_occupied == 0 then
        future_seat = SEAT_OCCUPIED
        changed = true
      -- 5. An occupied seat becomed empty if four or more seats adjacent to it are occupied  
      elseif seat == SEAT_OCCUPIED and num_occupied >= self.leave then
        future_seat = SEAT_EMPTY
        changed = true
      end
      
      -- 6. Set the future seat in the future row
      table.insert(future_row, future_seat)
    end
    -- 7. Set the future row 
    table.insert(future, future_row)
  end
  
  -- 8. The future is now
  self.seats = future
  
  -- 9. Return true if the occupation of a seat changed
  return changed
end

function Conway:show(before, after)
  -- Show the seats
  
  -- 1. If there is a before label, print it
  if before ~= nil then
    print(before)
  end
  
  -- 2. Loop for all of the rows
  for _, row in ipairs(self.seats) do
    
    -- 3. Print the row as text
    print(table.concat(row, ''))
  end

  -- 4. If there is an after label, print it
  if after ~= nil then
    print(after)
  end
end
  
function Conway:until_stable()
  -- Run multiple rounds until stable, return number of occupied seats
  
  -- 1. Loop until no changes
  while self:next_round() do end
  
  -- 2. Return the number of occupied seats
  return self:count_occupied()
end


function Conway:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:until_stable()
end


function Conway:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:until_stable()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Conway

-- ======================================================================
-- end                       c o n w a y . l u a                      end
-- ======================================================================
