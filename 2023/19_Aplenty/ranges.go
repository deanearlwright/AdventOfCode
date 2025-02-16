// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r a n g e s . g o
// ======================================================================
// Ranges for the Advent of Code 2023 Day 19 puzzle

package main

import "fmt"

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	X = 0
	M = 1
	A = 2
	S = 3
)

var (
	CAT2INDX = map[string]int{
		"x": X,
		"m": M,
		"a": A,
		"s": S,
	}
)

// ======================================================================
//                                                                 Ranges
// ======================================================================

// Ranges ... Object for Aplenty
type Ranges struct {
	Part2      bool
	Text       string
	Categories []*Range
}

// NewRanges ... Create a Ranges object
func NewRanges(part2 bool, text string) (*Ranges, error) {
	// Ranges Object for Aplenty

	// 1. Set the initial values
	p := new(Ranges)
	p.Part2 = part2
	p.Text = text
	p.Categories = make([]*Range, 4)

	// 2. Set the ranges
	for indx := 0; indx < 4; indx++ {
		one, err := NewRange(false, "")
		if err != nil {
			return nil, err
		}
		p.Categories[indx] = one
	}

	// 2. Return success
	return p, nil
}

func (p *Ranges) Combinations() int {

	// 1. Start with nothing
	result := 1

	// 2. Loop for the ranges
	for indx := 0; indx < 4; indx++ {

		// 3. Accumulate the combinations
		result = result * p.Categories[indx].Combinations()
	}

	// 9. Return the unique combinations
	return result
}

func (p *Ranges) Pass(r *Rule) {
	// 1. Get the category to check
	indx, ok := CAT2INDX[r.Category]
	if !ok {
		print("Rule ", r.String(), " category ", r.Category, " index ", indx, "\n")
		panic("invalid category")
	}

	// 2. Adjust the range for the rule passing
	p.Categories[indx].Pass(r.MinMax)

	// 3. Set the next workflow name
	p.Text = r.Where
}

func (p *Ranges) Fail(r *Rule) {
	// 1. Get the category to check
	indx := CAT2INDX[r.Category]

	// 2. Adjust the range for the rule failing
	p.Categories[indx].Fail(r.MinMax)
}

func (p *Ranges) Clone() *Ranges {

	// 1. Start with nothing
	result, _ := NewRanges(p.Part2, p.Text)

	// 2. Copy the range values
	for indx := 0; indx < 4; indx++ {
		clone := p.Categories[indx].Clone()
		result.Categories[indx] = clone
	}

	// 3. Return the clone
	return result
}

func (p *Ranges) String() string {
	return fmt.Sprintf("%s: x=%s, m=%s, a=%s, s=%s", p.Text,
		p.Categories[X].String(), p.Categories[M].String(),
		p.Categories[A].String(), p.Categories[S].String())
}

// ======================================================================
// end                        r a n g e s . g o                       end
// ======================================================================
