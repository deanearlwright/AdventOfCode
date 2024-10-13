// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
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
	solverExampleText = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
`
	solverPartOneText = solverExampleText
	solverPartTwoText = solverExampleText

	solverPartOneResult = "8"
	solverPartTwoResult = "2286"
)

// ======================================================================
//                                                              TestSolver
// ======================================================================

func TestSolverEmptyInit(t *testing.T) {
	// Test the default Solver creation

	// 1. Create default Solver object
	obj, err := NewSolver(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Games, 0)
}

func TestSolverTextInit(t *testing.T) {
	// Test the Solver object creation from text

	// 1. Create Solver object from text
	obj, err := NewSolver(false, fromText(solverExampleText))
	assert.NoError(t, err)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Games, 5)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
}

func TestSolverPartOne(t *testing.T) {
	// Test part one example of Solver object

	// 1. Create Solver object from text
	obj, err := NewSolver(false, fromText(solverPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, solverPartOneResult, result)
}

func TestSolverPartTwo(t *testing.T) {
	// Test part two example of Solver object

	// 1. Create Solver object from text
	obj, err := NewSolver(true, fromText(solverPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, solverPartTwoResult, result)
}

// ======================================================================
// end                  s o l v e r _ t e s t . g o                   end
// ======================================================================
