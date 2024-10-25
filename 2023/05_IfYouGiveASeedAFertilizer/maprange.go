// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         m a p r a n g e . g o
// ======================================================================
// Maprange for the Advent of Code 2023 Day 05 puzzle

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
const (
	blank = " "
)

// ======================================================================
//                                                               Maprange
// ======================================================================

// Maprange ... Objext for ranged map
type Maprange struct {
	Part2       bool
	Text        string
	DestStart   int
	SourceStart int
	RangeLength int
}

// NewMaprange ... Returns a new Maprange
func NewMaprange(part2 bool, text string) (*Maprange, error) {
	// Maprange Object for IfYouGiveASeedAFertilizer

	// 1. Set the initial values
	p := new(Maprange)
	p.Part2 = part2
	p.Text = text

	// 2. Split the text into three numbers
	numbers := strings.Split(text, blank)
	if len(numbers) != 3 {
		return nil, fmt.Errorf("unable to split '%s' into three", text)
	}

	// 3. Convert numbers to integers
	number, err := strconv.Atoi(numbers[0])
	if err != nil {
		return nil, fmt.Errorf("unable to convert '%s' from %s into a number: %s", numbers[0], text, err)
	}
	p.DestStart = number

	number, err = strconv.Atoi(numbers[1])
	if err != nil {
		return nil, fmt.Errorf("unable to convert '%s' from %s into a number: %s", numbers[1], text, err)
	}
	p.SourceStart = number

	number, err = strconv.Atoi(numbers[2])
	if err != nil {
		return nil, fmt.Errorf("unable to convert '%s' from %s into a number: %s", numbers[2], text, err)
	}
	p.RangeLength = number

	// 4. Return success
	return p, nil
}

// IsInSourceRange ... Returns true if source in the range
func (p *Maprange) IsInSourceRange(source int) bool {
	return source >= p.SourceStart && source < p.SourceStart+p.RangeLength
}

// IsInDestinationRange ... Returns true if destination is in the range
func (p *Maprange) IsInDestinationRange(dest int) bool {
	return dest >= p.DestStart && dest < p.DestStart+p.RangeLength
}

// MapSourceToDest ... Returns the destination from the source
func (p *Maprange) MapSourceToDest(source int) int {

	// 1. if not in range, return unaltered
	if !p.IsInSourceRange(source) {
		return source
	}

	// 2. Return the mapped source
	return p.DestStart + source - p.SourceStart
}

// ======================================================================
// end                      m a p r a n g e . g o                     end
// ======================================================================
