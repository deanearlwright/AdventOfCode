// ======================================================================
// Alchemical Reduction
//   Advent of Code 2018 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 05, Alchemical Reduction

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
	EXAMPLE_TEXT = `dabAcCaCBAcCcaDA
`
	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = EXAMPLE_TEXT

	PART_ONE_RESULT = "10"
	PART_TWO_RESULT = "4"
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

	// 3. Check methods
	newText := oneIteration(obj.Text[0])
	if newText != "dabAaCBAcaDA" {
		t.Fatalf("oneInteration(%s) is '%s' not 'dabAaCBAcCcaDA'",
			obj.Text[0], newText)
	}
	newText = multipleIterations(obj.Text[0])
	if newText != "dabCBAcaDA" {
		t.Fatalf("oneInteration(%s) is '%s' not 'dabCBAcaDA'",
			obj.Text[0], newText)
	}
	newText = removePolymer(obj.Text[0], "a")
	if newText != "dbcCCBcCcD" {
		t.Fatalf("removePolymer(%s) is '%s' not 'dbcCCBcCcD'",
			obj.Text[0], newText)
	}
	shortest := removePolymers(obj.Text[0])
	if shortest != "daDA" {
		t.Fatalf("removePolymers(%s) is '%s' not 'daDA'",
			obj.Text[0], shortest)
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
