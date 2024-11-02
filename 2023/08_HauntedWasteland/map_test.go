// ======================================================================
// Haunted Wasteland
//   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    m a p _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 08, Haunted Wasteland

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
	mapExampleText = `RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
`
	mapExampleText2 = `LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
`

	mapExampleText3 = `LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
`

	mapPartOneText = mapExampleText
	mapPartTwoText = mapExampleText3

	mapPartOneResult = "2"
	mapPartTwoResult = "6"
)

// ======================================================================
//                                                                TestMap
// ======================================================================

// TestMapEmptyInit ... Test the default Map creation
func TestMapEmptyInit(t *testing.T) {

	// 1. Create default Map object
	obj, err := NewMap(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Instructions, 0)
	assert.Equal(t, obj.InstIndx, 0)
	assert.Len(t, obj.Network, 0)
}

// TestMapTextInit ... Test the Map object creation from text
func TestMapTextInit(t *testing.T) {

	// 1. Create Map object from text
	obj, err := NewMap(false, fromText(mapExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 8)
	assert.Len(t, obj.Instructions, 2)
	assert.Equal(t, obj.InstIndx, 0)
	assert.Len(t, obj.Network, 7)

	// 3. Check methods
	assert.Equal(t, "R", obj.NextInst())
	assert.Equal(t, "L", obj.NextInst())
	assert.Equal(t, "R", obj.NextInst())
	assert.Equal(t, "L", obj.NextInst())

	assert.Equal(t, 2, obj.StartToFinishSteps("AAA", "ZZZ"))
}

// TestMapTextInit2 ... Test the Map object creation from text
func TestMapTextInit2(t *testing.T) {

	// 1. Create Map object from text
	obj, err := NewMap(false, fromText(mapExampleText2))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 4)
	assert.Len(t, obj.Instructions, 3)
	assert.Equal(t, obj.InstIndx, 0)
	assert.Len(t, obj.Network, 3)

	// 3. Check methods
	assert.Equal(t, 6, obj.StartToFinishSteps("AAA", "ZZZ"))
}

// TestMapTextInit3 ... Test the Map object creation from text
func TestMapTextInit3(t *testing.T) {

	// 1. Create Map object from text
	obj, err := NewMap(true, fromText(mapExampleText3))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 9)
	assert.Len(t, obj.Instructions, 2)
	assert.Equal(t, obj.InstIndx, 0)
	assert.Len(t, obj.Network, 8)

	// 3. Check methods
	assert.Equal(t, 2, obj.StartToFinishStepsTwo("11A"))
	assert.Equal(t, 3, obj.StartToFinishStepsTwo("22A"))

	assert.Equal(t, []int{2, 3}, obj.AllStartToFinishStepsTwo())
}

// TestMapPartOne ... Test part one example of Map object
func TestMapPartOne(t *testing.T) {

	// 1. Create Map object from text
	obj, err := NewMap(false, fromText(mapPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 8)
	assert.Len(t, obj.Instructions, 2)
	assert.Equal(t, obj.InstIndx, 0)
	assert.Len(t, obj.Network, 7)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, mapPartOneResult, result)
}

// TestMapPartTwo ... Test part two example of Map object
func TestMapPartTwo(t *testing.T) {
	// Test part two example of Map object

	// 1. Create Map object from text
	obj, err := NewMap(true, fromText(mapPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 9)
	assert.Len(t, obj.Instructions, 2)
	assert.Len(t, obj.Network, 8)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, mapPartTwoResult, result)
}

// ======================================================================
// end                     m a p _ t e s t . g o                      end
// ======================================================================
