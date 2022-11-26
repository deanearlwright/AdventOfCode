// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s t e p s _ t e s t . g o
// ======================================================================
// Test Steps for Advent of Code 2018 day 07, The Sum of Its Parts

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
	STEPS_TEXT = `
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
`
	NO_STEPS = `
`
)

// ======================================================================
//                                                              TestSteps
// ======================================================================

func TestStepsEmptyInit(t *testing.T) {
	// Test the default Steps creation

	// 1. Create default Steps object
	obj := NewSteps(false, fromText(NO_STEPS))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
}

func TestStepsTextInit(t *testing.T) {
	// Test the Steps object creation from text

	// 1. Create default Steps object
	obj := NewSteps(false, fromText(STEPS_TEXT))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 7 {
		t.Fatalf("len(Text) is %d not 7", len(obj.Text))
	}
	if len(obj.Steps) != 6 {
		t.Fatalf("len(Steps) is %d not 6", len(obj.Steps))
	}
	if obj.Letters != "ABCDEF" {
		t.Fatalf("Letters is '%s' not 'ABCDEF'", obj.Letters)
	}
	if obj.Initial != "C" {
		t.Fatalf("Initial is '%s' not 'C'", obj.Initial)
	}
	if obj.Final != "E" {
		t.Fatalf("Final is '%s' not 'E'", obj.Final)
	}

}

// ======================================================================
// end                     s t e p s _ t e s t. g o                   end
// ======================================================================
