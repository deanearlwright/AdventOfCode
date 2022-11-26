// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s t e p _ t e s t . g o
// ======================================================================
// Test Step for Advent of Code 2018 day 07, The Sum of Its Parts

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
	STEP_TEXT = "Step C must be finished before step A can begin."
)

// ======================================================================
//                                                             TestStep
// ======================================================================

func TestStepEmptyInit(t *testing.T) {
	// Test the default Step creation

	// 1. Attempt to create a default Step object
	obj := NewStep(false, "")

	// 2. Make sure it has the default values
	if obj != nil {
		t.Fatal("Default Step should not have been created")
	}
}

func TestStepTextInit(t *testing.T) {
	// Test the Step object creation from text

	// 1. Create default Step object
	obj := NewStep(false, STEP_TEXT)

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(STEP_TEXT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(STEP_TEXT))
	}
	if obj.Letter != "A" {
		t.Fatalf("Letter is '%s' not 'A'", obj.Letter)
	}
	value, found := obj.Before["C"]
	if !found {

		t.Fatalf("Step C should be before A")
	}
	if !value {
		t.Fatalf("A.before[C] should be true")
	}
	if obj.Completed {
		t.Fatalf("A should not yet be completed")
	}
	if obj.Cost != 1 {
		t.Fatalf("Cost is %d not 1", obj.Cost)
	}

	// 3. Check methods
	obj.IncreaseCost(60)
	if obj.Cost != 61 {
		t.Fatalf("New Cost is %d not 61", obj.Cost)
	}
}

// ======================================================================
// end                  s t e p _ t e s t. g o                end
// ======================================================================
