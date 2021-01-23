-- ======================================================================
-- Ticket Translation
--   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e s . l u a
-- ======================================================================
-- Rules for the Advent of Code 2020 Day 16 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rules = { part2=false, text='', rules = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Rules
-- ======================================================================


function Rules:Rules (o)
  -- Object for Ticket Translation


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rules = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end
  return o
end

function Rules:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Loop for all of the text
  local section = 'rul'
  for _, line in ipairs(text) do
    
    -- 2. Get the type of the input line
    local ltype = line:sub(1,3)

    -- 3. Check for the end of the rules
    if ltype == 'you' then
      section = ltype
    end
    
    -- 4. If still in the rules section, save rule
    if section == 'rul' then
      table.insert(self.rules, rule:Rule({part2=self.part2, text=line}))
    end
  end

end

function Rules:is_valid(number)
  -- Returns true if the number matches any rule
  
  -- 1. Loop for all the rules
  for _, rule in ipairs(self.rules) do
    
    -- 2. If the number is in this range for this rule, return true
    if rule:is_valid(number) then
      return true
    end
  end
  
  -- 3. Return false as this number is not in the range for any rule
  return false
end

function Rules:are_all_valid(numbers)
  -- Returns true if all of the numbers are valid for some rules
  
  -- 1. Loop for all of the numbers
  for _, number in ipairs(numbers) do
    
    -- 2. If the number is not valid, return false
    if not self:is_valid(number) then
      return false
    end
  end
  
  -- 3. Return true as all numbers are the range in some combination of rules
  return true
end

function Rules:determine_fields(position, numbers)
  -- Determine which rules match all of these numbers
  
  -- 1. Loop for all of the rules
  for _, rul in ipairs(self.rules) do
    
    -- 2. If all of the numbers are valid for this rule, renumber the position in the rule
    if rul:are_all_valid(numbers) then
      table.insert(rul.positions, position)
      -- print("Adding position", position, "to rule", rul.name)
    end
  end
end

function Rules:are_fields_resolved()
  -- Test if we need to continue rule resolution
  
  -- 1. Loop for all of the rules
  for _, rul in ipairs(self.rules ) do
    
    -- 2. If this rule is not resolved, return false
    if #rul.positions > 1 then
      return false
    end
  end
  
  -- 3. All rules are resolved, return true
  return true
end

function Rules:resolve_fields()
  -- There can be only one
  
  -- 1. Keep looping until everything settles out
  while not self:are_fields_resolved() do
    
    -- 2. Loop for all of the rules
    for rnum, _ in ipairs(self.rules) do
      
      -- 3. Get rules that could apply to this position (rule number == position number)
      local where = {}
      for _, rul in ipairs(self.rules) do
        for _, number in ipairs(rul.positions) do
          if number == rnum then
            table.insert(where, rul)
          end
        end
      end
      
      -- 4. If there is only one position for this rule, save it and remove it from other positions
      if #where == 1 then
        where[1].positions = {rnum}
        -- print('Setting', where[1].name, 'to position', rnum)
        self:remove_position(rnum)
      end
    end
  end
end

function Rules:remove_position(rnum)
  -- Remove the singleton rule from other rule positions
  
  -- 1. Loop for all of the rules
  for _, rul in ipairs(self.rules) do
    
    -- 2. Don't mess with the singleton rule
    if #rul.positions ~= 1 or rul.positions[1] ~= rnum then
    
      -- 3. Find the index of the rule in the positions (if it is there)
      local found = 0
      for indx, pos in ipairs(rul.positions) do
        if pos == rnum then
          found = indx
        end
      end
      
      -- 4. If we found it, remove it
      if found > 0 then
        table.remove(rul.positions, found)
        print('Removing', rnum, 'from', rul.name)
      end
    end
  end
end

        
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Rules

-- ======================================================================
-- end                        r u l e s . l u a                       end
-- ======================================================================
