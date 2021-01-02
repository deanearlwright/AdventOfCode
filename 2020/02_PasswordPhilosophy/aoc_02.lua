-- ======================================================================
-- Password Philosophy
--   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                           a o c _ 0 2 . l u a
-- ======================================================================
-- "Solve the puzzles for Advent of Code 2020 day 02"

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local argparse = require "argparse"

local passwords = require "passwords"

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
    :name "aoc_02"
    :description "Password Philosophy - Day 02 of Advent of Code 2020"
    :epilog "sample: lua aoc_02.lua input.txt"
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
  local solver = passwords:Passwords({part2=false, text=input_lines})

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
    local solver = passwords:Passwords({part2=true, text=input_lines})

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
-- end                         a o c _ 0 2 . l u a                      end
-- ======================================================================
