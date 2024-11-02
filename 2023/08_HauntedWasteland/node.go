// ======================================================================
// Haunted Wasteland
//   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         n o d e . g o
// ======================================================================
// Node for the Advent of Code 2023 Day 08 puzzle

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
//
//	constants
//
// ----------------------------------------------------------------------
const (
	startNode       = "AAA"
	finishNode      = "ZZZ"
	startSuffix     = "A"
	finishSuffix    = "Z"
	left            = "L"
	right           = "R"
	invalidNodeName = "666"
)

var (
	reChk   *regexp.Regexp
	reParts *regexp.Regexp
)

func init() {
	reChk = regexp.MustCompile("^[A-Z0-9][A-Z0-9][A-Z0-9] = .[A-Z0-9][A-Z0-9][A-Z0-9], [A-Z0-9][A-Z0-9][A-Z0-9].$")
	reParts = regexp.MustCompile("[A-Z0-9][A-Z0-9][A-Z0-9]")
}

// ======================================================================
//                                                                   Node
// ======================================================================

// Node ... Object for Haunted Wasteland
type Node struct {
	Part2 bool
	Text  string
	Name  string
	Left  string
	Right string
}

// NewNode ... Create a Node object
func NewNode(part2 bool, text string) (*Node, error) {
	// Node Object for Haunted Wasteland

	// 1. Set the initial values
	p := new(Node)
	p.Part2 = part2
	p.Text = text

	// 2. Fill it in from the text
	if len(text) > 0 {

		// 3. Does it look like a node?
		chk := reChk.FindAllString(text, -1)
		if chk == nil {
			return nil, fmt.Errorf("text '%s' not in expected format", text)
		}

		// 4. Get the parts and save them
		parts := reParts.FindAllString(text, -1)
		if parts == nil {
			return nil, fmt.Errorf("unable to parse '%s'", text)
		}
		p.Name = parts[0]
		p.Left = parts[1]
		p.Right = parts[2]
	}

	// 5. Return success
	return p, nil
}

// IsStart ... Returns true if a start node
func (n *Node) IsStart() bool {
	if n.Part2 && strings.HasSuffix(n.Name, startSuffix) {
		return true
	}
	if !n.Part2 && n.Name == startNode {
		return true
	}
	return false
}

// IsFinish ... Returns true if a finish node
func (n *Node) IsFinish() bool {
	if n.Part2 && strings.HasSuffix(n.Name, finishSuffix) {
		return true
	}
	if !n.Part2 && n.Name == finishNode {
		return true
	}
	return false
}

// Next ... Returns the next node name going in the indicated direction
func (n *Node) Next(dir string) string {

	// 1. Go left or right
	switch dir {
	case left:
		return n.Left
	case right:
		return n.Right
	}

	// 2. Not a good direction
	fmt.Printf("invalid direction '%s' for node '%s", dir, n.Name)
	return invalidNodeName
}

// ======================================================================
// end                          n o d e . g o                         end
// ======================================================================
