// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s t e p s . g o
// ======================================================================
// Steps for the Advent of Code 2018 Day 07 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"sort"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                  Steps
// ======================================================================

type Steps struct {
	Part2   bool
	Text    []string
	Steps   map[string]*Step
	Letters string
	Initial string
	Final   string
}

func NewSteps(part2 bool, text []string) *Steps {
	// Steps Object for The Sum of Its Parts

	// 1. Set the initial values
	p := new(Steps)
	p.Part2 = part2
	p.Text = text
	p.Steps = make(map[string]*Step)

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.processText(p.Text)
	}

	// 3. Get all the step letters
	p.Letters = p.GetAllLetters()

	// 4. Determine initial step(s)
	p.Initial = p.InitialStep()

	// 5. Add the initial steps as completed
	p.AddInitialSteps()

	// 6. Determine final step(s)
	p.Final = p.FinalStep()

	// 7. Return the Steps
	return p
}

func (p *Steps) processText(text []string) {
	// Assign values from text

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Decode the line
		step := NewStep(p.Part2, line)
		if step == nil {
			fmt.Printf("Error Decoding line %d '%s'\n", indx, line)
			continue
		}

		// 3. Is there already a step, merge it
		other, found := p.Steps[step.Letter]
		if found {
			other.AddRule(step)
			continue
		}

		// 4. Else add this step
		p.Steps[step.Letter] = step
	}
}

func (p *Steps) GetAllLetters() string {
	// Determine the initial step(s)

	// 1. Start with nothing
	letters := make(map[string]bool)

	// 2. Loop for all the steps
	for _, step := range p.Steps {

		// 3. Add the step's letter
		letters[step.Letter] = true

		// 4. Add the letter(s) of the precursor(s)
		for letter := range step.Before {
			letters[letter] = true
		}
	}

	// 5. Sort the letters
	sorted := make([]string, 0, len(letters))
	for letter := range letters {
		sorted = append(sorted, letter)
	}
	sort.Strings(sorted)

	// 6. Return the sorted letters as a string
	return strings.Join(sorted, "")
}

func (p *Steps) InitialStep() string {
	// Determine the initial step(s) - that have no dependencies

	// 1. Start with nothing
	initial := make([]string, 0, len(p.Letters))

	// 2. Loop for all the letters
	for _, letter := range strings.Split(p.Letters, "") {

		// 3. if there is not rule for creation, this is an initial step
		_, found := p.Steps[letter]
		if !found {
			initial = append(initial, letter)
		}
	}

	// 4. Sort the letters (mainly for ease of testing)
	sort.Strings(initial)

	// 5. Return the initial steps as a string
	return strings.Join(initial, "")
}

func (p *Steps) AddInitialSteps() {
	// Add initial steps (which had to rules to define them)

	// 1. Loop for all the initial letters
	for _, letter := range strings.Split(p.Initial, "") {

		// 2. Create a String for the letter
		text := fmt.Sprintf("Step %s must be finished before step %s can begin.",
			letter, letter)

		// 3. Create a Step using that text
		step := NewStep(p.Part2, text)

		// 4. Add step to Steps
		p.Steps[letter] = step
	}
}

func (p *Steps) FinalStep() string {
	// Determine final step(s) that no one depend on

	// 1. Start with nothing
	final := make([]string, 0, len(p.Letters))
	before := make(map[string]bool)

	// 2. Loop for all the steps
	for _, step := range p.Steps {

		// 3. Collect all of the dependencies
		for key := range step.Before {
			before[key] = true
		}
	}

	// 4. Loop for all the letters
	for _, letter := range strings.Split(p.Letters, "") {

		// 5. if no one depends on it, it is a final step
		_, found := before[letter]
		if !found {
			final = append(final, letter)
		}
	}

	// 6. Sort the letters (mainly for ease of testing)
	sort.Strings(final)

	// 7. Return the initial steps as a string
	return strings.Join(final, "")
}

func (p *Steps) Completed() bool {
	// Return true if final step(s) is/are completed

	// 1. Loop for all the final steps
	for _, letter := range strings.Split(p.Final, "") {

		// 2. If this step not completed, return false
		if !p.Steps[letter].Completed {
			return false
		}
	}

	// 3. All final steps are completed, return true
	return true
}

func (p *Steps) Backlog() string {
	// Return list of items that need to be worked

	// 1. Start with nothing
	backlog := make([]string, 0, len(p.Letters))

	// 2. Loop for all the letters
	for _, letter := range strings.Split(p.Letters, "") {

		// 3. If the step is not completed add it to the list
		if !p.Steps[letter].Completed {
			backlog = append(backlog, letter)
		}
	}

	// 4. Return the steps that need to be completed
	return strings.Join(backlog, "")
}

func (p *Steps) CanDo(toDo string) string {
	// Return steps that can be done at this point

	// 1. Start with nothing
	canDo := make([]string, 0, len(p.Letters))

	// 2. Loop for all steps that can be done
	for _, letter := range strings.Split(toDo, "") {

		// 3. Loop for all the precursors of this step
		ready := true
		for need := range p.Steps[letter].Before {

			// 4. If a needed steps is not completed, this step is not ready
			if !p.Steps[need].Completed {
				ready = false
			}
		}

		// 5. If this step is ready to do, add it to the list
		if ready {
			canDo = append(canDo, letter)
		}
	}

	// 7. Return the steps that can be worked on
	return strings.Join(canDo, "")
}

func (p *Steps) AddCost(cost int) {
	// Add additional cost to each steps

	// 1. Loop for all the steps
	for _, step := range p.Steps {

		// 2. Add in the additional cost
		step.Cost = step.Cost + cost
	}
}

// ======================================================================
// end                         s t e p s . g o                        end
// ======================================================================
