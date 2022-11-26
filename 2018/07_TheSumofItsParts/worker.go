// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         w o r k e r . g o
// ======================================================================
// Worker for the Advent of Code 2018 Day 07 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                 Worker
// ======================================================================

type Worker struct {
	Part2  bool
	Text   string
	step   *Step
	start  int
	finish int
}

func NewWorker(part2 bool, text string) *Worker {
	// Worker Object for The Sum of Its Parts

	// 1. Set the initial values
	p := new(Worker)
	p.Part2 = part2
	p.Text = text
	return p
}

func (p *Worker) Assign(step *Step, start int) {
	// Assign a task to a worker
	p.start = start
	p.step = step
	p.finish = start + step.Cost
}

func (p *Worker) Work(now int) int {
	// Let the worker work

	// 1. If the worker has nothing to do, nothing gets done
	if p.step == nil {
		return 0
	}

	// 2. If the worker is done, so is the step
	if now >= p.finish {
		cost := p.step.Cost
		p.step.Complete()
		p.step = nil
		return cost
	}

	// 3. Not done
	return 0
}

// ======================================================================
// end                        w o r k e r . g o                       end
// ======================================================================
