// ======================================================================
// Clumsy Crucible
//   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c r u c i b l e s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 17 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"container/heap"
	"fmt"
	"strconv"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	LOC   = 1000
	DIR   = 1000000
	STR   = 10000000
	HEAT  = 1000000000
	NORTH = 'N'
	SOUTH = 'S'
	EAST  = 'E'
	WEST  = 'W'
	XDIRS = "XNSEW"
)

var (
	DELTA = map[rune][]int{
		NORTH: {-1, 0},
		SOUTH: {1, 0},
		EAST:  {0, 1},
		WEST:  {0, -1},
	}
	TURNRIGHT = map[rune]rune{
		NORTH: EAST,
		SOUTH: WEST,
		EAST:  SOUTH,
		WEST:  NORTH,
	}
	TURNLEFT = map[rune]rune{
		NORTH: WEST,
		SOUTH: EAST,
		EAST:  NORTH,
		WEST:  SOUTH,
	}
	DIRS = map[rune]int{
		NORTH: 1000000,
		SOUTH: 2000000,
		EAST:  3000000,
		WEST:  4000000,
	}
)

// ----------------------------------------------------------------------
//                                                                IntHeap
// An IntHeap is a min-heap of ints.
// From: https://pkg.go.dev/container/heap
// ----------------------------------------------------------------------

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// ----------------------------------------------------------------------
//
//	Utility
//
// ----------------------------------------------------------------------
func heatEncode(row int, col int, direction rune, straight int, heat int) int {
	return LOC*row + col + DIRS[direction] + STR*straight + HEAT*heat
}

func heatDecode(state int) (int, int, rune, int, int) {
	heat := state / HEAT
	rest := state % HEAT
	straight := rest / STR
	rest = rest % STR
	dir := rest / DIR
	rest = rest % DIR
	row := rest / LOC
	col := rest % LOC
	return row, col, rune(XDIRS[dir]), straight, heat
}

func nextLoc(row int, col int, direction rune) (int, int) {
	nextRow := row + DELTA[direction][0]
	nextCol := col + DELTA[direction][1]
	return nextRow, nextCol
}

func equalLoc(row int, col int, loc []int) bool {
	return row == loc[0] && col == loc[1]
}

// ======================================================================
//                                                              Crucibles
// ======================================================================

// Crucibles ... Object for Clumsy Crucible
type Crucibles struct {
	Part2 bool
	Text  []string
	Rows  int
	Cols  int
	Loss  [][]int
}

// NewCrucibles ... Create a Crucibles object
func NewCrucibles(part2 bool, text []string) (*Crucibles, error) {

	// 1. Set the initial values
	p := new(Crucibles)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Crucibles object
	return p, nil
}

// processText ... Assign values from text
func (p *Crucibles) processText(text []string) error {

	// 1. Set the number of rows and cols
	p.Rows = len(text)
	p.Cols = len(text[0])

	// 2. Loop for each row and column
	p.Loss = make([][]int, p.Rows)
	for row, line := range text {
		p.Loss[row] = make([]int, p.Cols)
		for col, char := range line {

			// 3. Add the number to the Loss matrix
			num, err := strconv.Atoi(string(char))
			if err != nil {
				return fmt.Errorf("error at row %d, col %d: '%s'", row, col, string(char))
			}
			p.Loss[row][col] = num
		}
	}

	// 4. Return success
	return nil
}

// MinHeatLoss ... Return the minimum heat loss from the start to the goal
func (p Crucibles) MinHeatLoss() int {

	// 1. Initial values, maps, and heaps
	startLoc := []int{0, 0}
	startEast := heatEncode(startLoc[0], startLoc[1], EAST, 0, 0)
	startSouth := heatEncode(startLoc[0], startLoc[1], SOUTH, 0, 0)
	goalLoc := []int{p.Rows - 1, p.Cols - 1}
	// print("goal = ", goalLoc[0], ",", goalLoc[1], "\n")
	minStraight := 0
	maxStraight := 3
	if p.Part2 {
		minStraight = 4
		maxStraight = 10
	}
	seen := make(map[int]bool, p.Rows*p.Cols)
	//seen[startEast] = true
	//seen[startSouth] = true
	search := &IntHeap{startEast, startSouth}
	heap.Init(search)

	// 2. Loop until we can search no more
	for search.Len() > 0 {
		//if search.Len() > 6 {
		//	return -1
		//}
		var state int

		// 3. Get the lowest head lost value from the search heap
		state, ok := heap.Pop(search).(int)
		if !ok {
			print("Junk on stack -->", state)
			return 0
		}
		row, col, direction, straight, heatLoss := heatDecode(state)

		// 4. Check if we have been here before, if not mark our passage
		seenState := heatEncode(row, col, direction, straight, 0)
		_, ok = seen[seenState]
		if ok {
			// print("see r=", row, " c=", col, " d=", string(direction), " s=", straight, " h=", heatLoss, "\n")
			continue
		}
		seen[seenState] = true

		// 5. Where can we go from here?
		mayTurn := straight >= minStraight
		mustTurn := straight >= maxStraight
		directions := p.NextDirections(direction, mayTurn, mustTurn)
		//print("    r=", row, " c=", col, " d=", string(direction), " s=", straight, " h=", heatLoss, " t=", mayTurn, ",", mustTurn, " n=", string(directions), "\n")

		// 6. Loop for the possible directions
		for _, nextDir := range directions {

			// 7. Is this a valid grid square which we haven't seen before
			nextRow, nextCol := nextLoc(row, col, nextDir)
			delta := p.HeatDelta(nextRow, nextCol)
			if delta < 0 {
				continue
			}

			// 8. Add new state to search
			nextStraight := straight + 1
			if nextDir != direction {
				nextStraight = 1
			}

			// 9. If we made it, return heatloss
			if equalLoc(row, col, goalLoc) {
				// print("end r=", row, " c=", col, " d=", string(direction), " s=", straight, " h=", heatLoss, "\n")
				if straight >= minStraight {
					return heatLoss
				}
				continue
			}

			// 10. Continue search
			// print("add r=", nextRow, " c=", nextCol, " d=", string(nextDir), " s=", nextStraight, " h=", heatLoss+delta, "\n")
			heap.Push(search, heatEncode(nextRow, nextCol, nextDir, nextStraight, heatLoss+delta))
		}
	}

	// 11. Should not reach here
	print("Goal not found\n")
	return 0
}

func (p *Crucibles) NextDirections(direction rune, mayTurn bool, mustTurn bool) []rune {

	// 1. Start with nothing
	result := make([]rune, 0, 3)

	// 2. Can we keep going in the direction
	if !mustTurn {
		result = append(result, direction)
	}

	// 3. Can we turn?
	if mayTurn {
		result = append(result, TURNLEFT[direction])
		result = append(result, TURNRIGHT[direction])
	}

	// 4. Return the possible directions
	return result
}

func (p *Crucibles) HeatDelta(row int, col int) int {

	// 1. Check for valid row and column
	if row < 0 || col < 0 || row >= p.Rows || col >= p.Cols {
		return -1
	}

	// 2. Return the heat loss delta from the grid
	return p.Loss[row][col]
}

// PartOne ... Returns the solution for part one
func (p *Crucibles) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.MinHeatLoss())
}

// PartTwo ... Returns the solution for part two
func (p *Crucibles) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	return fmt.Sprint(p.MinHeatLoss())
}

// ======================================================================
// end                     c r u c i b l e s . g o                    end
// ======================================================================
