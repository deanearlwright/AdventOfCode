// ======================================================================
// Gear Ratios
//   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s c h e m a t i c . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 03 puzzle

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
	period = "."
	digits = "0123456789"
	gear   = "*"
)

// ======================================================================
//                                                              Schematic
// ======================================================================

// Object for Gear Ratios

type Schematic struct {
	Part2   bool
	Text    []string
	Numbers []*Item
	Symbols []*Item
}

func NewSchematic(part2 bool, text []string) (*Schematic, error) {

	// 1. Set the initial values
	p := new(Schematic)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Schematic object
	return p, nil
}

func (p *Schematic) processText(text []string) error {
	// Assign values from text

	// 0. Start with nothing
	var number *Item = nil
	var err error

	// 1. Loop for each line of the text
	for row, line := range text {

		// 2. Loop for each character in the line
		for col, char := range line {
			schar := string(char)
			//if schar != period {
			//	fmt.Printf("At row=%d, col=%d is {%s}\n", row, col, schar)
			//}
			if strings.ContainsAny(schar, digits) {
				if number == nil {
					number, err = NewNumber(row, col, schar)
					if err != nil {
						return err
					}
				} else {
					err = number.AddDigitToItem(row, col, schar)
					if err != nil {
						return err
					}
				}
			} else {
				if number != nil {
					p.Numbers = append(p.Numbers, number)
					number = nil
				}
				if schar != period {
					symbol, err := NewSymbol(row, col, schar)
					if err != nil {
						return err
					}
					p.Symbols = append(p.Symbols, symbol)
				}
			}
		}
		if number != nil {
			p.Numbers = append(p.Numbers, number)
			number = nil
		}
	}

	// 3. Return success
	return nil
}

func (p *Schematic) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the numbers
	for _, num := range p.Numbers {

		// 3. How many symbols are near this number
		knt := num.CountAdjacent(p.Symbols)

		// 4. If near any symbols, accumulate the number
		if knt > 0 {
			result = result + num.Value
		}
	}

	// 9. Return the solution for part one
	return fmt.Sprint(result)
}

func (p *Schematic) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the numbers
	for _, sym := range p.Symbols {

		// 3. Only interested in gears
		if sym.Symbol != gear {
			continue
		}

		// 4. How many numbers are near the gear?
		knt := sym.CountAdjacent(p.Numbers)

		// 5. If the gear is between two gears, get the gear ration
		if knt == 2 {
			result = result + sym.GearRatio(p.Numbers)
		}
	}

	// 9. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                        s c h e m a t i c . g o                       end
// ======================================================================
