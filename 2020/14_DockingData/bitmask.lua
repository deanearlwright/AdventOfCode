-- ======================================================================
-- Docking Data
--   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         b i t m a s k . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 14 puzzle

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local DEFAULT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
local MATCH_MASK = 'mask = ([01X]+)'
local MATCH_MEM = 'mem%[([0-9]+)%] = ([0-9]+)'
local OCT2BIN = {
    ['0'] = '000',
    ['1'] = '001',
    ['2'] = '010',
    ['3'] = '011',
    ['4'] = '100',
    ['5'] = '101',
    ['6'] = '110',
    ['7'] = '111'
}
-- ----------------------------------------------------------------------
--                                                                utility
-- ----------------------------------------------------------------------
local function getOct2bin(a) return OCT2BIN[a] end
local function convertBin36(n)
    local s = string.format('%012o', n)
    s = s:gsub('.', getOct2bin)
    return s
end
-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Bitmask = { part2 = false, text = {}, 
                  bitmask = DEFAULT_MASK, memory = {} }

-- ======================================================================
--                                                                Bitmask
-- ======================================================================

-- Object for Docking Data

function Bitmask:Bitmask (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.bitmask = DEFAULT_MASK
  o.memory = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

   return o
end

function Bitmask:execute()
  -- Run the initialization code

  -- 1. Loop for all instructions in the initialization code
  for _, line in ipairs(self.text) do

    -- 2. Execute a mask or mem instruction as indicated
    if line:sub(1,4) == 'mask' then
      self:save_mask(line)
    elseif self.part2 then
      self:save_masked_memory(line)
    else
      self:save_masked_value(line)
    end
  end
  
  -- 3. Return the sum of all of the memory locations
  local result = 0
  for _, value in pairs(self.memory) do
    result = result + value
  end
  return result
end
    
function Bitmask:save_mask(line)
  -- Save a new mask value

  -- 1. Parse the 'mask' line
  local mask = string.match(line, MATCH_MASK)
  assert(#mask == 36)

  -- 2. Save the mask
  self.bitmask = mask
end

function Bitmask:save_masked_value(line)
  -- Save a masked value at a sigle place in memory

  -- 1. Parse the 'mem' line
  local loc, value = string.match(line, MATCH_MEM)
  loc = tonumber(loc)
  value = tonumber(value)

  -- 2. Get the masked value
  local masked = self:apply_mask_to_value(value)

  -- 3. Save it to the specified location
  self.memory[loc] = masked
end

function Bitmask:apply_mask_to_value(value)
  -- Return the value with the mask applied

  -- 1. Get the value as 36 character bits
  local value36 = convertBin36(value)
  assert(#value36 == 36)
  assert(#self.bitmask == 36)

  -- 2. Apply the mask
  local bits = {}
  for indx = 1, 36 do
    local mask = self.bitmask:sub(indx, indx)
    local value = value36:sub(indx, indx)
    if mask == 'X' then
      table.insert(bits, value)
    else
      table.insert(bits, mask)
    end
  end
  assert(#bits == 36)
  
  -- Return the masked value as an integer
  local xbits = table.concat(bits, '')
  assert(#xbits == 36)
  return tonumber(xbits, 2)
end

function Bitmask:save_masked_memory(line)
  -- Save a value at multiple masked memory location
  
  -- 1. Parse the 'mem' line
  local loc, value = string.match(line, MATCH_MEM)
  loc = tonumber(loc)
  value = tonumber(value)
  
  -- 2. Get the masked memory location
  local masked_loc = self:apply_mask_to_location(loc)
  
  -- 3. Save value at the masked location
  self:save_multi_loc(masked_loc, value)
end

function Bitmask:apply_mask_to_location(location)
  -- Return the location with the mask applied
  -- print("apply_mask_to_location(", location, ")")

  -- 1. Get the location as 36 character bits
  local loc36 = convertBin36(location)
  assert(#loc36 == 36)
  assert(#self.bitmask == 36)
  -- print("loc36=", loc36)
  -- print("mask =", self.bitmask)
  
  -- 2. Apply the mask
  local bits = {}
  for indx = 1, 36 do
    local mask = self.bitmask:sub(indx, indx)
    local loc = loc36:sub(indx, indx)
    if mask == 'X' or mask == '1' then
      table.insert(bits, mask)
    else
      table.insert(bits, loc)
    end
  end
  assert(#bits == 36)
  
  -- Return the masked location as an integer
  local xbits = table.concat(bits, '')
  -- print("xbits=", xbits)
  assert(#xbits == 36)
  return xbits
end
  
function Bitmask:save_multi_loc(mask, value)
  -- Save the value to multiple locations
  -- print("save_multi_loc(", mask, ',', value, ')')

  -- 1. Locate the first floating bit in the masked location
  local first_x, _ = mask:find('X')

  -- 2. If there aren't any, save the value at the location
  if first_x == nil then
    local loc = tonumber(mask, 2)
    -- print(mask, '(', loc, ') = ', value)
    self.memory[loc] = value
    return
  end

  -- 3. Replace the floating bit with a 0 and with a 1
  local mask_0 = mask:sub(1, first_x - 1) .. '0' .. mask:sub(first_x + 1)
  local mask_1 = mask:sub(1, first_x - 1) .. '1' .. mask:sub(first_x + 1)
  assert(#mask_0 == 36)
  assert(#mask_1 == 36)
  
  -- 4. Save the value at those two locations (which may also expand further)
  self:save_multi_loc(mask_0, value)
  self:save_multi_loc(mask_1, value)
end
  

function Bitmask:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:execute()
end


function Bitmask:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:execute()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Bitmask

-- ======================================================================
-- end                      b i t m a s k . l u a                     end
-- ======================================================================
