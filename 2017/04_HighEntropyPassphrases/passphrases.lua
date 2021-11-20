-- ======================================================================
-- HighEntropyPassphrases
--   Advent of Code 2017 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p a s s p h r a s e s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2017 Day 04 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Passphrases = { part2 = false, text = {}, words = {} }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                            Passphrases
-- ======================================================================

-- Object for HighEntropyPassphrases

function Passphrases:Passphrases(o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.words = {}
  
  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)
  return o
end

function Passphrases:add_words(phrase)
  -- Break the passphrase into individual words, returns false if not unique
  
  -- 1. Start with nothing
  self.words = {}
  
  -- 2. Loop for the words in the phrase
  for word in phrase:gmatch("%a+") do
    
    -- 3. For part 2, sort the letters
    if self.part2 then
      word = self:sort_letters(word)
    end  
      
    -- 4. Check if word already exists, return false if it does
    if self:has_word(word) then
      return false
    end
    
    -- 5. Add the word to the collection
    table.insert(self.words, word)
  end
  
  -- 6. All words unique, return true
  return true
end

function Passphrases:sort_letters(word)
  -- Sort the letters in a word
  
  -- 1. Start with nothing
  local letters = {}
  
  -- 2. Loop for all of the letters in the word
  for letter in word:gmatch("%a") do
    table.insert(letters, letter)
  end
  
  -- 3. Sort the letters
  table.sort(letters)
  
  -- 4. Return the letters back into a word
  return table.concat(letters)
  
end

function Passphrases:has_word(word)
  -- Return true if word already exists
  
  -- 1. Loop for all of the words
  for indx = 1, #self.words do
    
    -- 2. Is the word here? Yes, return true
    if self.words[indx] == word then
      return true
    end
  end
  
  -- 3. Never found the word, return False
  return false
end

function Passphrases:count_valid()
  -- Count the number of valid passphrases
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the passphrases
  for indx = 1, #self.text do
    local phrase = self.text[indx]
    
    -- 3. Add the words to words
    if self:add_words(phrase) then
      
      -- 4. Increment count of valid phrases
      result = result + 1
    end
  end
  
  -- 5. Return the count of valid phrases
  return result
end

function Passphrases:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_valid()
end


function Passphrases:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:count_valid()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Passphrases

-- ======================================================================
-- end                  p a s s p h r a s e s . l u a                 end
-- ======================================================================
