// ======================================================================
// Mirage Maintenance
//   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    h i s t o r y _ t e s t . g o
// ======================================================================
// Test History for Advent of Code 2023 day 09, Mirage Maintenance

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
	historyText = "0 3 6 9 12 15"
)

// ======================================================================
//                                                            TestHistory
// ======================================================================

// TestHistoryEmptyInit ... Test the default History creation
func TestHistoryEmptyInit(t *testing.T) {

	// 1. Create default History object
	obj, err := NewHistory(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Values, 0)
}

// TestHistoryTextInit ... Test the History object creation from text
func TestHistoryTextInit(t *testing.T) {

	// 1. Create default History object
	obj, err := NewHistory(false, historyText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(historyText))
	assert.Len(t, obj.Values, 6)

	// 3. Check methods
	assert.Equal(t, []int{3, 3, 3, 3, 3}, Differences(obj.Values))
	assert.False(t, AllZero((obj.Values)))
	assert.False(t, AllZero([]int{3, 3, 3, 3, 3}))
	assert.True(t, AllZero([]int{0, 0, 0, 0}))
	assert.Equal(t, 18, NextValue(obj.Values))
	assert.Equal(t, 18, obj.NextValue())
	assert.Equal(t, 28, NextValue([]int{1, 3, 6, 10, 15, 21}))
	assert.Equal(t, 68, NextValue([]int{10, 13, 16, 21, 30, 45}))
	assert.Equal(t, 114, 18+28+68)

	assert.Equal(t, -3, obj.PrevValue())

}

// ======================================================================
// end                   h i s t o r y _ t e s t. g o                 end
// ======================================================================
