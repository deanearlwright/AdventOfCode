// ======================================================================
// Haunted Wasteland
//   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         m a p . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 08 puzzle

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
	startNodeName   = "AAA"
	endNodeName     = "ZZZ"
	startNodeSuffix = "A"
	endNodeSuffix   = "Z"
)

// ======================================================================
//                                                                    Map
// ======================================================================

// Map ... Object for Haunted Wasteland
type Map struct {
	Part2        bool
	Text         []string
	Instructions string
	InstIndx     int
	Network      map[string]*Node
}

// NewMap ... Create a Map object
func NewMap(part2 bool, text []string) (*Map, error) {

	// 1. Set the initial values
	p := new(Map)
	p.Part2 = part2
	p.Text = text
	p.Network = make(map[string]*Node, len(text))

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Map object
	return p, nil
}

// processText ... Assign values from text
func (p *Map) processText(text []string) error {

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. If we need instructions, add them
		if p.Instructions == "" {
			p.Instructions = line
			continue
		}

		// 3. Create a node from the map
		node, err := NewNode(p.Part2, line)
		if err != nil {
			return fmt.Errorf("error in line %d: %s", indx, err)
		}

		// 4. Add the node
		p.Network[node.Name] = node
	}

	// 5. Return success
	return nil
}

// NextInst ... Return the next instruction
func (p *Map) NextInst() string {

	// 1. Loop back to the front if reached the end
	if p.InstIndx >= len(p.Instructions) {
		p.InstIndx = 0
	}

	// 2. Get the next instruction
	result := p.Instructions[p.InstIndx]

	// 3. Get ready for the next call
	p.InstIndx = p.InstIndx + 1

	// 4. Return the instruction
	return string(result)
}

// StartToFinishSteps ... Return the number of steps to go from start to finish
func (p *Map) StartToFinishSteps(start string, end string) int {

	// 1. Have to start someplace
	result := 0
	p.InstIndx = 0
	here := start

	// 2. Loop until we get to the end
	for {

		// 3. Take a step
		result = result + 1
		here = p.Network[here].Next(p.NextInst())

		// 4. If this is the end, leave the loop
		if here == end {
			break
		}
	}

	// 5. Return the number of steps taken
	return result
}

// StartToFinishStepsTwo ... Return the number of steps to go from start to finish (for part two)
func (p *Map) StartToFinishStepsTwo(start string) int {

	// 1. Have to start someplace
	result := 0
	p.InstIndx = 0
	here := start

	// 2. Loop until we get to the end
	for {

		// 3. Take a step
		result = result + 1
		here = p.Network[here].Next(p.NextInst())

		// 4. If this is the end, leave the loop
		if strings.HasSuffix(here, endNodeSuffix) {
			break
		}
	}

	// 5. Return the number of steps taken
	return result
}

// AllStartToFinishStepsTwo ... Return the number of steps to go from all start to finish (for part two)
func (p *Map) AllStartToFinishStepsTwo() []int {

	// 1. Start with nothing
	result := make([]int, 0, len(p.Network))

	// 2. Loop for all of the start nodes
	for name := range p.Network {

		// 3. Ignore if not a starting node
		if !strings.HasSuffix(name, startNodeSuffix) {
			continue
		}

		// 4. Get the number of steps from this start to a finish
		steps := p.StartToFinishStepsTwo(name)

		// 5. Add these steps to the result
		result = append(result, steps)
	}

	// 6. Return the all the steps taken
	return result
}

// PartOne ... Returns the solution for part one
func (p *Map) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	return fmt.Sprint(p.StartToFinishSteps(startNodeName, endNodeName))
}

// PartTwo ... Returns the solution for part two
func (p *Map) PartTwo(verbose bool, limit int) string {

	// 1. Get the steps for each start
	allSteps := p.AllStartToFinishStepsTwo()

	// 2. Return the solution for part two
	return fmt.Sprint(LCM(allSteps))
}

// ======================================================================
// end                           m a p . g o                          end
// ======================================================================
