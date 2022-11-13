// ======================================================================
// Chronal Calibration
//   Advent of Code 2018 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c a l i b r a t i o n _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 01, Chronal Calibration

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
	EXAMPLE_TEXT = `+1
+1
+1
`
	PART_ONE_TEXT = `+1
+1
-2
`
	PART_TWO_TEXT = `
-6
+3
+8
+5
-6
`

	PART_ONE_RESULT = "0"
	PART_TWO_RESULT = "5"
)

// ======================================================================
//                                                        TestCalibration
// ======================================================================

func TestEmptyInit(t *testing.T) {
	// Test the default Calibration creation

	// 1. Create default Calibration object
	obj := NewCalibration(false, fromText(""))

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
	// Test the Calibration object creation from text

	// 1. Create Calibration object from text
	obj := NewCalibration(false, fromText(EXAMPLE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 3 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 3)
	}
	if len(obj.Numbers) != 3 {
		t.Fatalf("len(Numbers) is %d not %d",
			len(obj.Numbers), 3)
	}
}

func TestPartOne(t *testing.T) {
	// Test part one example of Calibration object

	// 1. Create Calibration object from text
	obj := NewCalibration(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 3 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 3)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	if result != PART_ONE_RESULT {
		t.Fatalf("PartOne returned '%s' not '%s'", result, PART_ONE_RESULT)
	}
}

func TestPartTwo(t *testing.T) {
	// Test part two example of Calibration object

	// 1. Create Calibration object from text
	obj := NewCalibration(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	if !obj.Part2 {
		t.Fatal("Part2 should be true")
	}
	if len(obj.Text) != 5 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 5)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end             c a l i b r a t i o n _ t e s t . g o              end
// ======================================================================
