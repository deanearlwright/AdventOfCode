// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s h i f t . g o
// ======================================================================
// Shift for the Advent of Code 2018 Day 04 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"regexp"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	EXAMPLE_TEXT = "[1518-11-01 00:00] Guard #10 begins shift"
)

var (
	shiftExp = regexp.MustCompile("\\d+")
)

// ======================================================================
//                                                                  Shift
// ======================================================================

type Shift struct {
	Part2  bool
	Text   string
	Date   string
	Asleep []bool
}

func NewShift(part2 bool, text string) *Shift {
	// Shift Object for Repose Record

	// 1. Set the initial values
	p := new(Shift)
	p.Part2 = part2
	p.Text = text
	p.Date = "unknown"
	p.Asleep = make([]bool, 60)

	// 2. Set the date (if we can)
	if len(text) > 12 {
		p.Date = text[1:11]
	}

	// 3. Return the shift
	return p
}

func (p *Shift) FallsAlseep(text string) {
	// Add sleep time to the shift

	// 1. Parse the date and time
	parts := shiftExp.FindAllString(text, -1)
	if len(parts) != 5 {
		fmt.Printf("regexp failed for line '%s'\n", text)
		return
	}

	// 2. Get the minute the guard fell asleep
	start, _ := strconv.Atoi(parts[4])

	// 3. Mark when the guard is asleep
	for minute := start; minute < 60; minute++ {
		p.Asleep[minute] = true
	}

	// 4. Save the date (if case shift started before midnight)
	p.Date = text[1:11]
}

func (p *Shift) WakesUp(text string) {
	// Remove sleep time from the shift

	// 1. Parse the date and time
	parts := shiftExp.FindAllString(text, -1)
	if len(parts) != 5 {
		fmt.Printf("regexp failed for line '%s'\n", text)
		return
	}

	// 2. Get the minute the guard woke up
	start, _ := strconv.Atoi(parts[4])

	// 3. Mark when the guard is awake
	for minute := start; minute < 60; minute++ {
		p.Asleep[minute] = false
	}
}

func (p *Shift) MinutesAsleep() int {
	// Return the number of minutes a guard has been asleep this shift

	// 1. Start with nothing
	minutes := 0

	// 2. Loop for all of the minutes of the shift
	for _, minute := range p.Asleep {

		// 3. If sleeping for this minute, add to total
		if minute {
			minutes++
		}
	}

	// 4. Return the number of minutes asleep
	return minutes
}

// ======================================================================
// end                      s h i f t . g o                     end
// ======================================================================
