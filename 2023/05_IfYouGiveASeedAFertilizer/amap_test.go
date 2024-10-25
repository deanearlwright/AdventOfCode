// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                      a m a p _ t e s t . g o
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
	amapExampleText = `seeds: 79 14 55 13

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
)

// ======================================================================
//                                                              TestAmap
// ======================================================================

func TestAmapEmptyInit(t *testing.T) {
	// Test the default Amap creation

	// 1. Create default Amap object
	obj, indx, err := NewAmap(false, fromText(""), 0)
	assert.NotNil(t, obj)
	assert.NoError(t, err)
	assert.Equal(t, 0, indx)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Ranges, 0)
}

func TestAmapTextInit(t *testing.T) {
	// Test the Amap object creation from text

	// 1. Create Amap object from text
	obj, indx, err := NewAmap(false, fromText(amapExampleText), 1)
	assert.NotNil(t, obj)
	assert.NoError(t, err)
	assert.Equal(t, 4, indx)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 17)
	assert.Equal(t, "seed", obj.From)
	assert.Equal(t, "soil", obj.To)
	assert.Len(t, obj.Ranges, 2)

	// 3. Check methods
	assert.Equal(t, 81, obj.Next(79))
	assert.Equal(t, 14, obj.Next(14))
	assert.Equal(t, 57, obj.Next(55))
	assert.Equal(t, 13, obj.Next(13))
}

// ======================================================================
// end                    a m a p _ t e s t . g o                     end
// ======================================================================
