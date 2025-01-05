// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p a t t e r n . g o
// ======================================================================
// Pattern for the Advent of Code 2023 Day 13 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	UNKNOWN = 0
	OFFGRID = -1
)

// ======================================================================
//                                                                Pattern
// ======================================================================

// Pattern ... Object for Point Of Incidence
type Pattern struct {
	Part2      bool
	Text       []string
	Rows       int
	Cols       int
	Reflection int
	Rotated    *Pattern
}

// NewPattern ... Create a Pattern object
func NewPattern(part2 bool, text string) (*Pattern, error) {
	// Pattern Object for Point Of Incidence

	// 1. Set the initial values
	p := new(Pattern)
	p.Part2 = part2
	if len(text) > 0 {
		p.Text = append(p.Text, text)
		p.Cols = len(text)
	}
	p.Rows = len(p.Text)

	// 2. Return success
	return p, nil
}

func (p *Pattern) HasText() bool {
	return p.Rows > 0
}

func (p *Pattern) AddText(text string) {
	if len(text) > 0 {
		p.Text = append(p.Text, text)
		p.Cols = len(text)
		p.Rows++
	}
}

// Rotate ... Creates a new pattern exchanging rows for columns
func (p *Pattern) Rotate() *Pattern {

	// 1. If it has already been generated, use it
	if p.Rotated != nil {
		return p.Rotated
	}

	// 2. Create a new empty pattern
	pattern, _ := NewPattern(p.Part2, "")

	// 3. Loop for every column in the text
	for cindx := range p.Cols {

		// 4. Start a new column
		column := ""

		// 5. Loop for all the rows in the pattern
		for _, row := range p.Text {

			// 6. Append this charater to the line
			column = column + string(row[cindx])
		}

		// 7. Add the columns as a row in the new pattern
		pattern.AddText(column)
	}

	// 8. Save and return the rotated pattern
	p.Rotated = pattern
	return pattern
}

// ExpRowDiff ... Get the expananded row differences
func (p *Pattern) ExpRowDiff(r1 int, r2 int) int {

	// 1. Start with difference between these rows
	result := p.RowDiff(r1, r2)

	// 2. If off the grid, no differences (recursion base case)
	if result == OFFGRID {
		return 0
	}

	// 3. Return the differences between these rows and the expanded rows
	return result + p.ExpRowDiff(r1-1, r2+1)
}

// AdjRowDiff ... Get the differences of Adjacent Rows
func (p *Pattern) AdjRowDiff() []int {

	// 1. Constuct a place for the results
	result := make([]int, p.Rows-1)

	// 2. Loop for the rows in the pattern
	for row := range p.Rows - 1 {

		// 3. Set the row difference
		result[row] = p.RowDiff(row, row+1)
	}

	// 4. Return the adjacent row differences
	return result
}

// RowDiff ... Return the number of differences between the two rows
func (p *Pattern) RowDiff(r1 int, r2 int) int {

	// 1. We have gone off the grid
	if r1 < 0 || r2 < 0 || r1 >= p.Rows || r2 >= p.Rows {
		return OFFGRID
	}

	// 2. Start with nothing
	result := 0

	// 3. Get the cooresponding row text
	t1 := p.Text[r1]
	t2 := p.Text[r2]

	// 4. Loop for every column
	for c := range p.Cols {

		// 5. Accumulate the number of differences
		if t1[c] != t2[c] {
			result++
		}
	}

	// 6. Return the number of differences
	return result
}

// FindReflection ... Find the reflection point (if any) for this pattern
func (p *Pattern) FindReflection() int {

	// 1. If we already know it, return it
	if p.Reflection != UNKNOWN {
		return p.Reflection
	}

	// 2. Assume that there isn't a reflection point
	result := OFFGRID

	// 3. Things must be perfect for Part 1, less so for Part 2
	limit := 0
	if p.Part2 {
		limit = 1
	}

	// 3. Loop for the adjacent differences rows
	for row, diff := range p.AdjRowDiff() {

		// 4. Need to start out with no (of just a few) differences
		if diff > limit {
			continue
		}

		// 5. Get the total differences
		expDiff := p.ExpRowDiff(row, row+1)

		// 6. If there are none, then we have the row
		if expDiff == limit {
			result = row + 1
			break
		}
	}

	// 7. Save and return the reflection point (if any)
	p.Reflection = result
	return result
}

// Score ... Return the number for the reflections in this pattern
func (p *Pattern) Score() int {

	// 1. Start with nothing
	result := 0

	// 2. If we don't know where the reflection is, try to find it.
	if p.Reflection == 0 {
		p.FindReflection()
	}

	// 3. If there is a reflection add it in
	if p.Reflection > 0 {
		result = p.Reflection
	}

	// 4. Is there a rotation, Get it's score
	if p.Rotated != nil {
		result = (result * 100) + p.Rotated.Score()
	}

	// 5. Return the total score for this pattern
	return result
}

// ======================================================================
// end                       p a t t e r n . g o                      end
// ======================================================================
