-- ======================================================================
-- Crab Combat
--   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p l a y e r . l u a
-- ======================================================================
-- Player for the Advent of Code 2020 Day 22 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Player = { part2=false, number=0, cards={} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Player
-- ======================================================================


function Player:Player(o)
  -- Object for Crab Combat

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.number = o.number or 0
  o.cards = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)
  return o
end

function Player:add_card(value)
  -- Add a card to the player

  -- 1. Add the card
  table.insert(self.cards, value)
end

function Player:add_cards(values)
  -- Add multiple cards to the player
  
  -- 1. Loop for all of the card values
  for _, value in ipairs(values) do
    
    -- 2. Add the card
    self:add_card(value)
  end
end


function Player:get_top_card()
  -- Return the top card from the player's deck
  
  -- 0. Precondition axioms
  assert(#self.cards > 0)
  
  -- 1. Take and return the top card
  return table.remove(self.cards, 1)
end

function Player:is_deck_empty()
  -- Return true if the player's deck is empty
  
  -- 1. Return true if the player has no cards
  return #self.cards == 0
end

function Player:has_at_least(number)
  -- Returns true if the player has at least the specified number of cards
  return #self.cards >= number
end


function Player:keep(winner, loser)
  -- Keep the winning card (and the losing one as well)
  
  -- 0. Precondition axioms
  assert(self.part2 or winner > loser)
  
  -- 1. Add the cards to the bottom of the desk
  self:add_card(winner)
  self:add_card(loser)
end

function Player:score()
  -- Score the cards in the player's deck
  
  -- 1. Start with nothing
  local result = 0
  local multiplier = #self.cards
  
  -- 2. Loop for all of the cards in the deck
  for _, value in ipairs(self.cards) do
    
    -- 3. Add in the score for this card
    result = result + value * multiplier
    
    -- 4. The next card is worth less
    multiplier = multiplier - 1
  end
  
  -- 5. Return the score
  return result
end

function Player:__tostring()
  -- Represent the player as a string
  return tostring(self.number) .. ': ' .. table.concat(self.cards, ', ')
end

function Player:clone(value)
  -- Make a copy of the player with the specified number of cards
  
  -- 1. Make a basic close
  local other = Player:Player({part2=self.part2, number=self.number})
  
  -- 2. Copy the cards
  for indx = 1, value do
    other:add_card(self.cards[indx])
  end
  
  -- 3. Return the clone
  return other
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Player

-- ======================================================================
-- end                       p l a y e r . l u a                      end
-- ======================================================================
