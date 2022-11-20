// ======================================================================
// No Matter How You Slice It
//   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c l a i m . g o
// ======================================================================
// Claim for the Advent of Code 2018 Day 03 puzzle

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
	claimExp = regexp.MustCompile("\\d+")
)

// ----------------------------------------------------------------------
//                                                                Min/Max
// ----------------------------------------------------------------------

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// ======================================================================
//                                                                  Claim
// ======================================================================

type Claim struct {
	Part2    bool
	Number   int
	Text     string
	Left     int
	Top      int
	Width    int
	Height   int
	Right    int
	Bottom   int
	Conflict bool
}

func NewClaim(part2 bool, text string) *Claim {
	// Claim Object for No Matter How You Slice It

	// 1. Set the initial values
	p := new(Claim)
	p.Part2 = part2
	p.Text = text
	p.Conflict = false

	// 2. Process the text
	parts := claimExp.FindAllString(text, -1)
	if len(parts) != 5 {
		fmt.Printf("regexp failed for line '%s'\n", text)
		return nil
	}

	// 3. Save the parts
	p.Number, _ = strconv.Atoi(parts[0])
	p.Left, _ = strconv.Atoi(parts[1])
	p.Top, _ = strconv.Atoi(parts[2])
	p.Width, _ = strconv.Atoi(parts[3])
	p.Height, _ = strconv.Atoi(parts[4])

	// 4. Compute right and bottom
	p.Right = p.Left + p.Width - 1
	p.Bottom = p.Top + p.Height - 1

	// 5. Return the new clain
	return p
}

func (p *Claim) Overlap(other *Claim) []string {

	// 1. initially no overlap
	var overlaps []string

	// 2. Elimate nonconflicting claims
	//fmt.Printf("Overlap step 2 %d %d: p.Right=%d o.Left=%d p.Bottom=%d o.Top=%d\n",
	//	p.Number, other.Number, p.Right, other.Left, p.Bottom, other.Top)
	if p.Right < other.Left || p.Left > other.Right {
		return overlaps
	}
	if p.Bottom < other.Top || p.Top > other.Bottom {
		return overlaps
	}

	// 3. Determine the range of overlap
	left := Max(p.Left, other.Left)
	right := Min(p.Right, other.Right)
	top := Max(p.Top, other.Top)
	bottom := Min(p.Bottom, other.Bottom)
	//fmt.Printf("Overlap step 3 %d %d: left=%d right=%d top=%d bottom=%d\n",
	//	p.Number, other.Number, left, right, top, bottom)

	// 4. Loop for the overlap seats
	for col := left; col < right+1; col++ {
		for row := top; row < bottom+1; row++ {
			overlaps = append(overlaps, fmt.Sprintf("%dx%d", col, row))
		}
	}

	// 5. Mark the claims in conflict
	p.Conflict = true
	other.Conflict = true

	// 6. Return the overlaps
	//fmt.Printf("First=%s, Last=%s\n",
	//	overlaps[0], overlaps[len(overlaps)-1])
	return overlaps
}

// ======================================================================
// end                      c l a i m . g o                     end
// ======================================================================
