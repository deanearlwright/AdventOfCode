// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p i p e m a z e . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 10 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"regexp"
	"slices"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	startChar = 'S'
	ground    = '.'
	pipe      = '|'
)

var (
	regToBlank = regexp.MustCompile("F-*7|L-*J|S-*7") //  U bends
	regToPipe  = regexp.MustCompile("F-*J|L-*7|S-*J") //  Kind of pipe -- just shifty
)

// ======================================================================
//                                                               Pipemaze
// ======================================================================

// Pipemaze ... Object for Pipe Maze
type Pipemaze struct {
	Part2 bool
	Text  []string
	Start *Location
}

// NewPipemaze ... Create a Pipemaze object
func NewPipemaze(part2 bool, text []string) (*Pipemaze, error) {

	// 1. Set the initial values
	p := new(Pipemaze)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Pipemaze object
	return p, nil
}

// processText ... Assign values from text
func (p *Pipemaze) processText(text []string) error {

	// 1. Loop for each line of the text
	for row, line := range text {

		// 2. Loop for each column of the line
		for col, char := range line {

			// 3. Is this the start?
			if char == startChar {
				p.Start = NewLocation(row, col)
				return nil
			}
		}
	}

	// 4. Start not found
	return fmt.Errorf("unable to find starting position")
}

// At ... Return the pipe at the indicated row and column
func (p *Pipemaze) At(row int, col int) rune {

	// 1. Check the coordinates and return pipe if good
	if len(p.Text) > 0 && row >= 0 && col >= 0 && row < len(p.Text) && col < len(p.Text[0]) {
		return rune(p.Text[row][col])
	}

	// 2. Return earth as a default
	fmt.Printf("illegal coordinate (%d, %d)", row, col)
	return ground
}

// Furthest ... Fing the number of steps to the furthest point
func (p *Pipemaze) Furthest() int {

	// 1. Create two animals
	animalOne := NewAnimal(p.Start.Copy(), "East")
	animalTwo := NewAnimal(p.Start.Copy(), "South")

	// 2. Loop until the get to the same place
	for {

		// 3. Let each move
		animalOne.Move(p)
		animalTwo.Move(p)

		// 4. If there are at the same place, we are done
		if animalOne.Loc.Equal(animalTwo.Loc) {
			break
		}
	}

	// 5. Return the number of steps
	return animalOne.Steps
}

// Loop ... Get the locations of the loop in the maze
func (p *Pipemaze) Loop() []*Location {

	// 1. Create an animal to run the maze
	animal := NewAnimal(p.Start.Copy(), "East")

	// 2. Get the locations
	locs := animal.Loop(p)

	// 3. Return the locations
	return locs
}

// OnlyLoop ... Clean up the maze to have only the loop parts
func (p *Pipemaze) OnlyLoop() {

	// 1. Get the locations of the loop in the maze
	locs := p.Loop()

	// 2. Sort the locations so we can use a binary search
	slices.SortFunc(locs, func(a, b *Location) int { return a.SortFunc(b) })

	// 3. Get text that is all ground
	newtext := make([]string, 0, len(p.Text))
	for rowindx := 0; rowindx < len(p.Text); rowindx = rowindx + 1 {
		row := make([]rune, 0, len(p.Text))
		for colindx := 0; colindx < len(p.Text[0]); colindx = colindx + 1 {
			here := NewLocation(rowindx, colindx)
			_, found := slices.BinarySearchFunc(locs, here,
				func(a, b *Location) int { return a.SortFunc(b) })
			athere := ground
			if found {
				athere = p.At(rowindx, colindx)
			}
			row = append(row, athere)
		}
		newtext = append(newtext, string(row))
	}

	// 4. Set the new text
	p.Text = newtext
}

// CountGround ... Count the number of ground spaces
func (p *Pipemaze) CountGround() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the rows
	for indx := 0; indx < len(p.Text); indx = indx + 1 {

		// 3. Get the number of ground locations in this ros
		rowknt := strings.Count(p.Text[indx], string(ground))

		// 4. Add the row count into the total
		result = result + rowknt
	}

	// 5. Return the number of ground spaces
	return result
}

// CountInsideGround ... Count the number of interier ground spaces
func (p *Pipemaze) CountInsideGround() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the rows
	for indx := 0; indx < len(p.Text); indx = indx + 1 {

		// 3. Get the number of interier spaces in this row
		knt := p.CountInsideGroundRow(indx)

		// 4. Accumulte the row counds
		result = result + knt
	}

	// 5. Return the number of ground spaces
	return result
}

// CountInsideGroundRow ... Count the number of interier ground spaces on one row
func (p *Pipemaze) CountInsideGroundRow(rowindx int) int {

	// 1. Start with nothing
	result := 0
	parity := false

	// 2. Get the row text
	row := p.Text[rowindx]

	// 3. Use regexps to simplify the row (U bends and offset pipes)
	row = regToBlank.ReplaceAllLiteralString(row, "")
	row = regToPipe.ReplaceAllLiteralString(row, string(pipe))

	// 5. Loop for all the remaining squares in the row
	for _, square := range row {

		// 6. If at pipe, increment parity
		if square == pipe {
			parity = !parity
		} else {
			// 7. Else if it is inside, increment result
			if square == ground && parity {
				result = result + 1
			}
		}
	}

	// 8. Return result
	return result
}

// PartOne ... Returns the solution for part one
func (p *Pipemaze) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.Furthest())
}

// PartTwo ... Returns the solution for part two
func (p *Pipemaze) PartTwo(verbose bool, limit int) string {

	// 1. Keep only the pipe loop
	p.OnlyLoop()

	// 2. Count the inside ground nests squares
	result := p.CountInsideGround()

	// 3. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                      p i p e m a z e . g o                     end
// ======================================================================
