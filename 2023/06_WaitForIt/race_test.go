// ======================================================================
// Wait For It
//   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r a c e _ t e s t . g o
// ======================================================================
// Test Race for Advent of Code 2023 day 06, Wait For It

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
	raceText = "7 9"
)

// ======================================================================
//                                                               TestRace
// ======================================================================

// TestRaceEmptyInit ... Test the default Race creation
func TestRaceEmptyInit(t *testing.T) {

	// 1. Create default Race object
	obj, err := NewRace(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, obj.Time, 0)
	assert.Equal(t, obj.Record, 0)
}

// TestRaceTextInit ... Test the Race object creation from text
func TestRaceTextInit(t *testing.T) {

	// 1. Create default Race object
	obj, err := NewRace(false, raceText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(raceText))
	assert.Equal(t, obj.Time, 7)
	assert.Equal(t, obj.Record, 9)

	// 3. Check the methods
	assert.False(t, obj.DoesItBeat(0))
	assert.False(t, obj.DoesItBeat(1))
	assert.True(t, obj.DoesItBeat(2))
	assert.True(t, obj.DoesItBeat(3))
	assert.True(t, obj.DoesItBeat(4))
	assert.True(t, obj.DoesItBeat(5))
	assert.False(t, obj.DoesItBeat(6))
	assert.False(t, obj.DoesItBeat(7))
	assert.False(t, obj.DoesItBeat(8))
	assert.False(t, obj.DoesItBeat(9))
	assert.False(t, obj.DoesItBeat(10))

	minHT, maxHT := obj.MinMaxHoldTimes()
	assert.Equal(t, 2, minHT)
	assert.Equal(t, 5, maxHT)

	assert.Equal(t, 4, obj.WaysToBeatRecord())
}

// TestRaceTextOther ... Test the Race object creation from text also
func TestRaceTextOther(t *testing.T) {

	// 1. Create default Race object
	obj, err := NewRace(false, "30 200")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), 6)
	assert.Equal(t, obj.Time, 30)
	assert.Equal(t, obj.Record, 200)

	// 3. Check the methods
	assert.False(t, obj.DoesItBeat(0))
	assert.False(t, obj.DoesItBeat(10))
	assert.True(t, obj.DoesItBeat(11))
	assert.True(t, obj.DoesItBeat(12))
	assert.True(t, obj.DoesItBeat(18))
	assert.True(t, obj.DoesItBeat(19))
	assert.False(t, obj.DoesItBeat(20))
	assert.False(t, obj.DoesItBeat(21))
	assert.False(t, obj.DoesItBeat(30))
	assert.False(t, obj.DoesItBeat(31))

	minHT, maxHT := obj.MinMaxHoldTimes()
	assert.Equal(t, 11, minHT)
	assert.Equal(t, 19, maxHT)

	assert.Equal(t, 9, obj.WaysToBeatRecord())
}

// ======================================================================
// end                      r a c e _ t e s t. g o                    end
// ======================================================================
