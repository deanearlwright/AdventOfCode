// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r e c o r d _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2018 day 04, Repose Record

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
	RECORD_TEXT = `
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
`
	PART_ONE_TEXT = RECORD_TEXT
	PART_TWO_TEXT = RECORD_TEXT

	PART_ONE_RESULT = "240"
	PART_TWO_RESULT = "4455"
)

// ======================================================================
//                                                             TestRecord
// ======================================================================

func TestRecordEmptyInit(t *testing.T) {
	// Test the default Record creation

	// 1. Create default Record object
	obj := NewRecord(false, fromText(""))

	// 2. Make sure it has the default values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 0 {
		t.Fatal("There should be no Text")
	}
	if len(obj.Guards) != 0 {
		t.Fatal("There should be no Guards")
	}
}

func TestRecordTextInit(t *testing.T) {
	// Test the Record object creation from text

	// 1. Create Record object from text
	obj := NewRecord(false, fromText(RECORD_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 17 {
		t.Fatalf("len(Text) is %d not 17", len(obj.Text))
	}
	if len(obj.Guards) != 2 {
		t.Fatalf("len(Guards) is %d not 2", len(obj.Guards))
	}

	// 3. Check methods
	most := obj.mostMinutesAsleep()
	if most.Number != 10 {
		t.Fatalf("Most minutes is %d not 10", most.Number)
	}
	minute, times := most.MostOftenSleeping()
	if minute != 24 {
		t.Fatalf("Minute most asleep is %d not 24", minute)
	}
	if times != 2 {
		t.Fatalf("Times most asleep is %d not 2", times)
	}
}

func TestRecordPartOne(t *testing.T) {
	// Test part one example of Record object

	// 1. Create Record object from text
	obj := NewRecord(false, fromText(PART_ONE_TEXT))

	// 2. Make sure it has the expected values
	if obj.Part2 {
		t.Fatal("Part2 should be false")
	}
	if len(obj.Text) != 17 {
		t.Fatalf("len(Text) is %d not 17", len(obj.Text))
	}
	if len(obj.Guards) != 2 {
		t.Fatalf("len(Guards) is %d not 2", len(obj.Guards))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	if result != PART_ONE_RESULT {
		t.Fatalf("PartOne returned '%s' not '%s'", result, PART_ONE_RESULT)
	}
}

func TestRecordPartTwo(t *testing.T) {
	// Test part two example of Record object

	// 1. Create Record object from text
	obj := NewRecord(true, fromText(PART_TWO_TEXT))

	// 2. Make sure it has the expected values
	if !obj.Part2 {
		t.Fatal("Part2 should be true")
	}
	if len(obj.Text) != 17 {
		t.Fatalf("len(Text) is %d not 17", len(obj.Text))
	}
	if len(obj.Guards) != 2 {
		t.Fatalf("len(Guards) is %d not 2", len(obj.Guards))
	}

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	if result != PART_TWO_RESULT {
		t.Fatalf("PartTwo returned '%s' not '%s'", result, PART_TWO_RESULT)
	}
}

// ======================================================================
// end                  r e c o r d _ t e s t . g o                   end
// ======================================================================
