// ======================================================================
// Repose Record
//   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         g u a r d . g o
// ======================================================================
// Guard for the Advent of Code 2018 Day 04 puzzle

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
const ()

var (
	guardExp = regexp.MustCompile("\\d+")
)

// ======================================================================
//                                                                 Guard
// ======================================================================

type Guard struct {
	Part2  bool
	Text   string
	Number int
	Shifts map[string]*Shift
}

func NewGuard(part2 bool, text string) *Guard {
	// Guard Object for Repose Record

	// 1. Set the initial values
	p := new(Guard)
	p.Part2 = part2
	p.Text = text
	p.Number = 0
	p.Shifts = make(map[string]*Shift)

	// 2. Parse date and number
	parts := shiftExp.FindAllString(text, -1)
	if len(parts) != 6 {
		fmt.Printf("regexp failed for line '%s'\n", text)
		return nil
	}

	// 3. Set the guard's number
	p.Number, _ = strconv.Atoi(parts[5])

	// 4. Return the new guard
	return p
}

func (p *Guard) FallsAsleep(text string) {
	// Guard falls asleep

	// 1. Create a shift
	shift := NewShift(p.Part2, text)

	// 2. Is this a new shift or sleeping again?
	existing, ok := p.Shifts[shift.Date]
	if ok {
		existing.FallsAlseep(text)
	} else {
		p.Shifts[shift.Date] = shift
		shift.FallsAlseep(text)
	}
}

func (p *Guard) WakesUp(text string) {
	// Guard wakes up

	// 1. Create a shift
	shift := NewShift(p.Part2, text)

	// 2. There better be an existing shift
	existing, ok := p.Shifts[shift.Date]
	if !ok {
		fmt.Printf("Guard wakes up without fallsing asleep: '%s'\n", text)
		return
	}

	// 3. Wake the guard up from his sleep
	existing.WakesUp(text)
}

func (p *Guard) MinutesAsleep() int {
	// How long has the guard been sleeping?

	// 1. Start with nothing
	minutes := 0

	// 2. Loop for all of the shifts
	for _, shift := range p.Shifts {

		// 3. Accumulate the minutes asleep
		minutes = minutes + shift.MinutesAsleep()
	}

	// 4. Return the total minutes asleep
	return minutes
}

func (p *Guard) MostOftenSleeping() (int, int) {
	// Returns the minute where the guard is most often asleep

	// 1. Start with nothing
	timesAsleep := make([]int, 60)
	most := 0
	mostAt := 0

	// 2. Loop for all of the shifts
	for _, shift := range p.Shifts {

		// 3. Loop for all of the minutes of the shift
		for minute, asleep := range shift.Asleep {

			// 4. If asleep, increment the count for that minute
			if asleep {
				timesAsleep[minute]++
			}
		}
	}

	// 5. Find the minute with the most times asleep
	for minute, times := range timesAsleep {
		if times > most {
			most = times
			mostAt = minute
		}
	}

	// 6. Return the minute with the most times asleep
	return mostAt, most
}

// ======================================================================
// end                      g u a r d . g o                     end
// ======================================================================
