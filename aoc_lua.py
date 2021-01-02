
# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ l u a . p y
# ======================================================================
"Generates lua base programming source files for Advent of Code"

AOC_DD_LUA = """-- ======================================================================
-- TITLE
--   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                           a o c _ D D . l u a
-- ======================================================================
-- "Solve the puzzles for Advent of Code YYYY day DD"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local argparse = require "argparse"

local MODULE = require "MODULE"

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ----------------------------------------------------------------------
--                                                      parse_commnd_line
-- ----------------------------------------------------------------------


function parse_command_line ()
  -- "Parse the command line options"

  -- 1. Create the command line parser
  local parser = argparse()
    :name "aoc_DD"
    :description "TITLE - Day DD of Advent of Code YYYY"
    :epilog "sample: lua aoc_DD.lua input.txt"
  parser:argument("filepath", "Location of puzzle input")
     :args(1)
  parser:flag("-v --verbose", "Print status messages to stdout")
  parser:option("-p --part", "Puzzle Part (1 or 2)", "1")
  parser:option("-l --limit", "Maximum limit (e.g., time, size, recursion) before stopping)", "0")

  -- 2. Get the options and arguments
  local args = parser:parse()

  -- 3. Validate arguments
  assert(args.part == "1" or args.part == "2")
  args.part = tonumber(args.part)
  args.limit = tonumber(args.limit)

  -- 4. Return the validated arguments
  return args
end

-- ----------------------------------------------------------------------
--                                                               part_one
-- ----------------------------------------------------------------------


function part_one(args, input_lines)
  -- "Process part one of the puzzle"

  -- 1. Create the puzzle solver
  local solver = MODULE:CLASS({part2=false, text=input_lines})

  -- 2. Determine the solution for part one
  local solution = solver:part_one(args)
  if solution == nil then
     print("There is no solution")
  else
     print("The solution for part one is " .. solution)
  end

    -- 3. Return result
    return solution ~= nil
end

-- ----------------------------------------------------------------------
--                                                               part_two
-- ----------------------------------------------------------------------


function part_two(args, input_lines)
    -- "Process part two of the puzzle"

    -- 1. Create the puzzle solver
    local solver = MODULE:CLASS({part2=true, text=input_lines})

    -- 2. Determine the solution for part two
    local solution = solver:part_two(args)
    if solution == nil then
        print("There is no solution")
    else
        print("The solution for part two is " .. solution)
    end

    -- 3. Return result
    return solution ~= nil
end

-- ----------------------------------------------------------------------
--                                                              from_file
-- ----------------------------------------------------------------------


function from_file(filepath)
  -- "Read the file"
  io.input(filepath)
  return from_text(io.read("*all"))
end

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- "Break the text into trimed, non-comment lines"

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch('[^\\r\\n]+') do

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
--                                                                   main
-- ----------------------------------------------------------------------


function main()
  -- "Read the Advent of Code problem and solve it"

  -- 1. Get the command line options
  local args = parse_command_line()

  -- 2. Read the puzzle file
  local input_text = from_file(args.filepath)

  -- 3. Process the appropiate part of the puzzle
  local result = nil
  if args.part == 1 then
    result = part_one(args, input_text)
  else
    result = part_two(args, input_text)
  end

  -- 5. Set return code (0 if solution found, 2 if not)
  if result then
    os.exit(0)
  end
  os.exit(2)
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
main()

-- ======================================================================
-- end                         a o c _ D D . l u a                      end
-- ======================================================================
"""

MODULE_LUA = """-- ======================================================================
-- TITLE
--   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         M O D U L E . l u a
-- ======================================================================
-- "A solver for the Advent of Code YYYY Day DD puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local CLASS = { part2 = false, text = {} numbers = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  CLASS
-- ======================================================================

-- "Object for TITLE"

function CLASS:CLASS (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  o.numbers = {}
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function CLASS:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. Add the number to the entries
    table.insert(self.numbers, tonumber(line))
    end

end

function CLASS:part_one(args)
  -- "Returns the solution for part one"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return nil
end


function CLASS:part_two(args)
  -- "Returns the solution for part two"

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return nil
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return CLASS

-- ======================================================================
-- end                      M O D U L E . l u a                     end
-- ======================================================================
"""

