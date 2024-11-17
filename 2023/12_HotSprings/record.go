// ======================================================================
// Hot Springs
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         r e c o r d . g o
// ======================================================================
// Record for the Advent of Code 2023 Day 12 puzzle

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
//	constants
//
// ----------------------------------------------------------------------
const (
	spring  = "."
	damaged = "#"
	unknown = "?"
	comma   = ","
)

var (
	du = map[string]bool{
		spring:  false,
		damaged: true,
		unknown: true,
	}
	su = map[string]bool{
		spring:  true,
		damaged: false,
		unknown: true,
	}
)

// ======================================================================
//                                                                 Record
// ======================================================================

// Record ... Object for Hot Springs
type Record struct {
	Part2   bool
	Text    string
	Row     string
	Damaged []int
}

// NewRecord ... Create a Record object
func NewRecord(part2 bool, text string) (*Record, error) {
	// Record Object for Hot Springs

	// 1. Set the initial values
	p := new(Record)
	p.Part2 = part2
	p.Text = text

	// 2. Not much to do if no test
	if len(text) == 0 {
		return p, nil
	}

	// 3. Split the text at a blank
	row, damaged, found := strings.Cut(text, " ")
	if !found {
		return nil, fmt.Errorf("no blank in '%s'", text)
	}

	// 4. Save the spring row map
	p.Row = row

	// 5. Convert the damaged list into integers
	groups := strings.Split(damaged, ",")
	p.Damaged = make([]int, 0, len(groups))
	for _, group := range groups {
		number, err := strconv.Atoi(group)
		if err != nil {
			return nil, fmt.Errorf("bad number '%s' in '%s'", group, text)
		}
		p.Damaged = append(p.Damaged, number)
	}

	// 2. Return success
	return p, nil
}

// Arrangements ... How many different arrangements are there
func (p *Record) Arrangements(seen *Seen, partial string) int {

	// 1. If the is no partial use the row
	if partial == "" {
		return p.Arrangements(seen, p.Expand())
	}

	// 2. Do we already know the answer, return it
	value := seen.FindObservation(partial)
	if value >= 0 {
		return value
	}

	// 3. Split the partial into row and knts
	row, knts, found := strings.Cut(partial, " ")
	if !found {
		fmt.Printf("no blank in '%s'\n", partial)
		return -1
	}

	// 4. Recursive base cases
	if len(knts) == 0 {
		if strings.Contains(row, damaged) {
			return 0
		}
		return 1
	}
	if len(row) == 0 {
		return 0
	}

	// 5. Start with nothing
	result := 0

	// 6.Handle good or unknown
	first := string(row[0])
	val, ok := su[first]
	if !ok {
		fmt.Printf("unexpected su character '%s' in '%s'\n", first, partial)
		return -1
	}
	if val {
		result = result + p.Arrangements(seen, fmt.Sprintf("%s %s", row[1:], knts))
	}

	// 7. Handle damaged or unknown
	val, ok = du[first]
	if !ok {
		fmt.Printf("unexpected du character '%s' in '%s'\n", first, partial)
		return -1
	}
	if val {
		firstknt, restknts, _ := strings.Cut(knts, comma)
		knt0, err := strconv.Atoi(firstknt)
		if err != nil {
			fmt.Printf("bad number '%s' in '%s'\n", firstknt, partial)
			return -1
		}
		if knt0 <= len(row) && (!strings.Contains(row[:knt0], spring)) && (knt0 == len(row) || string(row[knt0]) != damaged) {
			result = result + p.Arrangements(seen, fmt.Sprintf("%s %s", row[1+knt0:], restknts))
		}
	}

	// 8. Save and return result
	err := seen.AddObservation(partial, result)
	if err != nil {
		fmt.Printf("observation error: %s\n", err)
	}
	return result
}

// Expand ... Expand to solve
func (p *Record) Expand() string {

	// 1. Get the Row and Damaged array as a string
	rs := p.Row
	ds := p.DamagedString()

	// 2. If Part 1, add stopper
	if !p.Part2 {
		return fmt.Sprintf("%s. %s", rs, ds)
	}

	// 3. For Part 2, every thing is five times as large
	return fmt.Sprintf("%s?%s?%s?%s?%s. %s,%s,%s,%s,%s", rs, rs, rs, rs, rs, ds, ds, ds, ds, ds)
}

// DamagedString ... Return damaged counts as string
func (p *Record) DamagedString() string {
	return strings.Trim(strings.Replace(fmt.Sprint(p.Damaged), " ", comma, -1), "[]")
}

// ======================================================================
// end                        r e c o r d . g o                       end
// ======================================================================
