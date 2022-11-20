// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s h i f t _ t e s t . g o
// ======================================================================
// Test Shift for Advent of Code 2018 day 04, Repose Record

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
const (
	SHIFT_GUARD  = "[1518-11-01 00:00] Guard #10 begins shift"
	SHIFT_ASLEEP = "[1518-11-01 00:05] falls asleep"
	SHIFT_AWAKE  = "[1518-11-01 00:25] wakes up"
)

// ======================================================================
//                                                             TestShift
// ======================================================================

func TestShiftEmptyInit(t *testing.T) {
	// Test the default Shift creation

	// 1. Create default Shift object
	obj := NewShift(false, "")

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
	if obj.Date != "unknown" {
		t.Fatalf("Date is '%s' not '%s",
			obj.Date, "unknown")
	}
	if len(obj.Asleep) != 60 {
		t.Fatalf("len(Asleep) is %d not %d",
			len(obj.Asleep), 60)
	}
}

func TestShiftTextInit(t *testing.T) {
	// Test the Shift object creation from text

	// 1. Create default Shift object
	obj := NewShift(false, SHIFT_GUARD)

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(SHIFT_GUARD) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(SHIFT_GUARD))
	}
	if obj.Date != "1518-11-01" {
		t.Fatalf("Date is '%s' not '%s'",
			obj.Date, "1518-11-01")
	}
	if len(obj.Asleep) != 60 {
		t.Fatalf("len(Asleep) is %d not %d",
			len(obj.Asleep), 60)
	}

	// 3. Check methods
	minutes := obj.MinutesAsleep()
	if minutes != 0 {
		t.Fatalf("Initial MinutesAsleep() is %d not %d",
			minutes, 0)
	}
	obj.FallsAlseep(SHIFT_ASLEEP)
	minutes = obj.MinutesAsleep()
	if minutes != 55 {
		t.Fatalf("At time 5 MinutesAsleep() is %d not %d",
			minutes, 55)
	}
	obj.WakesUp(SHIFT_AWAKE)
	minutes = obj.MinutesAsleep()
	if minutes != 20 {
		t.Fatalf("At time 25 MinutesAsleep() is %d not %d",
			minutes, 20)
	}
}

// ======================================================================
// end                  s h i f t _ t e s t. g o                end
// ======================================================================
