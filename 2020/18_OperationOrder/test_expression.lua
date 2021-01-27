-- ======================================================================
-- Operation Order
--   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ e x p r e s s i o n . l u a
-- ======================================================================
-- Test Expression for Advent of Code 2020 day 18, Operation Order

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local expression = require('expression')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "123"

local EXAMPLES = {
   {text = '1', tokens = 1, part1 = 1, part2 = 1},
   {text = '1 + 2', tokens = 3, part1 = 3, part2 = 3},
   {text = '2 * 3', tokens = 3, part1 = 6, part2 = 6},
   {text = '(2 * 3)', tokens = 5, part1 = 6, part2 = 6},
   {text = '1 + 2 * 3 + 4 * 5 + 6', tokens = 11, part1 = 71, part2 = 231},
   {text = '1 + (2 * 3) + (4 * (5 + 6))', tokens = 17, part1 = 51, part2 = 51},
   {text = '2 * 3 + (4 * 5)', tokens = 9, part1 = 26, part2 = 46},
   {text = '5 + (8 * 3 + 9 + 3 * 4 * 3)', tokens = 15, part1 = 437, part2 = 1445},
   {text = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', tokens = 23, part1 = 12240, part2 = 669060},
   {text = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', tokens = 27, part1 = 13632, part2 = 23340},
}
-- ======================================================================
--                                                         TestExpression
-- ======================================================================

function test_empty_init()
  -- Test the default Expression creation

  -- 1. Create default Expression object
  local myobj = expression:Expression()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.tokens, 0)

end

function test_text_init()
  -- Test the Expression object creation from text

  -- 1. Create Homework object from text
  local myobj = expression:Expression({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  luaunit.assertEquals(#myobj.tokens, 1)
  
  luaunit.assertEquals(myobj:get_operand({'123'}), {'123'}, {})
  luaunit.assertEquals(myobj:evaluate_tokens({'123'}), {"123"})
  luaunit.assertEquals(myobj:evaluate(), 123)

  luaunit.assertEquals(myobj:get_operand({'1', '+', '2'}), {'1'}, {'+', '2'})
  luaunit.assertEquals(myobj:evaluate_tokens({'1', '+', '2'}), {'3'})

end

function test_part_one()
  -- Test part one expressions
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create an expression object
    local myobj = expression:Expression({text=example.text})
    -- print("test_part_one", example.text, "tokens=", table.concat(myobj.tokens,','))

    -- 3. Make sure it has the expected values
    luaunit.assertEquals(myobj.part2, false)
    luaunit.assertEquals(myobj.text, example.text)
    luaunit.assertEquals(#myobj.tokens, example.tokens)
    
    -- 4. Evaluate the expression
    luaunit.assertEquals(myobj:evaluate(), example.part1)
    
  end
end

function test_part_two()
  -- Test part one expressions
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create an expression object
    local myobj = expression:Expression({part2=true, text=example.text})
    -- print("test_part_two", example.text, "tokens=", table.concat(myobj.tokens,','))

    -- 3. Make sure it has the expected values
    luaunit.assertEquals(myobj.part2, true)
    luaunit.assertEquals(myobj.text, example.text)
    luaunit.assertEquals(#myobj.tokens, example.tokens)
    
    -- 4. Evaluate the expression
    luaunit.assertEquals(myobj:evaluate(), example.part2)
    
  end
end
    
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end               t e s t _ e x p r e s s i o n . p y              end
-- ======================================================================
