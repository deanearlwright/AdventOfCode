// ======================================================================
// Cosmic Expansion
//   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         g a l a x y . g o
// ======================================================================
// Galaxy for the Advent of Code 2023 Day 11 puzzle

package main

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
//                                                                 Galaxy
// ======================================================================

// Galaxy ... Object for Cosmic Expansion
type Galaxy struct {
	Row int64
	Col int64
}

// NewGalaxy ... Create a Galaxy object
func NewGalaxy(row int64, col int64) *Galaxy {
	// Galaxy Object for Cosmic Expansion

	// 1. Set the initial values
	p := new(Galaxy)
	p.Row = row
	p.Col = col

	// 2. Return success
	return p
}

// int64 abs from http://cavaliercoder.com/blog/optimized-abs-for-int64-in-go.html
func abs(n int64) int64 {
	y := n >> 63
	return (n ^ y) - y
}

// Distance ... Manhattan distance between two galaxies
func (g *Galaxy) Distance(o *Galaxy) int64 {

	return abs(g.Row-o.Row) + abs(g.Col-o.Col)
}

// DistanceAll ... Manhattan distance between two galaxies
func (g *Galaxy) DistanceAll(all []*Galaxy) int64 {

	// 1. Start with nothing
	result := int64(0)

	// 2. Loop for all of the other galaxies
	for _, a := range all {

		// 3. Compute the distance to this galaxy
		dist := g.Distance(a)

		// 4. Accumulated the distances
		result = result + dist
	}

	// 5. Return the total distances
	return result
}

// ======================================================================
// end                        g a l a x y . g o                       end
// ======================================================================
