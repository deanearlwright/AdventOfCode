// ======================================================================
// Hot Springs
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r e c o r d s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 12 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                Records
// ======================================================================

// Records ... Object for Hot Springs
type Records struct {
	Part2   bool
	Text    []string
	Records []*Record
}

// NewRecords ... Create a Records object
func NewRecords(part2 bool, text []string) (*Records, error) {

	// 1. Set the initial values
	p := new(Records)
	p.Part2 = part2
	p.Text = text
	p.Records = make([]*Record, 0, len(p.Text))

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText()
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Records object
	return p, nil
}

// processText ... Assign values from text
func (p *Records) processText() error {

	// 1. Loop for each line of the text
	for indx, line := range p.Text {

		// 2. Create a spring record
		record, err := NewRecord(p.Part2, line)
		if err != nil {
			return fmt.Errorf("error in line %d: %s", indx, err)
		}

		// 3. Save the record
		p.Records = append(p.Records, record)
	}

	// 4. Return success
	return nil
}

// PartOne ... Returns the solution for part one
func (p *Records) PartOne(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 0
	seen, err := NewSeen(p.Part2)
	if err != nil {
		fmt.Printf("unexpected error in NewSeen() %s", err)
		return ""
	}

	// 2. Loop for every records
	for indx, record := range p.Records {

		// 3. Get the number of possible arrangements for this record
		knt := record.Arrangements(seen, "")
		if knt <= 0 {
			fmt.Printf("problem computing the number of arrangements for record %d", indx)
			return ""
		}

		// 4. Accumulate the number of possible arrangements
		result = result + knt
	}

	// 5. Return the solution for part one
	return fmt.Sprint(result)
}

// PartTwo ... Returns the solution for part two
func (p *Records) PartTwo(verbose bool, limit int) string {

	// 1. Start with nothing
	result := 0

	// 2. Loop for every records
	for indx, record := range p.Records {

		// 3. Get the number of possible arrangements for this record
		seen, err := NewSeen(p.Part2)
		if err != nil {
			fmt.Printf("unexpected error in NewSeen() %s", err)
			return ""
		}
		knt := record.Arrangements(seen, "")
		if knt <= 0 {
			fmt.Printf("problem computing the number of arrangements for record %d", indx)
			return ""
		}
		fmt.Printf("%d: %d\n", indx, knt)

		// 4. Accumulate the number of possible arrangements
		result = result + knt
	}

	// 5. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                       r e c o r d s . g o                      end
// ======================================================================
