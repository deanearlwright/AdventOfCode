// ======================================================================
// Combo Breaker
//   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           h a n d s h a k e . t s
//
// A solver for the Advent of Code 2020 Day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const INITIAL_SUBJECT_NUMBER = 7;
const INITIAL_NUMBER = 1;
const DIVISOR = 20201227;
const HARD_LIMIT = 999999999;

// ======================================================================
//                                                              Handshake
// ======================================================================

export class Handshake {
  // Object for Combo Breaker
  text: string[];

  part2: boolean;

  cardPublic: number;

  cardPrivate: number;

  doorPublic: number;

  doorPrivate: number;

  constructor(text: string[], part2 = false) {
    // Create a Handshake object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.cardPublic = NaN;
    this.cardPrivate = NaN;
    this.doorPublic = NaN;
    this.doorPrivate = NaN;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.cardPublic = parseInt(this.text[0], 10);
      this.doorPublic = parseInt(this.text[1], 10);
    }
  }

  // eslint-disable-next-line class-methods-use-this
  transformNumber(num: number, privateKey: number): number {
    // Transfor the number using the private key (loop size)

    // 1. Always start with one
    let result = INITIAL_NUMBER;

    // 2. Loop private key times
    for (let indx = 0; indx < privateKey; indx += 1) {
      // 3. Set the value to itself multiplied by the subject number
      result *= num;

      // 4. Set the value to the remainder after dividing the value by 20201227
      result %= DIVISOR;
    }
    // 5. Return the transformed number
    return result;
  }

  // eslint-disable-next-line class-methods-use-this
  guessPrivate(publicKey: number): number {
    // Determine the private key from the public key

    // 1. Start with the initial subject number
    let value = INITIAL_NUMBER;

    // 2. Try various loop sized
    for (let indx = 0; indx < HARD_LIMIT; indx += 1) {
      // 3. Transform the current value
      value *= INITIAL_SUBJECT_NUMBER;
      value %= DIVISOR;

      // 4. If we are able to generate the public key, loop size is the private key
      if (value === publicKey) {
        return indx + 1;
      }
    }
    // 5. Hard limit failure
    return 0;
  }

  guessEncryptionKey(): number {
    // Deterine the encryption key that the handshake is trying to establish
    console.log(`The card's public key is ${this.cardPublic}`);
    console.log(`The door's public key is ${this.doorPublic}`);

    // 1. Determine th card's private key
    this.cardPrivate = this.guessPrivate(this.cardPublic);
    console.log(`The card's private key is ${this.cardPrivate}`);

    // 2. Determine the door's private key
    this.doorPrivate = this.guessPrivate(this.doorPublic);
    console.log(`The door's private key is ${this.doorPrivate}`);

    // 3. Have the card generate the encryption key
    const cardEncryption = this.transformNumber(this.doorPublic, this.cardPrivate);
    console.log(`The card's encryption key is ${cardEncryption}`);

    // 4. Have the door generate the encryption key
    const doorEncryption = this.transformNumber(this.cardPublic, this.doorPrivate);
    console.log(`The door's encryption key is ${doorEncryption}`);

    // 5. The encryption keys should be the same
    if (cardEncryption !== doorEncryption) {
      return NaN;
    }

    // 6. Return the shared encryption key
    return cardEncryption;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return this.guessEncryptionKey();
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                     h a n d s h a k e . t s                    end
// ======================================================================
