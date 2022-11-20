// ======================================================================
// No Matter How You Slice It
//   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         f a b r i c . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 03 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                  Fabric
// ======================================================================

// Object for No Matter How You Slice It

type Fabric struct {
	Part2  bool
	Text   []string
	Claims []*Claim
}

func NewFabric(part2 bool, text []string) *Fabric {

	// 1. Set the initial values
	p := new(Fabric)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.processText(p.Text)
	}

	return p
}

func (p *Fabric) processText(text []string) {
	// Assign values from text

	// 1. Loop for each line of the text
	for _, line := range text {

		// 2. Add the claim to the entries
		aClaim := NewClaim(p.Part2, line)
		if aClaim != nil {
			p.Claims = append(p.Claims, aClaim)
		}
	}
}

func (p *Fabric) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Start with no overlaps
	var overlaps = map[string]bool{}

	// 1. Loop for most of the claims
	for i := 0; i < len(p.Claims)-1; i++ {

		// 2. Loop for the remaining claims
		for j := i + 1; j < len(p.Claims); j++ {

			// 3. Get the conflicts between these two claims
			conflicts := (p.Claims[i]).Overlap(p.Claims[j])
			if verbose {
				fmt.Printf("Claim %d had %d overlaps with Claim %d\n",
					p.Claims[i].Number, len(conflicts), p.Claims[j].Number)
			}

			// 4. Add this conflicts in
			for _, conflict := range conflicts {
				overlaps[conflict] = true
			}
		}
	}

	// 5. Return the count of overlaps
	return strconv.Itoa(len(overlaps))
}

func (p *Fabric) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Process all the cross claims
	p.PartOne(false, 0)

	// 2. Search for the intact claim
	for _, claim := range p.Claims {

		// 3. If this is the intact claim, return its number
		if claim.Conflict == false {
			return strconv.Itoa(claim.Number)
		}
	}

	// 4. Didn't find an intact claim
	return ""
}

// ======================================================================
// end                        f a b r i c . g o                       end
// ======================================================================
