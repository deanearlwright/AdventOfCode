// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    g u a r d _ t e s t . g o
// ======================================================================
// Test Guard for Advent of Code 2018 day 04, Repose Record

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
	GUARD_SHIFT  = "[1518-11-01 00:00] Guard #10 begins shift"
	GUARD_ASLEEP = "[1518-11-01 00:05] falls asleep"
	GUARD_AWAKE  = "[1518-11-01 00:25] wakes up"
)

// ======================================================================
//                                                             TestGuard
// ======================================================================

func TestGuardEmptyInit(t *testing.T) {
	// Test the default Guard creation

	// 1. Create default Guard object
	obj := NewGuard(false, "")

	// 2. Make sure no guard was created
	if obj != nil {
		t.Fatal("Guard should not have been created")
	}
}

func TestGuardTextInit(t *testing.T) {
	// Test the Guard object creation from text

	// 1. Create default Guard object
	obj := NewGuard(false, GUARD_SHIFT)

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != len(GUARD_SHIFT) {
		t.Fatalf("len(Text) is %d not %d",
			len(obj.Text), len(GUARD_SHIFT))
	}

	// 3. Check methods
	minutes := obj.MinutesAsleep()
	if minutes != 0 {
		t.Fatalf("Initial minutes is %d not 0", minutes)
	}
	obj.FallsAsleep(GUARD_ASLEEP)
	minutes = obj.MinutesAsleep()
	if minutes != 55 {
		t.Fatalf("Falling asleep minutes is %d not 55", minutes)
	}
	obj.WakesUp(GUARD_AWAKE)
	minutes = obj.MinutesAsleep()
	if minutes != 20 {
		t.Fatalf("Waking up minutes is %d not 20", minutes)
	}
	minute, times := obj.MostOftenSleeping()
	if minute != 5 {
		t.Fatalf("Minute most asleep is %d not 5", minute)
	}
	if times != 1 {
		t.Fatalf("Times most asleep is %d not 1", minute)
	}
}

// ======================================================================
// end                  g u a r d _ t e s t. g o                end
// ======================================================================
