// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    p i p e m a z e _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 10, Pipe Maze

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
	pipemazeExampleText1 = `-L|F7
7S-7|
L|7||
-L-J|
L|-JF
`
	pipemazeExampleText2 = `7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
`
	pipemazeExampleText3 = `...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........`

	pipemazeExampleText4 = `.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...`

	pipemazePartOneText = pipemazeExampleText2
	pipemazePartTwoText = pipemazeExampleText4

	pipemazePartOneResult = "8"
	pipemazePartTwoResult = "8"
)

// ======================================================================
//                                                           TestPipemaze
// ======================================================================

// TestPipemazeEmptyInit ... Test the default Pipemaze creation
func TestPipemazeEmptyInit(t *testing.T) {

	// 1. Create default Pipemaze object
	obj, err := NewPipemaze(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Nil(t, obj.Start)
}

// TestPipemazeTextInit ... Test the Pipemaze object creation from text
func TestPipemazeTextInit(t *testing.T) {

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(false, fromText(pipemazeExampleText1))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.NotNil(t, obj.Start)
	assert.Equal(t, 1, obj.Start.Row)
	assert.Equal(t, 1, obj.Start.Col)

	// 3. Check methods
	assert.Equal(t, startChar, obj.At(1, 1))
	assert.Equal(t, 'L', obj.At(4, 0))
	assert.Equal(t, 4, obj.Furthest())
	assert.Equal(t, 0, obj.CountGround())
	obj.OnlyLoop()
	assert.Equal(t, 17, obj.CountGround())
	assert.Equal(t, 1, obj.CountInsideGround())
}

// TestPipemazeTextInitTwo ... Test the Pipemaze object creation from second example
func TestPipemazeTextInitTwo(t *testing.T) {

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(false, fromText(pipemazeExampleText2))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.NotNil(t, obj.Start)
	assert.Equal(t, 2, obj.Start.Row)
	assert.Equal(t, 0, obj.Start.Col)

	// 3. Check methods
	assert.Equal(t, startChar, obj.At(2, 0))
	assert.Equal(t, 'L', obj.At(4, 0))
	assert.Equal(t, 8, obj.Furthest())
	assert.Equal(t, 2, obj.CountGround())
	obj.OnlyLoop()
	assert.Equal(t, 9, obj.CountGround())
	assert.Equal(t, 1, obj.CountInsideGround())
}

// TestPipemazeTextInitThree ... Test the Pipemaze object creation from third example
func TestPipemazeTextInitThree(t *testing.T) {

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(false, fromText(pipemazeExampleText3))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 9)
	assert.NotNil(t, obj.Start)
	assert.Equal(t, 1, obj.Start.Row)
	assert.Equal(t, 1, obj.Start.Col)

	// 3. Check methods
	assert.Equal(t, startChar, obj.At(1, 1))
	assert.Equal(t, '.', obj.At(3, 3))
	assert.Equal(t, 23, obj.Furthest())
	assert.Equal(t, 53, obj.CountGround())
	obj.OnlyLoop()
	assert.Equal(t, 53, obj.CountGround())
	assert.Equal(t, 4, obj.CountInsideGround())
}

// TestPipemazeTextInitFour ... Test the Pipemaze object creation from fourth example
func TestPipemazeTextInitFour(t *testing.T) {

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(false, fromText(pipemazeExampleText4))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.NotNil(t, obj.Start)
	assert.Equal(t, 4, obj.Start.Row)
	assert.Equal(t, 12, obj.Start.Col)

	// 3. Check methods
	assert.Equal(t, startChar, obj.At(4, 12))
	assert.Equal(t, '.', obj.At(3, 14))
	assert.Equal(t, 70, obj.Furthest())
	assert.Equal(t, 60, obj.CountGround())
	obj.OnlyLoop()
	assert.Equal(t, 60, obj.CountGround())
	assert.Equal(t, 8, obj.CountInsideGround())
}

// TestPipemazePartOne ... Test part one example of Pipemaze object
func TestPipemazePartOne(t *testing.T) {

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(false, fromText(pipemazePartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.NotNil(t, obj.Start)
	assert.Equal(t, 2, obj.Start.Row)
	assert.Equal(t, 0, obj.Start.Col)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, pipemazePartOneResult, result)
}

// TestPipemazePartTwo ... Test part two example of Pipemaze object
func TestPipemazePartTwo(t *testing.T) {
	// Test part two example of Pipemaze object

	// 1. Create Pipemaze object from text
	obj, err := NewPipemaze(true, fromText(pipemazePartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.NotNil(t, obj.Start)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, pipemazePartTwoResult, result)
}

// ======================================================================
// end                p i p e m a z e _ t e s t . g o                 end
// ======================================================================
