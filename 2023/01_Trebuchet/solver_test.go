// ======================================================================
// Trebuchet
//   Advent of Code 2023 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s o l v e r _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 01, Trebuchet

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
	EXAMPLE_TEXT = `
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
`
	PART_ONE_TEXT = EXAMPLE_TEXT
	PART_TWO_TEXT = `
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
`

	PART_ONE_RESULT = "142"
	PART_TWO_RESULT = "281"
)

// ======================================================================
//                                                             TestSolver
// ======================================================================

func TestSolverEmptyInit(t *testing.T) {
	// Test the default Solver creation

	// 1. Create default Solver object
	solver := NewSolver(false, fromText(""))

	// 2. Make sure it has the default values
	assert.False(t, solver.Part2)
	assert.Len(t, solver.Text, 0)
	assert.Len(t, solver.First, 0)
	assert.Len(t, solver.Last, 0)
}

func TestSolverTextInit(t *testing.T) {
	// Test the Solver object creation from text

	// 1. Create Solver object from text
	solver := NewSolver(false, fromText(EXAMPLE_TEXT))

	// 2. Make sure it has the expected values
	assert.False(t, solver.Part2)
	assert.Equal(t, len(solver.First), len(solver.Text))
	assert.Equal(t, len(solver.Last), len(solver.Text))

	// 3. Check the numbers
	assert.Equal(t, []int{1, 3, 1, 7}, solver.First)
	assert.Equal(t, []int{2, 8, 5, 7}, solver.Last)
}

func TestSolverPartOne(t *testing.T) {
	// Test part one example of Solver object

	// 1. Create Solver object from text
	solver := NewSolver(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	assert.False(t, solver.Part2)
	assert.Equal(t, len(solver.First), len(solver.Text))
	assert.Equal(t, len(solver.Last), len(solver.Text))
	assert.Equal(t, []int{1, 3, 1, 7}, solver.First)
	assert.Equal(t, []int{2, 8, 5, 7}, solver.Last)

	// 3. Make sure it returns the expected solution
	result := solver.PartOne(false, 0)
	assert.Equal(t, PART_ONE_RESULT, result)
}

func TestSolverPartTwo(t *testing.T) {
	// Test part two example of Solver object

	// 1. Create Solver object from text
	solver := NewSolver(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	assert.True(t, solver.Part2)
	assert.Equal(t, len(solver.First), len(solver.Text))
	assert.Equal(t, len(solver.Last), len(solver.Text))
	assert.Equal(t, []int{2, 8, 1, 2, 4, 1, 7}, solver.First)
	assert.Equal(t, []int{9, 3, 3, 4, 2, 4, 6}, solver.Last)

	// 3. Make sure it returns the expected solution
	result := solver.PartTwo(false, 0)
	assert.Equal(t, PART_TWO_RESULT, result)
}

// ======================================================================
// end                  s o l v e r _ t e s t . g o                   end
// ======================================================================
