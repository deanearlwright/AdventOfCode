// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    g a m e _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 02, Cube Conundrum

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
	gameExampleText = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

	gamePartOneText = gameExampleText
	gamePartTwoText = gameExampleText

	gamePartOneResult = 1
	gamePartTwoResult = 48
)

// ======================================================================
//                                                               TestGame
// ======================================================================

func TestGameEmptyInit(t *testing.T) {
	// Test the default Game creation

	// 1. Create default Game object
	obj, err := NewGame(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, obj.ID, 0)
	assert.Len(t, obj.Draws, 0)
}

func TestGameTextInit(t *testing.T) {
	// Test the Game object creation from text

	// 1. Create Game object from text
	obj, err := NewGame(false, gameExampleText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 54)
	assert.Equal(t, obj.ID, 1)
	assert.Len(t, obj.Draws, 3)
	assert.Equal(t, obj.Draws[0].Count("red"), 4)
	assert.Equal(t, obj.Draws[0].Count("blue"), 3)
}

func TestGamePartOne(t *testing.T) {
	// Test part one example of Game object

	// 1. Create Game object from text
	obj, err := NewGame(false, gamePartOneText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 54)
	assert.Equal(t, obj.ID, 1)
	assert.Len(t, obj.Draws, 3)
	assert.Equal(t, obj.Draws[0].Count("red"), 4)
	assert.Equal(t, obj.Draws[0].Count("blue"), 3)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, gamePartOneResult, result)
}

func TestGamePartTwo(t *testing.T) {
	// Test part two example of Game object

	// 1. Create Game object from text
	obj, err := NewGame(true, gamePartTwoText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 54)
	assert.Equal(t, obj.ID, 1)
	assert.Len(t, obj.Draws, 3)
	assert.Equal(t, obj.Draws[0].Count("red"), 4)
	assert.Equal(t, obj.Draws[0].Count("blue"), 3)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, gamePartTwoResult, result)
}

// ======================================================================
// end                    g a m e _ t e s t . g o                     end
// ======================================================================
