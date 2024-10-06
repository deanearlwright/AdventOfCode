// ======================================================================
// Trebuchet
//   Advent of Code 2023 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 01 puzzle

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
	letters = "abcdefghijklmnopqrstuvwxyz"
	numbers = "0123456789"
)

var words = map[string]int{
	"zero":  0,
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

// ======================================================================
//                                                                 Solver
// ======================================================================

// Object for Trebuchet

type Solver struct {
	Part2 bool
	Text  []string
	First []int
	Last  []int
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.processText(p.Text)
	}

	return p
}

func (p *Solver) processText(text []string) {
	// Get first and last number from each line

	// 1. Loop for each line of the text
	for _, line := range text {

		// 2. Get the numbers from the line
		whereFirstNum, first := p.getFirstNumber(line)
		whereLastNum, last := p.getLastNumber(line)

		// 2.5 if part2, try to find a word before/after the number
		if p.Part2 {
			whereFirstWord, firstWord := p.getFirstWord(line)
			whereLastWord, lastWord := p.getLastWord(line)
			if whereFirstWord < whereFirstNum {
				first = firstWord
			}
			if whereLastWord > whereLastNum {
				last = lastWord
			}
		}

		// 3. Save them
		p.First = append(p.First, first)
		p.Last = append(p.Last, last)
	}
}

func (p *Solver) getFirstNumber(line string) (int, int) {
	where := strings.IndexAny(line, numbers)
	value := 0
	if where >= 0 {
		value = strings.Index(numbers, line[where:where+1])
	} else {
		where = len(line) + 1
	}
	return where, value
}

func (p *Solver) getLastNumber(line string) (int, int) {
	where := strings.LastIndexAny(line, numbers)
	value := 0
	if where >= 0 {
		value = strings.Index(numbers, line[where:where+1])
	} else {
		where = -10
	}
	return where, value
}

func (p *Solver) getFirstWord(line string) (int, int) {
	best := len(line) + 1
	value := 0
	for word, wordValue := range words {
		where := strings.Index(line, word)
		if where >= 0 && where < best {
			best = where
			value = wordValue
		}
	}
	return best, value
}

func (p *Solver) getLastWord(line string) (int, int) {
	best := -1
	value := 0
	for word, wordValue := range words {
		where := strings.LastIndex(line, word)
		if where >= 0 && where > best {
			best = where
			value = wordValue
		}
	}
	return best, value
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one
	sum := 0

	// 1. Loop for all the numbers
	for indx := 0; indx < len(p.First); indx++ {

		// 2. Combine first and last
		number := p.First[indx]*10 + p.Last[indx]

		// 3. Add it to the sum
		sum = sum + number
	}

	// 4. Return the solution for part one
	return fmt.Sprint(sum)
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	sum := 0

	// 1. Loop for all the numbers
	for indx := 0; indx < len(p.First); indx++ {

		// 2. Combine first and last
		number := p.First[indx]*10 + p.Last[indx]

		// 3. Add it to the sum
		sum = sum + number
	}

	// 4. Return the solution for part two
	return fmt.Sprint(sum)
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
