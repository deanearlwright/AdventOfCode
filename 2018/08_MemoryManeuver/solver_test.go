// ======================================================================
// Memory Maneuver
//   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 08, Memory Maneuver

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
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
`
	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = EXAMPLE_TEXT

	PART_ONE_RESULT = "138"
	PART_TWO_RESULT = "66"
)

// ======================================================================
//                                                             TestSolver
// ======================================================================

func TestSolverEmptyInit(t *testing.T) {
	// Test the default Solver creation

	// 1. Create default Solver object
	obj := NewSolver(false, fromText(""))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
}

func TestSolverTextInit(t *testing.T) {
	// Test the Solver object creation from text

	// 1. Create Solver object from text
	obj := NewSolver(false, fromText(EXAMPLE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 1 {
		t.Fatalf("len(Text) is %d not 1", len(obj.Text))
	}
}

func TestSolverPartOne(t *testing.T) {
	// Test part one example of Solver object

	// 1. Create Solver object from text
	obj := NewSolver(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 1 {
		t.Fatalf("len(Text) is %d not 1", len(obj.Text))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	if result != PART_ONE_RESULT {
		t.Fatalf("PartOne returned '%s' not '%s'", result, PART_ONE_RESULT)
	}
}

func TestSolverPartTwo(t *testing.T) {
	// Test part two example of Solver object

	// 1. Create Solver object from text
	obj := NewSolver(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	if !obj.Part2 {
		t.Fatal("Part2 should be true")
	}
	if len(obj.Text) != 1 {
		t.Fatalf("len(Text) is %d not 1", len(obj.Text))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  s o l v e r _ t e s t . g o                   end
// ======================================================================
