
# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ g o . p y
# ======================================================================
"Generates go base programming source files for Advent of Code"

AOC_DD_GO = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           a o c _ D D . g o
// ======================================================================
// Solve the puzzles for Advent of Code YYYY day DD

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "flag"
    "fmt"
    "os"
    "regexp"
    "strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
     SAVE_BLANK_LINES = false
)

// ----------------------------------------------------------------------
//                                                                globals
// ----------------------------------------------------------------------
var aocVerbose bool
var aocPart int
var aocLimit int
var aocInput string = "";

// ----------------------------------------------------------------------
//                                                          initialzation
// ----------------------------------------------------------------------

func init() {
  // Parse the command line options

  // 1. Create the command line parser
  flag.IntVar(&aocPart, "part", 1, "Part 1 or 2 of the puzzle")
  flag.IntVar(&aocPart, "p", 1, "Part 1 or 2 of the puzzle")
  flag.IntVar(&aocLimit, "limit", 0, "Optional execution limit")
  flag.IntVar(&aocLimit, "l", 0, "Optional execution limit")
  flag.BoolVar(&aocVerbose, "verbose", false, "Optional extra messages")
  flag.BoolVar(&aocVerbose, "v", false, "Optional extra messages")
  flag.StringVar(&aocInput, "input", "", "Input file name")
  flag.StringVar(&aocInput, "i", "", "Input file name")
}

// ----------------------------------------------------------------------
//                                                       parseCommandLine
// ----------------------------------------------------------------------

func parseCommandLine() {

    // 1. Parse the command line to aocXXXX variables
    flag.Parse()

    // 2. Verify that part is 1 or 2
    if aocPart != 1 && aocPart != 2 {
        fmt.Println("part (-p) must be 1 or 2")
        os.Exit(1)
    }

    // 3. If input file name not specified, get from unprocessed arguments
    if aocInput == "" {
        if flag.NArg() == 0 {
            fmt.Println("Input file name (-i) not specified")
            os.Exit(1)
        }
        aocInput = flag.Arg(0)
    }
}

// ----------------------------------------------------------------------
//                                                                partOne
// ----------------------------------------------------------------------

