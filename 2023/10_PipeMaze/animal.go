// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         a n i m a l . g o
// ======================================================================
// Animal for the Advent of Code 2023 Day 10 puzzle

package main

import "fmt"

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
var (
	Turns = map[string]map[rune]string{
		"North": {
			'|': "North",
			'-': "None",
			'L': "None",
			'J': "None",
			'7': "West",
			'F': "East",
			'.': "None",
			'S': "None",
		},
		"South": {
			'|': "South",
			'-': "None",
			'L': "East",
			'J': "West",
			'7': "None",
			'F': "None",
			'.': "None",
			'S': "None",
		},
		"East": {
			'|': "None",
			'-': "East",
			'L': "None",
			'J': "North",
			'7': "South",
			'F': "None",
			'.': "None",
			'S': "None",
		},
		"West": {
			'|': "None",
			'-': "West",
			'L': "North",
			'J': "None",
			'7': "None",
			'F': "South",
			'.': "None",
			'S': "None",
		},
	}
)

// ======================================================================
//                                                                 Animal
// ======================================================================

// Animal ... Object for Pipe Maze
type Animal struct {
	Loc   *Location
	Dir   string
	Steps int
}

// NewAnimal ... Create a Animal object
func NewAnimal(loc *Location, dir string) *Animal {
	// Animal Object for Pipe Maze

	// 1. Set the initial values
	p := new(Animal)
	p.Loc = loc
	p.Dir = dir
	p.Steps = 0

	// 2. Return success
	return p
}

// Move ... Move the animal
func (p *Animal) Move(maze *Pipemaze) error {

	// 1. Increment the number of steps
	p.Steps = p.Steps + 1

	// 2. Determine the new location
	p.Loc.Go(p.Dir)

	// 3. Get the pipe section a the new location
	pipe := maze.At(p.Loc.Row, p.Loc.Col)

	// 4. Determine the new direction
	table, found := Turns[p.Dir]
	if !found {
		return fmt.Errorf("invalid direction '%s' for animal at (%d,%d)", p.Dir, p.Loc.Row, p.Loc.Col)
	}
	p.Dir, found = table[pipe]
	if !found {
		return fmt.Errorf("invalid pipe section '%c' for animal at (%d,%d)", pipe, p.Loc.Row, p.Loc.Col)
	}

	// 5. Return success
	return nil
}

// Loop ... Return the locations in the loop
func (p *Animal) Loop(maze *Pipemaze) []*Location {

	// 1. Start with nothing
	locs := make([]*Location, 0, len(maze.Text)*len(maze.Text))

	// 2. Set the animal at the start
	p.Loc = maze.Start.Copy()
	p.Dir = "East"

	// 3. Loop until the animal returns to the start
	for {

		// 4. Move the animal
		p.Move(maze)

		// 5. Save the location
		locs = append(locs, p.Loc.Copy())

		// 6. If back at the start, we are done
		if p.Loc.Equal(maze.Start) {
			break
		}
	}

	// 7. Return the locations
	return locs
}

// ======================================================================
// end                        a n i m a l . g o                       end
// ======================================================================
