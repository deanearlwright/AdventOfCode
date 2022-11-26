// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 07, The Sum of Its Parts

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
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
`
	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = EXAMPLE_TEXT

	PART_ONE_RESULT = "CABDFE"
	PART_TWO_RESULT = "15"
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
	if len(obj.Steps.Steps) != 0 {
		t.Fatalf("len(Steps) is %d not 0", len(obj.Steps.Steps))
	}
	if obj.Steps.Letters != "" {
		t.Fatalf("Letters is '%s' not ''", obj.Steps.Letters)
	}
	if obj.Steps.Initial != "" {
		t.Fatalf("Initial is '%s' not ''", obj.Steps.Initial)
	}
	if obj.Steps.Final != "" {
		t.Fatalf("Final is '%s' not ''", obj.Steps.Final)
	}

	// 3. Check methods
	if !obj.Steps.Completed() {
		t.Fatal("Initial completion with no tasks should be true")
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
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not 7", len(obj.Text))
	}
	if len(obj.Steps.Steps) != 6 {
		t.Fatalf("len(Steps) is %d not 6", len(obj.Steps.Steps))
	}
	if obj.Steps.Letters != "ABCDEF" {
		t.Fatalf("Letters is '%s' not 'ABCDEF'", obj.Steps.Letters)
	}
	if obj.Steps.Initial != "C" {
		t.Fatalf("Initial is '%s' not 'C'", obj.Steps.Initial)
	}
	if obj.Steps.Final != "E" {
		t.Fatalf("Final is '%s' not 'E'", obj.Steps.Final)
	}

	// 3. Check methods
	if obj.Steps.Completed() {
		t.Fatal("Initial completion should be false")
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
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not 7", len(obj.Text))
	}
	if len(obj.Steps.Steps) != 6 {
		t.Fatalf("len(Steps) is %d not 6", len(obj.Steps.Steps))
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
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not 7", len(obj.Text))
	}
	if len(obj.Steps.Steps) != 6 {
		t.Fatalf("len(Steps) is %d not 6", len(obj.Steps.Steps))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(true, 2)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  s o l v e r _ t e s t . g o                   end
// ======================================================================
