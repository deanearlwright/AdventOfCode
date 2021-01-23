-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         t i c k e t s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 16 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local rules = require('rules')
local ticket = require('ticket')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Tickets = { part2 = false, text = {}, 
                  rules = nil, mine = nil, nearby = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                Tickets
-- ======================================================================

-- Object for Ticket Translation

function Tickets:Tickets (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rules = nil
  o.mine = nil
  o.nearby = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Tickets:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Start with the rules
  self.rules = rules:Rules({part2=self.part2, text=text})
  
  -- 2. Process the tickets
  local section = '???'
  for _, line in ipairs(text) do

    -- 3. Get the type of the input line
    local ltype = line:sub(1,3)
    
    -- 4. Process the line based on the line type
    if ltype == 'you' or ltype == 'nea' then
      section = ltype
    elseif section == 'you' then
      self.mine = ticket:Ticket({part2=self.part2, text=line})
    elseif section == 'nea' then
      table.insert(self.nearby, ticket:Ticket({part2=self.part2, text=line}))
    end
  end
end

function Tickets:scanning_error_rate()
  -- Return the ticket scanning error rate (sum of invalid values)
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the nearby tickets
  for _, tik in ipairs(self.nearby) do
    
    -- 3. Loop for all of the numbers on the ticket
    for _, number in ipairs(tik.numbers) do
      
      -- 4. If this number is not valid add it to the result and mark ticket invalid
      if not self.rules:is_valid(number) then
        result = result + number
        tik.valid = false
      end
    end
  end
  
  -- 5. Return the sum of the invalid numbers 
  return result
end

function Tickets:departure_fields()
  -- Return the product of the departure fields
  
  -- 1. Mark invalid tickets as such
  self:scanning_error_rate()
  
  -- 2. Find the field positions
  self:find_field_positions()
  
  -- 3. Determine the product of the departure fields
  local result = 1
  for _, rul in ipairs(self.rules.rules) do
    if rul.name:sub(1,9) == 'departure' then
      if #rul.positions ~= 1 then
        print('Unable to determine field for', rul.name)
      else
        result = result * self.mine.numbers[rul.positions[1]]
      end
    end
  end
  
  -- 4. Return that product
  return result
end

function Tickets:find_field_positions()
  -- Find the position for each field
  
  -- 1. Loop for each position on the ticket
  for position = 1, #self.mine.numbers do
    
    -- 2. Get the numbers for that position from the nearby valid tickets
    local numbers = {}
    for _, tik in ipairs(self.nearby) do
      if tik.valid then
        table.insert(numbers, tik.numbers[position])
      end
    end
    -- 3. Determine the fields for those numbers
    self.rules:determine_fields(position, numbers)
  end
  
  -- 4. Resolve conflicts in field assignment
  self.rules:resolve_fields()
end

    
function Tickets:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:scanning_error_rate()
end


function Tickets:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:departure_fields()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Tickets

-- ======================================================================
-- end                      t i c k e t s . l u a                     end
-- ======================================================================
