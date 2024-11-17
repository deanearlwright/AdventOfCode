// ======================================================================
// Hot Springs
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r e c o r d _ t e s t . g o
// ======================================================================
// Test Record for Advent of Code 2023 day 12, Hot Springs

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
	recordText = "???.### 1,1,3"
)

// ======================================================================
//                                                             TestRecord
// ======================================================================

// TestRecordEmptyInit ... Test the default Record creation
func TestRecordEmptyInit(t *testing.T) {

	// 1. Create default Record object
	obj, err := NewRecord(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Row, 0)
	assert.Len(t, obj.Damaged, 0)
}

// TestRecordTextInit ... Test the Record object creation from text
func TestRecordTextInit(t *testing.T) {

	// 1. Create default Record object
	obj, err := NewRecord(false, recordText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(recordText))
	assert.Len(t, obj.Row, 7)
	assert.Len(t, obj.Damaged, 3)

	// 3. Check methods
	seen, err := NewSeen(false)
	assert.NoError(t, err)
	assert.Equal(t, 1, obj.Arrangements(seen, ""))
	assert.Equal(t, 4, obj.Arrangements(seen, ".??..??...?##.. 1,1,3"))
	assert.Equal(t, 1, obj.Arrangements(seen, "?#?#?#?#?#?#?#?. 1,3,1,6"))
	assert.Equal(t, 1, obj.Arrangements(seen, "????.#...#.... 4,1,1"))
	assert.Equal(t, 4, obj.Arrangements(seen, "????.######..#####.. 1,6,5"))
	assert.Equal(t, 10, obj.Arrangements(seen, "?###????????. 3,2,1"))
}

func TestRecordTwoInit(t *testing.T) {

	// 1. Create default Record object
	obj, err := NewRecord(false, recordText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(recordText))
	assert.Len(t, obj.Row, 7)
	assert.Len(t, obj.Damaged, 3)

	// 3. Check methods
	seen, err := NewSeen(true)
	assert.NoError(t, err)
	assert.Equal(t, 1, obj.Arrangements(seen, ""))

	// 4. Checked more arrangements
	obj, err = NewRecord(true, ".??..??...?##. 1,1,3")
	assert.NoError(t, err)
	assert.Equal(t, 16384, obj.Arrangements(seen, ""))
	obj, err = NewRecord(true, "?#?#?#?#?#?#?#? 1,3,1,6")
	assert.NoError(t, err)
	assert.Equal(t, 1, obj.Arrangements(seen, ""))
	obj, err = NewRecord(true, "????.#...#... 4,1,1")
	assert.NoError(t, err)
	assert.Equal(t, 16, obj.Arrangements(seen, ""))
	obj, err = NewRecord(true, "????.######..#####. 1,6,5")
	assert.NoError(t, err)
	assert.Equal(t, 2500, obj.Arrangements(seen, ""))
	obj, err = NewRecord(true, "?###???????? 3,2,1")
	assert.NoError(t, err)
	assert.Equal(t, 506250, obj.Arrangements(seen, ""))
}

func TestRecordTwoInput39(t *testing.T) {
	obj, err := NewRecord(true, "..????????.?? 3,1")
	assert.NoError(t, err)
	seen, err := NewSeen(true)
	assert.NoError(t, err)
	assert.Equal(t, 79921360, obj.Arrangements(seen, ""))
}

func TestRecordTwoInput40(t *testing.T) {
	obj, err := NewRecord(true, "#?????.?????#???. 1,4,6")
	assert.NoError(t, err)
	seen, err := NewSeen(true)
	assert.NoError(t, err)
	assert.Equal(t, 40000, obj.Arrangements(seen, ""))
}

func TestRecordInput41(t *testing.T) {
	obj, err := NewRecord(true, "#.?????.?.?.???? 1,3,2,1")
	assert.NoError(t, err)
	seen, err := NewSeen(true)
	assert.NoError(t, err)
	assert.Equal(t, 3888, obj.Arrangements(seen, ""))
}

func TestRecordInput42(t *testing.T) {
	obj, err := NewRecord(true, "??????#???????????? 1,1,1,5,1,1")
	assert.NoError(t, err)
	seen, err := NewSeen(true)
	assert.NoError(t, err)
	assert.Equal(t, 1485501256595, obj.Arrangements(seen, ""))
}

// ======================================================================
// end                    r e c o r d _ t e s t. g o                  end
// ======================================================================
