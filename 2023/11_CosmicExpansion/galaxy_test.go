// ======================================================================
// Cosmic Expansion
//   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    g a l a x y _ t e s t . g o
// ======================================================================
// Test Galaxy for Advent of Code 2023 day 11, Cosmic Expansion

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
const ()

// ======================================================================
//                                                             TestGalaxy
// ======================================================================

// TestGalaxyInit ... Test the Galaxy creation
func TestGalaxyInit(t *testing.T) {

	// 1. Create default Galaxy object
	obj := NewGalaxy(1, 2)

	// 2. Make sure it has the default values
	assert.Equal(t, 1, obj.Row)
	assert.Equal(t, 2, obj.Col)
}

// TestGalaxyDistance ... Test the Galaxy distance function
func TestGalaxyDistance(t *testing.T) {

	// 1. Create default Galaxy object
	g1 := NewGalaxy(0, 4)
	g3 := NewGalaxy(2, 0)
	g5 := NewGalaxy(6, 1)
	g6 := NewGalaxy(7, 12)
	g7 := NewGalaxy(10, 9)
	g8 := NewGalaxy(11, 0)
	g9 := NewGalaxy(11, 5)

	// 2. Make sure the distances are correct
	assert.Equal(t, 9.0, g5.Distance(g9))
	assert.Equal(t, 9.0, g9.Distance(g5))
	assert.Equal(t, 15.0, g1.Distance(g7))
	assert.Equal(t, 15.0, g7.Distance(g1))
	assert.Equal(t, 17.0, g3.Distance(g6))
	assert.Equal(t, 17.0, g6.Distance(g3))
	assert.Equal(t, 5.0, g8.Distance(g9))
	assert.Equal(t, 5.0, g9.Distance(g8))
}

// ======================================================================
// end                    g a l a x y _ t e s t. g o                  end
// ======================================================================
