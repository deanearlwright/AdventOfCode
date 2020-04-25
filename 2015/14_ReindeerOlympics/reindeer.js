/* eslint-disable linebreak-style */
// ======================================================================
// Reindeer Olympics
//   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r e i n d e e r . j s
//
// A contestant for the Advent of Code 2015 Day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Reindeer
// ======================================================================

class Reindeer {
  // Reindeer can only either be flying (always at their top speed) or
  // resting (not moving at all), and always spend whole seconds in
  // either state.

  constructor(options) {
    // Create a Reindeet object

    // 1. Set the initial values
    this.name = options.name === undefined ? null : options.name;
    this.speed = options.speed === undefined ? null : options.speed;
    this.fly = options.fly === undefined ? null : options.fly;
    this.rest = options.rest === undefined ? null : options.rest;
    this.text = options.text === undefined ? null : options.text;
    this.distance = 0;
    this.atTick = 0;
    this.flyUntil = null;
    this.restUntil = null;
    this.points = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      // Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Regular Expression parser for reindeer
    // Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    const pattern = /([A-Z][A-Za-z]+) can fly ([0-9]+) km\/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds\./;

    // 2. Decompose input line
    const match = text.match(pattern);
    if (match) {
      // 3. Set reindeer values
      [, this.name, this.speed, this.fly, this.rest] = match;
      this.speed = parseInt(this.speed, 10);
      this.fly = parseInt(this.fly, 10);
      this.rest = parseInt(this.rest, 10);
    } else {
      // eslint-disable-next-line no-console
      console.log('Unable to parse input', text);
    }
  }

  start() {
    // On your mark, get set ...
    this.distance = 0;
    this.atTick = 0;
    this.flyUntil = this.fly;
    this.restUntil = null;
    this.points = 0;
  }

  tick() {
    // 1. Advance the clock
    this.atTick += 1;
    // 2. If flying, fly
    if (this.flyUntil !== null) {
      this.distance += this.speed;
      // 2a. Have we flown too long?
      if (this.atTick >= this.flyUntil) {
        this.flyUntil = null;
        this.restUntil = this.atTick + this.rest;
      }
      // 3. If resting, rest
    } else if (this.restUntil !== null) {
      if (this.atTick >= this.restUntil) {
        this.restUntil = null;
        this.flyUntil = this.atTick + this.fly;
      }
    } else {
      // eslint-disable-next-line no-console
      console.log('%s is neither flying nor resting at %d', this.name, this.atTick);
    }
  }

  goto(tick) {
    // 1. do it a tick at a time
    while (this.atTick < tick) {
      this.tick();
    }
  }

  reward() {
    this.points += 1;
  }
}

module.exports.Reindeer = Reindeer;
// ======================================================================
// end                      r e i n d e e r . j s                     end
// ======================================================================
