// ======================================================================
// Cosmic Expansion
//   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    i m a g e _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 11, Cosmic Expansion

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
	imageExampleText = `...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
`
	imagePartOneText = imageExampleText
	imagePartTwoText = ""

	imagePartOneResult = "374"
	imagePartTwoResult = ""
)

// ======================================================================
//                                                              TestImage
// ======================================================================

// TestImageEmptyInit ... Test the default Image creation
func TestImageEmptyInit(t *testing.T) {

	// 1. Create default Image object
	obj, err := NewImage(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Galaxies, 0)
}

// TestImageTextInit ... Test the Image object creation from text
func TestImageTextInit(t *testing.T) {

	// 1. Create Image object from text
	obj, err := NewImage(false, fromText(imageExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Len(t, obj.Galaxies, 9)

	// 3. Check methods
	assert.Equal(t, int64(5), obj.Galaxies[7].DistanceAll(obj.Galaxies[8:]))
	assert.Equal(t, int64(15), obj.Galaxies[6].DistanceAll(obj.Galaxies[7:]))
	assert.Equal(t, int64(33), obj.Galaxies[5].DistanceAll(obj.Galaxies[6:]))
	assert.Equal(t, int64(39), obj.Galaxies[4].DistanceAll(obj.Galaxies[5:]))
	assert.Equal(t, int64(43), obj.Galaxies[3].DistanceAll(obj.Galaxies[4:]))
	assert.Equal(t, int64(73), obj.Galaxies[2].DistanceAll(obj.Galaxies[3:]))
	assert.Equal(t, int64(79), obj.Galaxies[1].DistanceAll(obj.Galaxies[2:]))
	assert.Equal(t, int64(87), obj.Galaxies[0].DistanceAll(obj.Galaxies[1:]))
	assert.Equal(t, int64(374), obj.DistanceAll())

}

// TestImagePartOne ... Test part one example of Image object
func TestImagePartOne(t *testing.T) {

	// 1. Create Image object from text
	obj, err := NewImage(false, fromText(imagePartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Len(t, obj.Galaxies, 9)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, imagePartOneResult, result)
}

// TestImagePartTwo ... Test part two example of Image object
func TestImagePartTwo(t *testing.T) {
	// Test part two example of Image object

	// 1. Create Image object from text
	obj, err := NewImage(true, fromText(imagePartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Len(t, obj.Galaxies, 9)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, imagePartTwoResult, result)
}

// ======================================================================
// end                   i m a g e _ t e s t . g o                    end
// ======================================================================
