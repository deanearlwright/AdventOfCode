/* eslint-disable linebreak-style */
// ======================================================================
// Does not He Have Intern Elves For This
//   Advent of Code 2015 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           n a u g h t y . j s
//
// A solver for the Advent of Code 2015 Day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Naughty
// ======================================================================

class Naughty {
  // Object for Does not He Have Intern Elves For This

  constructor(options) {
    // Create a Naughty object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;

    // 2. Process text (if any)
    if (this.text !== null) {
      // TODO process the test
    }
  }

  static itHasThreeVowels(word) {
    const vowels = word.match(/(['aeiou'])/g);
    return vowels != null && vowels.length > 2;
  }

  static itHasDoubleLetter(word) {
    const part1 = 'aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm';
    const part2 = 'nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz';
    const doubles = word.match(new RegExp(`(${part1}|${part2})`, 'g'));
    return doubles !== null;
  }

  static itHasBadSequence(word) {
    const badseq = word.match(/(ab|cd|pq|xy)/g);
    return badseq !== null;
  }

  static itHasTwoPairs(word) {
    if (word.length < 4) {
      return false;
    }
    for (let i = 0; i < word.length - 1; i += 1) {
      const letters = word.substr(i, 2);
      const other = word.lastIndexOf(letters);
      if (other >= i + 2) {
        return true;
      }
    }
    return false;
  }

  static itHasLetterWhatLetter(word) {
    const part1 = 'a.a|b.b|c.c|d.d|e.e|f.f|g.g|h.h|i.i|j.j|k.k|l.l|m.m';
    const part2 = 'n.n|o.o|p.p|q.q|r.r|s.s|t.t|u.u|v.v|w.w|x.x|y.y|z.z';
    const lwl = word.match(new RegExp(`(${part1}|${part2})`, 'g'));
    return lwl !== null;
  }

  isItNaughty(word) {
    if (!this.part2) {
      if (Naughty.itHasThreeVowels(word)
      && Naughty.itHasDoubleLetter(word)
      && !Naughty.itHasBadSequence(word)) {
        return false;
      }
      return true;
    }
    if (Naughty.itHasTwoPairs(word)
    && Naughty.itHasLetterWhatLetter(word)) {
      return false;
    }
    return true;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Start with none
    let knt = 0;
    // 2. Loop for all of the strings
    for (let i = 0; i < this.text.length; i += 1) {
      // 3. If it is nice, increment count
      if (!this.isItNaughty(this.text[i])) {
        knt += 1;
      }
    }
    // 4. Return the number of nice strings
    return knt;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Start with none
    let knt = 0;
    // 2. Loop for all of the strings
    for (let i = 0; i < this.text.length; i += 1) {
      // 3. If it is nice, increment count
      if (!this.isItNaughty(this.text[i])) {
        knt += 1;
      }
    }
    // 4. Return the number of nice strings
    return knt;
  }
}

module.exports.Naughty = Naughty;
// ======================================================================
// end                       n a u g h t y . j s                      end
// ======================================================================
