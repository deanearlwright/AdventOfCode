-- ======================================================================
-- Monster Messages
--   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ r u l e s . l u a
-- ======================================================================
-- Test solver for Advent of Code 2020 day 19, Monster Messages

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local rules = require('rules')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- Break the text into trimed, non-comment lines

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch('[^\r\n]+') do

    -- 3. But ignore blank and comment lines
    line = line:gsub("%s*$", "")
    if #line > 0 and "!" ~= line:sub(1, 1) then

      -- 4. Add the line
      table.insert(result, line)
    end
  end

  -- 5. Return a table of cleaned lines
  return result
end

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = [[
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
]]
EXAMPLE_TWO = [[
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
]]
local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO

local PART_ONE_RESULT = 2
local PART_TWO_RESULT = 12

-- ======================================================================
--                                                              TestRules
-- ======================================================================


function test_empty_init()
  -- Test the default Rules creation

  -- 1. Create default Rules object
  local myobj = rules:Rules()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.rules, 0)
  luaunit.assertEquals(#myobj.messages, 0)

end

function test_text_init()
  -- Test the Rules object creation from text

  -- 1. Create Rules object from text
  local myobj = rules:Rules({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.rules["2"].definition, "4 4 | 5 5")
  luaunit.assertEquals(#myobj.messages, 5)
  luaunit.assertEquals(myobj.messages[2], "bababa")
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:count_rule0(), 2)

end

function test_try_rules()
  -- Test the Rules try_rules() method

  -- 1. Create Rules object from text
  local myobj = rules:Rules({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.rules["2"].definition, "4 4 | 5 5")
  luaunit.assertEquals(#myobj.messages, 5)
  luaunit.assertEquals(myobj.messages[2], "bababa")

  -- 3. Check try_rules() method
  luaunit.assertEquals(myobj:try_rules('', 'a'), {'a'})
  luaunit.assertEquals(myobj:try_rules('4', 'a'), {''})
  luaunit.assertEquals(myobj:try_rules('4', 'b'), {})
  luaunit.assertEquals(myobj:try_rules('4 4', 'aa'), {''})
  luaunit.assertEquals(myobj:try_rules('4 4', 'aaa'), {'a'})
  luaunit.assertEquals(myobj:try_rules('4 4', 'aab'), {'b'})
  luaunit.assertEquals(myobj:try_rules('4 4', 'abb'), {})
  luaunit.assertEquals(myobj:try_rules('5', 'a'), {})
  luaunit.assertEquals(myobj:try_rules('5', 'b'), {''})
  luaunit.assertEquals(myobj:try_rules('2', 'a'), {})
  luaunit.assertEquals(myobj:try_rules('2', 'aa'), {''})
  luaunit.assertEquals(myobj:try_rules('2', 'bbb'), {'b'})
  luaunit.assertEquals(myobj:try_rules('2', 'ab'), {})
  luaunit.assertEquals(myobj:try_rules('3', 'bb'), {})
  luaunit.assertEquals(myobj:try_rules('3', 'ab'), {''})
  luaunit.assertEquals(myobj:try_rules('1', 'a'), {})
  luaunit.assertEquals(myobj:try_rules('1', 'aa'), {})
  luaunit.assertEquals(myobj:try_rules('1', 'ab'), {})
  luaunit.assertEquals(myobj:try_rules('1', 'aaaa'), {})
  luaunit.assertEquals(myobj:try_rules('1', 'aaab'), {''})
  luaunit.assertEquals(myobj:try_rules('1', 'bbaba'), {'a'})
  luaunit.assertEquals(myobj:try_rules('1', 'abbb'), {''})
  luaunit.assertEquals(myobj:try_rules('2 3', 'a'), {})
  luaunit.assertEquals(myobj:try_rules('2 3', 'aa'), {})
  luaunit.assertEquals(myobj:try_rules('2 3', 'bb'), {})
  luaunit.assertEquals(myobj:try_rules('2 3', 'ab'), {})
  luaunit.assertEquals(myobj:try_rules('2 3', 'aaaa'), {})
  luaunit.assertEquals(myobj:try_rules('2 3', 'aaab'), {''})
  luaunit.assertEquals(myobj:try_rules('2 3', 'bbaba'), {'a'})
  luaunit.assertEquals(myobj:try_rules('2 3', 'abbb'), {})
  luaunit.assertEquals(myobj:try_rules('3 2', 'abbb'), {''})
  luaunit.assertEquals(myobj:try_rules('3 2', 'abaaa'), {'a'})
  luaunit.assertEquals(myobj:try_rules('0', 'ab'), {})
  luaunit.assertEquals(myobj:try_rules('0', 'aaaa'), {})
  luaunit.assertEquals(myobj:try_rules('0', 'abbb'), {})
  luaunit.assertEquals(myobj:try_rules('0', 'ababbb'), {''})
  luaunit.assertEquals(myobj:try_rules('0', 'abbbab'), {''})
  luaunit.assertEquals(myobj:try_rules('0', 'bababa'), {})
  luaunit.assertEquals(myobj:try_rules('0', 'aaabbb'), {})
  luaunit.assertEquals(myobj:try_rules('0', 'aaaabbb'), {'b'})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'abbb'), {})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'ababbb'), {''})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'abbbab'), {''})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'bababa'), {})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'aaabbb'), {})
  luaunit.assertEquals(myobj:try_rules('4 1 5', 'aaaabbb'), {'b'})
