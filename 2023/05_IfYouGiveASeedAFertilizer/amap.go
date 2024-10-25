// ======================================================================
// IfYouGiveASeedAFertilizer
//   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                            a m a p . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 05 puzzle

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
	colon    = ":"
	mapColon = " map:"
	toSplit  = "-to-"
)

// ======================================================================
//                                                                   Amap
// ======================================================================

// Amap ... Object for IfYouGiveASeedAFertilizer
type Amap struct {
	Part2  bool
	Text   string
	From   string
	To     string
	Ranges []*Maprange
}

// NewAmap ... Create new Amap from text
func NewAmap(part2 bool, text []string, start int) (*Amap, int, error) {

	// 1. Set the initial values
	p := new(Amap)
	p.Part2 = part2
	indx := 0
	var err error = nil

	// 2. Process text (if any)
	if len(text) > 0 {
		indx, err = p.processText(text, start)
		if err != nil {
			return nil, start, err
		}
	}

	// 3. Return the new Amap object
	return p, indx, nil
}

// processText ... Assign values from text
func (p *Amap) processText(text []string, start int) (int, error) {

	// 1. First line has to end with a colon
	first := strings.TrimSpace(text[start])
	// fmt.Printf("lines=%d, start=%d, first='%s'\n", len(text), start, first)
	toFrom, found := strings.CutSuffix(first, mapColon)
	if !found {
		return start, fmt.Errorf("first line (#%d) doesn't end with '%s': '%s'", start, mapColon, first)
	}
	p.Text = first

	// 2. Get the From and To from the first line text
	if !strings.Contains(toFrom, toSplit) {
		return start, fmt.Errorf("first line (#%d) doesn't contain '%s': '%s'", start, toSplit, first)
	}
	parts := strings.Split(toFrom, toSplit)
	if len(parts) != 2 {
		return start, fmt.Errorf("first line (#%d) had %d parts not 2: '%s'", start, len(parts), first)
	}
	p.From = parts[0]
	p.To = parts[1]

	// 3. Loop until we find another line ending with a colon and we run out of lines
	for indx := start + 1; indx < len(text); indx = indx + 1 {
		start = indx
		line := strings.TrimSpace(text[indx])
		// fmt.Printf("text[%d]='%s'\n", indx, line)
		if len(line) == 0 {
			continue
		}

		if strings.HasSuffix(line, colon) {
			// fmt.Printf("Breaking on colon, start=%d\n", start)
			break
		}

		// 4. Create a map range
		mr, err := NewMaprange(p.Part2, line)
		if err != nil {
			return indx, fmt.Errorf("unable to construct Maprange for line #%d: %s", indx, err)
		}

		// 5. Save the map range
		p.Ranges = append(p.Ranges, mr)
	}

	// 6. Return success
	return start, nil
}

// Next ... Returns the map number
func (p *Amap) Next(what int) int {

	// 1. Assume that the number is not mapped
	result := what

	// 2. Loop for all the mappings
	for _, maprange := range p.Ranges {

		// 3. Is it in this range?
		if maprange.IsInSourceRange(what) {
			return maprange.MapSourceToDest(what)
		}
	}

	// 9. Return the mapped number
	return result
}

// ======================================================================
// end                          a m a p . g o                         end
// ======================================================================
