-- ======================================================================
-- Operation Order
--   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         e x p r e s s i o n . l u a
-- ======================================================================
-- Expression for the Advent of Code 2020 Day 18 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Expression = { part2=false, text='', tokens = {} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                             Expression
-- ======================================================================


function Expression:Expression (o)
  -- Object for Operation Order


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.tokens = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
  end

  return o
end

function Expression:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)

  -- 1. Add space around parens
  local spaced = text:gsub("%(", " ( ")
  spaced = spaced:gsub("%)", " ) ")
  
  -- 2. Split into tokens on the spaces
  for token in string.gmatch(spaced, "%S+") do
    table.insert(self.tokens, token)
  end
  
end

function Expression:evaluate()
  -- Returns the result of the expression
  
  -- 1. Return the result of evaluating the tokens
  return tonumber(self:evaluate_tokens(self.tokens)[1])
end

function Expression:evaluate_tokens(tokens)
  -- Evaluate the tokens
  -- print("evaluate tokens = ", table.concat(tokens, ','), "length = ", #tokens) 
  local left
  local left_value
  local operation
  local right
  local right_value
  local result

  -- 1. Get the next operand
  left, tokens = self:get_operand(tokens, '+')
  if #left == 1 then
    left_value = tonumber(left[1])
  else
    left_value = tonumber(self:evaluate_tokens(left)[1])
  end
  if #tokens == 0 then
    return {tostring(left_value)}
  end
  
  -- 2. Get the operation
  operation, tokens = self:get_operation(tokens)
  
  -- 3. Get the other operand
  right, tokens = self:get_operand(tokens, operation)
  if #right == 1 then
    right_value = tonumber(right[1])
  else
    right_value = tonumber(self:evaluate_tokens(right)[1])
  end
  
  -- 4. Execute the operation
  if operation == '+' then
    result = left_value + right_value
  else
    result = left_value * right_value
  end
  
  -- 5. If no more tokens, we are done
  if #tokens == 0 then
    return {tostring(result)}
  end
  
  -- 6. Still more work to be done
  -- print("evaluate tokens before insert = ", table.concat(tokens, ','), "length = ", #tokens, "result =", result) 
  table.insert(tokens, 1, tostring(result))
  -- print("evaluate tokens after insert = ", table.concat(tokens, ','), "length = ", #tokens, "result =", result) 
  return self:evaluate_tokens(tokens)
end

function Expression:get_operand(tokens, last_op)
  -- Get the next operand
  local operand
  -- print("get_operand tokens = ", table.concat(tokens, ','), "length = ", #tokens, "last_op =", last_op) 
  
  -- 0. Precondition axioms
  assert(#tokens > 0)
  
  -- 1. Easy to handle a single token
  if #tokens == 1 then
    -- print("returning singleton token", tokens[1])
    return tokens, {}
  end
  
  -- 2. Get operand token(s)
  if self.part2 and last_op == '*' then
    operand = self:evaluate_tokens(tokens)
    tokens = {}
  elseif tokens[1] == "(" then
    table.remove(tokens, 1)
    operand, tokens = self:get_paren(tokens)
  else
    operand = {table.remove(tokens, 1)}
  end
  
  -- 3. Return the operand and the remaining tokens
  return operand, tokens
end

function Expression:get_operation(tokens)
  -- Return the next operation
  -- print("get_operation tokens = ", table.concat(tokens, ','), "length = ", #tokens) 
  
  -- 0. Precondition axioms
  assert(#tokens > 0)
  
  -- 1. The first token is the operation
  local operation = table.remove(tokens, 1)
  
  -- 2. Return the operation and the remaining tokens
  return operation, tokens
end

function Expression:get_paren(tokens)
  -- Return the parenthetical expression and the remaining tokens
  -- print("get_paren tokens = ", table.concat(tokens, ','), "length = ", #tokens) 
  
  -- 0. Precondition axioms
  assert(#tokens > 0)
  
  -- 1. Start with nothing
  local within = {}
  local depth = 0
  
  -- 2. Loop until we run out of tokens
  while #tokens > 0 do
    
    -- 3. Get the next token
    local token = table.remove(tokens, 1)
    -- print("get_paren loop", token, depth)
  
    -- 4. If this is the closing paren, return the collected within and the remaining tokens
    if token == ")" and depth == 0 then
      -- print("get_paren return, within =", table.concat(within,','), "tokens = ", table.concat(tokens,','))
      return within, tokens
    end
    
    -- 5. If a closing paren but not THE closing paren, decrease paren depth
    if token == ")" then
      depth = depth - 1
      assert(depth >= 0)
      
    -- 6. If an opening paren, increase paren depth
    elseif token == "(" then
      depth = depth + 1
      assert(depth >= 1)
    end
    
    -- 7. Add token to within collection
    table.insert(within, token)
  end
  
  -- 8. Unbalanced parens
  print(string.format("Unable to find closing paren at depth %d", depth))
  return {}, {}
end

    
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Expression

-- ======================================================================
-- end                   e x p r e s s i o n . l u a                  end
-- ======================================================================
