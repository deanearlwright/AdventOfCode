// ======================================================================
// Mirage Maintenance
//   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r e p o r t . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 09 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                 Report
// ======================================================================

// Report ... Object for Mirage Maintenance
type Report struct {
	Part2     bool
	Text      []string
	Histories []*History
}

// NewReport ... Create a Report object
func NewReport(part2 bool, text []string) (*Report, error) {

	// 1. Set the initial values
	p := new(Report)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Report object
	return p, nil
}

// processText ... Assign values from text
func (p *Report) processText(text []string) error {

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Add the number to the entries
		history, err := NewHistory(p.Part2, line)
		if err != nil {
			return fmt.Errorf("error in line %d: %s", indx, err)
		}
		p.Histories = append(p.Histories, history)
	}

	// 3. Return success
	return nil
}

// PartOne ... Returns the solution for part one
func (p *Report) PartOne(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the histories
	for _, history := range p.Histories {

		// 3. Accumulate the next values
		result = result + history.NextValue()
	}

	// 4. Return the solution for part one
	return fmt.Sprint(result)
}

// PartTwo ... Returns the solution for part two
func (p *Report) PartTwo(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the histories
	for _, history := range p.Histories {

		// 3. Accumulate the next values
		result = result + history.PrevValue()
	}

	// 4. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                        r e p o r t . g o                       end
// ======================================================================
