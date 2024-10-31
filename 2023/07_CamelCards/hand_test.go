// ======================================================================
// Camel Cards
//   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    h a n d _ t e s t . g o
// ======================================================================
// Test Hand for Advent of Code 2023 day 07, Camel Cards

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
	handText = "32T3K 765"
)

var (
	testHands = map[string]string{
		"AAAAA": handFive,
		"AA8AA": handFour,
		"23332": handFull,
		"TTT98": handThree,
		"23432": handTwo,
		"A23A4": handOne,
		"23456": handHigh,
	}
)

// ======================================================================
//                                                               TestHand
// ======================================================================

// TestHandEmptyInit ... Test the default Hand creation
func TestHandEmptyInit(t *testing.T) {

	// 1. Create default Hand object
	obj, err := NewHand(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Cards, 0)
	assert.Equal(t, obj.Bid, 0)
	assert.Equal(t, obj.Type, 0)

	// 3. Check methods
	count := obj.CountCards()
	assert.Len(t, count, 13)
	assert.Equal(t, 0, count["A"])
	assert.Equal(t, 0, count["K"])
	assert.Equal(t, 0, count["Q"])
	assert.Equal(t, 0, count["J"])
	assert.Equal(t, 0, count["T"])
	assert.Equal(t, 0, count["9"])
	assert.Equal(t, 0, count["8"])
	assert.Equal(t, 0, count["7"])
	assert.Equal(t, 0, count["6"])
	assert.Equal(t, 0, count["5"])
	assert.Equal(t, 0, count["4"])
	assert.Equal(t, 0, count["3"])
	assert.Equal(t, 0, count["2"])

	counts := CountCounts(count)
	assert.Len(t, counts, 6)
	assert.Equal(t, 13, counts[0])
	assert.Equal(t, 0, counts[1])
	assert.Equal(t, 0, counts[2])
	assert.Equal(t, 0, counts[3])
	assert.Equal(t, 0, counts[4])
	assert.Equal(t, 0, counts[5])
	assert.Equal(t, 13, counts[0]+counts[1]+counts[2]+counts[3]+counts[4]+counts[5])

	assert.Equal(t, handNone, obj.HandType1())
}

// TestHandTextInit ... Test the Hand object creation from text
func TestHandTextInit(t *testing.T) {

	// 1. Create default Hand object
	obj, err := NewHand(false, handText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(handText))
	assert.Len(t, obj.Cards, 5)
	assert.Equal(t, obj.Bid, 765)
	assert.Equal(t, obj.Type, 1)

	// 3. Check methods
	count := obj.CountCards()
	assert.Equal(t, 0, count["A"])
	assert.Equal(t, 1, count["K"])
	assert.Equal(t, 0, count["Q"])
	assert.Equal(t, 0, count["J"])
	assert.Equal(t, 1, count["T"])
	assert.Equal(t, 0, count["9"])
	assert.Equal(t, 0, count["8"])
	assert.Equal(t, 0, count["7"])
	assert.Equal(t, 0, count["6"])
	assert.Equal(t, 0, count["5"])
	assert.Equal(t, 0, count["4"])
	assert.Equal(t, 2, count["3"])
	assert.Equal(t, 1, count["2"])

	counts := CountCounts(count)
	assert.Len(t, counts, 6)
	assert.Equal(t, 9, counts[0])
	assert.Equal(t, 3, counts[1])
	assert.Equal(t, 1, counts[2])
	assert.Equal(t, 0, counts[3])
	assert.Equal(t, 0, counts[4])
	assert.Equal(t, 0, counts[5])
	assert.Equal(t, 13, counts[0]+counts[1]+counts[2]+counts[3]+counts[4]+counts[5])

	assert.Equal(t, handOne, obj.HandType1())
}

// TestHand ... Test each kind of hand
func TestHand(t *testing.T) {

	// 1. Loop for the example hands
	for handText, expectedType := range testHands {

		// 2. Create an Object for the Hand
		hand, err := NewHand(false, handText+" 1")
		assert.NoError(t, err)

		// 3. Get the hand type
		handType := hand.HandType1()

		// 4. Check it
		assert.Equal(t, expectedType, handType)
	}
}

