// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    w o r k f l o w s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 19, Aplenty

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
	workflowsExampleText = `
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
`
	workflowsPartOneText = workflowsExampleText
	workflowsPartTwoText = workflowsExampleText

	workflowsPartOneResult = "19114"
	workflowsPartTwoResult = "167409079868000"
)

// ======================================================================
//                                                          TestWorkflows
// ======================================================================

// TestWorkflowsEmptyInit ... Test the default Workflows creation
func TestWorkflowsEmptyInit(t *testing.T) {

	// 1. Create default Workflows object
	obj, err := NewWorkflows(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Flows, 0)
	assert.Len(t, obj.Parts, 0)
}

// TestWorkflowsTextInit ... Test the Workflows object creation from text
func TestWorkflowsTextInit(t *testing.T) {

	// 1. Create Workflows object from text
	obj, err := NewWorkflows(false, fromText(workflowsExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 16)
	assert.Len(t, obj.Flows, 11)
	assert.Len(t, obj.Parts, 5)

	// 3. Check methods
	assert.Equal(t, "A", obj.CheckPart(obj.Parts[0]))
	assert.Equal(t, "R", obj.CheckPart(obj.Parts[1]))
	assert.Equal(t, "A", obj.CheckPart(obj.Parts[2]))
	assert.Equal(t, "R", obj.CheckPart(obj.Parts[3]))
	assert.Equal(t, "A", obj.CheckPart(obj.Parts[4]))

	assert.Equal(t, 19114, obj.CheckParts())
	assert.Equal(t, 167409079868000, obj.Combinations(false, 0))
}

// TestWorkflowsPartOne ... Test part one example of Workflows object
func TestWorkflowsPartOne(t *testing.T) {

	// 1. Create Workflows object from text
	obj, err := NewWorkflows(false, fromText(workflowsPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 16)
	assert.Len(t, obj.Flows, 11)
	assert.Len(t, obj.Parts, 5)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, workflowsPartOneResult, result)
}

// TestWorkflowsPartTwo ... Test part two example of Workflows object
func TestWorkflowsPartTwo(t *testing.T) {
	// Test part two example of Workflows object

	// 1. Create Workflows object from text
	obj, err := NewWorkflows(true, fromText(workflowsPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 16)
	assert.Len(t, obj.Flows, 11)
	assert.Len(t, obj.Parts, 5)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, workflowsPartTwoResult, result)
}

// ======================================================================
// end               w o r k f l o w s _ t e s t . g o                end
// ======================================================================
