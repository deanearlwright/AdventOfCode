// ======================================================================
// Pulse Propagation
//   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c o n f i g u r a t i o n _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 20, Pulse Propagation

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
	configurationExampleOne = `
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
`
	configurationExampleTwo = `
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
`
	configurationPartOneText = configurationExampleOne
	configurationPartTwoText = ""

	configurationPartOneResult = "32000000"
	configurationPartTwoResult = "-1"
)

// ======================================================================
//                                                      TestConfiguration
// ======================================================================

// TestConfigurationEmptyInit ... Test the default Configuration creation
func TestConfigurationEmptyInit(t *testing.T) {

	// 1. Create default Configuration object
	obj, err := NewConfiguration(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Modules, 0)
}

// TestConfigurationOneInit ... Test the Configuration object creation from text example One
func TestConfigurationOneInit(t *testing.T) {

	// 1. Create Configuration object from text
	obj, err := NewConfiguration(false, fromText(configurationExampleOne))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Modules, 6)

	assert.Equal(t, "broadcaster", obj.Modules["broadcaster"].Name)
	assert.Equal(t, "", obj.Modules["broadcaster"].Type)
	assert.Len(t, obj.Modules["broadcaster"].Outputs, 3)
	assert.Equal(t, "a", obj.Modules["broadcaster"].Outputs[0])
	assert.Equal(t, "b", obj.Modules["broadcaster"].Outputs[1])
	assert.Equal(t, "c", obj.Modules["broadcaster"].Outputs[2])
	assert.Len(t, obj.Modules["broadcaster"].Inputs, 1)
	assert.Contains(t, obj.Modules["broadcaster"].Inputs, "button")

	assert.Equal(t, "a", obj.Modules["a"].Name)
	assert.Equal(t, "%", obj.Modules["a"].Type)
	assert.Len(t, obj.Modules["a"].Outputs, 1)
	assert.Equal(t, "b", obj.Modules["a"].Outputs[0])
	assert.Len(t, obj.Modules["a"].Inputs, 2)
	assert.Contains(t, obj.Modules["a"].Inputs, "inv")
	assert.Contains(t, obj.Modules["a"].Inputs, "broadcaster")

	// 3. Check methods
	low, high := obj.PushButtonOnce(1)
	assert.Equal(t, 8, low)
	assert.Equal(t, 4, high)
	low, high = obj.PushButtonOnce(2)
	assert.Equal(t, 8, low)
	assert.Equal(t, 4, high)

	obj.Reset()
	low, high = obj.PushButtonMulti(2)
	assert.Equal(t, 8+8, low)
	assert.Equal(t, 4+4, high)

	obj.Reset()
	low, high = obj.PushButtonMulti(PUSHES)
	assert.Equal(t, 8000, low)
	assert.Equal(t, 4000, high)
}

// TestConfigurationTwoInit ... Test the Configuration object creation from text example Two
func TestConfigurationTwoInit(t *testing.T) {

	// 1. Create Configuration object from text
	obj, err := NewConfiguration(false, fromText(configurationExampleTwo))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Modules, 7)

	assert.Equal(t, "broadcaster", obj.Modules["broadcaster"].Name)
	assert.Equal(t, "", obj.Modules["broadcaster"].Type)
	assert.Len(t, obj.Modules["broadcaster"].Outputs, 1)
	assert.Equal(t, "a", obj.Modules["broadcaster"].Outputs[0])
	assert.Len(t, obj.Modules["broadcaster"].Inputs, 1)
	assert.Contains(t, obj.Modules["broadcaster"].Inputs, "button")

	assert.Equal(t, "a", obj.Modules["a"].Name)
	assert.Equal(t, "%", obj.Modules["a"].Type)
	assert.Len(t, obj.Modules["a"].Outputs, 2)
	assert.Equal(t, "inv", obj.Modules["a"].Outputs[0])
	assert.Equal(t, "con", obj.Modules["a"].Outputs[1])
	assert.Len(t, obj.Modules["a"].Inputs, 1)
	assert.Equal(t, "broadcaster", obj.Modules["a"].Inputs[0])

	// 3. Check methods
	low, high := obj.PushButtonOnce(1) // First
	assert.Equal(t, 4, low)
	assert.Equal(t, 4, high)
	low, high = obj.PushButtonOnce(2) // Second
	assert.Equal(t, 4, low)
	assert.Equal(t, 2, high)
	low, high = obj.PushButtonOnce(3) // Third
	assert.Equal(t, 5, low)
	assert.Equal(t, 3, high)
	low, high = obj.PushButtonOnce(4) // Fourth
	assert.Equal(t, 4, low)
	assert.Equal(t, 2, high)

	obj.Reset()
	low, high = obj.PushButtonMulti(4)
	assert.Equal(t, 4+4+5+4, low)
	assert.Equal(t, 4+2+3+2, high)
	mod := obj.Modules["broadcaster"]
	assert.Len(t, mod.HighRecv, 1)
	assert.Len(t, mod.HighRecv["button"], 0)
	mod = obj.Modules["a"]
	assert.Len(t, mod.HighRecv, 1)
	assert.Len(t, mod.HighRecv["broadcaster"], 0)
	mod = obj.Modules["inv"]
	assert.Len(t, mod.HighRecv, 1)
	assert.Len(t, mod.HighRecv["a"], 2)
	mod = obj.Modules["b"]
	assert.Len(t, mod.HighRecv, 1)
	assert.Len(t, mod.HighRecv["inv"], 2)
	mod = obj.Modules["output"]
	assert.Len(t, mod.HighRecv, 1)
	assert.Len(t, mod.HighRecv["con"], 4)

	obj.Reset()
	low, high = obj.PushButtonMulti(PUSHES)
	assert.Equal(t, 4250, low)
	assert.Equal(t, 2750, high)

	obj.Reset()
	assert.Equal(t, 1, obj.WhenLow("output"))
}

// TestConfigurationPartOne ... Test part one example of Configuration object
func TestConfigurationPartOne(t *testing.T) {

	// 1. Create Configuration object from text
	obj, err := NewConfiguration(false, fromText(configurationPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Modules, 6)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, configurationPartOneResult, result)
}

// TestConfigurationPartTwo ... Test part two example of Configuration object
func TestConfigurationPartTwo(t *testing.T) {
	// Test part two example of Configuration object

	// 1. Create Configuration object from text
	obj, err := NewConfiguration(true, fromText(configurationPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Modules, 0)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, configurationPartTwoResult, result)
}

// ======================================================================
// end            c o n f i g u r a t i o n _ t e s t . g o           end
// ======================================================================
