// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    a n i m a l _ t e s t . g o
// ======================================================================
// Test Animal for Advent of Code 2023 day 10, Pipe Maze

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
//                                                             TestAnimal
// ======================================================================

// TestAnimal ... Test the default Animal creation
func TestAnimal(t *testing.T) {

	// 1. Create default Animal object
	loc := NewLocation(1, 3)
	obj := NewAnimal(loc, "North")
	assert.NotNil(t, obj)

	// 2. Make sure it has the default values
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 3, obj.Loc.Col)
	assert.Equal(t, "North", obj.Dir)
}

// TestAnimalSteps... Test the Animal scurrying
func TestAnimalSteps(t *testing.T) {

	// 1. Create default Animal object
	loc := NewLocation(1, 1)
	obj := NewAnimal(loc, "East")
	assert.NotNil(t, obj)

	// 2. Make sure it has the default values
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 1, obj.Loc.Col)
	assert.Equal(t, "East", obj.Dir)

	// 3. Check movement
	pipetext := `.....
.S-7.
.|.|.
.L-J.
.....`
	maze, err := NewPipemaze(false, fromText(pipetext))
	assert.NoError(t, err)
	assert.NotNil(t, maze)

	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 2, obj.Loc.Col)
	assert.Equal(t, "East", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 3, obj.Loc.Col)
	assert.Equal(t, "South", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 2, obj.Loc.Row)
	assert.Equal(t, 3, obj.Loc.Col)
	assert.Equal(t, "South", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 3, obj.Loc.Row)
	assert.Equal(t, 3, obj.Loc.Col)
	assert.Equal(t, "West", obj.Dir)
	assert.Equal(t, 4, obj.Steps)

	// 4. Create another animal
	loc = NewLocation(1, 1)
	obj = NewAnimal(loc, "South")
	assert.NotNil(t, obj)
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 1, obj.Loc.Col)
	assert.Equal(t, "South", obj.Dir)

	// 5. Move it wee beastie
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 2, obj.Loc.Row)
	assert.Equal(t, 1, obj.Loc.Col)
	assert.Equal(t, "South", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 3, obj.Loc.Row)
	assert.Equal(t, 1, obj.Loc.Col)
	assert.Equal(t, "East", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 3, obj.Loc.Row)
	assert.Equal(t, 2, obj.Loc.Col)
	assert.Equal(t, "East", obj.Dir)
	assert.NoError(t, obj.Move(maze))
	assert.Equal(t, 3, obj.Loc.Row)
	assert.Equal(t, 3, obj.Loc.Col)
	assert.Equal(t, "North", obj.Dir)
	assert.Equal(t, 4, obj.Steps)
}

// TestAnimalLoop ... Test the Animal scurrying around the maze loop
func TestAnimalLoop(t *testing.T) {

	// 1. Create default Animal object
	loc := NewLocation(1, 1)
	obj := NewAnimal(loc, "East")
	assert.NotNil(t, obj)

	// 2. Make sure it has the default values
	assert.Equal(t, 1, obj.Loc.Row)
	assert.Equal(t, 1, obj.Loc.Col)
	assert.Equal(t, "East", obj.Dir)

	// 3. Create a maze
	pipetext := `.....
.S-7.
.|.|.
.L-J.
.....`
	maze, err := NewPipemaze(false, fromText(pipetext))
	assert.NoError(t, err)
	assert.NotNil(t, maze)

	// 4. Scurry
	locs := obj.Loop(maze)
	assert.Len(t, locs, 8)
}

// ======================================================================
// end                    a n i m a l _ t e s t. g o                  end
// ======================================================================
