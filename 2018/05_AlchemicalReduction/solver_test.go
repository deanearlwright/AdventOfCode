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
    EXAMPLE_TEXT = `
`
    PART_ONE_TEXT = ""
    PART_TWO_TEXT = ""

    PART_ONE_RESULT = ""
    PART_TWO_RESULT = ""
)

// ======================================================================
//                                                              TestSolver
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
    if len(obj.Numbers) != 0 {
        t.Fatal("There should be no Numbers")
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
    if len(obj.Text) != len(EXAMPLE_TEXT) {
        t.Fatalf("len(Text) is %d not %d",
            len(obj.Text), len(EXAMPLE_TEXT))
    }
    if len(obj.Numbers) != len(EXAMPLE_TEXT) {
        t.Fatalf("len(Numbers) is %d not %d",
            len(obj.Numbers), len(EXAMPLE_TEXT))
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
    if len(obj.Text) != len(PART_ONE_TEXT) {
        t.Fatalf("len(Text) is %d not %d",
            len(obj.Text), len(PART_ONE_TEXT))
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
    if len(obj.Text) != len(PART_TWO_TEXT) {
        t.Fatalf("len(Text) is %d not %d",
            len(obj.Text), len(PART_TWO_TEXT))
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
