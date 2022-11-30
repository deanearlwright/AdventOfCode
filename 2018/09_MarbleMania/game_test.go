// ======================================================================
// Marble Mania
//   Advent of Code 2018 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    g a m e _ t e s t . g o
// ======================================================================
// Test Game for Advent of Code 2018 day 09, Marble Mania

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"testing"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

var (
	GAME_EXAMPLES = [...]int{
		10, 1618, 8317,
		13, 7999, 146373,
		17, 1184, 2764,
		21, 6111, 54718,
		30, 5807, 37305}
)

// ======================================================================
//                                                               TestGame
// ======================================================================

func TestGameShort(t *testing.T) {
	// Test the default Game creation

	// 1. Create default Game object
	obj := NewGame(9, 25)

	// 2. Make sure it has theexpected values
	if obj.numPlayers != 9 {
		t.Fatalf("Number of Players is %d not 9", obj.numPlayers)
	}
	if obj.numMarbles != 25 {
		t.Fatalf("Number of Marbles is %d not 25", obj.numMarbles)
	}
	if len(obj.players) != 9 {
		t.Fatalf("Length of Players is %d not 9", len(obj.players))
	}
	if len(obj.circle) != 1 {
		t.Fatalf("Length of circle is %d not 1", len(obj.circle))
	}
	if cap(obj.circle) != 25 {
		t.Fatalf("Capacity of circle is %d not 25", cap(obj.circle))
	}
	if obj.nextPlayer != 0 {
		t.Fatalf("Next Players is %d not 0", obj.nextPlayer)
	}
	if obj.nextMarble != 1 {
		t.Fatalf("Next Marble is %d not 1", obj.nextMarble)
	}
	if obj.current != 0 {
		t.Fatalf("Current is %d not 0", obj.current)
	}

	// 3. Check methods
	show := obj.Show()
	if show != "[----] (0)" {
		t.Fatalf("Initial show is '%s' not '[----] (0)'", show)
	}
	if obj.IsSpecial(1) {
		t.Fatal("One is not special")
	}
	if obj.IsSpecial(7) {
		t.Fatal("Seven is not special")
	}
	if !obj.IsSpecial(23) {
		t.Fatal("Twenty three should be special")
	}
	if !obj.IsSpecial(46) {
		t.Fatal("Forty six should be special")
	}
	if obj.IsSpecial(50) {
		t.Fatal("Fifty is not special")
	}

	// 4. First turn
	cwise := obj.Clockwise()
	if cwise != 1 {
		t.Fatalf("Initial closewise is %d not 1", cwise)
	}
	more := obj.Turn()
	if !more {
		t.Fatal("Game ended after first turn")
	}
	show = obj.Show()
	if show != "[   1]  0 (1)" {
		t.Fatalf("First turn show is '%s' not '[   1]  0 (1)'", show)
	}

}

func TestGameExamples(t *testing.T) {
	// Test the Game object creation from text

	// 1. Loop through the examples
	for i := 0; i < len(GAME_EXAMPLES); i = i + 3 {

		// 2. Get the values
		players := GAME_EXAMPLES[i]
		marbles := GAME_EXAMPLES[i+1]
		expected := GAME_EXAMPLES[i+2]

		// 2. Create the game object
		game := NewGame(players, marbles)

		// 3. Play the game
		total := game.AllTurns()

		// 4. Check the result
		if total != expected {
			t.Fatalf("Game(%d, %d) is %d not %d", players, marbles, total, expected)
		}
	}
}

// ======================================================================
// end                  g a m e _ t e s t. g o                end
// ======================================================================
