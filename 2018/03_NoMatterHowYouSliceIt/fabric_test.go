// ======================================================================
// No Matter How You Slice It
//   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    f a b r i c _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 03, No Matter How You Slice It

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
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
`
	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = EXAMPLE_TEXT

	PART_ONE_RESULT = "4"
	PART_TWO_RESULT = "3"
)

// ======================================================================
//                                                              TestFabric
// ======================================================================

func TestFabricEmptyInit(t *testing.T) {
	// Test the default Fabric creation

	// 1. Create default Fabric object
	obj := NewFabric(false, fromText(""))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
	if len(obj.Claims) != 0 {
		t.Fatal("There should be no Claims")
	}
}

func TestFabricTextInit(t *testing.T) {
	// Test the Fabric object creation from text

	// 1. Create Fabric object from text
	obj := NewFabric(false, fromText(EXAMPLE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 3 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 3)
	}
	if len(obj.Claims) != 3 {
		t.Fatalf("len(Claims) is %d not %d",
			len(obj.Claims), 3)
	}

	// 3. Check the claims
	if (obj.Claims[0]).Number != 1 {
		t.Fatalf("First Claim's Number is is %d not %d",
			(obj.Claims[0]).Number, 3)

	}
}

func TestFabricPartOne(t *testing.T) {
	// Test part one example of Fabric object

	// 1. Create Fabric object from text
	obj := NewFabric(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 3 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 3)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	if result != PART_ONE_RESULT {
		t.Fatalf("PartOne returned '%s' not '%s'", result, PART_ONE_RESULT)
	}
}

func TestFabricPartTwo(t *testing.T) {
	// Test part two example of Fabric object

	// 1. Create Fabric object from text
	obj := NewFabric(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	if !obj.Part2 {
		t.Fatal("Part2 should be true")
	}
	if len(obj.Text) != 3 {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), 3)
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  f a b r i c _ t e s t . g o                   end
// ======================================================================
