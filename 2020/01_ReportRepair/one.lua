local table = require "table"
local io = require "io"
local ut = require "luaunit"
local argparse = require "argparse"



function parse_cmd_line ()
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
    return parser:parse()
end

local args = parse_cmd_line()
print(args.verbose);
print(args.part);
print(args.limit);
print(args.filepath);

function from_file(filepath)
    -- "Read the file"
    io.input(filepath)
    return from_text(io.read("*all"))
end

function from_text(text)
    -- "Break the text into trimed, non-comment lines"

    -- 1. We start with no lines
    local result = {}

    -- 2. Loop for lines in the text
    for line in text:gmatch('[^\r\n]+') do

        -- 3. But ignore blank and comment lines
        line = line:gsub("%s*$", "")
        if #line > 0 then -- and not "!" == line:sub(1, 1) then

            -- 4. Add the line
            table.insert(result, line)
        end
    end

    -- 5. Return a table of clean lines
    return result  
end

local input = from_file(args.filepath)
print("numbers: ", #input)

local entries = {}
for key, line in pairs(input) do
	local n = tonumber(line)
	for i, entry in ipairs(entries) do
		if (entry + n == 2020) then
			print('2 prod: ', entry * n)
		end

		for j = i + 1, #entries, 1 do
			if entry + entries[j] + n == 2020 then
				print('3 prod: ', entry * entries[j] * n)
			end
		end
	end
	table.insert(entries, n)
end