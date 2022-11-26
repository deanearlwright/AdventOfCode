// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    w o r k e r _ t e s t . g o
// ======================================================================
// Test Worker for Advent of Code 2018 day 07, The Sum of Its Parts

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
	WORKER_TEXT = "1"
)

// ======================================================================
//                                                             TestWorker
// ======================================================================

func TestWorkerEmptyInit(t *testing.T) {
	// Test the default Worker creation

	// 1. Create default Worker object
	obj := NewWorker(false, "")

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
}

func TestWorkerTextInit(t *testing.T) {
	// Test the Worker object creation from text

	// 1. Create default Worker object
	obj := NewWorker(false, WORKER_TEXT)

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(WORKER_TEXT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(WORKER_TEXT))
	}
}

// ======================================================================
// end                  w o r k e r _ t e s t. g o                end
// ======================================================================
