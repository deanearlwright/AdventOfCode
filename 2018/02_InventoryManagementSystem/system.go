// ======================================================================
// Inventory Management System
//   Advent of Code 2018 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s y s t e m . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 02 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"os"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                 System
// ======================================================================

// Object for Inventory Management System

type System struct {
	Part2   bool
	Text    []string
	Numbers []int
}

func NewSystem(part2 bool, text []string) *System {

	// 1. Set the initial values
	p := new(System)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		// p.processText(p.Text)
	}

	return p
}

func (p *System) processText(text []string) {
	// Assign values from text

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Add the number to the entries
		num, err := strconv.Atoi(line)
		if err != nil {
			fmt.Printf("Error %s in line %d: '%s'\n", err.Error(), indx, line)
			os.Exit(1)
		}
		p.Numbers = append(p.Numbers, num)
	}
}

func countLetters(line string) map[byte]int {
	// Return a map of the letter counts

	// 1. Create an empty map
	counts := make(map[byte]int)

	// 2. Loop for all the letters in the line
	for indx := 0; indx < len(line); indx++ {
		letter := line[indx]

		// 3. Increment count of this letter
		current := counts[letter]
		counts[letter] = current + 1
	}

	// 4. Return letter counts
	return counts
}

func hasExactly(line string, num int) bool {
	// Returns true if the line has a letter that appears num times

	// 1. Get the appearance count of the letters
	counts := countLetters(line)

	// 2. Loop for all of the counts
	for _, count := range counts {

		// 3. Return true if there is a letter with the right count
		if count == num {
			return true
		}
	}

	// 4. So sad, not letter with the right stuff
	return false
}

func (p *System) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Initialize counts
	twos := 0
	threes := 0

	// 2. Loop for each line of the text
	for indx, line := range p.Text {

		// 3. Update the number of IDs with letters that appear twice
		if hasExactly(line, 2) {
			twos++
		}

		// 4. Update the number of IDs with letters that appear thrice
		if hasExactly(line, 3) {
			threes++
		}

		// 5. Verbose output
		if verbose {
			fmt.Printf("%d: %d %d %s\n",
				indx, twos, threes, line)
		}
	}

	// 6. Return the solution for part one
	return strconv.Itoa(twos * threes)
}

func differanceAt(line1 string, line2 string) int {
	// Returns position where strings differ (-1 if multiple)

	// 1. Start with no differences
	diffAt := -1

	// 2. Loop for all of the characters
	for indx := 0; indx < len(line1); indx++ {

		// 3. Are the characters the same or different
		if line1[indx] != line2[indx] {
			if diffAt != -1 {
				return -1
			}
			diffAt = indx
		}
	}

	// 4. Either they are the same (-1) or have one difference >= 0
	return diffAt
}

func allLettersBut(letters string, exclude int) string {
	// Returns the string minus the letter at the indicated position

	// 1. Start the result
	result := ""

	// 2. Loop for all the characters
	for indx := 0; indx < len(letters); indx++ {

		// 3. If not the excluded letter, add it
		if indx != exclude {
			result = result + string(letters[indx])
		}
	}

	// 3. Return the resulting string
	return result

}

func (p *System) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Loop for all of the box IDs
	for indx := 0; indx < len(p.Text)-1; indx++ {
		id1 := p.Text[indx]

		// 2. Loop for the rest of the box IDs
		for indx2 := indx + 1; indx2 < len(p.Text); indx2++ {
			id2 := p.Text[indx2]

			// 3. Compare the two IDs
			diff := differanceAt(id1, id2)

			// 4. If there is only one difference, return the common letters
			if diff >= 0 {
				return allLettersBut(id1, diff)
			}
		}
	}

	// 5. Return no solution for part two
	return ""
}

// ======================================================================
// end                        s y s t e m . g o                       end
// ======================================================================
