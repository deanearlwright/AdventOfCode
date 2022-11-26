// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 07 puzzle

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
//                                                              constants
// ----------------------------------------------------------------------
const (
	DEFAULT_WORKERS = 5
	DEFAULT_SECONDS = 60
)

// ======================================================================
//                                                                 Solver
// ======================================================================

// Object for The Sum of Its Parts

type Solver struct {
	Part2 bool
	Text  []string
	Steps *Steps
	Elves *Workers
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text
	p.Steps = NewSteps(part2, text)

	// 2. Return newly created step
	return p
}

func (p *Solver) Path() string {
	// Determine Path to complete

	// 1. Start with the initial steps
	result := make([]string, 0, len(p.Steps.Letters))
	for _, letter := range strings.Split(p.Steps.Initial, "") {
		result = append(result, letter)
	}

	// 2. Loop until completed
	for !p.Steps.Completed() {

		// 3. Get the steps to be completed
		backlog := p.Steps.Backlog()
		if len(backlog) == 0 {
			fmt.Print("There should be something to work")
			break
		}

		// 4. Which of these can be worked
		workable := p.Steps.CanDo(backlog)

		// 5. We will do the first of these
		work := string(workable[0:1])
		p.Steps.Steps[work].Complete()

		// 6. Add the step to the list of Completed Steps
		result = append(result, work)
	}

	// 7. Return the steps as worked
	return strings.Join(result, "")
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Return the solution for part one
	return p.Path()
}

func (p *Solver) CrowdSource(verbose bool, number int) int {
	// Build the sleigh with helpers

	// 1. Create the workers
	p.Elves = NewWorkers(p.Part2, strconv.Itoa(number))

	// 2. Loop for each second
	for time := 0; time < 2000; time++ {

		// 3. Have them do some work
		p.Elves.Work(time)

		// 4. Have they done it all?
		if p.Steps.Completed() {
			return time
		}
		// 5. Get steps to be completed
		backlog := p.Steps.Backlog()
		tasks := p.Steps.CanDo(backlog)

		// 6. Assign work to the workers
		assigned := p.Elves.Manage(tasks, p.Steps, time)
		if verbose && assigned > 0 {
			fmt.Printf("%5d %s\n", time, p.Elves.Display())
		}
	}

	// 6. We ran out of time
	fmt.Println("Ran out of time")
	return -1
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Determine number of workers
	if limit == 0 {
		limit = DEFAULT_WORKERS
		p.Steps.AddCost(DEFAULT_SECONDS)
	}

	// 2. Return the solution for part two
	return strconv.Itoa(p.CrowdSource(verbose, limit))
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
