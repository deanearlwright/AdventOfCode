// ======================================================================
// Chronal Coordinates
//   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 06, Chronal Coordinates

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
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9`

	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = EXAMPLE_TEXT

	PART_ONE_RESULT = "17"
	PART_TWO_RESULT = "16"
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
	if len(obj.Text) != 6 {
		t.Fatalf("len(Text) is %d not 6", len(obj.Text))
	}
	if len(obj.Coordinates) != 6 {
		t.Fatalf("len(Coordinates) is %d not 6", len(obj.Coordinates))
	}
	if obj.MinCol != 1 {
		t.Fatalf("MinCol is %d not 1", obj.MinCol)
	}
	if obj.MaxCol != 8 {
		t.Fatalf("MaxCol is %d not 8", obj.MinCol)
	}
	if obj.MinRow != 1 {
		t.Fatalf("MinRow is %d not 1", obj.MinRow)
	}
	if obj.MaxRow != 9 {
		t.Fatalf("MaxRow is %d not 9", obj.MaxRow)
	}

	// 3. Check methods
	distances := obj.Distances(4, 4)
	if distances["1,1"] != 6 {
		t.Fatalf("Distance from coord [1,1] to (4,4) is %d not 6", distances["1,1"])
	}
	if distances["8,3"] != 5 {
		t.Fatalf("Distance from coord [8,3] to (4,4) is %d not 5", distances["8,3"])
	}
	closest := obj.Closest(4, 4)
	if closest != "3,4" {
		t.Fatalf("Closest to (4,4) is '%s' not '3,4'", closest)
	}
	closest = obj.Closest(3, 6)
	if closest != "" {
		t.Fatalf("Closest to (3,6) is '%s' not ''", closest)
	}
	if obj.IsEdge(4, 4) {
		t.Fatal("isEdge(4,4) should be false not true")
	}
	if !obj.IsEdge(0, 4) {
		t.Fatal("isEdge(0,4) should be true not false")
	}
	obj.CalculateArea()
	if !obj.Coordinates["1,1"].Infinate {
		t.Fatal("Coordinate [1,1] should be infinate")
	}
	if obj.Coordinates["3,4"].Infinate {
		t.Fatal("Coordinate [3,4] should not be infinate")
	}
	area := obj.Coordinates["3,4"].Area
	if area != 9 {
		t.Fatalf("Area of [3,5] is %d not 9", area)
	}
	area = obj.Coordinates["5,5"].Area
	if area != 17 {
		t.Fatalf("Area of [5,5] is %d not 17", area)
	}
	area = obj.LargestArea()
	if area != 17 {
		t.Fatalf("The largest area is %d not 17", area)
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
	if len(obj.Text) != 6 {
		t.Fatalf("len(Text) is %d not 6", len(obj.Text))
	}
	if len(obj.Coordinates) != 6 {
		t.Fatalf("len(Coordinates) is %d not 6", len(obj.Coordinates))
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
	if len(obj.Text) != 6 {
		t.Fatalf("len(Text) is %d not 6", len(obj.Text))
	}
	if len(obj.Coordinates) != 6 {
		t.Fatalf("len(Coordinates) is %d not 6", len(obj.Coordinates))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 32)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  s o l v e r _ t e s t . g o                   end
// ======================================================================
