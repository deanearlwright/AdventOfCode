// ======================================================================
// Memory Maneuver
//   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    n o d e _ t e s t . g o
// ======================================================================
// Test Node for Advent of Code 2018 day 08, Memory Maneuver

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"strings"
	"testing"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	NODE_TEXT = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
)

var (
	NODE_SPLIT = strings.Split(NODE_TEXT, " ")
	ZERO_TEXT  = make([]string, 0)
)

// ======================================================================
//                                                               TestNode
// ======================================================================

func TestNodeEmptyInit(t *testing.T) {
	// Test the default Node creation

	// 1. Create default Node object
	obj, indx := NewNode(ZERO_TEXT, 0)

	// 2. Make sure it has the default values
	if obj.numKids != 0 {
		t.Fatalf("Number of Children is %d not 0", obj.numKids)
	}
	if obj.numMeta != 0 {
		t.Fatalf("Number of Metadata is %d not 0", obj.numMeta)
	}
	if indx != 0 {
		t.Fatalf("Index is %d not 0", indx)
	}

	// 3. Check methods
	sum := obj.Sum()
	if sum != 0 {
		t.Fatalf("Sum is %d not 0", sum)
	}
}

func TestNodeTextInit(t *testing.T) {
	// Test the Node object creation from text

	// 1. Create default Node object
	obj, indx := NewNode(NODE_SPLIT, 0)

	// 2. Make sure it has the expected values
	if obj.numKids != 2 {
		t.Fatalf("Number of Children is %d not 2", obj.numKids)
	}
	if obj.numMeta != 3 {
		t.Fatalf("Number of Metadata is %d not 3", obj.numMeta)
	}
	if indx != 16 {
		t.Fatalf("Index is %d not 16", indx)
	}

	// 3. Check methods
	sum := obj.Sum()
	if sum != 4 {
		t.Fatalf("Sum is %d not 4", sum)
	}
	sum = obj.SumAll()
	if sum != 138 {
		t.Fatalf("Total Sum is %d not 138", sum)
	}
	value := obj.Value()
	if value != 66 {
		t.Fatalf("Value is %d not 66", value)
	}
}

// ======================================================================
// end                      n o d e _ t e s t. g o                    end
// ======================================================================
