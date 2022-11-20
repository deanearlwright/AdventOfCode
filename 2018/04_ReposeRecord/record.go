// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r e c o r d . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 04 puzzle

// Note: The solution presented here requires sorted.txt as input

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                  Record
// ======================================================================

// Object for Repose Record

type Record struct {
	Part2  bool
	Text   []string
	Guards map[int]*Guard
}

func NewRecord(part2 bool, text []string) *Record {

	// 1. Set the initial values
	p := new(Record)
	p.Part2 = part2
	p.Text = text
	p.Guards = make(map[int]*Guard, 0)

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.processText(p.Text)
	}

	return p
}

func (p *Record) processText(text []string) {
	// Assign values from text

	// 1. Start with no guard
	var guard *Guard

	// 2. Loop for each line of the SORTED text
	for _, line := range text {

		// 3. Process Guard, falls asleep, and wakes up action
		if strings.HasSuffix(line, "begins shift") {
			newGuard := NewGuard(p.Part2, line)
			oldGuard, ok := p.Guards[newGuard.Number]
			if ok {
				guard = oldGuard
			} else {
				p.Guards[newGuard.Number] = newGuard
				guard = newGuard
			}
		} else if strings.HasSuffix(line, "falls asleep") {
			guard.FallsAsleep(line)
		} else if strings.HasSuffix(line, "wakes up") {
			guard.WakesUp(line)
		} else if len(line) > 0 {
			fmt.Printf("unexpected line '%s'\n", line)
		}
	}
}

func (p *Record) mostMinutesAsleep() *Guard {
	// Find the guard with the most minutes asleep

	// 1. Start with nothing
	var hasMostMinutesAsleep *Guard
	var numberOfMinutesAsleep int

	// 2. Loop for all the Guards
	for _, guard := range p.Guards {

		// 3. Get the total number of minutes asleep
		thisGuardSleeps := guard.MinutesAsleep()

		// 4. If this is the most minutes so far, save it
		if thisGuardSleeps > numberOfMinutesAsleep {
			numberOfMinutesAsleep = thisGuardSleeps
			hasMostMinutesAsleep = guard
		}
	}

	// 5. Return the sleepest guard
	return hasMostMinutesAsleep
}

func (p *Record) mostAsleepAtMinute() (int, int, int) {
	// Return the guard most consistently asleep and when that is

	// 1. Start with nothing
	guardNumber := 0
	guardMinute := 0
	guardTimes := 0

	// 2. Loop for all the Guards
	for _, guard := range p.Guards {

		// 3. Get the minute and times most asleep
		minute, times := guard.MostOftenSleeping()

		// 4. If this is the most times so far, save it
		if times > guardTimes {
			guardNumber = guard.Number
			guardMinute = minute
			guardTimes = times
		}
	}

	// 5. Return the sleepest guard, sleepest minute, and times
	return guardNumber, guardMinute, guardTimes
}
func (p *Record) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Find the guard with the most minutes asleep
	sleepest := p.mostMinutesAsleep()

	// 2. Find the minute that the guard spends the most sleeping
	minute, _ := sleepest.MostOftenSleeping()

	// 3. Be verbose if requested
	if verbose {
		fmt.Printf("Guard %d was the sleepist and was most often asleep at minute %d\n",
			sleepest.Number, minute)
	}
	// 4. Return the solution for part one
	return strconv.Itoa(sleepest.Number * minute)
}

func (p *Record) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Get the most consistently sleepy guard
	number, minute, times := p.mostAsleepAtMinute()

	// 2. Be verbose if requested
	if verbose {
		fmt.Printf("Guard %d was asleep at minute %d %d times\n",
			number, minute, times)
	}
	// 3. Return the solution for part one
	return strconv.Itoa(number * minute)
}

// ======================================================================
// end                        r e c o r d . g o                       end
// ======================================================================
