-- ======================================================================
-- Crab Cups
--   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         g a m e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 23 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Game = { part2 = false, text = {}, 
  cups = {}, current = 0, maximum = 0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Game
-- ======================================================================

-- Object for Crab Cups

function Game:Game (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.cups = {}
  o.current = 0
  o.maximum = 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:process_text(o.text)
  end

  return o
end

function Game:process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text == 1)

  -- 1. Start with nothing 
  local values = {}
  
  -- 2. Loop for each line of the text, adding the number to the values
  for num in text[1]:gmatch("%d") do
    table.insert(values, tonumber(num))
  end
  
  -- 3. Loop for most of the values
  for indx = 1, #values - 1 do
  
  -- 4. Make a linked list of the values
    self.cups[values[indx]] = values[indx+1]
  end
  
  -- 5. Make it a circular list
  self.cups[values[#values]] = values[1]
  
  -- 6. Save the maximum cup value
  self.maximum = #values
  
  -- 7. The first cup is the current cup (don't you worry anymore)
  self.current = values[1]
  
  -- 8. For part two add more cups
  if self.part2 then
    self:add_more_cups(values)
  end
  
end

function Game:add_more_cups(values)
  -- Add many more cups
  
  -- 1. Last cup now points to the new cups
  self.cups[values[#values]] = self.maximum + 1
  
  -- 2. Loop to one million (1000000) in total
  for value = self.maximum + 1, 1000000 do
    
    -- 3. Add another cup
    self.cups[value] = value + 1
  end
  
  -- 4. Make it circular
  self.cups[1000000] = values[1]
  
  -- 5. Now we have a much larger maximum
  self.maximum = 1000000
end

  
function Game:__tostring()
  -- Returns the game object as a string
  
  -- 1. Start with cups: and the current value
  local result = string.format('cups: (%d)', self.current)
  if self.current == 0 then
    return result
  end
  
  -- 2. Loop for all of the numbers
  local nxt = self.cups[self.current]
  while nxt ~= self.current do
    
    -- 3. Add the number to the result
    result = result .. string.format(' %d ', nxt)
    
    -- 4. Advance to the next cup
    nxt = self.cups[nxt]
  end
  
  -- 5. Return the formatted object
  return result
end

function Game:move()
  -- Make one move of the cups
          
  -- 1. Pick up three cups
  local picked1 = self.cups[self.current]
  local picked2 = self.cups[picked1]
  local picked3 = self.cups[picked2]
  local after_picked = self.cups[picked3]

  -- 2. Select the destination cup
  local destination = self.current - 1
  while destination < 1 or destination == picked1 or destination == picked2 or destination == picked3 do
    if destination < 1 then
      destination = self.maximum
    else
      destination = destination - 1
    end
  end  

  -- 3. Place the picked cups after the destination
  --    Before: ... -> c -> p1 -> p2 -> p3 -> a -> ...
  --            ... -> d -> x -> ...
  --    After:  ... -> c -> a -> ...
  --            ... -> d -> p1 -> p2 -> p3 -> x -> ...
  self.cups[self.current] = after_picked
  self.cups[picked3] = self.cups[destination]
  self.cups[destination] = picked1

  -- 4. Select new current cup
  self.current = self.cups[self.current]
end

function Game:labels()
  -- Return the cup labels (after 1) as a single string
  
  -- 1. Start with cups: and the current value
  local result = ''
  if self.current == 0 then
    return result
  end
  
  -- 2. Loop for all of the numbers
  local nxt = self.cups[1]
  while nxt ~= 1 do
    
    -- 3. Add the number to the result
    result = result .. string.format('%d', nxt)
    
    -- 4. Advance to the next cup
    nxt = self.cups[nxt]
  end
  
  -- 5. Return the cup labels
  return result
end
  
function Game:many_moves(number)
  -- Simulate many moves in the game
  
  -- 1. Loop for the moves
  for _ = 1, number do
    
    -- 2. Do a single move
    self:move()
  end
  
  -- 3. For part 2, Return 
  if self.part2 then
    return self:star_cups()
  end
  
  -- 4. For part 1, Return the labels on the cups
  return self:labels()
end

function Game:star_cups()
  -- Return product of labels on star cups
  
  -- 1. Start with nothing
  local values = {}
  local where = 1
  
  -- 2. Loop twice
  for _ = 1, 2 do
    table.insert(values, self.cups[where])
    where = self.cups[where]
  end
  
  -- 3. Return the product
  return values[1] * values[2]
end

function Game:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:many_moves(100)
end


function Game:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:many_moves(10000000)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Game

-- ======================================================================
-- end                         g a m e . l u a                        end
-- ======================================================================
