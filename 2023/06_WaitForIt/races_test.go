// ======================================================================
// Wait For It
//   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r a c e s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 06, Wait For It

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
	racesExampleText = `Time:      7  15   30
Distance:  9  40  200
`
	racesPartOneText = racesExampleText
	racesPartTwoText = racesExampleText

	racesPartOneResult = "288"
	racesPartTwoResult = "71503"
)

// ======================================================================
//                                                              TestRaces
// ======================================================================

// TestRacesEmptyInit ... Test the default Races creation
func TestRacesEmptyInit(t *testing.T) {

	// 1. Create default Races object
	obj, err := NewRaces(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Races, 0)
}

// TestRacesTextInit ... Test the Races object creation from text
func TestRacesTextInit(t *testing.T) {

	// 1. Create Races object from text
	obj, err := NewRaces(false, fromText(racesExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 2)
	assert.Len(t, obj.Races, 3)
}

// TestRacesPartOne ... Test part one example of Races object
func TestRacesPartOne(t *testing.T) {

	// 1. Create Races object from text
	obj, err := NewRaces(false, fromText(racesPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 2)
	assert.Len(t, obj.Races, 3)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, racesPartOneResult, result)
}

// TestRacesPartTwo ... Test part two example of Races object
func TestRacesPartTwo(t *testing.T) {
	// Test part two example of Races object

	// 1. Create Races object from text
	obj, err := NewRaces(true, fromText(racesPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 2)
	assert.Len(t, obj.Races, 1)
	assert.Equal(t, 71530, obj.Races[0].Time)
	assert.Equal(t, 940200, obj.Races[0].Record)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, racesPartTwoResult, result)
}

// ======================================================================
// end                   r a c e s _ t e s t . g o                    end
// ======================================================================
