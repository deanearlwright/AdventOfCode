local table = require "table"
local io = require "io"
local ut = require "luaunit"

local entries = {}

for line in io.lines("input.txt") do
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