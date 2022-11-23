// ======================================================================
// Chronal Coordinates
//   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 06 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	PART_TWO_LIMIT = 10000
)

// ======================================================================
//                                                                 Solver
// ======================================================================

// Object for Chronal Coordinates

type Solver struct {
	Part2       bool
	Text        []string
	Coordinates map[string]*Coord
	MinCol      int
	MaxCol      int
	MinRow      int
	MaxRow      int
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text
	p.Coordinates = make(map[string]*Coord)

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.processText(p.Text)
	}

	// 3. Determine max dimensions
	p.MaxDimensions()

	// 4. Return newly created object
	return p
}

func (p *Solver) processText(text []string) {
	// Assign values from text

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Create a coordinate from the line
		coord, err := NewCoord(p.Part2, line)

		// 3. If not succesful, ignore it
		if err != nil {
			fmt.Printf("Line %d '%s' error %s", indx, line, err)
			continue
		}

		// 4. Add it to the map of coordinates
		p.Coordinates[coord.Key] = coord
	}
}

func (p *Solver) MaxDimensions() {
	// Determine the maximum dimensions to the grid in questions

	// 1. Initialize dimentions
	p.MinCol = 99999
	p.MaxCol = -9999
	p.MinRow = 99999
	p.MaxRow = -9999

	// 2. Loop for all of the coordinates
	for _, coord := range p.Coordinates {

		// 3. Check the columns
		if coord.Col > p.MaxCol {
			p.MaxCol = coord.Col
		}
		if coord.Col < p.MinCol {
			p.MinCol = coord.Col
		}

		// 4. Check the rows
		if coord.Row > p.MaxRow {
			p.MaxRow = coord.Row
		}
		if coord.Row < p.MinRow {
			p.MinRow = coord.Row
		}
	}
}

func (p *Solver) IsEdge(col int, row int) bool {
	// Return true if location at edge (or beyond)

	// 1. Top and Bottom
	if row <= p.MinRow || row >= p.MaxRow {
		return true
	}

	// 2. Left and Right
	if col <= p.MinCol || col >= p.MaxCol {
		return true
	}

	// 3. Must be somewhere inside
	return false
}

func (p *Solver) Distances(col int, row int) map[string]int {
	// Return the distances from each coordinate

	// 1. Start the map
	distances := make(map[string]int)

	// 2. Loop for all of the coordinates
	for _, coord := range p.Coordinates {

		// 3. Get the distance
		distance := coord.Distance(col, row)

		// 4. Save the distance
		distances[coord.Key] = distance
	}

	// 5. Return the distances
	return distances
}

func (p *Solver) Closest(col int, row int) string {
	// Returns the key of the closest coordinate (or "" if tie)

	// 1. Start with nothing
	closestCoord := ""
	distanceToCoord := 9999999

	// 2. Get the distances
	distances := p.Distances(col, row)

	// 3. Loop for the coordinates
	for key, distance := range distances {

		// 4. If closer save it
		if distance < distanceToCoord {
			distanceToCoord = distance
			closestCoord = key

			// 5. If equally close, no one owns the location
		} else if distance == distanceToCoord {
			closestCoord = ""
		}
	}

	// 6. Return the closest coordinate
	return closestCoord
}

func (p *Solver) CalculateArea() {
	// Calculate the area for each of the coordinates

	// 1. Loop for all of known space
	for col := p.MinCol; col <= p.MaxCol; col++ {
		for row := p.MinRow; row <= p.MaxRow; row++ {

			// 2. Determine which coordinate is closest to this space
			closest := p.Closest(col, row)

			// 3. If there is no closest coordinate, on to the next location
			if closest == "" {
				continue
			}

			// 4. Get the closest coordinate
			coord := p.Coordinates[closest]

			// 5. Increment the area for this coordinate
			coord.Area++

			// 6. Keep track if it is infinate or not
			if p.IsEdge(col, row) {
				coord.Infinate = coord.Infinate || true
			}
		}
	}
}

func (p *Solver) LargestArea() int {
	// Return the largest non-infinate coordinate area

	// 1. Start with nothing
	largest := 0

	// 2. Loop for all the coordinates
	for _, coord := range p.Coordinates {

		// 3. Ignore ones with infinite area
		if coord.Infinate {
			continue
		}

		// 4. Remember this area if it is larger
		if coord.Area > largest {
			largest = coord.Area
		}
	}

	// 5. Return the largest area
	return largest
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Calculate the areas for each coordinate
	p.CalculateArea()

	// 1. Return the largest area
	return strconv.Itoa(p.LargestArea())
}

func (p *Solver) TotalDistance(col int, row int) int {

	// 1. Start with nothing
	total := 0

	// 2. Get the distances to the coordinates
	distances := p.Distances(col, row)

	// 3. Loop for all of the distances
	for _, distance := range distances {

		// 4. Add the distance to the total
		total = total + distance
	}

	// 5. Return the total distance
	return total
}

func (p *Solver) CalculateWithinDistance(maxDistance int) int {
	// Calculate the Number of locations within a specified distance

	// 1. Start with no locations within the maximum distance
	count := 0

	// 2. Loop for all of known space
	for col := p.MinCol; col <= p.MaxCol; col++ {
		for row := p.MinRow; row <= p.MaxRow; row++ {

			// 3. Determine the total distance to coordinates
			distance := p.TotalDistance(col, row)

			// 4. If within the maximum distance, incremente the count
			if distance < maxDistance {
				count++
			}
		}
	}

	// 5. Return the count of coordinates
	return count
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Determine the limit
	if limit == 0 {
		limit = PART_TWO_LIMIT
	}

	// 2. Return the solution for part two
	return strconv.Itoa(p.CalculateWithinDistance(limit))
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
