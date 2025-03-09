// ======================================================================
// Pulse Propagation
//   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c o n f i g u r a t i o n . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 20 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	PUSHES    = 1000
	ADDBUTTON = "button -> broadcaster"
	ADDSINK   = "%s -> *"
)

// ======================================================================
//                                                          Configuration
// ======================================================================

// Configuration ... Object for Pulse Propagation
type Configuration struct {
	Part2   bool
	Text    []string
	Modules map[string]*Module
	Pulses  []string
}

// NewConfiguration ... Create a Configuration object
func NewConfiguration(part2 bool, text []string) (*Configuration, error) {

	// 1. Set the initial values
	p := new(Configuration)
	p.Part2 = part2
	p.Text = text
	p.Modules = make(map[string]*Module)
	p.Pulses = make([]string, 0)

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Add the button to the configuration
	_, ok := p.Modules["broadcaster"]
	if ok {
		p.AddButton()
	}

	// 4. Determine the inputs for each module
	p.DetermineInputs()

	// 4. Return the new Configuration object
	return p, nil
}

// processText ... Assign values from text
func (p *Configuration) processText(text []string) error {

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Create a module from the line
		mod, err := NewModule(p.Part2, line)
		if err != nil {
			fmt.Printf("error creating module %d from '%s': %s\n", indx, line, err)
			return err
		}

		// 3. Save the module
		p.Modules[mod.Name] = mod
	}

	// 4. Return success
	return nil
}

// DetermineInputs ... Determine the inputs for each module
func (p *Configuration) DetermineInputs() {

	// 1. Loop for each module
	for _, mod := range p.Modules {

		// 2. Loop for each output of that module
		for _, output := range mod.Outputs {

			// 3. The output should exist
			outMod, ok := p.Modules[output]
			if !ok {
				fmt.Printf("Module '%s' output '%s' does not exist, adding\n", mod.Name, output)
				outMod = p.AddSink(output)
			}

			// 4. Add the input to the module
			outMod.AddInput(mod.Name)
		}
	}
}

// AddButton ... Add the button to the configuration
func (p *Configuration) AddButton() {

	// 1. Create a button module
	mod, err := NewModule(p.Part2, ADDBUTTON)
	if err != nil {
		fmt.Printf("error creating button module: %s\n", err)
		return
	}

	// 2. The button is its own input
	mod.AddInput(mod.Name)

	// 3. Save the button module
	p.Modules[mod.Name] = mod
}

// AddSink ... Add a module that just absorbes pulses
func (p *Configuration) AddSink(name string) *Module {

	// 1. Create a button module
	mod, err := NewModule(p.Part2, fmt.Sprintf(ADDSINK, name))
	if err != nil {
		fmt.Printf("error creating sink module %s: %s\n", name, err)
		return nil
	}

	// 2. Save the sink module
	p.Modules[mod.Name] = mod

	// 3. Return the new sink module
	return mod
}

// PushButtonOnce ... Push the button
func (p *Configuration) PushButtonOnce(push int) (int, int) {

	// 1. Reset the pulse queue
	p.Pulses = make([]string, 0)

	// 2. Push the button
	return p.NetworkPulse(push, "button Low broadcaster")
}

// PushButtonMulti ... Push the button multiple times
func (p *Configuration) PushButtonMulti(times int) (int, int) {

	// 1. Reset the pulse queue
	p.Pulses = make([]string, 0)

	// 2. Start with zero counts
	lowCount := 0
	highCount := 0

	// 3. Loop for the number of pushes
	for push := 1; push <= times; push++ {

		// 4. Push the button
		low, high := p.NetworkPulse(push, "button Low broadcaster")

		// 5. Accumulate the counts
		lowCount += low
		highCount += high
	}

	// 6. Return the accumulated counts
	return lowCount, highCount
}

func (p *Configuration) NetworkPulse(push int, pulse string) (int, int) {

	// 1. Start the counts at zero
	lowCount := 0
	highCount := 0

	// 2. Add the incoming pulse to the queue
	p.Pulses = append(p.Pulses, pulse)

	// 3. Loop until the queue is empty
	for len(p.Pulses) > 0 {

		// 4. Get the first pulse
		pulse, p.Pulses = p.Pulses[0], p.Pulses[1:]

		// 5. Get the from module, level and to module
		parts := strings.Split(pulse, " ")
		if len(parts) != 3 {
			fmt.Printf("unable to split '%s' into three parts\n", pulse)
			return 0, -1
		}

		// 6. Keep track of the pulse Levels
		switch parts[1] {
		case "Low":
			lowCount++
		case "High":
			highCount++
		}

		// 7. Get the receiving module
		mod, ok := p.Modules[parts[2]]
		if !ok {
			fmt.Printf("receiveing module '%s' for pulse '%s' does not exist\n", parts[2], pulse)
			return 0, -2
		}

		// 8. Pulse the module
		outLevel := mod.Pulse(push, pulse)

		// 9. Expand the outgoing pulse to the recipients and add them to the queue
		p.Pulses = append(p.Pulses, mod.OutputPulses(outLevel)...)
	}

	// 10. Return the counts
	return lowCount, highCount
}

// Reset ... Reset the configuration to the initial state
func (p *Configuration) Reset() {

	// 1. Reset each module
	for _, mod := range p.Modules {
		mod.Reset()
	}
}

// WhenLow ... Returns when module will receive the nth low pulse
func (p *Configuration) WhenLow(module string) int {

	// 1. Get the module
	mod, ok := p.Modules[module]
	if !ok {
		fmt.Printf("module '%s' does not exist\n", module)
		return -1
	}

	// 2. Verify the modules's inputs
	inputs := mod.Inputs
	if len(inputs) != 1 {
		fmt.Printf("module '%s' has %d inputs, not 1\n", module, len(inputs))
		return -2
	}
	input := inputs[0]

	// 3. Verify that the input is a conjunctions
	imod, ok := p.Modules[input]
	if !ok {
		fmt.Printf("input module '%s' does not exist\n", input)
		return -3
	}
	if imod.Type != CONJUNCTION {
		fmt.Printf("input module '%s' is not a conjunction\n", input)
		return -3
	}

	// 4. Run the configuration to get time of high inputs
	p.PushButtonMulti(10 * PUSHES)

	// 5. Get the time and cycle length of the high inputs
	result := 1
	for inp, highs := range imod.HighRecv {
		if len(highs) > 1 {
			if highs[0]*2 != highs[1] {
				fmt.Printf("input %s first=%d, next=%d, diff=%d\n", inp, highs[0], highs[1], highs[1]-highs[0])
			} else {
				result = result * highs[0]
			}
		} else {
			fmt.Printf("Not enough values for input %s\n", inp)
		}
	}

	// 6. Return when the module will receive the low pulse
	return result
}

// PartOne ... Returns the solution for part one
func (p *Configuration) PartOne(verbose bool, limit int) string {

	// 1. Return the solution for part one
	low, high := p.PushButtonMulti(PUSHES)
	return fmt.Sprintf("%d", low*high)
}

// PartTwo ... Returns the solution for part two
func (p *Configuration) PartTwo(verbose bool, limit int) string {

	// 1. Return the solution for part two
	at := p.WhenLow("rx")
	return fmt.Sprintf("%d", at)
}

// ======================================================================
// end                 c o n f i g u r a t i o n . g o                end
// ======================================================================
