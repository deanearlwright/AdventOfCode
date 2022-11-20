// ======================================================================
// No Matter How You Slice It
//   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c l a i m _ t e s t . g o
// ======================================================================
// Test Claim for Advent of Code 2018 day 03, No Matter How You Slice It

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
	CLAIM_TEXT = "#1 @ 3,2: 4x5"
	CLAIM_ONE  = "#1 @ 1,3: 4x4"
	CLAIM_TWO  = "#2 @ 3,1: 4x4"
	CLAIM_TRI  = "#3 @ 5,5: 2x2"
)

// ======================================================================
//                                                             TestClaim
// ======================================================================

func TestClaimEmptyInit(t *testing.T) {
	// Test the default Claim creation

	// 1. Create default Claim object
	obj := NewClaim(false, "")

	// 2. Make sure it could not be built
	if obj != nil {
		t.Fatal("NewClaim(false, '') should have failedPart2 should be false")
	}
}

func TestClaimTextInit(t *testing.T) {
	// Test the Claim object creation from text

	// 1. Create default Claim object
	obj := NewClaim(false, CLAIM_TEXT)

	// 2. Make sure it has the default values
	if obj.Part2 != false {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(CLAIM_TEXT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(CLAIM_TEXT))
	}
	if obj.Conflict {
		t.Fatal("There should be no Conflict")
	}
	if obj.Number != 1 {
		t.Fatalf("Number should be %d not %d", 1, obj.Number)
	}
	if obj.Left != 3 {
		t.Fatalf("Left should be %d not %d", 3, obj.Left)
	}
	if obj.Top != 2 {
		t.Fatalf("Top should be %d not %d", 2, obj.Top)
	}
	if obj.Width != 4 {
		t.Fatalf("Width should be %d not %d", 4, obj.Width)
	}
	if obj.Height != 5 {
		t.Fatalf("Height should be %d not %d", 5, obj.Height)
	}
	if obj.Right != 6 {
		t.Fatalf("Right should be %d not %d", 6, obj.Right)
	}
	if obj.Bottom != 6 {
		t.Fatalf("Bottom should be %d not %d", 6, obj.Bottom)
	}
}

func TestClaimOverlap(t *testing.T) {
	// Test the Claim object overlap

	// 1. Create the claims
	claim_one := NewClaim(false, CLAIM_ONE)
	claim_two := NewClaim(false, CLAIM_TWO)
	claim_tri := NewClaim(false, CLAIM_TRI)

	// 2. Look at self overlaps
	overlap := (claim_one).Overlap(claim_one)
	if len(overlap) != 16 {
		t.Fatalf("Overlap 1x1 should be %d not %d",
			16, len(overlap))
	}
	overlap = (claim_two).Overlap(claim_two)
	if len(overlap) != 16 {
		t.Fatalf("Overlap 2x2 should be %d not %d",
			16, len(overlap))
	}
	overlap = (claim_tri).Overlap(claim_tri)
	if len(overlap) != 4 {
		t.Fatalf("Overlap 3x3 should be %d not %d",
			16, len(overlap))
	}

	// 3. Look at cross overlaps
	overlap = (claim_one).Overlap(claim_two)
	if len(overlap) != 4 {
		t.Fatalf("Overlap 1x2 should be %d not %d",
			4, len(overlap))
	}
	overlap = (claim_two).Overlap(claim_one)
	if len(overlap) != 4 {
		t.Fatalf("Overlap 2x1 should be %d not %d",
			4, len(overlap))
	}
	overlap = (claim_one).Overlap(claim_tri)
	if len(overlap) != 0 {
		t.Fatalf("Overlap 1x3 should be %d not %d",
			0, len(overlap))
	}
	overlap = (claim_two).Overlap(claim_tri)
	if len(overlap) != 0 {
		t.Fatalf("Overlap 2x3 should be %d not %d",
			0, len(overlap))
	}
	overlap = (claim_tri).Overlap(claim_one)
	if len(overlap) != 0 {
		t.Fatalf("Overlap 3x1 should be %d not %d",
			0, len(overlap))
	}
	overlap = (claim_tri).Overlap(claim_two)
	if len(overlap) != 0 {
		t.Fatalf("Overlap 3x2 should be %d not %d",
			0, len(overlap))
	}
}

// ======================================================================
// end                    c l a i m _ t e s t. g o                    end
// ======================================================================
