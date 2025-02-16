// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         w o r k f l o w . g o
// ======================================================================
// Workflow for the Advent of Code 2023 Day 19 puzzle

package main

import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                               Workflow
// ======================================================================

// Workflow ... Object for Aplenty
type Workflow struct {
	Part2 bool
	Text  string
	Name  string
	Rules []*Rule
}

// NewWorkflow ... Create a Workflow object
func NewWorkflow(part2 bool, text string) (*Workflow, error) {
	// Workflow Object for Aplenty

	// 1. Set the initial values
	p := new(Workflow)
	p.Part2 = part2
	p.Text = text
	p.Rules = make([]*Rule, 0)

	// 2. Get the workflow
	if len(text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return success
	return p, nil
}

// processText ... Assign values from text
func (p *Workflow) processText(text string) error {

	// 1. Check format
	if !strings.HasSuffix(text, "}") {
		return fmt.Errorf("missing ending } for '%s'", text)
	}
	before, after, found := strings.Cut(text, "{")
	if !found {
		return fmt.Errorf("missing starting { for '%s'", text)
	}

	// 2. Save workflow name
	p.Name = before

	// 3. Process the rules
	parts := strings.Split(after[:len(after)-1], ",")
	last := len(parts) - 1
	if last < 1 {
		return fmt.Errorf("missing rules for '%s", text)
	}
	for indx, rule := range parts {

		// 4. Process the last rule
		if indx == last {
			if strings.ContainsAny(rule, "<>") {
				return fmt.Errorf("last rule '%s' should not contain conditional in '%s'", rule, text)
			}
			rule = "x>0:" + rule
		}

		// 5. Process conditional rule
		if !strings.ContainsAny(rule, "<>") {
			return fmt.Errorf("missing conditional in rule '%s' of '%s'", rule, text)
		}
		crule, err := NewRule(p.Part2, rule)
		if err != nil {
			return fmt.Errorf("error processing rule %s of '%s'", err, text)
		}
		p.Rules = append(p.Rules, crule)
	}

	// 6. Return success
	return nil
}

// CheckPart ... Check a part against the workflow, returning next workflow
func (p *Workflow) CheckPart(part *Part) string {

	// 1. Loop for the rules in the workflow
	for _, rule := range p.Rules {

		// 2. What says this rule?
		next := rule.CheckPart(part)

		// 3. If the part matches, go to the indicated workflow
		if next != "" {
			return next
		}
	}

	// 4. We should never get here!
	print("Part ", part.Text, " didn't match final rule in ", p.Name)
	return ""
}

// NextRanges ... Return the possible ranges for passing and failing this workglow
func (p *Workflow) NextRanges(r *Ranges) []*Ranges {

	// 1. Start with nothing
	result := make([]*Ranges, 0)

	// 2. Loop for the rules in the workflow
	for _, rule := range p.Rules {

		// 3. Make a copy of the ranges, pass, and append to the result
		passed := r.Clone()
		passed.Pass(rule)
		// print("Passed ", rule.Text, " in workflow ", p.Name, " with ", r.String(), " to ", passed.String(), "\n")
		result = append(result, passed)

		// 4. Continue on the the failed range
		r.Fail(rule)
		// print("Continuing with ", r.String(), " in workflow ", p.Name, "\n")
	}

	// 5. Return the ranges
	return result
}

// ======================================================================
// end                      w o r k f l o w . g o                     end
// ======================================================================
