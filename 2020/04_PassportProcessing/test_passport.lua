-- ======================================================================
-- Passport Processing
--   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ p a s s p o r t . l u a
-- ======================================================================
-- "Test Passport for Advent of Code 2020 day 04, Passport Processing"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local luaunit = require('luaunit')

local passport = require('passport')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local EXAMPLE_TEXT = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"

local EXAMPLES_ONE = { 
  {text = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", 
    one = true},
  {text = "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929", 
    one = false},
  {text = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", 
    one = true},
  {text = "hcl:#cfa07d eyr:2025 pid:166559648iyr:2011 ecl:brn hgt:59in",
    one = false}
}

local EXAMPLES_TWO = {
  { text = "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    two = false},
  { text = "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946", 
    two = false},
  { text = "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    two = false},
  { text = "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007", 
    two = false},
  { text = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
    two = true},
  { text = "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    two = true},
  { text = "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
    two = true},
  { text = "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    two = true}
}
-- ======================================================================
--                                                           TestPassport
-- ======================================================================

function test_empty_init()
  -- "Test the default Passport creation"

  -- 1. Create default Passport object
  local myobj = passport:Passport()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(myobj.num_fields, 0)

end

function test_text_init()
  -- "Test the Passport object creation from text"

  -- 1. Create Passports object from text
  local myobj = passport:Passport({text=EXAMPLE_TEXT})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, #EXAMPLE_TEXT)
  luaunit.assertEquals(myobj.num_fields, 8)
  
  -- 2. Check methods
  luaunit.assertEquals(myobj:is_valid(), true)
  
end

function test_examples_one()
  -- Test multiple passports
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES_ONE) do
    
    -- 2. Create a passport from the example text
    local myobj = passport:Passport({text=example['text']})
    
    -- 3. Check the passport
    luaunit.assertEquals(myobj:is_valid(), example['one'])
  end
end

function test_examples_two()
  -- Test multiple passports
  
  -- 1. Loop for all of the examples
  for _, example in ipairs(EXAMPLES_TWO) do
    
    -- 2. Create a passport from the example text
    local myobj = passport:Passport({part2=true, text=example['text']})
    
    -- 3. Check the passport
    luaunit.assertEquals(myobj:is_valid(), example['two'])
  end
end
    
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ p a s s p o r t . p y                end
-- ======================================================================
