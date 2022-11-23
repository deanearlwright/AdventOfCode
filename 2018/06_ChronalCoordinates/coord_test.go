// ======================================================================
// Chronal Coordinates
//   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c o o r d _ t e s t . g o
// ======================================================================
// Test Coord for Advent of Code 2018 day 06, Chronal Coordinates

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
	COORD_TEXT = "8, 3"
)

// ======================================================================
//                                                              TestCoord
// ======================================================================

func TestCoordEmptyInit(t *testing.T) {
	// Test the default Coord creation

	// 1. Create default Coord object
	obj, err := NewCoord(false, "")

	// 2. Make sure there was no Coord created
	if err == nil {
		t.Fatal("There should have been an error creating Coord from ''")
	}
	if obj != nil {
		t.Fatal("There should have been no Coord created from ''")
	}
}

func TestCoordTextInit(t *testing.T) {
	// Test the Coord object creation from text

	// 1. Create default Coord object
	obj, err := NewCoord(false, COORD_TEXT)

	// 2. Make sure that the Coord was created
	if err != nil {
		t.Fatalf("There should be no error creating Coord from text not %s", err)
	}
	if obj == nil {
		t.Fatal("There should have been a Coord created from text")
	}

	// 3. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(COORD_TEXT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(COORD_TEXT))
	}
	if obj.Col != 8 {

		t.Fatalf("Col is %d not 8", obj.Col)
	}
	if obj.Row != 3 {
		t.Fatalf("Row is %d not 3", obj.Row)
	}
	if obj.Key != "8,3" {
		t.Fatalf("Key is '%s' not '8,3'", obj.Key)
	}
	num := obj.Distance(8, 3)
	if num != 0 {
		t.Fatalf("Distance(8, 3) is %d not 0", num)
	}
	num = obj.Distance(9, 2)
	if num != 2 {
		t.Fatalf("Distance(9, 2) is %d not 2", num)
	}
	num = obj.Distance(7, 5)
	if num != 3 {
		t.Fatalf("Distance(7, 5) is %d not 3", num)
	}
}

// ======================================================================
// end                     c o o r d _ t e s t. g o                   end
// ======================================================================
