// ======================================================================
// Hot Springs
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r e c o r d s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 12, Hot Springs

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
	recordsExampleText = `???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
`
	recordsPartOneText = recordsExampleText
	recordsPartTwoText = recordsExampleText

	recordsPartOneResult = "21"
	recordsPartTwoResult = "525152"
)

// ======================================================================
//                                                            TestRecords
// ======================================================================

// TestRecordsEmptyInit ... Test the default Records creation
func TestRecordsEmptyInit(t *testing.T) {

	// 1. Create default Records object
	obj, err := NewRecords(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Records, 0)
}

// TestRecordsTextInit ... Test the Records object creation from text
func TestRecordsTextInit(t *testing.T) {

	// 1. Create Records object from text
	obj, err := NewRecords(false, fromText(recordsExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Records, 6)
}

// TestRecordsPartOne ... Test part one example of Records object
func TestRecordsPartOne(t *testing.T) {

	// 1. Create Records object from text
	obj, err := NewRecords(false, fromText(recordsPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Records, 6)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, recordsPartOneResult, result)
}

// TestRecordsPartTwo ... Test part two example of Records object
func TestRecordsPartTwo(t *testing.T) {
	// Test part two example of Records object

	// 1. Create Records object from text
	obj, err := NewRecords(true, fromText(recordsPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Records, 6)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, recordsPartTwoResult, result)
}

// ======================================================================
// end                 r e c o r d s _ t e s t . g o                  end
// ======================================================================
