// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r a n g e _ t e s t . g o
// ======================================================================
// Test Range for Advent of Code 2023 day 19, Aplenty

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
	rangeText = "1000:3000"
)

// ======================================================================
//                                                              TestRange
// ======================================================================

// TestRangeEmptyInit ... Test the default Range creation
func TestRangeEmptyInit(t *testing.T) {

	// 1. Create default Range object
	obj, err := NewRange(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 1, obj.Min)
	assert.Equal(t, 4000, obj.Max)
}

// TestRangeTextInit ... Test the Range object creation from text
func TestRangeTextInit(t *testing.T) {

	// 1. Create default Range object
	obj, err := NewRange(false, rangeText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(rangeText))
	assert.Equal(t, 1000, obj.Min)
	assert.Equal(t, 3000, obj.Max)

	// 3. Check methods
	assert.True(t, obj.CheckValue(2000))
	assert.True(t, obj.CheckValue(1000))
	assert.True(t, obj.CheckValue(3000))
	assert.False(t, obj.CheckValue(500))
	assert.False(t, obj.CheckValue(999))
	assert.False(t, obj.CheckValue(3001))

	assert.Equal(t, 2001, obj.Combinations())
}

// TestRangeMerge ... Test the Range object Pass and Fail
func TestRangeMerge(t *testing.T) {

	// 1. Create default Range object
	obj, err := NewRange(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 1, obj.Min)
	assert.Equal(t, 4000, obj.Max)

	// 3. Create more Range Objects
	objless3000, err := NewRange(false, "<3000")
	assert.NoError(t, err)
	assert.Equal(t, 1, objless3000.Min)
	assert.Equal(t, 2999, objless3000.Max)
	objmore1000, err := NewRange(false, ">1000")
	assert.NoError(t, err)
	assert.Equal(t, 1001, objmore1000.Min)
	assert.Equal(t, 4000, objmore1000.Max)

	// 4. Check Invert method
	invless3000 := objless3000.Invert()
	assert.NoError(t, err)
	assert.Equal(t, 3000, invless3000.Min)
	assert.Equal(t, 4000, invless3000.Max)
	invmore1000 := objmore1000.Invert()
	assert.NoError(t, err)
	assert.Equal(t, 1, invmore1000.Min)
	assert.Equal(t, 1000, invmore1000.Max)

	// 5. Check Less and More methods
	objlessPass := obj.Clone()
	assert.Equal(t, 1, objlessPass.Min)
	assert.Equal(t, 4000, objlessPass.Max)
	objlessFail := obj.Clone()
	objmorePass := obj.Clone()
	objmoreFail := obj.Clone()

	objlessPass.Pass(objless3000)
	objlessFail.Fail(objless3000)
	objmorePass.Pass(objmore1000)
	objmoreFail.Fail(objmore1000)

	assert.Equal(t, 1, objlessPass.Min)
	assert.Equal(t, 2999, objlessPass.Max)
	assert.Equal(t, 1001, objmorePass.Min)
	assert.Equal(t, 4000, objmorePass.Max)

	assert.Equal(t, 3000, objlessFail.Min)
	assert.Equal(t, 4000, objlessFail.Max)
	assert.Equal(t, 1, objmoreFail.Min)
	assert.Equal(t, 1000, objmoreFail.Max)
}

// ======================================================================
// end                     r a n g e _ t e s t. g o                   end
// ======================================================================
