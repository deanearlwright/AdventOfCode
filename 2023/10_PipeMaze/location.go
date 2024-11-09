// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         l o c a t i o n . g o
// ======================================================================
// Location for the Advent of Code 2023 Day 10 puzzle

package main

import "fmt"

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                               Location
// ======================================================================

// Location ... Object for Pipe Maze
type Location struct {
	Row int
	Col int
}

// NewLocation ... Create a Location object
func NewLocation(row int, col int) *Location {

	// 1. Set the initial values
	p := new(Location)
	p.Row = row
	p.Col = col

	// 2. Return the new location
	return p
}

// Copy ... Creates a copy of the location
func (p *Location) Copy() *Location {

	// 1. Create a copy
	copy := NewLocation(p.Row, p.Col)

	// 2. Return the copy
	return copy
}

// Go .. Move one space in the indicated direction
func (p *Location) Go(direction string) {

	switch direction {
	case "North":
		p.Row = p.Row - 1
	case "South":
		p.Row = p.Row + 1
	case "East":
		p.Col = p.Col + 1
	case "West":
		p.Col = p.Col - 1
	default:
		fmt.Printf("illegal direction '%s' at row=%d, col=%d", direction, p.Row, p.Col)
	}
}

// Equal ... Returns true if the two locations have the same row and column
func (p *Location) Equal(o *Location) bool {
	return p.Row == o.Row && p.Col == o.Col
}

// Less ... Returns true if first location is less than the second
func (p *Location) Less(o *Location) bool {
	if p.Row < o.Row {
		return true
	}
	if p.Row == o.Row && p.Col < o.Col {
		return true
	}
	return false
}

// SortFunc ... Returns -1, 0, 1 for sorting
func (p *Location) SortFunc(o *Location) int {
	if p.Equal(o) {
		return 0
	}
	if p.Less(o) {
		return -1
	}
	return 1
}

// ======================================================================
// end                      l o c a t i o n . g o                     end
// ======================================================================
