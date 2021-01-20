-- ======================================================================
-- Rambunctious Recitation
--   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         g a m e . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 15 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local memory = require('memory')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Game = { part2 = false, text = {}, memory = nil }

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                   Game
-- ======================================================================

-- Object for Rambunctious Recitation

function Game:Game (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.memory = memory:Memory({part2=o.part2})
  
  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Set memory from text (if there is any)
  if o.text ~= nil and #o.text > 0 then
    o.memory = memory:Memory({part2=o.part2, text=o.text[1]})
  end

  return o
end

function Game:number_spoken(turn)
  -- Return the nth number spoken
  assert(turn>self.memory.turn)
  
  -- 1. Loop until we get to the specified turn
  while self.memory.turn < turn - 1 do
    self.memory:add_last_spoken()
  end
  
  -- 2. Return the number spoken on that turn
  return self.memory.age
end

  

function Game:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:number_spoken(2020)
end


function Game:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part two
  return self:number_spoken(30000000)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Game

-- ======================================================================
-- end                         g a m e . l u a                        end
-- ======================================================================
