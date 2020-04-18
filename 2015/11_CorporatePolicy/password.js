/* eslint-disable linebreak-style */
// ======================================================================
// Corporate Policy
//   Advent of Code 2015 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a s s w o r d . j s
//
// A solver for the Advent of Code 2015 Day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Password
// ======================================================================

class Password {
  // Object for Corporate Policy

  constructor(options) {
    // Create a Password object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.current = null;

    // 2. Process text (if any)
    if (this.text !== null) {
      [this.current] = options.text;
      this.current = this.current.trim();
    }
  }

  static isValid(password) {
    const abcRe = /abc|bcd|cde|def|efg|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz/;
    const iolRe = /[^abcdefghjkmnpqrstuvwxyz]/;
    const pairRe = /aa|bb|cc|dd|ee|ff|gg|hh|jj|kk|mm|nn|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz/;
    if (password.length !== 8) {
      return false;
    }
    if (password.search(abcRe) === -1) {
      return false;
    }
    if (password.search(iolRe) !== -1) {
      return false;
    }
    const firstPair = password.search(pairRe);
    if (firstPair === -1) {
      return false;
    }
    const restPassword = password.slice(firstPair + 2);
    if (restPassword.search(pairRe) === -1) {
      return false;
    }
    return true;
  }

  static increment(current) {
    const iolRe = /[^abcdefghjkmnpqrstuvwxyz]/;
    const nextLetter = {
      a: 'b',
      b: 'c',
      c: 'd',
      d: 'e',
      e: 'f',
      f: 'g',
      g: 'h',
      h: 'j',
      i: 'j',
      j: 'k',
      k: 'm',
      l: 'm',
      m: 'n',
      n: 'p',
      o: 'p',
      p: 'q',
      q: 'r',
      r: 's',
      s: 't',
      t: 'u',
      u: 'v',
      v: 'w',
      w: 'x',
      x: 'y',
      y: 'z',
      z: 'a',
    };
    let nextPswd = current;
    while (nextPswd !== null) {
      const bad = nextPswd.search(iolRe);
      if (bad !== -1) {
        const before = nextPswd.substr(0, bad);
        const here = nextPswd.charAt(bad);
        const next = nextLetter[here];
        const after = 'aaaaaaaa'.substr(bad + 1);
        return before + next + after;
      }
      for (let i = 7; i > 0; i -= 1) {
        const before = nextPswd.substr(0, i);
        const here = nextPswd.charAt(i);
        const next = nextLetter[here];
        const after = nextPswd.substr(i + 1);
        nextPswd = before + next + after;
        if (next !== 'a') {
          return nextPswd;
        }
      }
    }
    return null;
  }

  static next(current) {
    let pswd = current;
    while (pswd !== null) {
      pswd = Password.increment(pswd);
      if (Password.isValid(pswd)) {
        return pswd;
      }
    }
    return pswd;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return Password.next(this.current);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Get the solution for part one
    const pswdOne = Password.next(this.current);
    // 1. Return the solution for part two
    return Password.next(pswdOne);
  }
}

module.exports.Password = Password;
// ======================================================================
// end                      p a s s w o r d . j s                     end
// ======================================================================
