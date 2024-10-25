// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         a l m a n a c . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 05 puzzle

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
//
//	types
//
// ----------------------------------------------------------------------
type mapOfMappings map[string]int

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	seedsColon = "seeds: "
)

var (
	toMaps = []string{"soil", "fertilizer", "water", "light", "temperature", "humidity", "location"}
)

// ======================================================================
//                                                                Almanac
// ======================================================================

// Almanac ... Object for IfYouGiveASeedAFertilizer
type Almanac struct {
	Part2 bool
	Text  []string
	Seeds []int
	Maps  []*Amap
	ToMap mapOfMappings
}

// NewAlmanac ... Create an Almanac object for IfYouGiveASeedAFertilizer
func NewAlmanac(part2 bool, text []string) (*Almanac, error) {

	// 1. Set the initial values
	p := new(Almanac)
	p.Part2 = part2
	p.Text = text
	p.ToMap = make(mapOfMappings, len(text))

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Almanac object
	return p, nil
}

// processText ... Assign values from text
func (p *Almanac) processText(text []string) error {
	// Assign values from text

	// 1. First line is the seeds
	seeds, found := strings.CutPrefix(text[0], seedsColon)
	if !found {
		return fmt.Errorf("first line '%s' does not start with '%s'", text[0], seedsColon)
	}

	for indx, seed := range strings.Split(seeds, blank) {
		number, err := strconv.Atoi(seed)
		if err != nil {
			return fmt.Errorf("unable to convert %d seed '%s' of line '%s'", indx, seed, text[0])
		}
		p.Seeds = append(p.Seeds, number)
	}

	// 2. Process the maps
	for indx := 1; indx < len(text); {

		// 3. Get the next map
		amap, next, err := NewAmap(p.Part2, text, indx)
		if err != nil {
			return err
		}

		// 4. Save the map
		p.Maps = append(p.Maps, amap)
		p.ToMap[amap.To] = len(p.Maps) - 1

		// 5. Onward to the next map (or the end of text)
		indx = next
		if indx+1 >= len(text) {
			indx = len(text)
		}
	}

	// 6. Make sure we got all the maps
	for _, tomap := range toMaps {
		_, found := p.ToMap[tomap]
		if !found {
			return fmt.Errorf("almanac missing %s to mapping", tomap)
		}
	}

	// 7. Return success
	return nil
}

// GetLocationForSeed ... Return the location for a given seed
func (p *Almanac) GetLocationForSeed(seed int) int {

	// 1. Start with the seed
	result := seed

	// 2. Loop for all the To mappings
	for _, tomap := range toMaps {
		mapNumber := p.ToMap[tomap]

		// 3. Do this convertion
		result = p.Maps[mapNumber].Next(result)

	}

	// 4. Return the location
	return result
}

// PartOne ... Returns the solution for part one
func (p *Almanac) PartOne(verbose bool, limit int) string {

	// 1. Start with a very big location
	result := 999999999999

	// 2. Loop for all the seeds
	for _, seed := range p.Seeds {

		// 3. Get the location for that seed
		loc := p.GetLocationForSeed(seed)

		// 4. Get the nearest (lowest) location
		result = min(result, loc)
	}

	// 5. Return the solution for part one
	return fmt.Sprint(result)
}

// PartTwo ... Returns the solution for part two
func (p *Almanac) PartTwo(verbose bool, limit int) string {

	// 1. Start with a very big location
	result := 999999999999

	// 2. Loop for all the seeds/index pairs
	for indx := 0; indx < len(p.Seeds); indx = indx + 2 {

		// 3. Loop for all the seeds
		for offset := 0; offset < p.Seeds[indx+1]; offset = offset + 1 {

			// 4. Get the location for that seed
			loc := p.GetLocationForSeed(p.Seeds[indx] + offset)

			// 5. Get the nearest (lowest) location
			result = min(result, loc)
		}
	}

	// 6. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                       a l m a n a c . g o                      end
// ======================================================================