func partOne(verbose bool, limit int, input_lines []string) string {
    // Process part one of the puzzle

    // 1. Create the puzzle solver
    solver := NewCLASS(false, input_lines)

    // 2. Determine the solution for part one
    solution := solver.PartOne(verbose, limit)
    if solution == "" {
        fmt.Println("There is no solution")
    } else {
        fmt.Println("The solution for part one is " + solution)
    }

    // 3. Return result
    return solution
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

func partTwo(verbose bool, limit int, input_lines []string) string {
    // Process part two of the puzzle

    // 1. Create the puzzle solver
    solver := NewCLASS(true, input_lines)

    // 2. Determine the solution for part two
    solution := solver.PartTwo(verbose, limit)
    if solution == "" {
        fmt.Println("There is no solution")
    } else {
        fmt.Println("The solution for part two is " + solution)
    }

    // 3. Return result
    return solution
}

// ----------------------------------------------------------------------
//                                                               fromFile
// ----------------------------------------------------------------------

func fromFile(filepath string) []string {
    // 1. Read the file
    b, err := os.ReadFile(filepath)
    if err != nil {
        fmt.Print(err)
        os.Exit(2)
    }

    // 2. Return the contents as a string
    return fromText(string(b))
}

// ----------------------------------------------------------------------
//                                                               fromText
// ----------------------------------------------------------------------

func fromText(text string) []string {
    // Break the text into trimed, non-comment lines

    // 1. We start with no lines
    var result []string

    // 2. Break up the text into lines
    lines := regexp.MustCompile(`\\r?\\n`).Split(text, -1)

    // 3. Loop for lines in the text
    for _, line := range lines {

        // 4. Ignore comment lines and maybe blank lines
        if len(line) > 0 {
            if !strings.HasPrefix(line, "!") {
                result = append(result, line)
            }
        } else if SAVE_BLANK_LINES {
            result = append(result, "")
        }
    }

    // 5. Return a table of cleaned text lines
    return result
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

func main() {
    // Read the Advent of Code problem and solve it

    // 1. Get the command line options
    parseCommandLine()

    // 2. Read the puzzle file
    input_text := fromFile(aocInput)

    // 3. Process the appropiate part of the puzzle
    var result string
    if aocPart == 1 {
        result = partOne(aocVerbose, aocLimit, input_text)
    } else {
        result = partTwo(aocVerbose, aocLimit, input_text)
    }

    // 5. Set return code (0 if solution found, 2 if not)
    if len(result) > 0 {
        os.Exit(0)
    }
    os.Exit(2)
}

// ======================================================================
// end                         a o c _ D D . g o                      end
// ======================================================================
"""

MODULE_GO = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         M O D U L E . g o
// ======================================================================
// A solver for the Advent of Code YYYY Day DD puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "fmt"
    "os"
    "strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
)

// ======================================================================
//                                                                  CLASS
// ======================================================================

// Object for TITLE

type CLASS struct {
    Part2 bool
    Text  []string
    Numbers []int
}

func NewCLASS(part2 bool, text []string) (*CLASS, error) {

    // 1. Set the initial values
    p := new(CLASS)
    p.Part2 = part2
    p.Text = text

    // 2. Process text (if any)
    if p.Text != nil && len(p.Text) > 0 {
        err := p.processText(p.Text)
        if err != nil {
           return nil, err
        }
    }

    // 3. Return the new CLASS object
    return p, nil
}


func (p *CLASS) processText(text []string) error {
    // Assign values from text

    // 1. Loop for each line of the text
    for indx, line := range text {

        // 2. Add the number to the entries
        num, err := strconv.Atoi(line)
        if err != nil {
            return err
        }
        p.Numbers = append(p.Numbers, num)
    }
}

func (p *CLASS) PartOne(verbose bool, limit int) string {
    // Returns the solution for part one

    // 1. Return the solution for part one
    return ""
}


func (p *CLASS) PartTwo(verbose bool, limit int) string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return ""
}


// ======================================================================
// end                        M O D U L E . g o                       end
// ======================================================================
"""

MODULE_TEST_GO = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    M O D U L E _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code YYYY day DD, TITLE

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "testing"
    "github.com/stretchr/testify/assert"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
    MODULEExampleTest = `
`
    MODULEPartOneText = ""
    MODULEPartTwoText = ""

    MODULEPartOneResult = ""
    MODULEPartOneResult = ""
)

// ======================================================================
//                                                              TestCLASS
// ======================================================================

func TestCLASSEmptyInit(t *testing.T) {
    // Test the default CLASS creation

    // 1. Create default CLASS object
    obj, err := NewCLASS(false, fromText(""))
    assert.NoError(err)

    // 2. Make sure it has the default values
    assert.False(t, obj.Part2)
    assert.Len(t, obj.Text, 0)
    assert.Len(t, obj.Numbers, 0)
}

func TestCLASSTextInit(t *testing.T) {
    // Test the CLASS object creation from text

    // 1. Create CLASS object from text
    obj, err := NewCLASS(false, fromText(EXAMPLE_TEXT))
    assert.NoError(err)

    // 2. Make sure it has the expected values
    assert.False(t, obj.Part2)
    assert.Equal(t, len(obj.Text), len(obj.Numbers))
}

func TestCLASSPartOne(t *testing.T) {
    // Test part one example of CLASS object

    // 1. Create CLASS object from text
    obj, err := NewCLASS(false, fromText(MODULEPartOneText))
    assert.NoError(err)

    // 2. Make sure it has the expected values
    assert.False(t, obj.Part2)
    assert.Equal(t, len(obj.Text), len(obj.Numbers))

    // 3. Make sure it returns the expected solution
    result := obj.PartOne(false, 0)
    assert.Equal(t, MODULEPartOneResult, result)
}

func TestCLASSPartTwo(t *testing.T) {
    // Test part two example of CLASS object

    // 1. Create CLASS object from text
    obj, err := NewCLASS(true, fromText(MODULEPartTwoText))
    assert.NoError(err)


    // 2. Make sure it has the expected values
    assert.True(t, obj.Part2)
    assert.Equal(t, len(obj.Text), len(obj.Numbers))

    // 3. Make sure it returns the expected solution
    result := obj.PartTwo(false, 0)
    assert.Equal(t, MODULEPartTwoResult, result)
}

// ======================================================================
// end                  M O D U L E _ t e s t . g o                   end
// ======================================================================
"""

PART_ONE_TXT = """Advent of Code YYYY Day DD Part One

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

---// Day DD: TITLE -----

---// Part One -----

"""

PART_TWO_TXT = """Advent of Code YYYY Day DD Part Two

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

---// Day DD: TITLE -----

---// Part Two -----

"""

EXTRA_GO = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         E X T R A . g o
// ======================================================================
// OTHER for the Advent of Code YYYY Day DD puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
)

// ======================================================================
//                                                                 OTHER
// ======================================================================

type OTHER struct {
    Part2   bool
    Text    string
}

func NewOTHER(part2 bool, text string) (*OTHER, error) {
    // OTHER Object for TITLE

    // 1. Set the initial values
    p := new(OTHER)
    p.Part2 = part2
    p.Text = text

    // 2. Return success
    return p, nil
}

// ======================================================================
// end                      E X T R A . g o                     end
// ======================================================================
"""

EXTRA_TEST_GO = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    E X T R A _ t e s t . g o
// ======================================================================
// Test OTHER for Advent of Code YYYY day DD, TITLE

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "testing"
    "github.com/stretchr/testify/assert"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
    EXTRAText = ""
)

