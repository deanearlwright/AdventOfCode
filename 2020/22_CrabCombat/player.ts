// ======================================================================
// Crab Combat
//   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p l a y e r . t s
//
// Player for the Advent of Code 2020 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Player
// ======================================================================

export class Player {
  // Object for Crab Combat
  text: string[];

  part2: boolean;

  id: number;

  cards: number[];

  constructor(text: string[], part2 = false) {
    // Create a Player object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.id = 0;
    this.cards = [];

    // 2. Process Text
    if (this.text.length > 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Get player number and cards
    // 1. Loop for all of the lines of text
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];
      // 2. If this is the player line, save id
      if (line.startsWith('Player')) {
        this.id = parseInt(line.substr(7, 1), 10);
      } else {
        // 3. Otherwise save the card
        this.addCard(parseInt(line, 10));
      }
    }
  }

  addCard(card: number) {
    // Add a card to the player
    this.cards.push(card);
  }

  addCards(cards: number[]) {
    // Add multiple cards to the player
    this.cards = this.cards.concat(cards);
  }

  getTopCard(): number {
    // Returns the top card from the player's deck
    return this.cards.shift() || 0;
  }

  isEmpty(): boolean {
    // Returns true if the player has no more cards in the deck
    return this.cards.length === 0;
  }

  keep(high: number, low: number) {
    // Keep the cards from a round of the game
    this.addCard(high);
    this.addCard(low);
  }

  score(): number {
    // Return the score for these cards

    // 1. Start with nothing
    let result = 0;
    let multiplier = this.cards.length;

    // 2. Loop for all of the cards
    for (let indx = 0; indx < this.cards.length; indx += 1) {
      const card = this.cards[indx];
      // 3. Add in the score for this card
      result += card * multiplier;
      // 4. The next card is not worth as much
      multiplier -= 1;
    }
    // 5. Return the total score
    return result;
  }

  toString(): string {
    // Return the important information for this player
    return `${this.id}: ${this.cards.join(', ')} = ${this.score()}`;
  }

  hasAtLeast(amount: number): boolean {
    // Does the play have at least the specified number of cards?
    return this.cards.length >= amount;
  }

  clone(amount: number): Player {
    // Create a copy of the player with the top n cards

    // 1. Create a basic player
    const cloned = new Player([], this.part2);
    cloned.id = this.id;

    // 2. Copy the top few cards
    for (let indx = 0; indx < amount; indx += 1) {
      cloned.addCard(this.cards[indx]);
    }

    // 3. Return the new micro-Player
    return cloned;
  }
}

// ======================================================================
// end                        p l a y e r . t s                       end
// ======================================================================
