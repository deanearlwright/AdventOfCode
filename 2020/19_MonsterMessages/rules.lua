-- ======================================================================
-- Monster Messages
--   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         r u l e s . l u a
-- ======================================================================
-- A solver for the Advent of Code 2020 Day 19 puzzle

-- ----------------------------------------------------------------------
--                                                                require
-- ----------------------------------------------------------------------
local rule = require('rule')

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Rules = { part2 = false, text = {}, rules = {}, messages = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                  Rules
-- ======================================================================

-- Object for Monster Messages

function Rules:Rules (o)

  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.rules = {}
  o.messages = {}

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

  -- 1. Loop for each line of the text
  for _, line in ipairs(text) do

    -- 2. If the line contains a colon, add a rule
    if nil ~= string.find(line, ":") then
      local new_rule = rule:Rule({part2=self.part2, text=line})
      self.rules[new_rule.number] = new_rule
    -- 3. Else add a message
    else
       table.insert(self.messages, line)
    end
  end
end

function Rules:try_rule(number, message)
  -- Try to match the message against the specified rule
  -- Returns {} on failure or chars remaining to match
  
  -- print("try_rule: Trying rule", number, "against", message)
  
  -- 1. Get the rule in question
  local rul = self.rules[number]
  -- print("try_rule: Trying rule", number, "rule.number", rul.number, "definition", rul.definition, "constant", rul:is_constant())
  
  -- 2. if rule is for a letter, the message must start with that
  if rul:is_constant() then
    -- print("try_rule: a constant", rul:letter(), message:sub(1,1))
    if #message > 0 and message:sub(1,1) == rul:letter() then
      if #message == 1 then
        -- print("try_rule: matched message completely")
        return {''}
      end  
      -- print("try_rule: returning", string.sub(message, 2))
      return {string.sub(message, 2)}
    end
    -- print("try_rule: Rule", number, "for", self.definition, "does not match", message)
    return {}
  end
  
  -- 3. Start with nothing
  local result = {}
  
  -- 4. Try to match each (or only) alternate of the rule
  for _, alternative in ipairs(rul:alternatives()) do
    -- print("try_rule: Checking", alternative, "of rule", number, "against", message)
    
    -- 5. Try matchin and get the remainder of the message after matching
    local remaining = self:try_rules(alternative, message)
    
    -- 6. If match, remember what still needs to be matched
    if #remaining > 0 then
      for _, remains in ipairs(remaining) do
        table.insert(result, remains)
      end
    end
  end
  
  -- 7. Return the results of the matches (characters left to match)
  return result
end

function Rules:try_rules(numbers, message)
  -- Try to match a string of rules to the message
  -- Returns {} on failure or list of character remaining to match
  
  -- print("try_rules: Checking", numbers, "against", message)
  
  -- 1. We want to match the entire message initially but
  --    as we match the rules we want to match against the remaining
  --    chatacter of the message (which different rules may have different possibilities)
  local messages = {message}
  
  -- 2. Loop for each rule in the (partial) rule definition
  for number in string.gmatch(numbers, "%d+") do
    -- print("try_rules: Checking single", number, "against", table.concat(messages,','))
    
    -- 3. Match each rule in the definition keeping track of what remains
    local remains = {}
    for _, msg in ipairs(messages) do
      for _, remaining in ipairs(self:try_rule(number, msg)) do
        -- print("remaining", remaining)
        table.insert(remains, remaining)
      end
    end
    
    -- 4. If we matched nothing, this definition is a bust
    if #remains == 0 then
      -- print("try_rules: unable to match rule", number, "against", table.concat(messages, ','))
      return {}
    end
    
    -- 5. What the matching rule left must be matched by the next
    -- print("remains", table.concat(remains, ','))
    messages = remains
  end
  
  -- 6. Return what this rule definition did not match
  -- print("try_rules: Checking", numbers, "against", message, "returning", table.concat(messages,','))
  return messages
end

function Rules:match_rule(number, message)
  -- Return true if the specified rule matches the message
  
  -- print("match_rule: Matching rule", number, "against", message)
  
  -- 1. Loop for each match
  for _, match in ipairs(self:try_rule(number, message)) do
      
    -- 2. Return true if we have an exact match
    -- print("match_rule: rule", number, "matched and left", #match, "characters")
    if #match == 0 then
      return true
    end
  end
  
  -- 3. Nothing matched (or matched but not completely) so return false
  return false
end

function Rules:count_rule0()
  -- Return the number of messages that match rule 0 exactly
  
  -- 1. Start with nothing
  local result = 0
  
  -- 2. Loop for all of the messages
  for _, msg in ipairs(self.messages) do
    
    -- 3. Increment the count if the message matches rule 0
    if self:match_rule("0", msg) then
      result = result + 1
    end
  end
  
  -- 4. Return the count of message that matched rule 0
  return result
end
      

function Rules:part_one(args)
  -- Returns the solution for part one

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Return the solution for part one
  return self:count_rule0()
end


function Rules:part_two(args)
  -- Returns the solution for part two

  -- 0. Precondition axioms
  local verbose = args.verbose or false
  local limit = args.limit or 0
  assert(verbose == true or verbose == false)
  assert(limit >= 0)

  -- 1. Alter a few choice rules
  local new_8 = rule:Rule({part2=true, text="8: 42 | 42 8"})
  local new_11 = rule:Rule({part2=true, text="11: 42 31 | 42 11 31"})
  self.rules["8"] = new_8
  self.rules["11"] = new_11
  
  -- 2. Return the solution for part two
  return self:count_rule0()
end

-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------

return Rules

-- ======================================================================
-- end                        r u l e s . l u a                       end
-- ======================================================================
