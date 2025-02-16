// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         w o r k f l o w s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 19 puzzle

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
const (
	STARTAT  = "in"
	REJECTED = "R"
	ACCEPTED = "A"
)

// ======================================================================
//                                                              Workflows
// ======================================================================

// Workflows ... Object for Aplenty
type Workflows struct {
	Part2 bool
	Text  []string
	Flows map[string]*Workflow
	Parts []*Part
}

// NewWorkflows ... Create a Workflows object
func NewWorkflows(part2 bool, text []string) (*Workflows, error) {

	// 1. Set the initial values
	p := new(Workflows)
	p.Part2 = part2
	p.Text = text
	p.Flows = make(map[string]*Workflow)
	p.Parts = make([]*Part, 0)

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Workflows object
	return p, nil
}

// processText ... Assign values from text
func (p *Workflows) processText(text []string) error {

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Lines that start with a left currly brace are parts
		if strings.HasPrefix(line, "{") {
			part, err := NewPart(p.Part2, line)
			if err != nil {
				return fmt.Errorf("error (part) in line %d: %s", indx, err)
			}
			p.Parts = append(p.Parts, part)
			continue
		}

		// 3. Opther lines are workflows
		workflow, err := NewWorkflow(p.Part2, line)
		if err != nil {
			return fmt.Errorf("error (workflow) in line %d: %s", indx, err)
		}
		p.Flows[workflow.Name] = workflow
	}

	// 4. Return success
	return nil
}

// CheckPart ... Check a part against the workflow, returning A or R
func (p *Workflows) CheckPart(part *Part) string {

	// 1. Start at the very beginning
	wfName := STARTAT

	// 2. Loop until resolution
	for {

		// 3. Process the current rule
		wfName = p.Flows[wfName].CheckPart(part)

		// 4. If we have reach the end, return result
		if wfName == REJECTED || wfName == ACCEPTED {
			return wfName
		}
	}
}

// CheckParts ... Check all the parts, total rating number of those approved
func (p *Workflows) CheckParts() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the parts
	for _, part := range p.Parts {

		// 3. Evaluate the part
		evaluation := p.CheckPart(part)

		// 4. If approved, accumulating rating
		if evaluation == ACCEPTED {
			result = result + part.Rating()
		}
	}

	// 5. Return total rating number of approved parts
	return result
}

// Combinations
func (p *Workflows) Combinations(verbose bool, limit int) int {

	// 1. Start with nothing
	result := 0

	// 2. Initialize queue
	initialRange, _ := NewRanges(true, STARTAT)
	queue := []*Ranges{initialRange}

	// 3. Loop until the queue is empty
	for len(queue) > 0 {
		if verbose {
			fmt.Printf("Queue length %d, result %d\n", len(queue), result)
		}

		// 4. Get the next item to evaluate
		indx := len(queue) - 1
		item := queue[indx]
		queue = queue[:indx]
		if verbose {
			fmt.Printf("Evaluating %s\n", item.String())
		}

		// 5. Ignore if Rejected
		if item.Text == REJECTED {
			continue
		}

		// 6. Accumulate the combinations if Accepted
		if item.Text == ACCEPTED {
			result = result + item.Combinations()
			continue
		}

		// 7. Process the item
		more := p.Flows[item.Text].NextRanges(item)

		// 8. Add the new items to the queue
		queue = append(queue, more...)
	}

	// 9. Return the total number of combinations
	return result
}

// PartOne ... Returns the solution for part one
func (p *Workflows) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.CheckParts())
}

// PartTwo ... Returns the solution for part two
func (p *Workflows) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.Combinations(false, 10000))
}

// ======================================================================
// end                     w o r k f l o w s . g o                    end
// ======================================================================