// ======================================================================
//                                                             TestOTHER
// ======================================================================

func TestOTHEREmptyInit(t *testing.T) {
    // Test the default OTHER creation

    // 1. Create default OTHER object
    obj, err := NewOTHER(false, "")
    assert.NoError(err)

    // 2. Make sure it has the default values
    assert.False(t, obj.Part2)
    assert.Len(t, obj.Text, 0)
    }
}

func TestOTHERTextInit(t *testing.T) {
    // Test the OTHER object creation from text

    // 1. Create default OTHER object
    obj, err := NewOTHER(false, EXTRAText)
    assert.NoError(err)

    // 2. Make sure it has the default values
    assert.False(t, obj.Part2)
    assert.Equal(t, len(obj.Text), len(EXTRAText))
}

// ======================================================================
// end                  E X T R A _ t e s t. g o                end
// ======================================================================
"""

GO_MOD = """
module DIR

go 1.22

require github.com/stretchr/testify v1.9.0
"""

GO_FILES = {
    'aoc_DD.go': AOC_DD_GO,
    'MODULE.go': MODULE_GO,
    'MODULE_test.go': MODULE_TEST_GO,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
    'go.mod': GO_MOD,
}

GO_EXTRA = {
    'EXTRA.go': EXTRA_GO,
    'EXTRA_test.go': EXTRA_TEST_GO,
}

GO_UPDATE = {}


def go_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Start with simple conversions
    result = {
        "YYYY": "%4d" % args.year,
        "DD": "%02d" % args.day,
        "D D": ' '.join(list("%02d" % args.day)),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
        "EXTRA": args.ename.lower(),
        "OTHER": args.ename.capitalize(),
        "E X T R A": ' '.join(list(args.ename.lower())),
        "DIR": "%02d_%s" % (args.day, ''.join(args.title))
    }

    # 9. Return the text converters
    return result


def go_after(args, converters, text):
    "Cleanup text"

    # 0. Precondition axioms
    assert args
    assert converters
    assert text

    # 9. Return the input text
    return text

# ======================================================================
# end                          a o c _ g o . p y                     end
# ======================================================================
