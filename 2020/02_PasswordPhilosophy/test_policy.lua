-- ======================================================================
-- Password Philosophy
--   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p o l i c y . l u a
-- ======================================================================
-- "Test Policy for Advent of Code 2020 day 02, Password Philosophy"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

policy = require('policy')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
EXAMPLE_TEXT = "1-3 a: abcde"

EXAMPLES = {
  {text = "1-3 a: abcde", one = true, two = true},
  {text = "1-3 b: cdefg", one = false, two = false},
  {text = "2-9 c: ccccccccc", one = true, two = false}
  }

-- ======================================================================
--                                                             TestPolicy
-- ======================================================================

function test_empty_init()
  -- "Test the default Policy creation"

  -- 1. Create default Policy object
  local myobj = policy:Policy()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.low, 0)
  luaunit.assertEquals(myobj.high, 0)
  luaunit.assertEquals(myobj.letter, '?')
  luaunit.assertEquals(myobj.password, '?')
end

function test_text_init()
  -- Test the Policy object creation from text

  -- 1. Create Passwords object from text
  local myobj = policy:Policy({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(myobj.text, EXAMPLE_TEXT)
  
  -- 3. Check the password
  luaunit.assertEquals(myobj:check_password(), true)
end

function test_part_one()
  -- Test the examples from part one
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create the policy
    local myobj = policy:Policy({text=example['text']})
    
    -- 3. Check the password
    luaunit.assertEquals(myobj:check_password(), example['one'])
  end
end  
    
function test_part_two()
  -- Test the examples from part two
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES) do
    
    -- 2. Create the policy
    local myobj = policy:Policy({part2=true, text=example['text']})
  luaunit.assertEquals(myobj.part2, true)
    
    -- 3. Check the password
    luaunit.assertEquals(myobj:check_password(), example['two'])
  end
end  

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                   t e s t _ p o l i c y . p y                  end
-- ======================================================================
