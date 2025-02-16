// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r a n g e . g o
// ======================================================================
// Range for the Advent of Code 2023 Day 19 puzzle

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
	MIN = 1
	MAX = 4000
)

// ======================================================================
//                                                                  Range
// ======================================================================

// Range ... Object for Aplenty
type Range struct {
	Part2 bool
	Text  string
	Min   int
	Max   int
}

// NewRange ... Create a Range object
func NewRange(part2 bool, text string) (*Range, error) {
	// Range Object for Aplenty

	// 1. Set the initial values
	p := new(Range)
	p.Part2 = part2
	p.Text = text

	// 2. Get min and max
	min := MIN
	max := MAX
	var err error

	// 2a. min : max
	if strings.Contains(text, ":") {
		parts := strings.Split(text, ":")
		if len(parts) != 2 {
			return nil, fmt.Errorf("invalid range format '%s'", text)
		}
		min, err = strconv.Atoi(parts[0])
		if err != nil {
			return nil, fmt.Errorf("unable to convert min value '%s'", text)
		}
		max, err = strconv.Atoi(parts[1])
		if err != nil {
			return nil, fmt.Errorf("unable to convert max value '%s'", text)
		}
	}
	// 2b. < min
	if strings.HasPrefix(text, "<") {
		_, after, found := strings.Cut(text, "<")
		if found {
			value, err := strconv.Atoi(after)
			if err != nil {
				return nil, fmt.Errorf("bad number '%s' after < in '%s'", after, text)
			}
			max = value - 1
		}
	}
	// 2c. > max
	if strings.HasPrefix(text, ">") {
		_, after, found := strings.Cut(text, ">")
		if found {
			value, err := strconv.Atoi(after)
			if err != nil {
				return nil, fmt.Errorf("bad number '%s' after > in '%s'", after, text)
			}
			min = value + 1
		}
	}

	// 3. Validate min and max
	if min < MIN {
		return nil, fmt.Errorf("min value %d is less than %d in '%s'", min, MIN, text)
	}
	if max > MAX {
		return nil, fmt.Errorf("max value %d is greater than %d in '%s'", max, max, text)
	}
	if min >= max {
		return nil, fmt.Errorf("min value %d is greater than or equal to max value %d in '%s'", min, max, text)
	}

	// 4. Save min and max
	p.Min = min
	p.Max = max

	// 5. Return success
	return p, nil
}

func (p *Range) CheckValue(value int) bool {
	return value >= p.Min && value <= p.Max
}

func (p *Range) Combinations() int {
	if p.Min > p.Max {
		return 0
		//panic("Invalid range")
	}
	return 1 + p.Max - p.Min
}

func (p *Range) Pass(other *Range) {
	if other.Min > p.Min {
		p.Min = other.Min
	}
	if other.Max < p.Max {
		p.Max = other.Max
	}
	//if p.Min > p.Max {
	//	panic("Invalid range")
	//}
}

func (p *Range) Fail(other *Range) {
	p.Pass(other.Invert())
}

func (p *Range) Clone() *Range {
	new, _ := NewRange(p.Part2, p.Text)
	new.Min = p.Min
	new.Max = p.Max
	return new
}

func (p *Range) Invert() *Range {
	new, _ := NewRange(p.Part2, "")
	if p.Min > MIN {
		new.Max = p.Min - 1
	} else {
		new.Min = p.Max + 1
	}
	return new
}

func (p *Range) String() string {
	return fmt.Sprintf("%d:%d", p.Min, p.Max)
}

// ======================================================================
// end                         r a n g e . g o                        end
// ======================================================================
