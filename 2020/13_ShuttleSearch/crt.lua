-- ======================================================================
-- Shuttle Search
--   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                             c r t . l u a
-- ======================================================================
-- Chinese remainder theorem
-- From https://rosettacode.org/wiki/Chinese_remainder_theorem#Lua
--   with revisions

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local crt = {}
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                    Crt
-- ======================================================================

local function prodf(a, ...) return a and a * prodf(...) or 1 end
local function prodt(t) return prodf(table.unpack(t)) end
 
local function mulInv(a, b)
    
    local b0, x0, x1 = b, 0, 1
    
    if b == 1 then
        return 1
    end
    
    while a > 1 do
        local q =a // b
        a, b = b, a % b
        x0, x1 = x1 -q * x0, x0
    end
 
    if x1 < 0 then
        x1 = x1 + b0
    end
 
    return x1
end
 
function crt.chineseRemainder(n, a)
    local prod = prodt(n)
 
    local p
    local sum = 0
    for i = 1, #n do
        p = prod // n[i]
        sum = sum + a[i] * mulInv(p, n[i]) * p
    end
 
    return sum % prod
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return crt

-- ======================================================================
-- end                           c r t . l u a                        end
-- ======================================================================
