// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    w o r k f l o w _ t e s t . g o
// ======================================================================
// Test Workflow for Advent of Code 2023 day 19, Aplenty

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
	workflowText = "px{a<2006:qkq,m>2090:A,rfg}"
)

// ======================================================================
//                                                           TestWorkflow
// ======================================================================

// TestWorkflowEmptyInit ... Test the default Workflow creation
func TestWorkflowEmptyInit(t *testing.T) {

	// 1. Create default Workflow object
	obj, err := NewWorkflow(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, "", obj.Name)
	assert.Len(t, obj.Rules, 0)
}

// TestWorkflowTextInit ... Test the Workflow object creation from text
func TestWorkflowTextInit(t *testing.T) {

	// 1. Create default Workflow object
	obj, err := NewWorkflow(false, workflowText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(workflowText))
	assert.Equal(t, "px", obj.Name)
	assert.Len(t, obj.Rules, 3)
	assert.Equal(t, "qkq", obj.Rules[0].Where)
	assert.Equal(t, "A", obj.Rules[1].Where)
	assert.Equal(t, "rfg", obj.Rules[2].Where)

	// 3. Check methods
	part, err := NewPart(false, "{x=787,m=2655,a=1222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "qkq", obj.CheckPart(part))
	part, err = NewPart(false, "{x=787,m=2655,a=3222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "A", obj.CheckPart(part))
	part, err = NewPart(false, "{x=787,m=1655,a=3222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "rfg", obj.CheckPart(part))

}

// ======================================================================
// end                  w o r k f l o w _ t e s t. g o                end
// ======================================================================
