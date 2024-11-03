// ======================================================================
// Mirage Maintenance
//   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r e p o r t _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 09, Mirage Maintenance

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
	reportExampleText = `0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45`
	reportPartOneText = reportExampleText
	reportPartTwoText = reportExampleText

	reportPartOneResult = "114"
	reportPartTwoResult = "2"
)

// ======================================================================
//                                                             TestReport
// ======================================================================

// TestReportEmptyInit ... Test the default Report creation
func TestReportEmptyInit(t *testing.T) {

	// 1. Create default Report object
	obj, err := NewReport(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Histories, 0)
}

// TestReportTextInit ... Test the Report object creation from text
func TestReportTextInit(t *testing.T) {

	// 1. Create Report object from text
	obj, err := NewReport(false, fromText(reportExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 3)
	assert.Len(t, obj.Histories, 3)
}

// TestReportPartOne ... Test part one example of Report object
func TestReportPartOne(t *testing.T) {

	// 1. Create Report object from text
	obj, err := NewReport(false, fromText(reportPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 3)
	assert.Len(t, obj.Histories, 3)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, reportPartOneResult, result)
}

// TestReportPartTwo ... Test part two example of Report object
func TestReportPartTwo(t *testing.T) {
	// Test part two example of Report object

	// 1. Create Report object from text
	obj, err := NewReport(true, fromText(reportPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 3)
	assert.Len(t, obj.Histories, 3)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, reportPartTwoResult, result)
}

// ======================================================================
// end                  r e p o r t _ t e s t . g o                   end
// ======================================================================
