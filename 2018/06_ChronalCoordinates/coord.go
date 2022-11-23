// ======================================================================
// Chronal Coordinates
//   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c o o r d . g o
// ======================================================================
// Coord for the Advent of Code 2018 Day 06 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                  Coord
// ======================================================================

type Coord struct {
	Part2    bool
	Text     string
	Col      int
	Row      int
	Key      string
	Area     int
	Infinate bool
}

func NewCoord(part2 bool, text string) (*Coord, error) {
	// Coord Object for Chronal Coordinates

	// 1. Set the initial values
	p := new(Coord)
	p.Part2 = part2
	p.Text = text
	p.Col = 0
	p.Row = 0
	p.Key = "???"
	p.Area = 0
	p.Infinate = false

	// 2. Split the line
	parts := strings.Split(text, ", ")
	if len(parts) != 2 {
		return nil, errors.New("splitting line")
	}
	col, err := strconv.Atoi(parts[0])
	if err != nil {
		return nil, errors.New("obtailing col")
	}
	row, err := strconv.Atoi(parts[1])
	if err != nil {
		return nil, errors.New("obtailing row")
	}

	// 3. Set the column and row
	p.Key = fmt.Sprintf("%d,%d", col, row)
	p.Col = col
	p.Row = row

	// 4. Return the newly created coordinate
	return p, nil
}

func abs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

func (p *Coord) Distance(col int, row int) int {
	// Returns the manhattan distance from the Coordinage to the (col, row)
	return abs(col-p.Col) + abs(row-p.Row)
}

// ======================================================================
// end                         c o o r d . g o                        end
// ======================================================================
