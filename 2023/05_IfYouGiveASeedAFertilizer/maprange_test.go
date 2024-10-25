// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    m a p r a n g e _ t e s t . g o
// ======================================================================
// Test Maprange for Advent of Code 2023 day 05, IfYouGiveASeedAFertilizer

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
	maprangeText = "50 98 2"
)

// ======================================================================
//                                                           TestMaprange
// ======================================================================

func TestMaprangeEmptyInit(t *testing.T) {
	// Test the default Maprange creation

	// 1. Create default Maprange object
	obj, err := NewMaprange(false, "")
	assert.Nil(t, obj)
	assert.Error(t, err)
}

func TestMaprangeTextInit(t *testing.T) {
	// Test the Maprange object creation from text

	// 1. Create default Maprange object
	obj, err := NewMaprange(false, maprangeText)
	assert.NotNil(t, obj)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 7)
	assert.Equal(t, 50, obj.DestStart)
	assert.Equal(t, 98, obj.SourceStart)
	assert.Equal(t, 2, obj.RangeLength)

	// 3. Check methods
	assert.False(t, obj.IsInDestinationRange(49))
	assert.True(t, obj.IsInDestinationRange(50))
	assert.True(t, obj.IsInDestinationRange(51))
	assert.False(t, obj.IsInDestinationRange(52))

	assert.False(t, obj.IsInSourceRange(97))
	assert.True(t, obj.IsInSourceRange(98))
	assert.True(t, obj.IsInSourceRange(99))
	assert.False(t, obj.IsInSourceRange(100))

	assert.Equal(t, 97, obj.MapSourceToDest(97))
	assert.Equal(t, 50, obj.MapSourceToDest(98))
	assert.Equal(t, 51, obj.MapSourceToDest(99))
	assert.Equal(t, 100, obj.MapSourceToDest(100))
}

// ======================================================================
// end                  m a p r a n g e _ t e s t. g o                end
// ======================================================================
