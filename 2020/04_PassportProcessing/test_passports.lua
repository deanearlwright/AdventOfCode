-- ======================================================================
-- Passport Processing
--   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p a s s p o r t s . l u a
-- ======================================================================
-- "Test solver for Advent of Code 2020 day 04, Passport Processing"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local passports = require('passports')
-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------
local SAVE_BLANK_LINES = true

function from_text(text)
  -- "Break the text into trimed, non-comment lines"

  -- 1. We start with no lines
  local result = {}
  
  -- 2. Set up to save blank lines (if desired)
  text = text:gsub('[\r]', '')
  if SAVE_BLANK_LINES then
    text = text:gsub('\n\n', '\n \n')
  end  
  
  -- 3. Loop for lines in the text
  for line in text:gmatch('[^\n]+') do
    line = line:gsub("%s*$", "")
  
    -- 4. Ignore comment lines
    if #line > 0 and "!" == line:sub(1, 1) then
      -- Ignore
    else -- not a comment line
      if #line > 0 or SAVE_BLANK_LINES then
        table.insert(result, line)
      end  
    end
  end
  
  -- 5. Return a table of cleaned text lines
  return result
end
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = [[
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
]]

local EXAMPLE_TWO = [[
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
]]


local PART_ONE_TEXT = EXAMPLE_TEXT
local PART_TWO_TEXT = EXAMPLE_TWO

local PART_ONE_RESULT = 2
local PART_TWO_RESULT = 4

-- ======================================================================
--                                                          TestPassports
-- ======================================================================


function test_empty_init()
  -- "Test the default Passports creation"

  -- 1. Create default Passports object
  local myobj = passports:Passports()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.passports, 0)

end

function test_text_init()
  -- "Test the Passports object creation from text"

  -- 1. Create Passports object from text
  local myobj = passports:Passports({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 13)
  luaunit.assertEquals(#myobj.passports, 4)
  
  -- 3. Check methods
  luaunit.assertEquals(myobj:count_valid(), 2)

end

function test_part_one()
  -- "Test part one example of Passports object"

  -- 1. Create Passports object from text
  local myobj = passports:Passports({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- "Test part two example of Passports object"

  -- 1. Create Passports object from text
  local myobj = passports:Passports({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end               t e s t _ p a s s p o r t s . l u a              end
-- ======================================================================
