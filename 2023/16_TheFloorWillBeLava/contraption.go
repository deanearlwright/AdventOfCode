// ======================================================================
// The Floor Will Be Lava
//   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c o n t r a p t i o n . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 16 puzzle

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
	EMPTY   = '.'
	MIRRORF = '/'
	MIRRORB = '\\'
	SPLITV  = '|'
	SPLITH  = '-'
	CHARS   = "./\\|-"
	LOC     = 1000
	NORTH   = 'N'
	SOUTH   = 'S'
	EAST    = 'E'
	WEST    = 'W'
)

var (
	DELTA = map[rune][]int{
		NORTH: {-1, 0},
		SOUTH: {1, 0},
		EAST:  {0, 1},
		WEST:  {0, -1},
	}
	MIRRORS = map[rune]map[rune]rune{
		MIRRORF: {
			NORTH: EAST,
			SOUTH: WEST,
			EAST:  NORTH,
			WEST:  SOUTH,
		},
		MIRRORB: {
			NORTH: WEST,
			SOUTH: EAST,
			EAST:  SOUTH,
			WEST:  NORTH,
		},
	}

	SPLITS = map[rune]map[rune]string{
		SPLITV: {
			NORTH: string(NORTH),
			SOUTH: string(SOUTH),
			EAST:  string(NORTH) + string(SOUTH),
			WEST:  string(NORTH) + string(SOUTH),
		},
		SPLITH: {
			NORTH: string(EAST) + string(WEST),
			SOUTH: string(EAST) + string(WEST),
			EAST:  string(EAST),
			WEST:  string(WEST),
		},
	}
	DIRS = map[rune]int{
		NORTH: 1000000,
		SOUTH: 2000000,
		EAST:  3000000,
		WEST:  4000000,
	}
)

// ----------------------------------------------------------------------
//
//	Utility
//
// ----------------------------------------------------------------------
func beamEncode(row int, col int, direction rune) int {
	return LOC*row + col + DIRS[direction]
}

func nextLoc(row int, col int, direction rune) (int, int) {
	nextRow := row + DELTA[direction][0]
	nextCol := col + DELTA[direction][1]
	return nextRow, nextCol
}

// ======================================================================
//                                                            Contraption
// ======================================================================

// Contraption ... Object for The Floor Will Be Lava
type Contraption struct {
	Part2 bool
	Text  []string
	Rows  int
	Cols  int
	Tiles [][]bool
	Grid  [][]rune
	Beams map[int]bool
}

// NewContraption ... Create a Contraption object
func NewContraption(part2 bool, text []string) (*Contraption, error) {

	// 1. Set the initial values
	p := new(Contraption)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Initialize the tiles
	p.Tiles = make([][]bool, p.Rows)
	for row := range p.Rows {
		cols := make([]bool, p.Cols)
		p.Tiles[row] = cols
	}

	// 4. Initialize the beam cache
	p.Beams = make(map[int]bool, p.Rows*p.Cols)

	// 5. Return the new Contraption object
	return p, nil
}

// processText ... Assign values from text
func (p *Contraption) processText(text []string) error {

	// 1. Determine the size of the grid
	p.Rows = len(text)
	p.Cols = len(text[0])

	// 2. Initialize the tiles
	p.Grid = make([][]rune, p.Rows)
	for row := range p.Rows {
		cols := make([]rune, p.Cols)
		p.Grid[row] = cols
	}

	// 3. Loop for each line and column of the text
	for row, line := range text {
		for col, char := range line {

			// 4. Check the character
			if !strings.ContainsAny(string(char), CHARS) {
				return fmt.Errorf("unexpected character '%s' on row %d col %d", string(char), row, col)
			}
			// 5. Set the character in the grid
			p.Grid[row][col] = char
		}
	}

	// 6. Return success
	return nil
}

// Reset ... Reset the tiles
func (p *Contraption) Reset() {

	// 1. Loop for all of the tiles
	for row := range p.Rows {
		for col := range p.Cols {

			// 2. Mark it unenergized
			p.Tiles[row][col] = false
		}
	}

	// 2. Clear out where the beam has been
	p.Beams = make(map[int]bool, p.Rows*p.Cols)
}

// Energized ... Return the count of the energized tiles
func (p *Contraption) Energized() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the tiles
	for row := range p.Rows {
		for col := range p.Cols {

			// 3. If the tile is energized, increment the count
			if p.Tiles[row][col] {
				result = result + 1
			}
		}
	}

	// 4. Return the count of the energized tiles
	return result
}

// Beam ... Send a beam into the contraption
func (p *Contraption) Beam(row int, col int, direction rune) {

	// 1. If out of the contration, nothing to do
	if row < 0 || col < 0 || row >= p.Rows || col >= p.Cols {
		return
	}

	// 2. Nothing to do if we have been here before going this way
	beam := beamEncode(row, col, direction)
	_, ok := p.Beams[beam]
	if ok {
		return
	}

	// 3. Mark out passage and energize the tile
	p.Beams[beam] = true
	p.Tiles[row][col] = true

	// 4. Determine the next direction(s) of the beam
	nextDirs := p.NextDirs(row, col, direction)

	// 5. Loop for each new direction
	for _, dir := range nextDirs {

		// 6. Get the next location
		newRow, newCol := nextLoc(row, col, dir)

		// 7. Follow that beam
		p.Beam(newRow, newCol, dir)
	}
}

func (p *Contraption) NextDirs(row int, col int, direction rune) string {

	// 1. Start with nothing
	result := ""

	// 1. If out of the contration, nothing to do
	if row < 0 || col < 0 || row >= p.Rows || col >= p.Cols {
		return result
	}

	// 2. Get the the type of space
	thing := p.Grid[row][col]

	// 3. Determine the new direction(s)
	switch thing {
	case EMPTY:
		result = string(direction)
	case MIRRORF:
		result = string(MIRRORS[thing][direction])
	case MIRRORB:
		result = string(MIRRORS[thing][direction])
	case SPLITV:
		result = SPLITS[thing][direction]
	case SPLITH:
		result = SPLITS[thing][direction]
	}

	// 4. Return the new direction
	return result
}

// MostTiles ... How many tiles can be activated
func (p *Contraption) MostTiles() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the rows
	for row := range p.Rows {

		// 3. Enter the contraction from west and east
		p.Reset()
		p.Beam(row, 0, EAST)
		energy := p.Energized()
		if energy > result {
			result = energy
		}
		p.Reset()
		p.Beam(row, p.Cols-1, WEST)
		energy = p.Energized()
		if energy > result {
			result = energy
		}
	}

	// 4. Loop for all the columns
	for col := range p.Cols {

		// 5. Enter the contraction from north and south
		p.Reset()
		p.Beam(0, col, SOUTH)
		energy := p.Energized()
		if energy > result {
			result = energy
		}
		p.Reset()
		p.Beam(p.Rows-1, col, NORTH)
		energy = p.Energized()
		if energy > result {
			result = energy
		}
	}

	// 6. Return the most activations posible
	return result
}

// PartOne ... Returns the solution for part one
func (p *Contraption) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	p.Beam(0, 0, EAST)
	return fmt.Sprint(p.Energized())
}

// PartTwo ... Returns the solution for part two
func (p *Contraption) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.MostTiles())
}

// ======================================================================
// end                   c o n t r a p t i o n . g o                  end
// ======================================================================
