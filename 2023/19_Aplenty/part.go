// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p a r t . g o
// ======================================================================
// Part for the Advent of Code 2023 Day 19 puzzle

package main

import (
	"fmt"
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
var (
	CATEGORIES = []string{"x", "m", "a", "s"}
	INDEXES    = map[string]int{
		"x": 0,
		"m": 1,
		"a": 2,
		"s": 3,
	}
)

// ======================================================================
//                                                                   Part
// ======================================================================

// Part ... Object for Aplenty
type Part struct {
	Part2      bool
	Text       string
	Categories []int
}

// NewPart ... Create a Part object
func NewPart(part2 bool, text string) (*Part, error) {
	// Part Object for Aplenty

	// 1. Set the initial values
	p := new(Part)
	p.Part2 = part2
	p.Text = text
	p.Categories = make([]int, 4)

	// 2. Get the ratings
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
func (p *Part) processText(text string) error {

	// 1. Check the format of the string
	if !(strings.HasPrefix(text, "{") && strings.HasSuffix(text, "}")) {
		return fmt.Errorf("missing braces on '%s'", text)
	}
	parts := strings.Split(text[1:len(text)-1], ",")
	if len(parts) != 4 {
		return fmt.Errorf("should have four categories '%s'", text)
	}

	// 2. Loop for each part of the text
	for indx, part := range parts {

		// 3. Break it into category and number
		catValue := strings.Split(part, "=")
		if len(catValue) != 2 {
			return fmt.Errorf("invalid category=value in '%s", text)
		}
		if catValue[0] != CATEGORIES[indx] {
			return fmt.Errorf("unexpected category '%s' in '%s'", catValue[0], text)
		}
		value, err := strconv.Atoi(catValue[1])
		if err != nil {
			return fmt.Errorf("bad number '%s' in '%s'", catValue[1], text)
		}

		// 4. Save the category value
		p.Categories[indx] = value
	}

	// 5. Return success
	return nil
}

// Rating ... Return the rating for the part
func (p *Part) Rating() int {
	return p.Categories[0] + p.Categories[1] + p.Categories[2] + p.Categories[3]
}

// GetValue ... Returns the value of the specified category
func (p *Part) GetValue(category string) int {

	// 1. Convert the category to an index
	indx, ok := INDEXES[category]
	if !ok {
		return 0
	}

	// 2. Return the value
	return p.Categories[indx]
}

// ======================================================================
// end                          p a r t . g o                         end
// ======================================================================
