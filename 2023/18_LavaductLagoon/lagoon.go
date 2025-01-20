// ======================================================================
// Lavaduct Lagoon
//   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         l a g o o n . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 18 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	LOC   = 100000000
	LOCP  = LOC * 10000000
	UP    = 'U'
	DOWN  = 'D'
	RIGHT = 'R'
	LEFT  = 'L'
	DIRS  = "RDLU"
)

var (
	DELTA = map[rune][]int{
		UP:    {-1, 0},
		DOWN:  {1, 0},
		RIGHT: {0, 1},
		LEFT:  {0, -1},
	}
)

// ----------------------------------------------------------------------
//
//	Utility
//
// ----------------------------------------------------------------------
func nextLoc(row int, col int, direction rune, length int) (int, int) {
	nextRow := row + DELTA[direction][0]*length
	nextCol := col + DELTA[direction][1]*length
	return nextRow, nextCol
}

// ======================================================================
//                                                                 Lagoon
// ======================================================================

// Lagoon ... Object for Lavaduct Lagoon
type Lagoon struct {
	Part2   bool
	Text    []string
	Corners [][]int
	Trench  int
}

// NewLagoon ... Create a Lagoon object
func NewLagoon(part2 bool, text []string) (*Lagoon, error) {

	// 1. Set the initial values
	p := new(Lagoon)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Lagoon object
	return p, nil
}

// processText ... Assign values from text
func (p *Lagoon) processText(text []string) error {

	// 1. Start in the upper left
	row := 0
	col := 0
	p.Corners = make([][]int, 1, 2+len(p.Text))
	p.Corners[0] = []int{row, col}

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Decode the line
		parts := strings.Fields(line)
		if len(parts) != 3 {
			return fmt.Errorf("bad format in line %d: '%s'", indx, line)
		}
		direction := parts[0]
		if len(direction) != 1 || !strings.ContainsAny(direction, DIRS) {
			return fmt.Errorf("invalid direction '%s' in line %d: '%s'", direction, indx, line)
		}
		strMeters := parts[1]
		meters, err := strconv.ParseInt(strMeters, 10, 64)
		if err != nil {
			return fmt.Errorf("invalid meters '%s' in line %d: '%s'", strMeters, indx, line)
		}
		color := parts[2]
		if len(color) != 9 {
			return fmt.Errorf("invalid color length '%s' in line %d: '%s'", color, indx, line)
		}
		if !strings.HasPrefix(color, "(#") {
			return fmt.Errorf("invalid color prefix '%s' in line %d: '%s'", color, indx, line)
		}
		if !strings.HasSuffix(color, ")") {
			return fmt.Errorf("invalid color suffix '%s' in line %d: '%s'", color, indx, line)
		}
		color = color[2:8]

		// 3. Part 2 needs to decode the color
		if p.Part2 {
			meters, err = strconv.ParseInt(color[0:5], 16, 64)
			if err != nil {
				return fmt.Errorf("invalid color meters '%s' in line %d: '%s'", color, indx, line)
			}
			dirn, err := strconv.ParseInt(string(color[5]), 16, 64)
			if err != nil {
				return fmt.Errorf("invalid color number '%s' in line %d: '%s'", string(color[5]), indx, line)
			}
			if dirn < 0 || dirn > 3 {
				return fmt.Errorf("invalid color value '%s' in line %d: '%s'", string(color[5]), indx, line)
			}
			direction = string(DIRS[dirn])
		}

		// 4. Calculate next corner and save it
		row, col = nextLoc(row, col, rune(direction[0]), int(meters))
		p.Corners = append(p.Corners, []int{row, col})
		p.Trench = p.Trench + int(meters)
	}

	// 4. And then back to the start
	if row != 0 || col != 0 {
		return fmt.Errorf("dig plan did not return to origin")
	}

	// 5. Return success
	return nil
}

// ShoelaceArea ... Return the area of the lagoon
//
//	from https://en.wikipedia.org/wiki/Shoelace_formula
func (p *Lagoon) ShoelaceArea() int {

	// 1. Start with nothing
	corners := len(p.Corners)
	result := 0

	// 2. Loop for the remaining corners
	for indx := 0; indx < corners; indx++ {
		jndx := (indx + 1) % corners

		// 3. Get the row and column of this corner
		rcIndx := p.Corners[indx]
		rcJndx := p.Corners[jndx]

		// 4. Add in this corner
		result = result + (rcIndx[0] * rcJndx[1]) - (rcJndx[0] * rcIndx[1])
	}

	// 6. Return the area
	return int(math.Abs(float64(result / 2)))
}

// LagoonArea ... Total size of the lagoon
func (p *Lagoon) LagoonArea() int {

	// 1. Get the area by the shoestring method
	slArea := p.ShoelaceArea()

	// 2. Get the number of interior points
	interior := 1 + slArea - p.Trench/2

	// 3. Return the total size of the lagoon
	print("sl=", slArea, " int=", interior, " trench=", p.Trench, " total=", interior+p.Trench, "\n")
	return interior + p.Trench
}

// PartOne ... Returns the solution for part one
func (p *Lagoon) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.LagoonArea())
}

// PartTwo ... Returns the solution for part two
func (p *Lagoon) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.LagoonArea())
}

// ======================================================================
// end                        l a g o o n . g o                       end
// ======================================================================
