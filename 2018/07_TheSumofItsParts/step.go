// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s t e p . g o
// ======================================================================
// Step for the Advent of Code 2018 Day 07 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"regexp"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	COST_ORDER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

var reStep = regexp.MustCompile("[A-Z]")

// ======================================================================
//                                                                   Step
// ======================================================================

type Step struct {
	Part2     bool
	Text      string
	Letter    string
	Before    map[string]bool
	Completed bool
	Cost      int
}

func NewStep(part2 bool, text string) *Step {
	// Step Object for The Sum of Its Parts

	// 1. Set the initial values
	p := new(Step)
	p.Part2 = part2
	p.Text = text
	p.Letter = ""
	p.Before = make(map[string]bool)

	// 2. Process Text (if any)
	parts := reStep.FindAllString(text, -1)
	if len(parts) != 3 {
		fmt.Printf("unable to parse step '%s'\n", text)
		return nil
	}

	// 3. Step the step's name
	p.Letter = parts[2]

	// 4. Set the step that must be completed
	if parts[1] != parts[2] {
		p.Before[parts[1]] = true
	} else if !p.Part2 {
		p.Completed = true
	}

	// 5. Set the cost
	p.Cost = 1 + strings.Index(COST_ORDER, p.Letter)

	// 6. Return newly created step
	return p
}

func (p *Step) AddRule(other *Step) {
	// Combine two rules

	// 1. Check that they are for the same step
	if p.Letter != other.Letter {
		fmt.Printf("Unable to AddRule for step %s to step %s\n",
			other.Letter, p.Letter)
	}

	// 2. Copy before steps
	for key, _ := range other.Before {
		p.Before[key] = true
	}
}

func (p *Step) AddBefore(key string) {
	// Add a required step
	p.Before[key] = true
}

func (p *Step) IncreaseCost(more int) {
	// Add to the base cost
	p.Cost = p.Cost + more
}

func (p *Step) Complete() {
	// Complete this step

	// 1. Should only to this once
	if p.Completed {
		fmt.Errorf("Multiple completions for step %s", p.Letter)
	}

	// 2. Mark step as completed
	p.Completed = true
}

// ======================================================================
// end                          s t e p . g o                         end
// ======================================================================
