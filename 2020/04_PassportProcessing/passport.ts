// ======================================================================
// Passport Processing
//   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a s s p o r t . t s
//
// Passport for the Advent of Code 2020 Day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Fields = Record<string, string>;
type FieldsRe = Record<string, RegExp>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE = RegExp('([a-z][a-z][a-z]):([a-z0-9#]+)', 'g');
const REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
const FIELD_RE: FieldsRe = {
  byr: RegExp('^[0-9][0-9][0-9][0-9]$'),
  iyr: RegExp('^[0-9][0-9][0-9][0-9]$'),
  eyr: RegExp('^[0-9][0-9][0-9][0-9]$'),
  hgt: RegExp('^(?:[0-9][0-9][0-9]cm|[0-9][0-9]in)$'),
  hcl: RegExp('^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$'),
  ecl: RegExp('^(?:amb|blu|brn|gry|grn|hzl|oth)$'),
  pid: RegExp('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$'),
  cid: RegExp('^.*$'),
};

// ======================================================================
//                                                               Passport
// ======================================================================

export class Passport {
  // Object for Passport Processing
  text: string;

  part2: boolean;

  fields: Fields;

  numFields: number;

  constructor(text: string, part2 = false) {
    // Create a Passport object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.fields = {};
    this.numFields = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processFields();
    }
  }

  processFields() {
    // Process the field information in the text
    // 1. Match the field value pairs in the text
    const matches = Array.from(this.text.matchAll(RE));

    // 2. Loop for all of the field=value pairs
    for (let indx = 0; indx < matches.length; indx += 1) {
      const match = matches[indx];
      // 3. Get the field and value parts
      const field = match[1];
      const value = match[2];
      // 4. Add the field and value to the passport
      this.fields[field] = value;
      this.numFields += 1;
    }
  }

  is_valid(): boolean {
    // Returns true if the passport is valid

    // 1. Loop for all of the required fields
    for (let indx = 0; indx < REQUIRED.length; indx += 1) {
      const field = REQUIRED[indx];

      // 2. If passport does not contain the field, it is invalid
      //    (This is not very intuitive but it google says to do)
      if (!Object.prototype.hasOwnProperty.call(this.fields, field)) {
        return false;
      }
    }

    // 3. All fields found, for part 1 that is all you need
    if (!this.part2) {
      return true;
    }

    // 4. For part two, each field has validation criteria
    for (let indx = 0; indx < REQUIRED.length; indx += 1) {
      const field = REQUIRED[indx];

      // 5. If the field does not pass validation, the passport is invalid
      if (!this.is_field_valid(field)) {
        return false;
      }
    }

    // 6. All of the fields validate, so all is well
    return true;
  }

  is_field_valid(field: string): boolean {
    // Return true if the field passes the validation for that field

    // 1. Get the field value
    const value = this.fields[field];
    if (!value) {
      return false;
    }

    // 2. Validate the value using the appropiate regular expression
    if (!value.match(FIELD_RE[field])) {
      return false;
    }

    // 3. Do validation based on the field name, return false if validate fails
    let num = 0;
    switch (field) {
      case 'byr':
        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        num = +value;
        if (num < 1920 || num > 2002) {
          return false;
        }
        break;
      case 'iyr':
        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        num = +value;
        if (num < 2010 || num > 2020) {
          return false;
        }
        break;
      case 'eyr':
        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        num = +value;
        if (num < 2020 || num > 2030) {
          return false;
        }
        break;
      case 'hgt':
        // hgt (Height) - a number followed by either cm or in:
        // If cm, the number must be at least 150 and at most 193.
        // If in, the number must be at least 59 and at most 76.
        if (value.endsWith('cm')) {
          num = +value.substr(0, 3);
          if (num < 150 || num > 193) {
            return false;
          }
        } else if (value.endsWith('in')) {
          num = +value.substr(0, 2);
          if (num < 59 || num > 76) {
            return false;
          }
        } else {
          return false;
        }
        break;
      case 'hcl':
        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        break;
      case 'ecl':
        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        break;
      case 'pid':
        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        break;
      default:
        console.log(`Unexpected field: ${field}`);
    }

    // 9. It must be good
    return true;
  }
}

// ======================================================================
// end                      p a s s p o r t . t s                     end
// ======================================================================
