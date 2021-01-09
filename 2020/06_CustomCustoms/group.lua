-- ======================================================================
-- Custom Customs
--   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
--
-- lua implementation by Dr. Dean Earl Wright III
-- ======================================================================

-- ======================================================================
--                         g r o u p . l u a
-- ======================================================================
-- Group for the Advent of Code 2020 Day 06 puzzle

-- ----------------------------------------------------------------------
--                                                                  local
-- ----------------------------------------------------------------------
local Group = { part2=false, text='', questions={} }
-- ----------------------------------------------------------------------
--                                                              constants
-- ----------------------------------------------------------------------

-- ======================================================================
--                                                                 Group
-- ======================================================================


function Group:Group (o)
  -- Object for Custom Customs


  -- 1. Set the initial values
  o = o or {}
  o.part2 = o.part2 or false
  o.text = o.text or {}
  o.questions = {}

  -- 2. Create the object metatable
  self.__index = self
  setmetatable(o, self)

  -- 3. Process text (if any)
  if o.text ~= nil and #o.text > 0 then
     o:_process_text(o.text)
     if o.part2 then
       o:all_fixup()
    end
  end

  return o
end

function Group:_process_text(text)
  -- Assign values from text

  -- 0. Precondition axioms
  assert(text ~= nil and #text > 0)
  
  -- 1. Loop for each person in the group
  for _, line in ipairs(text) do
    
    -- 2. Loop for each person's answers
    for indx = 1, #line do
      
      -- 3. Record the yes answers
      local yes = line:sub(indx, indx)
      self.questions[yes] = true
    end
  end
  
end

function Group:all_fixup()
  -- fixup questions to support everyone not anyone
  
  -- 1. Loop for all of the answers
  for question, _ in pairs(self.questions) do
    
    -- 2. Loop for all of the persons
    for _, line in ipairs(self.text) do
      
      -- 3. If did this person answer yes to the question?
      if nil == line:find(question) then
        
        -- 4. No, Set the answer to the question to false
        self.questions[question] = false
        break
      end
    end
  end
end

        
    
function Group:count_yes()
  -- Count the number of yes answers
  
  -- 1. Start with None
  local result = 0
  
  -- 2. Loop for all the answers
  for _, value in pairs(self.questions) do
  
    -- 3. Increment the count
    if value or not self.part2 then
      result = result + 1
    end
  end
  
  -- 4. Return the coun of yes answers
  return result
end

  
-- ----------------------------------------------------------------------
--                                                  module initialization
-- ----------------------------------------------------------------------
return Group

-- ======================================================================
-- end                      g r o u p . l u a                     end
-- ======================================================================
