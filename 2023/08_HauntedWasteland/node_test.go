// ======================================================================
// Haunted Wasteland
//   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    n o d e _ t e s t . g o
// ======================================================================
// Test Node for Advent of Code 2023 day 08, Haunted Wasteland

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
	nodeText = "AAA = (BBB, CCC)"
)

// ======================================================================
//                                                               TestNode
// ======================================================================

// TestNodeEmptyInit ... Test the default Node creation
func TestNodeEmptyInit(t *testing.T) {

	// 1. Create default Node object
	obj, err := NewNode(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Equal(t, "", obj.Text)
	assert.Equal(t, "", obj.Name)
	assert.Equal(t, "", obj.Left)
	assert.Equal(t, "", obj.Right)

}

// TestNodeTextInit ... Test the Node object creation from text
func TestNodeTextInit(t *testing.T) {

	// 1. Create default Node object
	obj, err := NewNode(false, nodeText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, nodeText, obj.Text)
	assert.Equal(t, "AAA", obj.Name)
	assert.Equal(t, "BBB", obj.Left)
	assert.Equal(t, "CCC", obj.Right)

	// 3. Check methods
	assert.True(t, obj.IsStart())
	assert.False(t, obj.IsFinish())

	assert.Equal(t, "BBB", obj.Next(left))
	assert.Equal(t, "CCC", obj.Next(right))
	assert.Equal(t, "666", obj.Next("X"))
}

// ======================================================================
// end                      n o d e _ t e s t. g o                    end
// ======================================================================
