// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    p a t t e r n _ t e s t . g o
// ======================================================================
// Test Pattern for Advent of Code 2023 day 13, Point Of Incidence

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
var (
	patternText = []string{
		"#.##..##.",
		"..#.##.#.",
		"##......#",
		"##......#",
		"..#.##.#.",
		"..##..##.",
		"#.#.##.#."}
)

// ======================================================================
//                                                            TestPattern
// ======================================================================

// TestPatternEmptyInit ... Test the default Pattern creation
func TestPatternEmptyInit(t *testing.T) {

	// 1. Create default Pattern object
	obj, err := NewPattern(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)
	assert.Equal(t, 0, obj.Reflection)
	assert.Equal(t, (*Pattern)(nil), obj.Rotated)
}

// TestPatternTextInit ... Test the Pattern object creation from text
func TestPatternTextInit(t *testing.T) {

	// 1. Create default Pattern object
	obj, err := NewPattern(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)

	// 3. Add the rest of the text
	for _, line := range patternText {
		obj.AddText(line)
	}
	assert.Len(t, obj.Text, 7)
	assert.Equal(t, 7, obj.Rows)
	assert.Equal(t, 9, obj.Cols)
	assert.Equal(t, 0, obj.Reflection)
	assert.Equal(t, (*Pattern)(nil), obj.Rotated)

	// 4. Get a rotated pattern
	robj := obj.Rotate()
	assert.Len(t, robj.Text, 9)
	assert.Equal(t, 9, robj.Rows)
	assert.Equal(t, 7, robj.Cols)
	assert.Equal(t, 0, robj.Reflection)
	assert.Equal(t, (*Pattern)(nil), robj.Rotated)
	assert.Equal(t, robj, obj.Rotated)

	// 5. Look for the differences
	assert.Equal(t, -1, obj.RowDiff(-1, 0))
	assert.Equal(t, 5, obj.RowDiff(0, 1))
	assert.Equal(t, 7, obj.RowDiff(1, 2))
	assert.Equal(t, 0, obj.RowDiff(2, 3))
	assert.Equal(t, 7, obj.RowDiff(3, 4))
	assert.Equal(t, 4, obj.RowDiff(4, 5))
	assert.Equal(t, 5, obj.RowDiff(5, 6))
	assert.Equal(t, -1, obj.RowDiff(6, 7))
	assert.Equal(t, -1, obj.RowDiff(7, 8))
	assert.Equal(t, 0, obj.RowDiff(1, 4))

	assert.Equal(t, []int{5, 7, 0, 7, 4, 5}, obj.AdjRowDiff())
	assert.Equal(t, 1, obj.ExpRowDiff(2, 3))

	// 6. Reflection points
	assert.Equal(t, -1, obj.FindReflection())
	assert.Equal(t, 5, robj.FindReflection())
	assert.Equal(t, 5, obj.Score())
}

func TestPatternTextInitTwo(t *testing.T) {

	// 1. Create default Pattern object
	obj, err := NewPattern(true, "")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)

	// 3. Add the rest of the text
	for _, line := range patternText {
		obj.AddText(line)
	}
	assert.Len(t, obj.Text, 7)
	assert.Equal(t, 7, obj.Rows)
	assert.Equal(t, 9, obj.Cols)
	assert.Equal(t, 0, obj.Reflection)
	assert.Equal(t, (*Pattern)(nil), obj.Rotated)

	// 4. Reflection point
	assert.Equal(t, 3, obj.FindReflection())
	assert.Equal(t, 3, obj.Score())

}

// ======================================================================
// end                   p a t t e r n _ t e s t. g o                 end
// ======================================================================
