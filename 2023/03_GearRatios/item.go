// ======================================================================
// Gear Ratios
//   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         i t e m . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 03 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                   Item
// ======================================================================

// Object for Gear Ratios

type Item struct {
	Value    int
	Symbol   string
	Row      int
	StartCol int
	EndCol   int
}

func NewItem(row int, col int) *Item {

	// 1. Set the row and column
	p := &Item{Row: row, StartCol: col, EndCol: col}

	// 2. Doesn't have any values yet
	p.Value = -1
	p.Symbol = ""

	// 2. Return the new Item object
	return p
}

func NewNumber(row int, col int, char string) (*Item, error) {

	// 1. Set the initial values
	p := NewItem(row, col)

	// 2. Set the number
	value, err := strconv.Atoi(char)
	if err != nil {
		return nil, fmt.Errorf("when is a number not a number row=%d col=%d char=%s err=%s",
			row, col, char, err)
	}
	p.Value = value

	// 3. Return success
	return p, nil
}

func NewSymbol(row int, col int, char string) (*Item, error) {

	// 1. Set the initial values
	p := NewItem(row, col)

	// 2. Set the symbol
	p.Symbol = char

	// 3. Return success
	return p, nil
}

func (p *Item) AddDigitToItem(row int, col int, char string) error {

	// 1. Adjust the column
	if row != p.Row {
		return fmt.Errorf("attempt to change from from %d to %d", p.Row, row)
	}
	if col != p.EndCol+1 {
		return fmt.Errorf("row of %d is OK, but attempt to change endcol from %d to %d", row, p.EndCol, col)
	}
	p.EndCol = col

	// 2. Get the next digit
	value, err := strconv.Atoi(char)
	if err != nil {
		return fmt.Errorf("when is a number not a number row=%d col=%d char=%s err=%s",
			row, col, char, err)
	}

	// 3. Update the value
	p.Value = p.Value*10 + value

	// 4. Return success
	return nil
}

func (p *Item) IsAdjacent(other *Item) bool {

	// 1. Must be on the same row or only one above or below
	if p.Row != other.Row && p.Row != (other.Row-1) && p.Row != (other.Row+1) {
		// println("Failed in row", p.Row, other.Row)
		return false
	}

	// 2. Must be in a nearby Column
	if p.StartCol == other.StartCol || p.StartCol == other.EndCol || p.EndCol == other.StartCol || p.EndCol == other.EndCol {
		// println("Success alighment")
		return true
	}
	if p.StartCol < other.StartCol {
		if p.EndCol+1 < other.StartCol {
			// println("Failed col <", p.StartCol, p.EndCol, other.StartCol, other.EndCol)
			return false
		}
	} else if p.StartCol > other.EndCol+1 {
		// println("Failed col >=", p.StartCol, p.EndCol, other.StartCol, other.EndCol)
		return false
	}

	// 3. Row and Column look good
	// println("Success", p.Row, p.StartCol, p.EndCol, other.StartCol, other.EndCol)
	return true
}

func (p *Item) CountAdjacent(other []*Item) int {

	// 1. Start with none
	result := 0

	// 2. Loop for all of the other items
	for _, o := range other {

		// 3. Is this item adjacent, if so increment the count of items
		if p.IsAdjacent(o) {
			result = result + 1
		}
	}

	// 4. Return the number of adjacent items
	return result
}

func (p *Item) GearRatio(other []*Item) int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the other items
	for _, o := range other {

		// 3. Is this item adjacent, ...
		if p.IsAdjacent(o) {

			// 4. If this is the first gear, save it, otherwise return gear ration
			if result == 0 {
				result = o.Value
			} else {
				return result * o.Value
			}
		}
	}

	// 4. What?  We should have found two adjacent numbers
	println("Couldn't find two number adjacent to symbol", p.Symbol, "at (", p.Row, ",", p.StartCol, ")")
	return 0
}

// ======================================================================
// end                          i t e m . g o                         end
// ======================================================================
