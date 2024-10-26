// ======================================================================
// Wait For It
//   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r a c e s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 06 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	timePrefix = "Time:"
	distPrefix = "Distance:"
	unKern     = ""
)

// ======================================================================
//                                                                  Races
// ======================================================================

// Races ... Object for Wait For It
type Races struct {
	Part2 bool
	Text  []string
	Races []*Race
}

// NewRaces ... Create a Races object
func NewRaces(part2 bool, text []string) (*Races, error) {

	// 1. Set the initial values
	p := new(Races)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Races object
	return p, nil
}

// processText ... Assign values from text
func (p *Races) processText(text []string) error {

	// 1. There should be two line of text
	if len(text) != 2 {
		return fmt.Errorf("expected 2 lines of text not %d", len(text))
	}

	// 2. First line is time and the second is record distance
	timeText := text[0]
	distText := text[1]

	// 3. Take off the prefixes
	cleanTime, found := strings.CutPrefix(timeText, timePrefix)
	if !found {
		return fmt.Errorf("missing prefix '%s' for '%s", timePrefix, timeText)
	}
	cleanDist, found := strings.CutPrefix(distText, distPrefix)
	if !found {
		return fmt.Errorf("missing prefix '%s' for '%s", distPrefix, distText)
	}

	// 4. Split the time and record distances
	times := strings.Fields(cleanTime)
	dists := strings.Fields(cleanDist)
	if len(times) != len(dists) {
		return fmt.Errorf("number of times (%d) is not the same as the number of distances (%d)",
			len(times), len(dists))
	}

	// 5. Part Two fixes "kerning"
	if p.Part2 {
		times = []string{strings.Join(times, unKern)}
		dists = []string{strings.Join(dists, unKern)}
	}

	// 6. Loop for the pairs of times and distances
	for indx := 0; indx < len(times); indx = indx + 1 {

		// 7. Get the time and record distances
		time := times[indx]
		dist := dists[indx]
		timeDist := time + timeDistCut + dist

		// 8. Create a single race
		race, err := NewRace(p.Part2, timeDist)
		if err != nil {
			return fmt.Errorf("unable to construct race from '%s': %s", timeDist, err)
		}

		// 9. Add this race in with the others
		p.Races = append(p.Races, race)
	}

	// 10. Return success
	return nil
}

// PartOne ... Returns the solution for part one
func (p *Races) PartOne(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 1

	// 2. Loop for all the races
	for _, race := range p.Races {

		// 3. Get the number of ways to with this race
		ways := race.WaysToBeatRecord()

		// 4. Keep running total
		result = result * ways
	}

	// 5. Return the solution for part one
	return fmt.Sprint(result)
}

// PartTwo ... Returns the solution for part two
func (p *Races) PartTwo(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 1

	// 2. Loop for all the races
	for _, race := range p.Races {

		// 3. Get the number of ways to with this race
		ways := race.WaysToBeatRecord()

		// 4. Keep running total
		result = result * ways
	}

	// 5. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                         r a c e s . g o                        end
// ======================================================================
