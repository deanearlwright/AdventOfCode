// ======================================================================
// Gear Ratios
//   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    i t e m _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 03, Gear Ratios

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              TestItem
// ======================================================================

func TestNewItem(t *testing.T) {
	// Test the default Item creation

	// 1. Create the default Item object
	obj := NewItem(3, 5)

	// 2. Make sure it has the default values
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 5, obj.StartCol)
	assert.Equal(t, 5, obj.EndCol)
	assert.Equal(t, -1, obj.Value)
	assert.Equal(t, "", obj.Symbol)
}

func TestNewNumber(t *testing.T) {
	// Test the Numeric Item object creation

	// 1. Create Item object from text
	obj, err := NewNumber(3, 5, "7")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 5, obj.StartCol)
	assert.Equal(t, 5, obj.EndCol)
	assert.Equal(t, 7, obj.Value)
	assert.Equal(t, "", obj.Symbol)

	// 3. Add another digit
	err = obj.AddDigitToItem(3, 6, "4")
	assert.NoError(t, err)

	// 4. Make sure it has the expected values
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 5, obj.StartCol)
	assert.Equal(t, 6, obj.EndCol)
	assert.Equal(t, 74, obj.Value)
	assert.Equal(t, "", obj.Symbol)

}

func TestNewSymbol(t *testing.T) {
	// Test the Symbol Item object creation

	// 1. Create Item object from text
	obj, err := NewSymbol(3, 5, "*")
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 5, obj.StartCol)
	assert.Equal(t, 5, obj.EndCol)
	assert.Equal(t, -1, obj.Value)
	assert.Equal(t, "*", obj.Symbol)
}

func TestAdjacency(t *testing.T) {
	// Test the Item adjacency

	// 1. Two Item objects
	objn, err := NewNumber(3, 5, "7")
	assert.NoError(t, err)
	err = objn.AddDigitToItem(3, 6, "4")
	assert.NoError(t, err)
	objs, err := NewSymbol(3, 7, "*")
	assert.NoError(t, err)

	// 2. Same Row, imediately before or after
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 3. Same Row, But distant
	objs.StartCol = 9
	objs.EndCol = 9
	assert.False(t, objn.IsAdjacent(objs))
	assert.False(t, objs.IsAdjacent(objn))

	// 3. Adjacent Row, near col
	objs.Row = 2
	objs.StartCol = 7
	objs.EndCol = 7
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 4. Far Row, near col
	objs.Row = 1
	objs.StartCol = 7
	objs.EndCol = 7
	assert.False(t, objn.IsAdjacent(objs))
	assert.False(t, objs.IsAdjacent(objn))

	// 5. Adjacent Row, middle col
	err = objn.AddDigitToItem(3, 7, "8")
	assert.NoError(t, err)
	objs.Row = 2
	objs.StartCol = 6
	objs.EndCol = 6
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 6. Adjacent Row, distanct
	objs.StartCol = 2
	objs.EndCol = 2
	assert.False(t, objn.IsAdjacent(objs))
	assert.False(t, objs.IsAdjacent(objn))

	// 7. Adjacent Row, one before
	objs.StartCol = 4
	objs.EndCol = 4
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 8. Adjacent Row, Same Start Column
	objs.StartCol = 5
	objs.EndCol = 5
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 9. Adjacent Row, Same End Column
	objs.StartCol = 7
	objs.EndCol = 7
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 10. Adjacent Row, Adjacent Column
	objs.StartCol = 8
	objs.EndCol = 8
	assert.True(t, objn.IsAdjacent(objs))
	assert.True(t, objs.IsAdjacent(objn))

	// 11. Adjacent Row, Distant Column
	objs.StartCol = 9
	objs.EndCol = 9
	assert.False(t, objn.IsAdjacent(objs))
	assert.False(t, objs.IsAdjacent(objn))
}

func TestCountAdjacency(t *testing.T) {
	// Test counting of adjacent Items

	// 1. Create come objects
	obj467, err := NewNumber(0, 0, "4")
	assert.NoError(t, err)
	err = obj467.AddDigitToItem(0, 1, "6")
	assert.NoError(t, err)
	err = obj467.AddDigitToItem(0, 2, "7")
	assert.NoError(t, err)

	obj114, err := NewNumber(0, 5, "1")
	assert.NoError(t, err)
	err = obj114.AddDigitToItem(0, 6, "1")
	assert.NoError(t, err)
	err = obj114.AddDigitToItem(0, 7, "4")
	assert.NoError(t, err)

	obj35, err := NewNumber(2, 2, "3")
	assert.NoError(t, err)
	err = obj35.AddDigitToItem(2, 3, "5")
	assert.NoError(t, err)

	obj633, err := NewNumber(3, 6, "6")
	assert.NoError(t, err)
	err = obj633.AddDigitToItem(3, 7, "3")
	assert.NoError(t, err)
	err = obj633.AddDigitToItem(3, 8, "3")
	assert.NoError(t, err)

	objstar, err := NewSymbol(1, 3, "*")
	assert.NoError(t, err)

	objpound, err := NewSymbol(3, 6, "#")
	assert.NoError(t, err)

	// 2. Create collections
	numbers := []*Item{obj467, obj114, obj35, obj633}
	symbols := []*Item{objstar, objpound}

	// 3. Check adjacency counts
	assert.Equal(t, 1, obj467.CountAdjacent(symbols))
	assert.Equal(t, 0, obj114.CountAdjacent(symbols))
	assert.Equal(t, 1, obj35.CountAdjacent(symbols))
	assert.Equal(t, 1, obj633.CountAdjacent(symbols))
	assert.Equal(t, 2, objstar.CountAdjacent(numbers))
	assert.Equal(t, 1, objpound.CountAdjacent(numbers))

	// 4. Check gear ration
	assert.Equal(t, 16345, objstar.GearRatio(numbers))
}

// ======================================================================
// end                    i t e m _ t e s t . g o                     end
// ======================================================================
