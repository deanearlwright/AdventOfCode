// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    w o r k e r s _ t e s t . g o
// ======================================================================
// Test Workers for Advent of Code 2018 day 07, The Sum of Its Parts

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
	WORKERS_TEXT = "2"
)

// ======================================================================
//                                                            TestWorkers
// ======================================================================

func TestWorkersEmptyInit(t *testing.T) {
	// Test the default Workers creation

	// 1. Create default Workers object
	obj := NewWorkers(false, "")

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
	if len(obj.Workers) != 0 {
		t.Fatal("There should be no Workers")
	}
}

func TestWorkersTextInit(t *testing.T) {
	// Test the Workers object creation from text

	// 1. Create default Workers object
	obj := NewWorkers(false, WORKERS_TEXT)

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(WORKERS_TEXT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(WORKERS_TEXT))
	}
	if len(obj.Workers) != 2 {
		t.Fatalf("There are %d workers not 2", len(obj.Workers))
	}

	// 3. Check methods
	display := obj.Display()
	if display != ". ." {
		t.Fatalf("Workers display as '%s' not '. .", display)
	}
}

// ======================================================================
// end                   w o r k e r s _ t e s t. g o                 end
// ======================================================================
