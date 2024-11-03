// ======================================================================
// Mirage Maintenance
//   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         h i s t o r y . g o
// ======================================================================
// History for the Advent of Code 2023 Day 09 puzzle

package main

import (
	"fmt"
	"slices"
	"strconv"
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
//                                                                History
// ======================================================================

// History ... Object for Mirage Maintenance
type History struct {
	Part2  bool
	Text   string
	Values []int
}

// NewHistory ... Create a History object
func NewHistory(part2 bool, text string) (*History, error) {
	// History Object for Mirage Maintenance

	// 1. Set the initial values
	p := new(History)
	p.Part2 = part2
	p.Text = strings.TrimSpace(text)

	// 2. Fill in the values
	p.Values = make([]int, 0, len(p.Text))
	for _, valueStr := range strings.Fields(p.Text) {
		valueInt, err := strconv.Atoi(valueStr)
		if err != nil {
			return nil, fmt.Errorf("unable to convert '%s' in '%s'", valueStr, p.Text)
		}
		p.Values = append(p.Values, valueInt)
	}

	// 3. Return success
	return p, nil
}

// NextValue ... Get the next value for this history
func (p *History) NextValue() int {
	return NextValue(p.Values)
}

// PrevValue ... Get the previous value for this history
func (p *History) PrevValue() int {

	// 1. Copy the numbers
	seulaV := make([]int, len(p.Values))
	copy(seulaV, p.Values)

	// 2. And reverse them
	slices.Reverse(seulaV)

	// 3. The next value of the reversed slice is the previous value
	return NextValue(seulaV)
}

// Differences ... Returns a vector of the differences
func Differences(values []int) []int {

	// 1. Start with nothing
	result := make([]int, 0, len(values))

	// 2. Loop for almost all the values
	for indx := 0; indx+1 < len(values); indx = indx + 1 {

		// 3. Add the difference to the result
		diff := values[indx+1] - values[indx]
		result = append(result, diff)
	}

	// 4. Return the differences
	return result
}

// AllZero ... Return true if the vector is all zero values
func AllZero(values []int) bool {

	// 1. Loop for all the values
	for _, value := range values {

		// 2. If not zero return false
		if value != 0 {
			return false
		}
	}

	// 3. Then they must be all zero
	return true
}

// LastValue ... Returns the last value in the sequence
func LastValue(values []int) int {
	if len(values) == 0 {
		return 0
	}
	return values[len(values)-1]
}

// NextValue ... Determine the next value in the sequence
func NextValue(values []int) int {

	// 1. Assume the last value is the next value
	result := LastValue(values)

	// 1. Get the differences of this sequence
	diffs := Differences(values)

	// 2. If the differences are all zero, the next value is the last value
	if AllZero(diffs) {
		return result
	}

	// 3. Else the next value is a bit more complicated
	return result + NextValue(diffs)
}

// ======================================================================
// end                       h i s t o r y . g o                      end
// ======================================================================