end

function test_try_rule()
  -- Test the Rules try_rule() method

  -- 1. Create Rules object from text
  local myobj = rules:Rules({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.rules["2"].definition, "4 4 | 5 5")
  luaunit.assertEquals(#myobj.messages, 5)
  luaunit.assertEquals(myobj.messages[2], "bababa")

  -- 3. Check try_rule() method
  luaunit.assertEquals(myobj:try_rule('0', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('2', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('3', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('4', 'a'), {''})
  luaunit.assertEquals(myobj:try_rule('5', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('5', 'b'), {''})
  luaunit.assertEquals(myobj:try_rule('2', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('2', 'aa'), {''})
  luaunit.assertEquals(myobj:try_rule('2', 'ab'), {})
  luaunit.assertEquals(myobj:try_rule('2', 'bb'), {''})
  luaunit.assertEquals(myobj:try_rule('2', 'aaaabb'), {'aabb'})
  luaunit.assertEquals(myobj:try_rule('3', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('3', 'aa'), {})
  luaunit.assertEquals(myobj:try_rule('3', 'ab'), {''})
  luaunit.assertEquals(myobj:try_rule('3', 'bb'), {})
  luaunit.assertEquals(myobj:try_rule('3', 'aaaabb'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'a'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'aa'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'ab'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'bb'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'aaaa'), {})
  luaunit.assertEquals(myobj:try_rule('1', 'aaab'), {''})
  luaunit.assertEquals(myobj:try_rule('1', 'abaa'), {''})
  luaunit.assertEquals(myobj:try_rule('1', 'aaaabb'), {})
  luaunit.assertEquals(myobj:try_rule('0', ''), {})
  luaunit.assertEquals(myobj:try_rule('0', 'ababbb'), {''})
  luaunit.assertEquals(myobj:try_rule('0', 'abbbab'), {''})
  luaunit.assertEquals(myobj:try_rule('0', 'bababa'), {})
  luaunit.assertEquals(myobj:try_rule('0', 'aaabbb'), {})
  luaunit.assertEquals(myobj:try_rule('0', 'aaaabbb'), {'b'})
end

function test_match_rule()
  -- Test the Rules match_rule() method

  -- 1. Create Rules object from text
  local myobj = rules:Rules({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 11)
  luaunit.assertEquals(myobj.rules["2"].definition, "4 4 | 5 5")
  luaunit.assertEquals(#myobj.messages, 5)
  luaunit.assertEquals(myobj.messages[2], "bababa")

  -- 3. Check match_rule() method
  luaunit.assertEquals(myobj:match_rule('0', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('2', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('3', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('4', 'a'), true)
  luaunit.assertEquals(myobj:match_rule('5', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('5', 'b'), true)
  luaunit.assertEquals(myobj:match_rule('2', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('2', 'aa'), true)
  luaunit.assertEquals(myobj:match_rule('2', 'ab'), false)
  luaunit.assertEquals(myobj:match_rule('2', 'bb'), true)
  luaunit.assertEquals(myobj:match_rule('2', 'aaaabb'), false)
  luaunit.assertEquals(myobj:match_rule('3', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('3', 'aa'), false)
  luaunit.assertEquals(myobj:match_rule('3', 'ab'), true)
  luaunit.assertEquals(myobj:match_rule('3', 'bb'), false)
  luaunit.assertEquals(myobj:match_rule('3', 'aaaabb'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'a'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'aa'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'ab'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'bb'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'aaaa'), false)
  luaunit.assertEquals(myobj:match_rule('1', 'aaab'), true)
  luaunit.assertEquals(myobj:match_rule('1', 'abaa'), true)
  luaunit.assertEquals(myobj:match_rule('1', 'aaaabb'), false)
  luaunit.assertEquals(myobj:match_rule('0', ''), false)
  luaunit.assertEquals(myobj:match_rule('0', 'ababbb'), true)
  luaunit.assertEquals(myobj:match_rule('0', 'abbbab'), true)
  luaunit.assertEquals(myobj:match_rule('0', 'bababa'), false)
  luaunit.assertEquals(myobj:match_rule('0', 'aaabbb'), false)
  luaunit.assertEquals(myobj:match_rule('0', 'aaaabbb'), false)
end

function test_part_one()
  -- Test part one example of Rules object

  -- 1. Create Rules object from text
  local myobj = rules:Rules({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- Test part two example of Rules object

  -- 1. Create Rules object from text
  local myobj = rules:Rules({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ r u l e s . l u a                end
-- ======================================================================
