// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         w o r k e r s . g o
// ======================================================================
// Workers for the Advent of Code 2018 Day 07 puzzle

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
const ()

// ======================================================================
//                                                                Workers
// ======================================================================

type Workers struct {
	Part2   bool
	Text    string
	Workers []*Worker
}

func NewWorkers(part2 bool, text string) *Workers {
	// Workers Object for The Sum of Its Parts

	// 1. Set the initial values
	p := new(Workers)
	p.Part2 = part2
	p.Text = text
	p.Workers = make([]*Worker, 0, 99)

	// 2. Process Text
	if len(text) > 0 {
		number, ok := strconv.Atoi(text)
		if ok != nil {
			fmt.Printf("Unable to process Workers text '%s'", text)
			return nil
		}

		// 3. Create workers
		for i := 0; i < number; i++ {
			p.Workers = append(p.Workers, NewWorker(p.Part2, strconv.Itoa(i)))
		}
	}

	// 4. Return the workers
	return p
}

func (p *Workers) Manage(tasks string, steps *Steps, now int) int {
	// Manage the worker assignments

	// 1. Start with nothing
	assignments := 0

	// 2. Loop for all the tasks to assign
	for _, task := range strings.Split(tasks, "") {

		// 3. If already being worked, get another task
		if p.InWork(task) {
			continue
		}

		// 4. Find a worker for the task
		assigned := p.Assign(steps.Steps[task], now)

		// 5. If we couldn't find a worker, we are done for now
		if !assigned {
			break
		}

		// 6. Increment the number of assignments made
		assignments++
	}

	// 7. Return the number of assignments made
	return assignments
}

func (p *Workers) InWork(task string) bool {
	// Return true if this step is being worked

	// 1. Loop for all of the workers
	for _, worker := range p.Workers {

		// 2. If this worker is idle, can't be working it
		if worker.step == nil {
			continue
		}

		// 3. Is the worker working on this step
		if worker.step.Letter == task {
			return true
		}
	}

	// 4. No one is working on this step
	return false
}

func (p *Workers) Assign(step *Step, now int) bool {
	// Attempt to assign the step to a worker

	// 1. Loop for all of the workers
	for _, worker := range p.Workers {

		// 2. Ignore, a worker that is working?
		if worker.step != nil {
			continue
		}

		// 3. Assign this work
		worker.Assign(step, now)

		// 4. Return success
		return true
	}

	// 5. Couldn't find a free worker
	return false
}

func (p *Workers) Work(now int) {
	// Make the workers work

	// 1. Loop for all of the workers
	for _, worker := range p.Workers {

		// 2. Work that worker
		worker.Work(now)
	}
}

func (p *Workers) Display() string {
	// Display the workers and their assignments

	// 1. Start with nothing
	result := make([]string, 0, len(p.Workers))

	// 2. Loop for all of the workers
	for _, worker := range p.Workers {

		// 3. If the worker is working add the name of the step
		if worker.step != nil {
			result = append(result, worker.step.Letter)
		} else {

			// 4. Else just a period
			result = append(result, ".")
		}
	}

	// 5. Return the display of the workers
	return strings.Join(result, " ")
}

// ======================================================================
// end                       w o r k e r s . g o                      end
// ======================================================================
