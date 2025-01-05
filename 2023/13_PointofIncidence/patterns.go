// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p a t t e r n s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 13 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import "fmt"

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                               Patterns
// ======================================================================

// Patterns ... Object for Point Of Incidence
type Patterns struct {
	Part2    bool
	Text     []string
	Patterns []*Pattern
}

// NewPatterns ... Create a Patterns object
func NewPatterns(part2 bool, text []string) (*Patterns, error) {

	// 1. Set the initial values
	p := new(Patterns)
	p.Part2 = part2
	p.Text = text
	p.Patterns = []*Pattern{}

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Patterns object
	return p, nil
}

// processText ... Assign values from text
func (p *Patterns) processText(text []string) error {

	// 1. Start with an empty pattern
	pattern, _ := NewPattern(p.Part2, "")

	// 1. Loop for each line of the text
	for _, line := range text {

		// 2. Add the text to the current pattern
		if line == "" {
			if pattern.HasText() {
				pattern.Rotate()
				p.Patterns = append(p.Patterns, pattern)
				pattern, _ = NewPattern(p.Part2, "")
			}
		} else {
			pattern.AddText(line)
		}
	}
	if pattern.HasText() {
		pattern.Rotate()
		p.Patterns = append(p.Patterns, pattern)
	}

	// 3. Return success
	return nil
}

// Score ... Return the total of the scores of all the patterns
func (p *Patterns) Score() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the patterns
	for _, pattern := range p.Patterns {

		// 3. Add in the score for this pattern
		result = result + pattern.Score()
	}

	// 4. Return the total of the scores
	return result
}

// PartOne ... Returns the solution for part one
func (p *Patterns) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.Score())
}

// PartTwo ... Returns the solution for part two
func (p *Patterns) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.Score())
}

// ======================================================================
// end                      p a t t e r n s . g o                     end
// ======================================================================