TEST_MODULE_LUA = """-- ======================================================================
-- TITLE
--   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ M O D U L E . l u a
-- ======================================================================
-- "Test solver for Advent of Code YYYY day DD, TITLE"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

MODULE = require('MODULE')

-- ----------------------------------------------------------------------
--                                                              from_text
-- ----------------------------------------------------------------------

function from_text(text)
  -- "Break the text into trimed, non-comment lines"

  -- 1. We start with no lines
  local result = {}

  -- 2. Loop for lines in the text
  for line in text:gmatch('[^\\r\\n]+') do

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
EXAMPLE_TEXT = [[
]]
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = nil
PART_TWO_RESULT = nil

-- ======================================================================
--                                                              TestCLASS
-- ======================================================================


function test_empty_init()
  -- "Test the default CLASS creation"

  -- 1. Create default CLASS object
  local myobj = MODULE:CLASS()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)

end

function test_text_init()
  -- "Test the CLASS object creation from text"

  -- 1. Create CLASS object from text
  local myobj = MODULE:CLASS({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)
  luaunit.assertEquals(#myobj.numbers, 0)

end

function test_part_one()
  -- "Test part one example of CLASS object"

  -- 1. Create CLASS object from text
  local myobj = MODULE:CLASS({text=from_text(PART_ONE_TEXT)})

  -- 2. Check the part one result
  luaunit.assertEquals(myobj:part_one({verbose=false, limit=0}), PART_ONE_RESULT)

end

function test_part_two()
  -- "Test part two example of CLASS object"

  -- 1. Create CLASS object from text
  local myobj = MODULE:CLASS({part2=true, text=from_text(PART_TWO_TEXT)})

  -- 2. Check the part two result
  luaunit.assertEquals(myobj:part_two({verbose=false, limit=0}), PART_TWO_RESULT)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ M O D U L E . l u a                end
-- ======================================================================
"""

PART_ONE_TXT = """Advent of Code YYYY Day DD Part One

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

----- Day DD: TITLE -----

----- Part One -----

"""

PART_TWO_TXT = """Advent of Code YYYY Day DD Part Two

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

----- Day DD: TITLE -----

----- Part Two -----

"""

EXTRA_LUA = """-- ======================================================================
-- TITLE
--   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         E X T R A . l u a
-- ======================================================================
-- "OTHER for the Advent of Code YYYY Day DD puzzle"

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local OTHER = { part2=false, text='' }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 OTHER
-- ======================================================================


function OTHER:OTHER (o)
  -- "Object for TITLE"


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function OTHER:_process_text(text)
  -- "Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

end
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return OTHER

-- ======================================================================
-- end                      E X T R A . l u a                     end
-- ======================================================================
"""

TEST_EXTRA_LUA = """-- ======================================================================
-- TITLE
--   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                    t e s t _ E X T R A . l u a
-- ======================================================================
-- "Test OTHER for Advent of Code YYYY day DD, TITLE"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
luaunit = require('luaunit')

EXTRA = require('EXTRA')

-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

-- ======================================================================
--                                                             TestOTHER
-- ======================================================================

function test_empty_init()
  -- "Test the default OTHER creation"

  -- 1. Create default OTHER object
  local myobj = EXTRA:OTHER()

  -- 2. Make sure it has the default values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)

end

function test_text_init()
  -- "Test the OTHER object creation from text"

  -- 1. Create CLASS object from text
  local myobj = EXTRA:OTHER({text=from_text(EXAMPLE_TEXT)})

  -- 2. Make sure it has the expected values
  luaunit.assertEquals(myobj.part2, false)
  luaunit.assertEquals(#myobj.text, 0)

end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
os.exit( luaunit.LuaUnit.run() )

-- ======================================================================
-- end                 t e s t _ E X T R A . p y                end
-- ======================================================================
"""

LUA_FILES = {
    'aoc_DD.lua': AOC_DD_LUA,
    'MODULE.lua': MODULE_LUA,
    'test_MODULE.lua': TEST_MODULE_LUA,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
}

LUA_EXTRA = {
    'EXTRA.lua': EXTRA_LUA,
    'test_EXTRA.lua': TEST_EXTRA_LUA,
}


def lua_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Start with simple conversions
    result = {
        "YYYY": "%4d" % args.year,
        "DD": "%02d" % args.day,
        "D D": ' '.join(list("%02d" % args.day)),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
        "EXTRA": args.ename.lower(),
        "OTHER": args.ename.capitalize(),
        "E X T R A": ' '.join(list(args.ename.lower())),
    }

    # 9. Return the text converters
    return result


def lua_after(args, converters, text):
    "Cleanup text"

    # 0. Precondition axioms
    assert args
    assert converters
    assert text

    # 9. Return the input text
    return text

# ======================================================================
# end                          a o c _ l u a . p y                   end
# ======================================================================
