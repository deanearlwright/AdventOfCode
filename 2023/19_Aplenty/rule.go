// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                          r u l e . g o
// ======================================================================
// Rule for the Advent of Code 2023 Day 19 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                   Rule
// ======================================================================

// Rule ... Object for Aplenty
type Rule struct {
	Part2    bool
	Text     string
	Category string
	MinMax   *Range
	Where    string
}

// NewRule ... Create a Rule object
func NewRule(part2 bool, text string) (*Rule, error) {
	// Rule Object for Aplenty

	// 1. Set the initial values
	p := new(Rule)
	p.Part2 = part2
	p.Text = text

	// 2. Get the ratings
	if len(text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	} else {
		p.MinMax, _ = NewRange(part2, "")
	}

	// 3. Return success
	return p, nil
}

// processText ... Assign values from text
func (p *Rule) processText(text string) error {

	// 1. Split the rule into conditional and target
	parts := strings.Split(text, ":")
	if len(parts) != 2 {
		return fmt.Errorf("invalid rule (colon) '%s'", text)
	}

	// 2. Save the target and the category
	p.Where = parts[1]
	p.Category = string(parts[0][0])

	// 3. Process the Range
	conditional := parts[0][1:]
	minmax, err := NewRange(p.Part2, conditional)
	if err != nil {
		return fmt.Errorf("invalid conditional '%s' in '%s'", conditional, text)
	}
	p.MinMax = minmax

	// 5. Return success
	return nil
}

// CheckPart ... Check a part against the rule, returning next rule or ""
func (p *Rule) CheckPart(part *Part) string {

	// 1. Get the value from the part
	value := part.GetValue(p.Category)

	// 2. If the value matches, the range go to the specified rule
	if p.MinMax.CheckValue(value) {
		return p.Where
	}

	// 3. No match, onto the next rule
	return ""
}

// String ... Representation of the rule
func (p *Rule) String() string {
	return p.Text
}

// ======================================================================
// end                          r u l e . g o                         end
// ======================================================================
