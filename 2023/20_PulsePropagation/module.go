// ======================================================================
// Pulse Propagation
//   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         m o d u l e . g o
// ======================================================================
// Module for the Advent of Code 2023 Day 20 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"maps"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	NONE = ""
	HIGH = "High"
	LOW  = "Low"

	BUTTON      = "*"
	FLIPFLOP    = "%"
	CONJUNCTION = "&"
	TYPES       = BUTTON + FLIPFLOP + CONJUNCTION
	BROADCASTER = ""
	SPLITTER    = " -> "
	COMMA       = ", "
	IGNORE      = "*"
)

// ======================================================================
//                                                                 Module
// ======================================================================

// Module ... Object for Pulse Propagation
type Module struct {
	Part2    bool
	Text     string
	Name     string
	Type     string
	Outputs  []string
	Inputs   []string
	Received map[string]string
	FlipFlop bool
	HighRecv map[string][]int
}

// NewModule ... Create a Module object
func NewModule(part2 bool, text string) (*Module, error) {
	// Module Object for Pulse Propagation

	// 1. Set the initial values
	p := new(Module)
	p.Part2 = part2
	p.Text = text
	p.Outputs = make([]string, 0)
	p.Inputs = make([]string, 0)
	p.Received = make(map[string]string)
	p.HighRecv = make(map[string][]int)

	// 2. Process text (if any)
	if text != "" {
		err := p.processText()
		if err != nil {
			return nil, err
		}
	}

	// 3. Return success
	return p, nil
}

// _processText ... Assign values from text
func (p *Module) processText() error {

	// 1. Split the text into parts
	parts := strings.Split(p.Text, SPLITTER)
	if len(parts) != 2 {
		return fmt.Errorf("unable to split '%s' into two parts", p.Text)
	}

	// 2. Save the output names
	if !strings.Contains(parts[1], IGNORE) {
		p.Outputs = strings.Split(parts[1], COMMA)
	}

	// 3. Get the type and name
	if strings.ContainsAny(parts[0], TYPES) {
		p.Type = string(parts[0][0])
		p.Name = parts[0][1:]
	} else {
		p.Type = BROADCASTER
		p.Name = parts[0]
	}

	// 4. Return success
	return nil
}

// AddInput ... Add an input to a module
func (p *Module) AddInput(from string) {

	p.Inputs = append(p.Inputs, from)
	p.Received[from] = LOW
	p.HighRecv[from] = make([]int, 0)
}

// Pulse ... Process a pulse
// Pulse processes an incoming pulse string and returns the resulting pulse string.
// Returns the resulting pulse string, which can be NONE, HIGH, or LOW.
func (p *Module) Pulse(push int, pulse string) string {

	// 1. Start with nothing
	result := NONE

	// 2. Validate the incoming pulse
	from, level, err := p.ValidatePulse(pulse)
	if err != nil {
		fmt.Printf("invalid pulse '%s' received at '%s': %s\n", pulse, p.Name, err)
		return ""
	}
	// fmt.Printf("'%s' pulse received at '%s' from='%s'\n", level, p.Name, from)

	// 3. Remember the pulse
	p.Received[from] = level
	if level == HIGH {
		p.HighRecv[from] = append(p.HighRecv[from], push)
	}

	// 3. Process the pulse
	switch p.Type {
	case FLIPFLOP:
		if level == LOW {
			if p.FlipFlop {
				p.FlipFlop = false
				result = LOW
			} else {
				p.FlipFlop = true
				result = HIGH
			}
		}
		// fmt.Printf("flipflow '%s' now %v sending '%s'\n", p.Name, p.FlipFlop, result)
	case CONJUNCTION:
		result = LOW
		for level := range maps.Values(p.Received) {
			if level == LOW {
				result = HIGH
				break
			}
		}
		// fmt.Printf("conjunction '%s' sending '%s'\n", p.Name, result)
	case BROADCASTER:
		if len(p.Outputs) == 0 {
			result = NONE
		} else {
			result = level
		}
		// fmt.Printf("broadcaster '%s' sending '%s'\n", p.Name, result)
	default:
		fmt.Printf("unknown type '%s' for '%s'\n", p.Type, p.Name)
	}

	// 4. Return the outgoing pulse (NONE, HIGH, or LOW)
	return result
}

// ValidatePulse validates an incoming pulse string.
//
// The pulse string is expected to be in the format "sender level recipient".
// The function performs the following checks:
// 1. Decodes the incoming pulse by splitting it into parts.
// 2. Ensures the pulse has exactly three parts.
// 3. Verifies that the sender is known.
// 4. Checks that the level is either HIGH or LOW.
// 5. Confirms that the recipient matches the module's name.
//
// Parameters:
//
//	pulse - the incoming pulse string to be validated.
//
// Returns:
//
//	sender - the sender part of the pulse string if validation is successful.
//	level - the level part of the pulse string if validation is successful.
//	err - an error if the validation fails, otherwise nil.
func (p *Module) ValidatePulse(pulse string) (string, string, error) {

	// 1. Decode the incoming pulse
	pulseParts := strings.Split(pulse, " ")

	// 2. Check the pulse
	if len(pulseParts) != 3 {
		return "", "", fmt.Errorf("invalid format")
	}
	_, ok := p.Received[pulseParts[0]]
	if !ok {
		return "", "", fmt.Errorf("invalid sender")
	}
	if HIGH != pulseParts[1] && LOW != pulseParts[1] {
		return "", "", fmt.Errorf("invalid level")
	}
	if pulseParts[2] != p.Name {
		return "", "", fmt.Errorf("invalid receipient")
	}

	// 2. Return success
	return pulseParts[0], pulseParts[1], nil
}

// OutputPulses generates a list of output pulses for the module based on the given level.
// It returns an empty list if the level is NONE.
//
// Parameters:
//   - level: A string representing the pulse level.
//
// Returns:
//   - A slice of strings, each representing an outgoing pulse in the format "ModuleName Level Output".
func (p *Module) OutputPulses(level string) []string {

	// 1. Start with nothing
	result := make([]string, 0)

	// 2. If no level, return nothing
	if level == NONE {
		return result
	}

	// 3. Create an outgoing pulse for each of the outputs
	for _, output := range p.Outputs {
		result = append(result, fmt.Sprintf("%s %s %s", p.Name, level, output))
	}

	// 4. Return the output pulses
	return result
}

// Reset ... Reset the module to the initial state
func (p *Module) Reset() {
	for input := range p.Received {
		p.Received[input] = LOW
		p.HighRecv[input] = make([]int, 0)
	}
	p.FlipFlop = false
}

// ======================================================================
// end                        m o d u l e . g o                       end
// ======================================================================
