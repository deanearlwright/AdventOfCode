// ======================================================================
// Parabolic Reflector Dish
//   Advent of Code 2023 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         d i s h . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 14 puzzle

package main

import (
	"fmt"
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
const (
	ROCK   = 'O'
	CUBE   = '#'
	BLNK   = '.'
	LOC    = 1000
	CYCLES = 1000000000
)

// ----------------------------------------------------------------------
//
//	Utility
//
// ----------------------------------------------------------------------
func locEncode(row int, col int) int {
	return row*LOC + col
}

func locDecode(loc int) (int, int) {
	row := loc / LOC
	col := loc % LOC
	return row, col
}

func locLoad(loc int, south int) int {
	row := loc / LOC
	return south - row
}

// ======================================================================
//                                                                   Dish
// ======================================================================

// Dish ... Object for Parabolic Reflector Dish
type Dish struct {
	Part2  bool
	Text   []string
	Cubes  map[int]int
	Rocks  map[int]int
	Rows   int
	Cols   int
	Images map[string]int
	Loads  []int
}

// NewDish ... Create a Dish object
func NewDish(part2 bool, text []string) (*Dish, error) {

	// 1. Set the initial values
	p := new(Dish)
	p.Part2 = part2
	p.Text = text
	p.Cubes = make(map[int]int)
	p.Rocks = make(map[int]int)

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Dish object
	return p, nil
}

// processText ... Assign values from text
func (p *Dish) processText(text []string) error {

	// 1. Set rows and columns
	p.Rows = len(text)
	p.Cols = len(text[0])

	// 2. Loop for each row and column of the text
	for row, line := range text {
		for col, char := range line {

			// 3. Add the rocks and cubes to the appropiate map
			loc := locEncode(row, col)
			if char == ROCK {
				p.Rocks[loc] = loc
			}
			if char == CUBE {
				p.Cubes[loc] = loc
			}
		}
	}

	// 4. Return success
	return nil
}

// RocksToRow ... Return a mapping of the rocks in each row
func (p *Dish) RocksToRow() map[int][]int {

	// 1. Start with nothing
	result := make(map[int][]int, p.Rows)

	// 2. Loop for all of the Rocks
	for rock := range p.Rocks {
		row, col := locDecode(rock)

		// 3. Add column to the appropiate row
		columns, ok := result[row]
		if !ok {
			columns = make([]int, 0, p.Cols)
		}
		columns = append(columns, col)
		result[row] = columns
	}

	// 4. Return the mapping
	return result
}

// TiltNorth ... Tilt the dish to the north
func (p *Dish) TiltNorth() {

	// 1. Start with no rock in place
	rolled := make(map[int]int, len(p.Rocks))

	// 2. Get the rocks in each row
	r2r := p.RocksToRow()

	// 3. Loop for all rows from the north to the south
	for row := 0; row < p.Rows; row++ {

		// 4. Get the rocks in this row
		rocks, ok := r2r[row]

		// 5. If no rocks in this row, ignore it
		if !ok {
			continue
		}

		// 6. Move all the rocks in the row
		p.TiltRowNorth(row, rocks, rolled)
	}

	// 7. Set the new location of the rocks
	p.Rocks = rolled
}

// TiltRowNorth ... Roll a row's worth of rocks
func (p *Dish) TiltRowNorth(row int, rocks []int, rolled map[int]int) {

	// 1. Loop for the rocks in this row
	for _, rock := range rocks {

		// 2. Roll the rock to the north
		newRow := p.TiltRockNorth(row, rock, rolled)

		// 3. Save the rock's new position
		loc := locEncode(newRow, rock)
		rolled[loc] = loc
	}
}

// TiltRockNorth ... Roll a rock to the north
func (p *Dish) TiltRockNorth(row int, col int, rolled map[int]int) int {

	// 1. Assume it can't move
	next := row

	// 2. It can only move if not too far north (regression base case)
	if row > 0 {
		// 3. Check if the next space north is empty
		loc := locEncode(row-1, col)
		_, ok := p.Cubes[loc]
		if !ok {
			_, ok := rolled[loc]
			if !ok {

				// 4. It is, try moving north another row
				next = p.TiltRockNorth(row-1, col, rolled)
			}
		}
	}

	// 5. Return the new row for this rock (could be the same row)
	return next
}

// Load ... Return the total load on the north support beams
func (p *Dish) Load() int {

	// 1. Start with no load
	result := 0

	// 2. Loop for all the rocks
	for rock := range p.Rocks {

		// 3. Add in the load for this rock
		result = result + locLoad(rock, p.Rows)
	}

	// 4. Return the total load
	return result
}

// Cycle ... Tilt the dish north, west, south, and east
func (p *Dish) Cycle() int {

	// 1. Rock and Roll
	p.TiltNorth()
	p.TiltWest()
	p.TiltSouth()
	p.TiltEast()

	// 2. Return the load on the north support beam
	return p.Load()
}

// TiltSouth ... Tilt the dish to the south
func (p *Dish) TiltSouth() {

	// 1. Start with no rock in place
	rolled := make(map[int]int, len(p.Rocks))

	// 2. Get the rocks in each row
	r2r := p.RocksToRow()

	// 3. Loop for all rows from the south to north
	for row := p.Rows - 1; row >= 0; row-- {

		// 4. Get the rocks in this row
		rocks, ok := r2r[row]

		// 5. If no rocks in this row, ignore it
		if !ok {
			continue
		}

		// 6. Move all the rocks in the row
		p.TiltRowSouth(row, rocks, rolled)
	}

	// 7. Set the new location of the rocks
	p.Rocks = rolled
}

// TiltRowSouth ... Roll a row's worth of rocks
func (p *Dish) TiltRowSouth(row int, rocks []int, rolled map[int]int) {

	// 1. Loop for the rocks in this row
	for _, rock := range rocks {

		// 2. Roll the rock to the south
		newRow := p.TiltRockSouth(row, rock, rolled)

		// 3. Save the rock's new position
		loc := locEncode(newRow, rock)
		rolled[loc] = loc
	}
}

// TiltRockSouth ... Roll a rock to the south
func (p *Dish) TiltRockSouth(row int, col int, rolled map[int]int) int {

	// 1. Assume it can't move
	next := row

	// 2. It can only move if not too far south (regression base case)
	if row < p.Rows-1 {
		// 3. Check if the next space south is empty
		loc := locEncode(row+1, col)
		_, ok := p.Cubes[loc]
		if !ok {
			_, ok := rolled[loc]
			if !ok {

				// 4. It is, try moving south another row
				next = p.TiltRockSouth(row+1, col, rolled)
			}
		}
	}

	// 5. Return the new row for this rock (could be the same row)
	return next
}

// RocksToCol ... Return a mapping of the rocks in each column
func (p *Dish) RocksToCol() map[int][]int {

	// 1. Start with nothing
	result := make(map[int][]int, p.Rows)

	// 2. Loop for all of the Rocks
	for rock := range p.Rocks {
		row, col := locDecode(rock)

		// 3. Add row to the appropiate column
		rows, ok := result[col]
		if !ok {
			rows = make([]int, 0, p.Rows)
		}
		rows = append(rows, row)
		result[col] = rows
	}

	// 4. Return the mapping
	return result
}

// TiltWest ... Tilt the dish to the west
func (p *Dish) TiltWest() {

	// 1. Start with no rock in place
	rolled := make(map[int]int, len(p.Rocks))

	// 2. Get the rocks in each column
	r2c := p.RocksToCol()

	// 3. Loop for all columns from the west to east
	for col := 0; col < p.Cols; col++ {

		// 4. Get the rocks in this columns
		rocks, ok := r2c[col]

		// 5. If no rocks in this column ignore it
		if !ok {
			continue
		}

		// 6. Move all the rocks in the column
		p.TiltColWest(col, rocks, rolled)
	}

	// 7. Set the new location of the rocks
	p.Rocks = rolled
}

// TiltColWest ... Roll a column's worth of rocks
func (p *Dish) TiltColWest(col int, rocks []int, rolled map[int]int) {

	// 1. Loop for the rocks in this column
	for _, rock := range rocks {

		// 2. Roll the rock to the west
		newCol := p.TiltRockWest(rock, col, rolled)

		// 3. Save the rock's new position
		loc := locEncode(rock, newCol)
		rolled[loc] = loc
	}
}

// TiltRockWest ... Roll a rock to the west
func (p *Dish) TiltRockWest(row int, col int, rolled map[int]int) int {

	// 1. Assume it can't move
	next := col

	// 2. It can only move if it isn't too far west (regression base case)
	if col > 0 {
		// 3. Check if the next space west is empty
		loc := locEncode(row, col-1)
		_, ok := p.Cubes[loc]
		if !ok {
			_, ok := rolled[loc]
			if !ok {

				// 4. It is, try moving west another column
				next = p.TiltRockWest(row, col-1, rolled)
			}
		}
	}

	// 5. Return the new column for this rock (could be the same column)
	return next
}

// TiltEast ... Tilt the dish to the east
func (p *Dish) TiltEast() {

	// 1. Start with no rock in place
	rolled := make(map[int]int, len(p.Rocks))

	// 2. Get the rocks in each column
	r2c := p.RocksToCol()

	// 3. Loop for all columns from the east to west
	for col := p.Cols - 1; col >= 0; col-- {

		// 4. Get the rocks in this columns
		rocks, ok := r2c[col]

		// 5. If no rocks in this column ignore it
		if !ok {
			continue
		}

		// 6. Move all the rock in this column
		p.TiltColEast(col, rocks, rolled)
	}

	// 7. Set the new location of the rocks
	p.Rocks = rolled
}

// TiltColEast ... Roll a column's worth of rocks
func (p *Dish) TiltColEast(col int, rocks []int, rolled map[int]int) {

	// 1. Loop for the rocks in this column
	for _, rock := range rocks {

		// 2. Roll the rock to the east
		newCol := p.TiltRockEast(rock, col, rolled)

		// 3. Save the rock's new position
		loc := locEncode(rock, newCol)
		rolled[loc] = loc
	}
}

// TiltRockEast ... Roll a rock to the east
func (p *Dish) TiltRockEast(row int, col int, rolled map[int]int) int {

	// 1. Assume it can't move
	next := col

	// 2. It can only move if it isn't too far east (regression base case)
	if col < p.Cols-1 {
		// 3. Check if the next space west is empty
		loc := locEncode(row, col+1)
		_, ok := p.Cubes[loc]
		if !ok {
			_, ok := rolled[loc]
			if !ok {

				// 4. It is, try moving west another column
				next = p.TiltRockEast(row, col+1, rolled)
			}
		}
	}

	// 5. Return the new column for this rock (could be the same column)
	return next
}

// String ... Produce a string representation
func (p *Dish) String() string {

	// 1. Create a matrix of all periods
	matrix := make([][]rune, p.Rows)
	for row := range p.Rows {
		columns := make([]rune, p.Cols)
		for col := range p.Cols {
			columns[col] = BLNK
		}
		matrix[row] = columns
	}

	// 2. Put in the cube shaped rocks
	for cube := range p.Cubes {
		row, col := locDecode(cube)
		matrix[row][col] = CUBE
	}

	// 3. Put in the round shaped rocks
	for cube := range p.Rocks {
		row, col := locDecode(cube)
		matrix[row][col] = ROCK
	}

	// 4. Turn the rows of runes into strings
	result := make([]string, p.Rows)
	for row := range p.Rows {
		result[row] = string(matrix[row])
	}

	// 5. Return the total string
	return strings.Join(result, "\n")
}

// SaveMemory ... Save a rock pattern
func (p *Dish) SaveMemory(current int) int {

	// 1. Get the load and image
	load := p.Load()
	image := p.String()

	// 2. Save the current load
	p.Loads = append(p.Loads, load)

	// 3. If this a repreat, return when
	previous, ok := p.Images[image]
	if ok {
		return previous
	}

	// 4. Else add this image
	p.Images[image] = current

	// 5. Return not yet found
	return -1
}

// FindRepeat ... Find a repeat in the cycle
func (p *Dish) FindRepeat() (int, int) {

	// 1. Create memory
	p.Images = make(map[string]int)
	p.Loads = make([]int, 0)

	// 2. Set initial value
	p.SaveMemory(0)

	// 3. Loop until we have a repeat
	for current := 1; current <= CYCLES; current++ {

		// 4. Run a cycle
		p.Cycle()

		// 5. Save the information
		previous := p.SaveMemory(current)

		// 6. If we found a repeat, report it
		if previous >= 0 {
			return previous, current
		}
	}

	// 7. Never found a repeat
	return -1, -1
}

// Future ... Returns the load from the future
func (p *Dish) Future(future int) int {

	// 1. Find when the dish spin cycle repeats
	previous, current := p.FindRepeat()
	if previous < 0 {
		return -1
	}

	// 2. Determine the cycle length and remaining steps to do
	cycleLen := current - previous
	remaining := (future - current) % cycleLen

	// 3. Return the load for the future step
	return p.Loads[previous+remaining]
}

// PartOne ... Returns the solution for part one
func (p *Dish) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	p.TiltNorth()
	return fmt.Sprint(p.Load())
}

// PartTwo ... Returns the solution for part two
func (p *Dish) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.Future(CYCLES))
}

// ======================================================================
// end                          d i s h . g o                         end
// ======================================================================
