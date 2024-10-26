// ======================================================================
// Wait For It
//   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r a c e . g o
// ======================================================================
// Race for the Advent of Code 2023 Day 06 puzzle

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	timeDistCut = " "
)

// ======================================================================
//                                                                   Race
// ======================================================================

// Race ... Object for Wait For It
type Race struct {
	Part2  bool
	Text   string
	Time   int
	Record int
}

// NewRace ... Create a Race object
func NewRace(part2 bool, text string) (*Race, error) {
	// Race Object for Wait For It

	// 1. Set the initial values
	p := new(Race)
	p.Part2 = part2
	p.Text = strings.TrimSpace(text)

	// 2. Handle empty input
	if len(p.Text) == 0 {
		return p, nil
	}

	// 3. Separate the time and record distance
	time, dist, found := strings.Cut(p.Text, timeDistCut)
	if !found {
		return nil, fmt.Errorf("expected '%s' in text '%s'", timeDistCut, text)
	}

	// 4. Convert and save the race time and record distance
	num, err := strconv.Atoi(strings.TrimSpace(time))
	if err != nil {
		return nil, fmt.Errorf("unable to convert time '%s' in '%s'", time, text)
	}
	p.Time = int(num)
	num, err = strconv.Atoi(strings.TrimSpace(dist))
	if err != nil {
		return nil, fmt.Errorf("unable to convert distance '%s' in '%s'", dist, text)
	}
	p.Record = int(num)

	// 5. Return success
	return p, nil
}

// DoesItBeat ... Does this hold time beat the record?
func (p *Race) DoesItBeat(holdTime int) bool {

	// 1. Handle bad hold times
	if holdTime < 0 || holdTime > p.Time {
		return false
	}

	// 2. Compute the distance
	distance := holdTime * (p.Time - holdTime)

	// 3. Does it beat the record?
	return distance > p.Record
}

// WaysToBeatRecord ... Return how many way the record can be beat
func (p *Race) WaysToBeatRecord() int {

	// 1. Get the minimum and maximun hold times to beat the record
	minHT, maxHT := p.MinMaxHoldTimes()

	// 2. Might not be able to beat the record
	if minHT == 0 && maxHT == 0 {
		return 0
	}

	// 3. Or there could be only one
	if minHT == maxHT {
		return 1
	}

	// Or there could be several
	return 1 + maxHT - minHT
}

// MinMaxHoldTimes ... Returns the minimum and maximum hold times to beat record
func (p *Race) MinMaxHoldTimes() (int, int) {

	// 1. Calculate the discriminate
	disc := p.Time*p.Time - 4*p.Record

	// 2. If less than zero, it can't be beat
	if disc < 0 {
		return 0, 0
	}

	// 3. If zero than single time
	if disc == 0 {
		return p.Time / 2, p.Time / 2
	}

	// 4. Else two times
	root := math.Sqrt(float64(disc))
	minus := ((float64(-p.Time) - root) / -2.0)
	plus := ((float64(-p.Time) + root) / -2.0)
	fmt.Printf("disc=%d, root=%f, minus=%f, plus=%f\n", disc, root, minus, plus)
	return int(math.Ceil(math.Min(minus, plus) + .001)), int(math.Floor(math.Max(minus, plus) - .001))
}

// ======================================================================
// end                          r a c e . g o                         end
// ======================================================================
