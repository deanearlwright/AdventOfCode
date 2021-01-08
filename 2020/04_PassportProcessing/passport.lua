-- ======================================================================
-- Passport Processing
--   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         p a s s p o r t . l u a
-- ======================================================================
-- "Passport for the Advent of Code 2020 Day 04 puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Passport = { part2=false, text='', fields = {}, num_fields = 0 }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
local FV_MATCH = "[a-z0-9]+:[#0-9a-z]+"
local FV_CAPTURE = "([a-z0-9]+):([#0-9a-z]+)"
local REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

local FIELD_TESTS = {}
FIELD_TESTS["byr"] = {match="%d%d%d%d", low=1920, high=2002}
FIELD_TESTS["iyr"] = {match="%d%d%d%d", low=2010, high=2020}
FIELD_TESTS["eyr"] = {match="%d%d%d%d", low=2020, high=2030}
FIELD_TESTS["hgt"] = {match="%d+in|%d+cm", cml=150, cmh=193, inl=59, inh=76}
FIELD_TESTS["hcl"] = {match="#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]"}
FIELD_TESTS["ecl"] = {match="amb|blu|brn|gry|grn|hzl|oth"}
FIELD_TESTS["pid"] = {match="[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",
                        low=0, high=999999999}

-- byr (Birth Year) - four digits; at least 1920 and at most 2002.
-- iyr (Issue Year) - four digits; at least 2010 and at most 2020.
-- eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
-- hgt (Height) - a number followed by either cm or in:
--   If cm, the number must be at least 150 and at most 193.
--   If in, the number must be at least 59 and at most 76.
-- hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
-- ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
-- pid (Passport ID) - a nine-digit number, including leading zeroes.

-- ======================================================================
--                                                               Passport
-- ======================================================================


function Passport:Passport (o)
  -- "Object for Passport Processing"


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.fields = o.fields or {}
  o.num_fields = o.num_fields or 0

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Passport:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Start with nothing
  self.fields = {}
  self.num_fields = 0
  
  -- 2. Loop for the field value pairs
  for pair in text:gmatch(FV_MATCH) do
    local field, value = pair:match(FV_CAPTURE)
    self.fields[field] = value
    self.num_fields = self.num_fields + 1
  end  

end

function Passport:is_valid()
  -- Returns true if the passport is valid
  
  -- 1. Loop for all of the required fields
  for _, field in ipairs(REQUIRED_FIELDS) do
    
    -- 2. If the field is missing the passport is invalid
    if nil == self.fields[field] then
      return false
    end
    
    -- 3. For part two, we check the field values
    if self.part2 then
      if self:is_field_valid(field) == false then
        return false
      end
    end
    
  end
      
  -- 4. All fields are there (and for part2 look good)
  return true
end

function Passport:is_field_valid(field)
  -- Returns true if the field is valid data
  
  -- 1. Return false if the field is not in the passport
  local value = self.fields[field]
  if value == nil then
    return false
  end
  
  -- 2. Get the detailed requirements
  local tests = FIELD_TESTS[field]
  if tests == nil or tests.match == nil then
    return false
  end
  
  -- 3. Must match one of the patterns
  local is_match = false
  for pattern in tests.match:gmatch("[^|]+") do
    local matched = value:match(pattern)
    if nil ~= matched and #matched == #value then
      is_match = true
    end
  end
    if is_match == false then
    return false
  end
  
  -- 4. If there is a high and low value, check the number
  if nil ~= tests.low then
    local number = tonumber(value)
    if number < tests.low or number > tests.high then
      return false
    end
  end
    
  -- 5. If there is a high and low in/cm value, check the number
  if nil ~= tests.inl then
    local number = tonumber(value:match("%d+"))
    if nil == value:match("cm") then
      if number < tests.inl or number > tests.inh then
        return false
      end
    else if number < tests.cml or number > tests.cmh then
        return false
      end  
    end 
  end
  
  -- 6. The value looks good for this field
  return true
end

  
    
  
  

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Passport

-- ======================================================================
-- end                     p a s s p o r t . l u a                    end
-- ======================================================================
