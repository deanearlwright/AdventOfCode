// ======================================================================
// Lens Library
//   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         h a s h . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 15 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"slices"
	"strconv"
	"strings"
	"unicode"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	EQUALS = "="
	DASH   = "-"
	BOXES  = 256
)

// ----------------------------------------------------------------------
//
//	utility
//
// ----------------------------------------------------------------------
func isAlpha(str string) bool {
	for _, r := range str {
		if !unicode.IsLetter(r) {
			return false
		}
	}
	return true
}

func isDigits(str string) bool {
	for _, r := range str {
		if !unicode.IsDigit(r) {
			return false
		}
	}
	return true
}

func splitStep(step string) (string, string, error) {
	var (
		label string
		focal string
		found bool
	)

	// 1. Split the step into label and focal
	if strings.HasSuffix(step, DASH) {
		label = step[:len(step)-1]
		focal = DASH
	} else {
		label, focal, found = strings.Cut(step, "=")
		if !found {
			return "", "", fmt.Errorf("instruction step missing equal sign '%s'", step)
		}
	}

	// 2. Verify the label
	if !isAlpha(label) {
		return "", "", fmt.Errorf("instruction step label invalid '%s' in step '%s'", label, step)

	}

	// 3. Verify the focal (dash or number)
	if len(focal) != 1 {
		return "", "", fmt.Errorf("instruction step focal invalid '%s' in step '%s'", focal, step)
	}
	if !(focal == DASH || isDigits(focal)) {
		return "", "", fmt.Errorf("instruction step focal invalid '%s' in step '%s'", focal, step)
	}

	// 4. Return the parts and success
	return label, focal, nil
}

func hash(str string) int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the characters in the string
	for _, rune := range str {

		// 3. Add the ASCII code the the current value
		result = result + int(rune)

		// 4. Set the current value to itself multiplied by 17.
		result = result * 17

		// 5. Set the current value to the remainder of dividing itself by 256
		result = result % 256
	}

	// 6. Return the hash of the string
	return result
}

func findLens(box []string, label string) int {

	// 1. Loop for each lens in the box
	for indx, lens := range box {

		// 2. Break up the len info
		lensLabel, _, _ := splitStep(lens)

		// 3. Return the indx if the labels match
		if lensLabel == label {
			return indx
		}
	}

	// 4. Return not found
	return -1
}

func setBox(box []string, step string) []string {

	// 1. Get the parts of the step
	label, focal, _ := splitStep(step)

	// 2. Find the index of the label in the box (if any)
	indx := findLens(box, label)

	// 3. If operation character is dash, remove lens with label
	if focal == DASH {
		if indx >= 0 {
			box = slices.Delete(box, indx, indx+1)
		}

		// 4. If operation character is equals, replace or add lens
	} else {
		if indx >= 0 {
			box[indx] = step
		} else {
			box = append(box, step)
		}

	}

	// 5. Return the updated box
	return box
}

func boxPower(number int, box []string) int {

	// 1. Start with nothing
	result := 0

	// 1. Loop for each lens in the box
	for indx, lens := range box {

		// 2. Break up the len info
		_, focal, _ := splitStep(lens)
		power, _ := strconv.Atoi(focal)

		// 3. Accumulate the focal power
		result = result + (number+1)*(indx+1)*power
	}

	// 4. Return the focal power of the box
	return result
}

// ======================================================================
//                                                                   Hash
// ======================================================================

// Hash ... Object for Lens Library
type Hash struct {
	Part2 bool
	Text  []string
	Steps []string
	Boxes [][]string
}

// NewHash ... Create a Hash object
func NewHash(part2 bool, text []string) (*Hash, error) {

	// 1. Set the initial values
	p := new(Hash)
	p.Part2 = part2
	p.Text = text
	p.Steps = make([]string, 0)
	p.Boxes = make([][]string, BOXES)

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Initialize boxes
	for indx := 0; indx < BOXES; indx++ {
		lenses := make([]string, 0, 10)
		p.Boxes[indx] = lenses
	}

	// 4. Return the new Hash object
	return p, nil
}

// processText ... Assign values from text
func (p *Hash) processText(text []string) error {

	// 0. Precondition axioms
	if len(text) != 1 {
		return fmt.Errorf("length of text is %d should be 1", len(text))
	}

	// 1. Loop for each step of the instructions
	for _, step := range strings.Split(text[0], ",") {

		// 2. Verify the format
		_, _, err := splitStep(step)
		if err != nil {
			return err
		}

		// 3. Add the step to the instructions
		p.Steps = append(p.Steps, step)
	}

	// 3. Return success
	return nil
}

// SumStepHash ... Return the sum of the step hash
func (p *Hash) SumStepHash() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the steps
	for _, step := range p.Steps {

		// 3. Get the hash of the step and add it to the result
		result = result + hash(step)
	}

	// 4. Return the sum of the hashed step
	return result
}

func (p *Hash) ExecuteStep(step string) int {

	// 1. Split up the step
	label, _, _ := splitStep(step)

	// 2. Get the label hash
	hashed := hash(label)

	// 3. Update the indicated box
	p.Boxes[hashed] = setBox(p.Boxes[hashed], step)

	// 4. Return length of box (for debugging)
	return len(p.Boxes[hashed])
}

func (p *Hash) ExecuteAllSteps() {

	// 1. Loop for all the instruction steps
	for _, step := range p.Steps {

		// 2. Execute the step
		p.ExecuteStep(step)
	}
}

func (p *Hash) Power() int {

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the boxes
	for indx, box := range p.Boxes {

		// 2. Execute the focal power
		result = result + boxPower(indx, box)
	}

	// 4. Return the focal power of the boxes
	return result
}

// PartOne ... Returns the solution for part one
func (p *Hash) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.SumStepHash())
}

// PartTwo ... Returns the solution for part two
func (p *Hash) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	p.ExecuteAllSteps()
	return fmt.Sprint(p.Power())
}

// ======================================================================
// end                          h a s h . g o                         end
// ======================================================================
