// ======================================================================
// Inventory Management System
//   Advent of Code 2018 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s y s t e m _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 02, Inventory Management System

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"testing"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	EXAMPLE_TEXT = `
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
`

	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = `
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
`

	PART_ONE_RESULT = "12"
	PART_TWO_RESULT = "fgij"
)

var EXAMPLE_TWOS = [...]bool{false, true, true, false, true, true, false}
var EXAMPLE_THREES = [...]bool{false, true, false, true, false, false, true}

// ======================================================================
//                                                             TestSystem
// ======================================================================

func TestEmptyInit(t *testing.T) {
	// Test the default System creation

	// 1. Create default System object
	obj := NewSystem(false, fromText(""))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
	if len(obj.Numbers) != 0 {
		t.Fatal("There should be no Numbers")
	}
}

func TestTextInit(t *testing.T) {
	// Test the System object creation from text

	// 1. Create System object from text
	obj := NewSystem(false, fromText(EXAMPLE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 7)
	}
	if len(obj.Numbers) != 0 {
		t.Fatal("There should be no Numbers")
	}
}

func TestHasExactly(t *testing.T) {
	// Test the hasExactly() function

	// 1. Create System object from text
	obj := NewSystem(false, fromText(EXAMPLE_TEXT))

	// 2. Loop for all the lines of text
	for indx, line := range obj.Text {

		// 3. Call hasExactly for twos and threes
		twos := hasExactly(line, 2)
		threes := hasExactly(line, 3)

		// 4. Check the results
		if twos != EXAMPLE_TWOS[indx] {
			t.Logf("hasExactly('%s', 2) should be %t not %t\n",
				line, EXAMPLE_TWOS[indx], twos)
		}
		if threes != EXAMPLE_THREES[indx] {
			t.Logf("hasExactly('%s', 3) should be %t not %t\n",
				line, EXAMPLE_THREES[indx], threes)
		}

	}
}

func TestPartOne(t *testing.T) {
	// Test part one example of System object

	// 1. Create System object from text
	obj := NewSystem(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 7)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	if result != PART_ONE_RESULT {
		t.Fatalf("PartOne returned '%s' not '%s'", result, PART_ONE_RESULT)
	}
}

func TestPartTwo(t *testing.T) {
	// Test part two example of System object

	// 1. Create Calibration object from text
	obj := NewSystem(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	if !obj.Part2 {
		t.Fatal("Part2 should be true")
	}
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 7)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  s y s t e m _ t e s t . g o                   end
// ======================================================================
