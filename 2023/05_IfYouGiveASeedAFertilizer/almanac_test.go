// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    a l m a n a c _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 05, IfYouGiveASeedAFertilizer

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
	almanacExampleText = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
`
	almanacPartOneText = almanacExampleText
	almanacPartTwoText = almanacExampleText

	almanacPartOneResult = "35"
	almanacPartTwoResult = "46"
)

// ======================================================================
//                                                            TestAlmanac
// ======================================================================

func TestAlmanacEmptyInit(t *testing.T) {
	// Test the default Almanac creation

	// 1. Create default Almanac object
	obj, err := NewAlmanac(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Seeds, 0)
	assert.Len(t, obj.Maps, 0)
	assert.Len(t, obj.ToMap, 0)
}

func TestAlmanacTextInit(t *testing.T) {
	// Test the Almanac object creation from text

	// 1. Create Almanac object from text
	obj, err := NewAlmanac(false, fromText(almanacExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 26)
	assert.Len(t, obj.Seeds, 4)
	assert.Len(t, obj.Maps, 7)
	assert.Len(t, obj.ToMap, 7)

	// 3. Check methods
	assert.Equal(t, 82, obj.GetLocationForSeed(79))
	assert.Equal(t, 43, obj.GetLocationForSeed(14))
	assert.Equal(t, 86, obj.GetLocationForSeed(55))
	assert.Equal(t, 35, obj.GetLocationForSeed(13))
}

func TestAlmanacPartOne(t *testing.T) {
	// Test part one example of Almanac object

	// 1. Create Almanac object from text
	obj, err := NewAlmanac(false, fromText(almanacPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 26)
	assert.Len(t, obj.Seeds, 4)
	assert.Len(t, obj.Maps, 7)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, almanacPartOneResult, result)
}

func TestAlmanacPartTwo(t *testing.T) {
	// Test part two example of Almanac object

	// 1. Create Almanac object from text
	obj, err := NewAlmanac(true, fromText(almanacPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 26)
	assert.Len(t, obj.Seeds, 4)
	assert.Len(t, obj.Maps, 7)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, almanacPartTwoResult, result)
}

// ======================================================================
// end                 a l m a n a c _ t e s t . g o                  end
// ======================================================================