// TestLess ... Test sorting function
func TestLess(t *testing.T) {

	// 1. Create the hands
	hand1, err := NewHand(false, "32T3K 765")
	assert.NoError(t, err)
	assert.Equal(t, 1, hand1.Type)
	hand2, err := NewHand(false, "T55J5 684")
	assert.NoError(t, err)
	assert.Equal(t, 3, hand2.Type)
	hand3, err := NewHand(false, "KK677 28")
	assert.NoError(t, err)
	assert.Equal(t, 2, hand3.Type)
	hand4, err := NewHand(false, "KTJJT 220")
	assert.NoError(t, err)
	assert.Equal(t, 2, hand4.Type)
	hand5, err := NewHand(false, "QQQJA 483")
	assert.NoError(t, err)
	assert.Equal(t, 3, hand5.Type)

	// 2. Compare the hands
	assert.True(t, hand1.Less(hand2)) // 32T3K one pair < T44J5 three
	assert.True(t, hand1.Less(hand3)) // 32T3K one pair < KK677 two pair
	assert.True(t, hand1.Less(hand4)) // 32T3K one pair < KTJJT two pair
	assert.True(t, hand1.Less(hand5)) // 32T3K one pair < QQQJA three

	assert.False(t, hand2.Less(hand1)) // T55J5 three > 32T3K one pair
	assert.False(t, hand2.Less(hand3)) // T55J5 three > KK677 two pair
	assert.False(t, hand2.Less(hand4)) // T55J5 three > KTJJT two pair
	assert.True(t, hand2.Less(hand5))  // T55J5 three < QQQJA three

	assert.False(t, hand3.Less(hand1)) // KK677 two pair > 32T3K one pair
	assert.True(t, hand3.Less(hand2))  // KK677 two pair < T55J5 three
	assert.False(t, hand3.Less(hand4)) // KK677 two pair > KTJJT two pair
	assert.True(t, hand3.Less(hand5))  // KK677 two pair < QQQJA three

	assert.False(t, hand4.Less(hand1)) // KTJJT two pair > 32T3K one pair
	assert.True(t, hand4.Less(hand2))  // KTJJT two pair < T55J5 three
	assert.True(t, hand4.Less(hand3))  // KTJJT two pair < KK677 two pair
	assert.True(t, hand4.Less(hand5))  // KTJJT two pair < QQQJA three

	assert.False(t, hand5.Less(hand1)) // QQQJA three > 32T3K one pair
	assert.False(t, hand5.Less(hand2)) // QQQJA three > T55J5 three
	assert.False(t, hand5.Less(hand3)) // QQQJA three > KK677 two pair
	assert.False(t, hand5.Less(hand4)) // QQQJA three > KTJJT two pair
}

// TestLessTwo ... Test sorting function for Part Two
func TestLessTwo(t *testing.T) {

	// 1. Create the hands
	hand1, err := NewHand(true, "32T3K 765")
	assert.NoError(t, err)
	assert.Equal(t, 1, hand1.Type)
	hand2, err := NewHand(true, "T55J5 684")
	assert.NoError(t, err)
	assert.Equal(t, 5, hand2.Type)
	hand3, err := NewHand(true, "KK677 28")
	assert.NoError(t, err)
	assert.Equal(t, 2, hand3.Type)
	hand4, err := NewHand(true, "KTJJT 220")
	assert.NoError(t, err)
	assert.Equal(t, 5, hand4.Type)
	hand5, err := NewHand(true, "QQQJA 483")
	assert.NoError(t, err)
	assert.Equal(t, 5, hand5.Type)

	// 2. Compare the hands
	assert.True(t, hand1.Less(hand2)) // 32T3K one pair < T44J5 four
	assert.True(t, hand1.Less(hand3)) // 32T3K one pair < KK677 two pair
	assert.True(t, hand1.Less(hand4)) // 32T3K one pair < KTJJT four
	assert.True(t, hand1.Less(hand5)) // 32T3K one pair < QQQJA four

	assert.False(t, hand2.Less(hand1)) // T55J5 four > 32T3K one pair
	assert.False(t, hand2.Less(hand3)) // T55J5 four > KK677 two pair
	assert.True(t, hand2.Less(hand4))  // T55J5 four < KTJJT four
	assert.True(t, hand2.Less(hand5))  // T55J5 four < QQQJA four

	assert.False(t, hand3.Less(hand1)) // KK677 two pair > 32T3K one pair
	assert.True(t, hand3.Less(hand2))  // KK677 two pair < T55J5 four
	assert.True(t, hand3.Less(hand4))  // KK677 two pair < KTJJT four
	assert.True(t, hand3.Less(hand5))  // KK677 two pair < QQQJA four

	assert.False(t, hand4.Less(hand1)) // KTJJT four > 32T3K one pair
	assert.False(t, hand4.Less(hand2)) // KTJJT four > T55J5 four
	assert.False(t, hand4.Less(hand3)) // KTJJT four > KK677 two pair
	assert.False(t, hand4.Less(hand5)) // KTJJT four > QQQJA four

	assert.False(t, hand5.Less(hand1)) // QQQJA four > 32T3K one pair
	assert.False(t, hand5.Less(hand2)) // QQQJA four > T55J5 four
	assert.False(t, hand5.Less(hand3)) // QQQJA four > KK677 two pair
	assert.True(t, hand5.Less(hand4))  // QQQJA four < KTJJT four
}

// ======================================================================
// end                      h a n d _ t e s t. g o                    end
// ======================================================================
