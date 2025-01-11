// ======================================================================
// Parabolic Reflector Dish
//   Advent of Code 2023 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    d i s h _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 14, Parabolic Reflector Dish

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
	dishExampleText = `O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....`
	dishTiltedNorth = `OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....`

	dishPartOneText = dishExampleText
	dishPartTwoText = dishExampleText

	dishPartOneResult = "136"
	dishPartTwoResult = "64"
)

// ======================================================================
//                                                               TestDish
// ======================================================================

// TestDishEmptyInit ... Test the default Dish creation
func TestDishEmptyInit(t *testing.T) {

	// 1. Create default Dish object
	obj, err := NewDish(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)
	assert.Len(t, obj.Cubes, 0)
	assert.Len(t, obj.Rocks, 0)
}

// TestDishTextInit ... Test the Dish object creation from text
func TestDishTextInit(t *testing.T) {

	// 1. Create Dish object from text
	obj, err := NewDish(false, fromText(dishExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

	assert.Contains(t, obj.Cubes, locEncode(0, 5))
	assert.Contains(t, obj.Cubes, locEncode(1, 4))
	assert.Contains(t, obj.Cubes, locEncode(1, 9))
	assert.Contains(t, obj.Cubes, locEncode(9, 0))
	assert.Contains(t, obj.Cubes, locEncode(9, 5))

	assert.Contains(t, obj.Rocks, locEncode(0, 0))
	assert.Contains(t, obj.Rocks, locEncode(1, 0))
	assert.Contains(t, obj.Rocks, locEncode(1, 2))
	assert.Contains(t, obj.Rocks, locEncode(1, 3))
	assert.Contains(t, obj.Rocks, locEncode(9, 1))
	assert.Contains(t, obj.Rocks, locEncode(9, 2))

	// 3. Check methods
	r2r := obj.RocksToRow()
	assert.Len(t, r2r, 8)
	assert.Len(t, r2r[0], 1)
	assert.Len(t, r2r[1], 3)
	assert.Len(t, r2r[9], 2)
	assert.Contains(t, r2r[0], 0)
	assert.Contains(t, r2r[1], 0)
	assert.Contains(t, r2r[1], 2)
	assert.Contains(t, r2r[1], 3)
	assert.Contains(t, r2r[9], 1)
	assert.Contains(t, r2r[9], 2)

	assert.Equal(t, 104, obj.Load())
	assert.Equal(t, dishExampleText, obj.String())

	obj.TiltNorth()
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r = obj.RocksToRow()
	assert.Len(t, r2r, 6)
	assert.Len(t, r2r[0], 5)
	assert.Len(t, r2r[1], 2)
	assert.Len(t, r2r[2], 4)
	assert.Contains(t, r2r[0], 0)
	assert.Contains(t, r2r[0], 1)
	assert.Contains(t, r2r[0], 2)
	assert.Contains(t, r2r[0], 3)
	assert.Contains(t, r2r[0], 7)
	assert.Contains(t, r2r[1], 0)
	assert.Contains(t, r2r[1], 1)
	assert.Contains(t, r2r[2], 0)
	assert.Contains(t, r2r[2], 1)
	assert.Contains(t, r2r[2], 4)
	assert.Contains(t, r2r[2], 9)

	assert.Equal(t, 136, obj.Load())
	assert.Equal(t, dishTiltedNorth, obj.String())

	obj.TiltWest()
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r = obj.RocksToRow()
	assert.Len(t, r2r, 6)
	assert.Len(t, r2r[0], 5)
	assert.Len(t, r2r[1], 2)
	assert.Len(t, r2r[2], 4)
	assert.Len(t, r2r[3], 3)
	assert.Len(t, r2r[6], 3)
	assert.Len(t, r2r[7], 1)
	assert.Contains(t, r2r[0], 0)
	assert.Contains(t, r2r[0], 1)
	assert.Contains(t, r2r[0], 2)
	assert.Contains(t, r2r[0], 3)
	assert.Contains(t, r2r[0], 6)
	assert.Contains(t, r2r[1], 0)
	assert.Contains(t, r2r[1], 1)
	assert.Contains(t, r2r[2], 0)
	assert.Contains(t, r2r[2], 1)
	assert.Contains(t, r2r[2], 2)
	assert.Contains(t, r2r[2], 7)
	assert.Contains(t, r2r[3], 0)
	assert.Contains(t, r2r[3], 4)
	assert.Contains(t, r2r[3], 5)
	assert.Contains(t, r2r[6], 0)
	assert.Contains(t, r2r[6], 6)
	assert.Contains(t, r2r[6], 7)
	assert.Contains(t, r2r[7], 0)

	obj.TiltSouth()
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r = obj.RocksToRow()
	assert.Len(t, r2r, 9)
	assert.Len(t, r2r[1], 1)
	assert.Len(t, r2r[2], 2)
	assert.Len(t, r2r[3], 2)
	assert.Len(t, r2r[4], 3)
	assert.Len(t, r2r[8], 1)
	assert.Len(t, r2r[9], 2)
	assert.Contains(t, r2r[1], 6)
	assert.Contains(t, r2r[2], 0)
	assert.Contains(t, r2r[2], 3)
	assert.Contains(t, r2r[3], 0)
	assert.Contains(t, r2r[3], 2)

	obj.TiltEast()
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

}

// TestDishTextNorth ... Test the Dish object creation from text
func TestDishTextNorth(t *testing.T) {

	// 1. Create Dish object from text
	obj, err := NewDish(false, fromText(dishTiltedNorth))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

	// 3. Check methods
	assert.Equal(t, 136, obj.Load())

	r2c := obj.RocksToCol()
	assert.Len(t, r2c, 9)
	assert.Len(t, r2c[0], 4)
	assert.Len(t, r2c[1], 3)
	assert.Len(t, r2c[9], 2)
	assert.Contains(t, r2c[0], 0)
	assert.Contains(t, r2c[0], 1)
	assert.Contains(t, r2c[0], 2)
	assert.Contains(t, r2c[0], 3)
	assert.Contains(t, r2c[1], 0)
	assert.Contains(t, r2c[1], 1)
	assert.Contains(t, r2c[1], 2)
	assert.Contains(t, r2c[9], 2)
	assert.Contains(t, r2c[9], 6)

	assert.Equal(t, 87, obj.Cycle())
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r := obj.RocksToRow()
	assert.Len(t, r2r, 9)
	assert.Len(t, r2r[0], 0)
	assert.Len(t, r2r[1], 1)
	assert.Len(t, r2r[2], 2)
	assert.Len(t, r2r[3], 2)
	assert.Len(t, r2r[4], 3)
	assert.Len(t, r2r[5], 2)
	assert.Len(t, r2r[6], 1)
	assert.Len(t, r2r[7], 4)
	assert.Len(t, r2r[8], 1)
	assert.Len(t, r2r[9], 2)

	assert.Equal(t, 69, obj.Cycle())
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r = obj.RocksToRow()
	assert.Len(t, r2r, 8)
	assert.Len(t, r2r[0], 0)
	assert.Len(t, r2r[1], 1)
	assert.Len(t, r2r[2], 0)
	assert.Len(t, r2r[3], 1)
	assert.Len(t, r2r[4], 3)
	assert.Len(t, r2r[5], 2)
	assert.Len(t, r2r[6], 2)
	assert.Len(t, r2r[7], 3)
	assert.Len(t, r2r[8], 2)
	assert.Len(t, r2r[9], 4)

	assert.Equal(t, 69, obj.Cycle())
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)
	r2r = obj.RocksToRow()
	assert.Len(t, r2r, 8)
	assert.Len(t, r2r[0], 0)
	assert.Len(t, r2r[1], 1)
	assert.Len(t, r2r[2], 0)
	assert.Len(t, r2r[3], 1)
	assert.Len(t, r2r[4], 3)
	assert.Len(t, r2r[5], 2)
	assert.Len(t, r2r[6], 2)
	assert.Len(t, r2r[7], 3)
	assert.Len(t, r2r[8], 2)
	assert.Len(t, r2r[9], 4)
}

func TestDishTextCycle(t *testing.T) {

	// 1. Create Dish object from text
	obj, err := NewDish(false, fromText(dishExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

	// 3. Check methods
	previous, current := obj.FindRepeat()
	assert.Equal(t, 3, previous)
	assert.Equal(t, 10, current)
}

// TestDishPartOne ... Test part one example of Dish object
func TestDishPartOne(t *testing.T) {

	// 1. Create Dish object from text
	obj, err := NewDish(false, fromText(dishPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, dishPartOneResult, result)
}

// TestDishPartTwo ... Test part two example of Dish object
func TestDishPartTwo(t *testing.T) {
	// Test part two example of Dish object

	// 1. Create Dish object from text
	obj, err := NewDish(true, fromText(dishPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Cubes, 17)
	assert.Len(t, obj.Rocks, 18)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, dishPartTwoResult, result)
}

// ======================================================================
// end                    d i s h _ t e s t . g o                     end
// ======================================================================
