// ======================================================================
// Memory Maneuver
//   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         n o d e . g o
// ======================================================================
// Node for the Advent of Code 2018 Day 08 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                   Node
// ======================================================================

type Node struct {
	numKids  int
	numMeta  int
	Childs   []*Node
	Metadata []int
}

func NewNode(text []string, index int) (*Node, int) {
	// Node Object for Memory Maneuver

	// 1. Set the initial values
	p := new(Node)
	indx := index

	// 2. Process text
	if indx+2 < len(text) {
		p.numKids, _ = strconv.Atoi(text[indx])
		p.numMeta, _ = strconv.Atoi(text[indx+1])
		indx = indx + 2
	}

	// 3. Save Child nodes
	p.Childs = make([]*Node, p.numKids)
	var child *Node
	for i := 0; i < p.numKids; i++ {
		child, indx = NewNode(text, indx)
		p.Childs[i] = child
	}

	// 4. Save metadata
	p.Metadata = make([]int, p.numMeta)
	for i := 0; i < p.numMeta; i++ {
		p.Metadata[i], _ = strconv.Atoi(text[indx+i])
	}

	// 4. Return the new node and index into
	return p, indx + p.numMeta
}

func (p *Node) Sum() int {
	// Sum the metadata numbers

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the metadata
	for _, num := range p.Metadata {

		// 3. Add to the sum
		result = result + num
	}

	// 4. Return the sum of the metadata
	return result
}

func (p *Node) SumAll() int {
	// Sum the metadata numbers

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the metadata in this Node
	for _, num := range p.Metadata {

		// 3. Add to the sum
		result = result + num
	}

	// 4. Loop for all the children in this Node
	for _, child := range p.Childs {

		// 5. Add to the sum of metadata of that child
		result = result + child.SumAll()
	}

	// 6. Return the total sum of the metadata
	return result
}

func (p *Node) Value() int {
	// Return the value of a node

	// 1. If there are no children, value is sum of metadata
	if p.numKids == 0 {
		return p.Sum()
	}

	// 2. Start with nothing
	result := 0

	// 3. Loop for all the metadata in this Node
	for _, num := range p.Metadata {

		// 4. Ignore the number if not a valid child index
		if num < 1 || num > p.numKids {
			continue
		}

		// 5. Get the value of the indexed child
		value := p.Childs[num-1].Value()

		// 6. Add the value to the total
		result = result + value
	}

	// 7. Return the total value of the indexed children
	return result
}

// ======================================================================
// end                          n o d e . g o                         end
// ======================================================================
