-- ======================================================================
-- Crab Combat
--   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                          g a m e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 22 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local player = require('player')
local set = require('set')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Game = { part2 = false, text = {}, 
  players = {}, previous = set.Set({}) }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Game
-- ======================================================================

-- Object for Crab Combat

function Game:Game (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.players = {}
  o.previous = set:Set({})
  o.the_winner = 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Game:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Don't have a player yet
  local plyr = 0

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Is this a Player line, ...
    if nil ~= line:find("Player") then
      -- 3. Increment the player number and create the player
      plyr = plyr + 1
      table.insert(self.players, player:Player({part2=self.part2, number=plyr}))
    else
      -- 4. Otherwise add card to player
      self.players[plyr]:add_card(tonumber(line))
    end
  end
end

function Game:winner()
  -- Returns the winning player number (1 or 2) or 0 if there is no winner
  
  -- 0. Precondition axioms
  assert(#self.players == 2)
  
  -- 1. If there is a save winner, return it
  if self.the_winner > 0 then
    return self.the_winner
  end
  
  -- 2. If someone rules out of cards the other player is the winner
  if self.players[2]:is_deck_empty() then
    self.the_winner = 1
  elseif self.players[1]:is_deck_empty() then
    self.the_winner = 2
  end
  
  -- 3. Return the winner or no one (yet)
  return self.the_winner
end

function Game:one_round()
  -- Play one round of the game
  
  -- 0. Precondition axioms
  assert(#self.players == 2)
  
  -- 1. Get a card from each player
  local card1 = self.players[1]:get_top_card()
  local card2 = self.players[2]:get_top_card()
  
  -- 2. Determine who won the round and gets to keep the cards
  if card1 > card2 then
    self.players[1]:keep(card1, card2)
  else
    self.players[2]:keep(card2, card1)
  end
end

function Game:one_round_recursive()
  -- Play one round of the game of the recursive
  
  -- 0. Precondition axioms
  assert(#self.players == 2 and self.part2)
  
  -- 1. Infinite game pervention
  local hash = self:hash()
  if self.previous:has(hash) then
    self.the_winner = 1
    return
  end
  
  -- 2. Save the current position
  self.previous:add(hash)
  
  -- 3. Get a card from each player
  local card1 = self.players[1]:get_top_card()
  local card2 = self.players[2]:get_top_card()
  
  -- 4. Check if going down the recursive hole
  if self:is_recursive(card1, card2) then
    
    -- 5. Play out a recursive subgame
    if 1 == self:sub_game(card1, card2) then
      self.players[1]:keep(card1, card2)
    else
      self.players[2]:keep(card2, card1)
    end  
  else
    -- 6. Determine who won the round and gets to keep the cards using the normal rules
    if card1 > card2 then
      self.players[1]:keep(card1, card2)
    else
      self.players[2]:keep(card2, card1)
    end
  end
end

function Game:play()
  -- Play until there is a winner and return the winning score
  
  -- 1. Loop until there is a winner
  while self:winner() == 0 do
    
    -- 2. Play a round
    self:one_round()
  end
  
  -- 3. Return the winner's score
  return self.players[self.the_winner]:score()
end

function Game:play_recursive()
  -- Play until there is a winner in the recursive version and return the winning score
  
  -- 1. Loop until there is a winner
  while self:winner() == 0 do
    
    -- 2. Play a round
    self:one_round_recursive()
  end
  
  -- 3. Return the winner's score
  return self.players[self.the_winner]:score()
end

function Game:hash()
  -- Return a hash of the game
  
  -- 0. Precondition axioms
  assert(#self.players == 2 and self.part2)
  
  -- 1. Return the strings of the two players cards
  return tostring(self.players[1]) .. ';' .. tostring(self.players[2])
end

function Game:sub_game(card1, card2)
  -- Create a play a sub game, return the number of the winner
  
  -- 0. Precondition axioms
  assert(#self.players == 2 and self.part2 and self:is_recursive(card1, card2))
  
  -- 1. Create a new game
  local new_game = Game:Game({part2=true})
  
  -- 2. Copy the players but with limited cards  
  local player1 = self.players[1]:clone(card1)
  local player2 = self.players[2]:clone(card2)
  table.insert(new_game.players, player1)
  table.insert(new_game.players, player2)
   
  -- 3. Loop until there is a winner
  while new_game:winner() == 0 do
    
    -- 4. Play a round of the recursive game
    new_game:one_round_recursive()
  end
  
  -- 5. Return the winner of the subgame  
  return new_game.the_winner
end

function Game:is_recursive(card1, card2)
  -- Return true if a recursive sub-game should be played
  
  -- 0. Precondition axioms
  assert(#self.players == 2 and self.part2)
  
  -- Return true if both players have enough cards
  return self.players[1]:has_at_least(card1) and self.players[2]:has_at_least(card2)
end
  
function Game:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  if #self.players == 2 then
    return self:play()
  end
  return nil
end


function Game:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  if #self.players == 2 then
    return self:play_recursive()
  end
  return nil
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Game

-- ======================================================================
-- end                         g a m e . l u a                        end
-- ======================================================================
