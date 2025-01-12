// ======================================================================
// Lens Library
//   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    h a s h _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 15, Lens Library

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	hashExampleText = `
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
`
	hashPartOneText = hashExampleText
	hashPartTwoText = hashExampleText

	hashPartOneResult = "1320"
	hashPartTwoResult = "145"
)

// ======================================================================
//                                                               TestHash
// ======================================================================

// TestHashEmptyInit ... Test the default Hash creation
func TestHashEmptyInit(t *testing.T) {

	// 1. Create default Hash object
	obj, err := NewHash(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Steps, 0)
	assert.Len(t, obj.Boxes, 256)
}

// TestHashTextInit ... Test the Hash object creation from text
func TestHashTextInit(t *testing.T) {

	// 1. Create Hash object from text
	obj, err := NewHash(false, fromText(hashExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 1)
	assert.Len(t, obj.Steps, 11)
	assert.Len(t, obj.Boxes, 256)

	// 3. Check methods
	assert.Equal(t, 52, hash("HASH"))
	assert.Equal(t, 30, hash("rn=1"))
	assert.Equal(t, 253, hash("cm-"))
	assert.Equal(t, 97, hash("qp=3"))
	assert.Equal(t, 47, hash("cm=2"))

	assert.Equal(t, 1320, obj.SumStepHash())

	assert.Equal(t, 1, obj.ExecuteStep("rn=1"))
	assert.Equal(t, 1, obj.ExecuteStep("cm-"))
	assert.Equal(t, 1, obj.ExecuteStep("qp=3"))
	assert.Equal(t, 2, obj.ExecuteStep("cm=2"))
	assert.Equal(t, 0, obj.ExecuteStep("qp-"))
	assert.Equal(t, 1, obj.ExecuteStep("pc=4"))
	assert.Equal(t, 2, obj.ExecuteStep("ot=9"))
	assert.Equal(t, 3, obj.ExecuteStep("ab=5"))
	assert.Equal(t, 2, obj.ExecuteStep("pc-"))
	assert.Equal(t, 3, obj.ExecuteStep("pc=6"))
	assert.Equal(t, 3, obj.ExecuteStep("ot=7"))

	assert.Equal(t, 5, boxPower(0, obj.Boxes[0]))
	assert.Equal(t, 140, boxPower(3, obj.Boxes[3]))

	assert.Equal(t, 145, obj.Power())
}

// TestHashPartOne ... Test part one example of Hash object
func TestHashPartOne(t *testing.T) {

	// 1. Create Hash object from text
	obj, err := NewHash(false, fromText(hashPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 1)
	assert.Len(t, obj.Steps, 11)
	assert.Len(t, obj.Boxes, 256)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, hashPartOneResult, result)
}

// TestHashPartTwo ... Test part two example of Hash object
func TestHashPartTwo(t *testing.T) {
	// Test part two example of Hash object

	// 1. Create Hash object from text
	obj, err := NewHash(true, fromText(hashPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 1)
	assert.Len(t, obj.Steps, 11)
	assert.Len(t, obj.Boxes, 256)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, hashPartTwoResult, result)
}

// ======================================================================
// end                    h a s h _ t e s t . g o                     end
// ======================================================================
