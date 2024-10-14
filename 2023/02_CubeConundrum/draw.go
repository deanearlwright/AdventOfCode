// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         d r a w . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 02 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//
//	types
//
// ----------------------------------------------------------------------
type colorMap = map[string]int
type Draws = []*Draw

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
var (
	colors   = []string{"red", "green", "blue"}
	maximums = colorMap{"red": 12, "green": 13, "blue": 14}
)

// ======================================================================
//                                                                   Draw
// ======================================================================

// Object for Cube Conundrum

type Draw struct {
	Part2  bool
	Text   string
	Colors colorMap
}

func NewDraw(part2 bool, text string) (*Draw, error) {

	// 1. Set the initial values
	p := new(Draw)
	p.Part2 = part2
	p.Text = text
	p.Colors = make(colorMap)

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Draw object
	return p, nil
}

func (p *Draw) processText(text string) error {
	// Assign values from text

	// 1. Loop for the colors in the draw
	for _, kntcolor := range strings.Split(text, ", ") {

		// 2. Get the count and color
		knt, color, found := strings.Cut(kntcolor, " ")
		if !found {
			return fmt.Errorf("unable to get count and color from --> %s", kntcolor)
		}
		count, err := strconv.Atoi(knt)
		if err != nil {
			return fmt.Errorf("invalid count for --> %s", kntcolor)
		}

		// 3. Save the count for this color
		if slices.Contains(colors, color) {
			p.Colors[color] = count
		} else {
			return fmt.Errorf("invalid color for --> %s", kntcolor)
		}
	}

	// 4. Return success
	return nil
}

func (p *Draw) IsLegal() bool {
	// Returns true if legal draw

	// 1. Loop for all the colors
	for _, color := range colors {

		// 2. If there are some of qubes of the color, check how many
		knt, ok := p.Colors[color]
		if ok {
			if knt > maximums[color] {
				return false
			}
		}
	}

	// 3. The draw is OK
	return true
}

func (p *Draw) Count(color string) int {
	// Returns number of cubes of the specified color

	// 1. Get amd return the count (if the color is in the draw)
	knt, ok := p.Colors[color]
	if ok {
		return knt
	}

	// 2. Otherwise there are none
	return 0
}

// ======================================================================
// end                          d r a w . g o                         end
// ======================================================================
