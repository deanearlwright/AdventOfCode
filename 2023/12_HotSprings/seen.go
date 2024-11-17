// ======================================================================
// HotSprings
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s e e n . g o
// ======================================================================
// Seen for the Advent of Code 2023 Day 12 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

var (
	observations = []string{
		"# 1:1",
		"? 1:1",
		"#. 1:1",
		".# 1:1",
		"## 2:1",
		"?. 1:1",
		"?# 1:1",
		"?# 2:1",
		".? 1:1",
		"#? 1:1",
		"#? 2:1",
		"?? 1:2",
		"?? 2:1",
		"??? 1:3",
		"??? 1,1:3",
		"??? 2:2",
		"??? 3:1",
	}
)

// ======================================================================
//                                                                   Seen
// ======================================================================

// Seen ... Object for HotSprings
type Seen struct {
	Part2        bool
	Observations map[string]int
}

// NewSeen ... Create a Seen object
func NewSeen(part2 bool) (*Seen, error) {
	// Seen Object for HotSprings

	// 1. Set the initial values
	p := new(Seen)
	p.Part2 = part2
	p.Observations = make(map[string]int, 10000)

	// 2. Loop for all the initial observations
	for indx, obs := range observations {

		// 3. Decode the observation
		text, num, found := strings.Cut(obs, ":")
		if !found {
			return nil, fmt.Errorf("missing colon in observation %d '%s'", indx, obs)
		}
		number, err := strconv.Atoi(num)
		if err != nil {
			return nil, fmt.Errorf("bad number in observeration %d '%s'", indx, obs)
		}

		// 4. Save the observation
		p.Observations[text] = number
	}

	// 5. Return success
	return p, nil
}

// AddObservation ... Add a new observation
func (p *Seen) AddObservation(text string, num int) error {

	// 1. Check if we have seen this observation before ...
	value, seen := p.Observations[text]
	if seen {
		// 2. There is a problem if values are not the same
		if value != num {
			return fmt.Errorf("different values for '%s' was %d now %d", text, value, num)
		}
	} else {
		// 3. Save the observation
		p.Observations[text] = num
	}

	// 4. Return success
	return nil
}

// FindObservation ... Find an observation
func (p *Seen) FindObservation(text string) int {

	// 1. Is this text already seen?  Yes, return the value
	value, seen := p.Observations[text]
	if seen {
		return value
	}

	// 2. Nope, return negative
	return -1
}

// ======================================================================
// end                          s e e n . g o                         end
// ======================================================================
