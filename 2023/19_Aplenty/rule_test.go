// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r u l e _ t e s t . g o
// ======================================================================
// Test Rule for Advent of Code 2023 day 19, Aplenty

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
	ruleText  = "a<2006:qkq"
	ruleTwo   = "m>2090:A"
	ruleThree = "x>0:R"
)

// ======================================================================
//                                                               TestRule
// ======================================================================

// TestRuleEmptyInit ... Test the default Rule creation
func TestRuleEmptyInit(t *testing.T) {

	// 1. Create default Rule object
	obj, err := NewRule(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, "", obj.Category)
	assert.Equal(t, 1, obj.MinMax.Min)
	assert.Equal(t, 4000, obj.MinMax.Max)
	assert.Equal(t, "", obj.Where)
}

// TestRuleTextInit ... Test the Rule object creation from text
func TestRuleTextInit(t *testing.T) {

	// 1. Create default Rule object
	obj, err := NewRule(false, ruleText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(ruleText))
	assert.Equal(t, "a", obj.Category)
	assert.Equal(t, 1, obj.MinMax.Min)
	assert.Equal(t, 2005, obj.MinMax.Max)
	assert.Equal(t, "qkq", obj.Where)

	// 3. Check Methods
	part, err := NewPart(false, "{x=787,m=2655,a=1222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "qkq", obj.CheckPart(part))
	part.Categories[2] = 3000
	assert.Equal(t, "", obj.CheckPart(part))
}

// TestRuleTextTwo ... Test the Rule object creation from text
func TestRuleTextTwo(t *testing.T) {

	// 1. Create default Rule object
	obj, err := NewRule(false, ruleTwo)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(ruleTwo))
	assert.Equal(t, "m", obj.Category)
	assert.Equal(t, 2091, obj.MinMax.Min)
	assert.Equal(t, 4000, obj.MinMax.Max)
	assert.Equal(t, "A", obj.Where)

	// 3. Check Methods
	part, err := NewPart(false, "{x=787,m=2655,a=1222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "A", obj.CheckPart(part))
	part.Categories[1] = 2000
	assert.Equal(t, "", obj.CheckPart(part))
}

// TestRuleTextThree ... Test the Rule object creation from text
func TestRuleTextThree(t *testing.T) {

	// 1. Create default Rule object
	obj, err := NewRule(false, ruleThree)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(ruleThree))
	assert.Equal(t, "x", obj.Category)
	assert.Equal(t, 1, obj.MinMax.Min)
	assert.Equal(t, 4000, obj.MinMax.Max)
	assert.Equal(t, "R", obj.Where)

	// 3. Check Methods
	part, err := NewPart(false, "{x=787,m=2655,a=1222,s=2876}")
	assert.NoError(t, err)
	assert.Equal(t, "R", obj.CheckPart(part))
	part.Categories[0] = 2000
	assert.Equal(t, "R", obj.CheckPart(part))
}

// ======================================================================
// end                      r u l e _ t e s t. g o                    end
// ======================================================================
