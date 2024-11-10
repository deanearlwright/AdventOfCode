// ======================================================================
// Cosmic Expansion
//   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           i m a g e . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 11 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	galaxy = '#'
)

// ======================================================================
//                                                                  Image
// ======================================================================

// Image ... Object for Cosmic Expansion
type Image struct {
	Part2    bool
	Text     []string
	Galaxies []*Galaxy
}

// NewImage ... Create a Image object
func NewImage(part2 bool, text []string) (*Image, error) {

	// 1. Set the initial values
	p := new(Image)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText()
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Image object
	return p, nil
}

// processText ... Assign values from text
func (p *Image) processText() error {

	// 1. Get the expansion increment
	expInc := int64(2)
	if p.Part2 {
		expInc = int64(1000000)
	}

	// 2. Get the expanded index for the columns
	expCols := make([]int64, 0, len(p.Text[0])+1)
	expandIndx := int64(0)
	expCols = append(expCols, expandIndx)
	for indx := 0; indx < len(p.Text[0]); indx = indx + 1 {
		if p.IsColEmpty(indx) {
			expandIndx = expandIndx + expInc
		} else {
			expandIndx = expandIndx + 1
		}
		expCols = append(expCols, expandIndx)
	}

	// 3. Get the expanded index for the rows
	expRows := make([]int64, 0, len(p.Text)+1)
	expandIndx = int64(0)
	expRows = append(expRows, expandIndx)
	for indx := 0; indx < len(p.Text); indx = indx + 1 {
		if p.IsRowEmpty(indx) {
			expandIndx = expandIndx + expInc
		} else {
			expandIndx = expandIndx + 1
		}
		expRows = append(expRows, expandIndx)
	}

	// 4. Loop through the image
	for rowIndx, row := range p.Text {
		for colIndx, col := range row {

			// 5. If there is a galaxy here, add it
			if col == galaxy {
				p.Galaxies = append(p.Galaxies, NewGalaxy(expRows[rowIndx], expCols[colIndx]))
			}
		}
	}

	// 5. Return success
	return nil
}

// IsRowEmpty ... Returns true if row is empty
func (p *Image) IsRowEmpty(indx int) bool {
	return !strings.Contains(p.Text[indx], string(galaxy))
}

// IsColEmpty ... Returns true if column is empty
func (p *Image) IsColEmpty(indx int) bool {

	// 1. Loop for all the rows
	for _, row := range p.Text {

		// 2. If this row has a galaxy in the column, return false
		if galaxy == row[indx] {
			return false
		}
	}

	// 3. Never did see a galaxy, return true
	return true
}

// DistanceAll ... Returns the sum of the distances between each galaxies
func (p *Image) DistanceAll() int64 {

	// 1. Start with nothing
	result := int64(0)

	// 2. Loop for each galaxy
	for indx, g := range p.Galaxies {

		// 3. Get the distances to each of the other new galaxies
		dist := g.DistanceAll(p.Galaxies[indx+1:])

		// 4. Accumulate the distances
		result = result + dist
	}

	// 5. Return the total of the distances
	return result
}

// PartOne ... Returns the solution for part one
func (p *Image) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.DistanceAll())
}

// PartTwo ... Returns the solution for part two
func (p *Image) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.DistanceAll())
}

// ======================================================================
// end                         i m a g e . g o                        end
// ======================================================================
