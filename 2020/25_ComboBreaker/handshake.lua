-- ======================================================================
-- Combo Breaker
--   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         h a n d s h a k e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 25 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Handshake = { part2 = false, text = {}, 
    card_public = nil, door_public = nil, card_private = nil, door_private = nil }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local INITIAL_SUBJECT_NUMBER = 7
local DIVISOR = 20201227
local HARD_LIMIT = 999999999

-- ======================================================================
--                                                              Handshake
-- ======================================================================

-- Object for Combo Breaker

function Handshake:Handshake (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.numbers = {}
  o.card_public = nil
  o.door_public = nil
  o.card_private = nil
  o.door_private = nil

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
    assert(#o.text == 2)
    o.card_public = tonumber(o.text[1])
    o.door_public = tonumber(o.text[2])
  end

  return o
end

function Handshake:transform_number(number, private)
  -- Transform the number using the private key (loop size)
  
  -- 0. Precondition axioms
  assert(number > 0)
  assert(private > 0)

  -- 1. Always start with 1
  local value = 1

  -- 2. Loop private key times
  for _ = 1, private do

    -- 3. Set the value to itself multiplied by the subject number
    value = value * number

    -- 4. Set the value to the remainder after dividing the value by 20201227
    value = value % DIVISOR
  end
  
  -- 5. Return the transformed number
  return value
end

function Handshake:guess_private(public)
  -- Determine the private key from the public key

  -- 1. Impose a hard_limit
  local hard_limit = HARD_LIMIT

  -- 2. Start with the initial subject number
  local value = 1

  -- 3. Try various loop sizes
  for loop_size = 1, hard_limit do

    -- 4. Transform the current value
    value = value * INITIAL_SUBJECT_NUMBER
    value = value % DIVISOR

    -- 5. If we were able to generate the public key, loop_size is the private key
    if value == public then
      return loop_size
    end
  end
  
  -- 6. Hard failure
  return 0
end

function Handshake:guess_encryption_key()
  -- Determine the encryption key is the handshake trying to establish
  print(string.format("The card's public key is %d", self.card_public))
  print(string.format("The door's public key is %d", self.door_public))

  -- 1. Determine the card's private key
  self.card_private = self:guess_private(self.card_public)
  print(string.format("The card's private key is %d", self.card_private))

  -- 2. Determine the door's private key
  self.door_private = self:guess_private(self.door_public)
  print(string.format("The door's private key is %d", self.door_private))

  -- 3. Have the card generate the encryption key
  local card_encryption = self:transform_number(self.door_public, self.card_private)
  print(string.format("The card's encryption key is %d", card_encryption))

  -- 4. Have the door generate the encryption key
  local door_encryption = self:transform_number(self.card_public, self.door_private)
  print(string.format("The door's encryption key is %d", door_encryption))

  -- 5. The encription keys should be the same
  if card_encryption ~= door_encryption then
    return nil
  end
  
  -- 6. Return the shared encryption key
  return card_encryption
end

function Handshake:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:guess_encryption_key()
end


function Handshake:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return nil
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Handshake

-- ======================================================================
-- end                   h a n d s h a k e . l u a                    end
-- ======================================================================
