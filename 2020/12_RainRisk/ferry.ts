// ======================================================================
// Rain Risk
//   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           f e r r y . t s
//
// Ferry for the Advent of Code 2020 Day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Loc = [number, number];
type Dir = 'N' | 'E' | 'S' | 'W';
type Turn = 'L' | 'R';
type Inst = Loc | Dir | 'F';
type Facing = 0 | 1 | 2 | 3;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const FACING = ['N', 'E', 'S', 'W'];
const TURNING = { L: -1, R: 1 };
const DELTA = {
  N: [0, -1],
  S: [0, 1],
  E: [1, 0],
  W: [-1, 0],
};

// ======================================================================
//                                                                  Ferry
// ======================================================================

export class Ferry {
  // Object for Rain Risk
  part2: boolean;

  start: Loc;

  loc: Loc;

  facing: Facing;

  waypoint: Loc;

  constructor(part2 = false) {
    // Create a Ferry object

    // 1. Set the initial values
    this.part2 = part2 === undefined ? false : part2;
    this.start = [0, 0];
    this.loc = [0, 0];
    this.facing = 1; // east
    this.waypoint = [10, -1]; // 10 east, 1 north
  }

  manhattanDistance(): number {
    // Return the manhattan (taxicab) distance from start

    return Math.abs(this.start[0] - this.loc[0]) + Math.abs(this.start[1] - this.loc[1]);
  }

  execute(inst: string) {
    // Execute a navigation instruction

    // 1. Break the instruction into parts
    const letter = inst.substr(0, 1) as Inst;
    const amount = parseInt(inst.substr(1), 10);

    // 2. Execute instruction
    switch (letter) {
      case 'N':
      case 'S':
      case 'E':
      case 'W':
        this.executeMove(letter, amount);
        break;
      case 'F':
        this.executeForward(amount);
        break;
      case 'L':
      case 'R':
        this.executeTurn(letter, amount);
        break;
      default:
        console.log(`Invalid instruction ${inst}`);
    }
  }

  executeMove(dir: Dir, amount: number) {
    // Move the ferry (or the waypoint)

    // 1. get the delta for the direction
    const delta = DELTA[dir];

    // 2. For part 2, move the waypoint; for part 1, move the ferry
    if (this.part2) {
      this.waypoint[0] += amount * delta[0];
      this.waypoint[1] += amount * delta[1];
    } else {
      this.loc[0] += amount * delta[0];
      this.loc[1] += amount * delta[1];
    }
  }

  executeForward(amount: number) {
    // Move the ferry

    // 1. For part2, the data is the waypoint; for part 1, the direction of the ferry
    let delta = [0, 0];
    if (this.part2) {
      delta = this.waypoint;
    } else {
      const dir = FACING[this.facing] as Dir;
      delta = DELTA[dir];
    }

    // 2. Move the ferry
    this.loc[0] += amount * delta[0];
    this.loc[1] += amount * delta[1];
  }

  executeTurn(way: Turn, degrees: number) {
    // Turn the ferry (or the waypoint)

    // 1. For part2, turn the waypoint
    if (this.part2) {
      let newWayPoint: Loc = [0, 0];
      switch (way) {
        case 'R':
          switch (degrees) {
            case 90:
              newWayPoint = [-this.waypoint[1], this.waypoint[0]];
              break;
            case 180:
              newWayPoint = [-this.waypoint[0], -this.waypoint[1]];
              break;
            case 270:
              newWayPoint = [this.waypoint[1], -this.waypoint[0]];
              break;
            default:
              console.log(`Invalid degrees ${degrees} for ${way} turn`);
              break;
          }
          break;
        case 'L':
          switch (degrees) {
            case 90:
              newWayPoint = [this.waypoint[1], -this.waypoint[0]];
              break;
            case 180:
              newWayPoint = [-this.waypoint[0], -this.waypoint[1]];
              break;
            case 270:
              newWayPoint = [-this.waypoint[1], this.waypoint[0]];
              break;
            default:
              console.log(`Invalid degrees ${degrees} for ${way} turn`);
              break;
          }
          break;
        default:
          console.log(`Invalid turn ${way}`);
          break;
      }
      this.waypoint = newWayPoint;
    } else {
      // 2a. Get the turring values
      const amount = degrees / 90;
      const plusMinus = TURNING[way];

      // 2b. Do it
      this.facing = (4 + this.facing + amount * plusMinus) % 4 as Facing;
    }
  }
}

// ======================================================================
// end                         f e r r y . t s                        end
// ======================================================================
