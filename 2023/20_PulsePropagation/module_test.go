// ======================================================================
// Pulse Propagation
//   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    m o d u l e _ t e s t . g o
// ======================================================================
// Test Module for Advent of Code 2023 day 20, Pulse Propagation

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
	flipflopText    = "%a -> inv, con"
	broadcasterText = "broadcaster -> a, b, c"
	conjunctionText = "&inv -> a"
	outputText      = "output -> *"
)

// ======================================================================
//                                                             TestModule
// ======================================================================

// TestModuleEmptyInit ... Test the default Module creation
func TestModuleEmptyInit(t *testing.T) {

	// 1. Create a default Module object
	obj, err := NewModule(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Name, 0)
	assert.Len(t, obj.Type, 0)
	assert.Len(t, obj.Outputs, 0)
	assert.Len(t, obj.Inputs, 0)
	assert.Len(t, obj.Received, 0)
	assert.False(t, obj.FlipFlop)
}

// TestModuleFlipFlopInit ... Test the Module object creation from flipflop text
func TestModuleFlipFlopInit(t *testing.T) {

	// 1. Create a flipflop Module object
	obj, err := NewModule(false, flipflopText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(flipflopText))
	assert.Equal(t, "a", obj.Name)
	assert.Equal(t, "%", obj.Type)
	assert.Len(t, obj.Outputs, 2)
	assert.Len(t, obj.Inputs, 0)
	assert.Len(t, obj.Received, 0)
	assert.False(t, obj.FlipFlop)

	// 3. Check methods
	obj.AddInput("broadcaster")
	assert.Len(t, obj.Inputs, 1)
	assert.Len(t, obj.Received, 1)
	assert.Equal(t, obj.Inputs[0], "broadcaster")
	assert.Equal(t, obj.Received["broadcaster"], "Low")

	level := obj.Pulse(1, "broadcaster High a")
	assert.Equal(t, NONE, level)
	assert.False(t, obj.FlipFlop)
	level = obj.Pulse(2, "broadcaster High a")
	assert.Equal(t, NONE, level)
	assert.False(t, obj.FlipFlop)
	level = obj.Pulse(3, "broadcaster Low a")
	assert.Equal(t, HIGH, level)
	assert.True(t, obj.FlipFlop)
	level = obj.Pulse(4, "broadcaster Low a")
	assert.Equal(t, LOW, level)
	assert.False(t, obj.FlipFlop)

	assert.Len(t, obj.HighRecv["broadcaster"], 2)
	assert.Equal(t, 1, obj.HighRecv["broadcaster"][0])
	assert.Equal(t, 2, obj.HighRecv["broadcaster"][1])
}

// TestModuleBroadcasterInit ... Test the Module object creation from broadcaster text
func TestModuleBroadcasterInit(t *testing.T) {

	// 1. Create a boadcaster Module object
	obj, err := NewModule(false, broadcasterText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(broadcasterText))
	assert.Equal(t, "broadcaster", obj.Name)
	assert.Equal(t, "", obj.Type)
	assert.Len(t, obj.Outputs, 3)
	assert.Len(t, obj.Inputs, 0)
	assert.Len(t, obj.Received, 0)
	assert.False(t, obj.FlipFlop)

	// 3. Check methods
	obj.AddInput("button")
	assert.Len(t, obj.Inputs, 1)
	assert.Len(t, obj.Received, 1)
	assert.Equal(t, obj.Inputs[0], "button")
	assert.Equal(t, obj.Received["button"], "Low")

	level := obj.Pulse(1, "button High broadcaster")
	assert.Equal(t, HIGH, level)
	assert.False(t, obj.FlipFlop)
	level = obj.Pulse(2, "button Low broadcaster")
	assert.Equal(t, LOW, level)
	assert.False(t, obj.FlipFlop)

	assert.Len(t, obj.HighRecv["button"], 1)
	assert.Equal(t, 1, obj.HighRecv["button"][0])
}

// TestModuleConjunctionInit ... Test the Module object creation from conjunction text
func TestModuleConjunctionInit(t *testing.T) {

	// 1. Createa conjunction Module object
	obj, err := NewModule(false, conjunctionText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(conjunctionText))
	assert.Equal(t, "inv", obj.Name)
	assert.Equal(t, "&", obj.Type)
	assert.Len(t, obj.Outputs, 1)
	assert.Len(t, obj.Inputs, 0)
	assert.Len(t, obj.Received, 0)
	assert.False(t, obj.FlipFlop)

	// 3. Check methods
	obj.AddInput("broadcaster")
	assert.Len(t, obj.Inputs, 1)
	assert.Len(t, obj.Received, 1)
	assert.Equal(t, obj.Inputs[0], "broadcaster")
	assert.Equal(t, obj.Received["broadcaster"], "Low")

	level := obj.Pulse(1, "broadcaster Low inv")
	assert.Equal(t, HIGH, level)
	assert.False(t, obj.FlipFlop)
	level = obj.Pulse(2, "broadcaster High inv")
	assert.Equal(t, LOW, level)
	assert.False(t, obj.FlipFlop)

	assert.Len(t, obj.HighRecv["broadcaster"], 1)
	assert.Equal(t, 2, obj.HighRecv["broadcaster"][0])
}

// TestModuleOutput ... Test the Module object creation from output text
func TestModuleOutputInit(t *testing.T) {

	// 1. Create a boadcaster Module object
	obj, err := NewModule(false, outputText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(outputText))
	assert.Equal(t, "output", obj.Name)
	assert.Equal(t, "", obj.Type)
	print("outputs", obj.Outputs, '\n')
	assert.Len(t, obj.Outputs, 0)
	assert.Len(t, obj.Inputs, 0)
	assert.Len(t, obj.Received, 0)
	assert.False(t, obj.FlipFlop)

	// 3. Check methods
	obj.AddInput("button")
	assert.Len(t, obj.Inputs, 1)
	assert.Len(t, obj.Received, 1)
	assert.Equal(t, obj.Inputs[0], "button")
	assert.Equal(t, obj.Received["button"], "Low")

	level := obj.Pulse(1, "button High output")
	assert.Equal(t, NONE, level)
	assert.False(t, obj.FlipFlop)
	level = obj.Pulse(2, "button Low output")
	assert.Equal(t, NONE, level)
	assert.False(t, obj.FlipFlop)

	assert.Len(t, obj.HighRecv["button"], 1)
	assert.Equal(t, 1, obj.HighRecv["button"][0])
}

// ======================================================================
// end                    m o d u l e _ t e s t. g o                  end
// ======================================================================
