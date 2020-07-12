// ======================================================================
// Two Steps Forward
//   Advent of Code 2016 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           d o o r s . t s
//
// A solver for the Advent of Code 2016 Day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Md5 } from 'ts-md5/dist/md5';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Path = string;
type Location = number;
type LocPath = string;
type Directions = 0 | 1 | 2 | 3;

type NextRoom = [number, number, number, number];
interface Room {
  location: Location;
  next: NextRoom;
  previous?: Room;
  path: Path;
  locPath: LocPath;
}
type Grid = Record<LocPath, Room>;

type XY = [number, number];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const locationConstant = 10;
const startX = 1;
const startY = 1;
const finishX = 4;
const finishY = 4;
const minLoc = 1;
const maxLoc = 4;
const badNext: Location = -1;
const up: Directions = 0;
const down: Directions = 1;
const left: Directions = 2;
const right: Directions = 3;

const dirLetter = 'UDLR';
const deltas = [-1, 1, -locationConstant, locationConstant];

const hashLocked = '01234567890a';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Doors
// ======================================================================

export class Doors {
  // Object for Two Steps Forward
  text: string[];

  part2: boolean;

  salt: string;

  start: Location;

  vault: Location;

  grid: Grid;

  constructor(text: string[], part2 = false) {
    // Create a Doors object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.salt = '';
    this.start = Doors.xyToLocation(startX, startY);
    this.vault = Doors.xyToLocation(finishX, finishY);
    this.grid = <Grid>{};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      [this.salt] = this.text;
    }

    // 3. Starting location
    const firstRoom = this.initialLocation();
    this.grid[firstRoom.locPath] = firstRoom;
  }

  initializeLocation(loc: Location, path: string): Room {
    const room: Room = {
      location: loc,
      next: this.doorsFromHere(loc, path),
      path,
      locPath: `${loc}${path}`,
    } as Room;
    return room;
  }

  doorsFromHere(loc: Location, path: string): NextRoom {
    // 1. Start with no doors
    // const locPath = `${loc}${path}`;
    const nextRoom: NextRoom = [NaN, NaN, NaN, NaN];
    // 2. Open doors based on the hash
    const hash = <string>Md5.hashStr(this.salt + path);
    for (let direction = 0; direction < 4; direction += 1) {
      if (hashLocked.indexOf(hash[direction]) >= 0) {
        nextRoom[direction] = badNext;
      } else {
        nextRoom[direction] = Doors.deltaLoc(loc, direction);
      }
    }
    // 3. Some doors are actually walls
    const [x, y] = Doors.locationToXY(loc);
    if (x === minLoc) nextRoom[left] = badNext;
    if (x === maxLoc) nextRoom[right] = badNext;
    if (y === minLoc) nextRoom[up] = badNext;
    if (y === maxLoc) nextRoom[down] = badNext;
    // 4. Return the doors
    // console.log(`Hash for loc=${locPath} seed=${this.salt} is
    //  ${ hash.substring(0, 4) } ${ Doors.showDoors(nextRoom) }`);
    // console.log(`U=${nextRoom[0]} D=${nextRoom[1]} L=${nextRoom[2]} R=${nextRoom[3]}`);
    return nextRoom;
  }

  static showDoors(doors: NextRoom): string {
    let openClosed = '';
    for (let direction = 0; direction < 4; direction += 1) {
      openClosed += doors[direction] === badNext ? '.' : dirLetter[direction];
    }
    return openClosed;
  }

  static areTheyAllLocked(doors: NextRoom): boolean {
    if (Doors.firstUnlocked(doors) === badNext) {
      return true;
    }
    return false;
  }

  static firstUnlocked(doors: NextRoom): number {
    // 1. Prefer down and to the wright
    if (doors[down] !== badNext) return down;
    if (doors[right] !== badNext) return right;
    // 2. What ever we can get
    for (let direction = 0; direction < 4; direction += 1) {
      if (doors[direction] !== badNext) {
        return direction;
      }
    }
    return badNext;
  }

  initialLocation(): Room {
    return this.initializeLocation(this.start, '');
  }

  static xyToLocation(x: number, y: number): Location {
    return x * locationConstant + y;
  }

  static locationToXY(loc: Location): XY {
    return [Math.trunc(loc / locationConstant), loc % locationConstant];
  }

  static deltaLoc(loc: Location, direction: number): Location {
    return loc + deltas[direction];
  }

  removeDoorFromPreviousRoom(room: Room): Room {
    const previousRoom = room.previous;
    if (previousRoom !== undefined && room.path.length > 0) {
      // const previousPath = room.path.substring(0, room.path.length - 1);
      const previousDir = room.path.substring(room.path.length - 1);
      const previousIndex = dirLetter.indexOf(previousDir);
      if (previousRoom.next[previousIndex] !== room.location) {
        console.log(`removeDoor No path from previous=${previousRoom.locPath} ${previousDir} ${Doors.showDoors(previousRoom.next)} to ${room.locPath}`);
        console.log(`U=${previousRoom.next[0]} D=${previousRoom.next[1]} L=${previousRoom.next[2]} R=${previousRoom.next[3]}`);
      } else {
        previousRoom.next[previousIndex] = badNext;
      }
      return previousRoom;
    }
    if (room.location !== this.start) {
      console.log(`removeDoorFromPreviousRoom loc=${room.locPath} has no previous room`);
    }
    return room;
  }

  pathToVault(room: Room, verbose = false, limit = 99): Room {
    let currentRoom = room;
    let nextRoom = room;
    if (verbose) console.log(`shortestPathTo loc=${room.location} path=${room.path} limit=${limit}`);
    // 1. Have we made it
    while (currentRoom.location !== this.vault && currentRoom.path.length < limit) {
      // 2. Is there a way out of this room?
      if (Doors.areTheyAllLocked(currentRoom.next)) {
        // 3. Can't go forward, try to back up
        if (currentRoom.previous === undefined) {
          if (verbose) console.log(`No previous room at location ${currentRoom.locPath}`);
          return currentRoom;
        }
        currentRoom = this.removeDoorFromPreviousRoom(currentRoom);
        if (verbose) console.log(`Backed up to room ${currentRoom.locPath} ${Doors.showDoors(currentRoom.next)}`);
      } else {
        const dirNum = Doors.firstUnlocked(currentRoom.next);
        const nextLocation = currentRoom.next[dirNum];
        const nextPath = currentRoom.path + dirLetter[dirNum];
        const locPath = `${nextLocation}${nextPath}`;
        if (locPath in this.grid) {
          nextRoom = this.grid[locPath];
          if (verbose) console.log(`Returning to room ${locPath} ${Doors.showDoors(nextRoom.next)} from room ${currentRoom.location}`);
          if (nextRoom.previous !== currentRoom) console.log(`Odd, previous of ${locPath} is ${nextRoom.previous} not ${currentRoom.locPath}`);
        } else {
          nextRoom = this.initializeLocation(nextLocation, nextPath);
          this.grid[locPath] = nextRoom;
          if (verbose) console.log(`Moved from ${currentRoom.location} to ${locPath} ${Doors.showDoors(nextRoom.next)}`);
          nextRoom.previous = currentRoom;
        }
        currentRoom = nextRoom;
      }
    }
    // 9. Made it to the vault
    this.removeDoorFromPreviousRoom(currentRoom);
    if (currentRoom.location !== this.vault) {
      if (verbose) console.log(`Reached limit of ${limit}`);
      return currentRoom;
    }
    if (verbose) console.log(`Found the vault at ${currentRoom.location} ${currentRoom.path}`);
    return currentRoom;
  }

  shortestPathTo(verbose = false, limit = 0): string {
    if (verbose) console.log(`shortestPathTo limit=${limit}`);
    // 1. Start with nothing
    let shortestPath = '';
    let shortestLength = 0;
    // 2. A very good place to start
    let startingRoom = this.grid[`${this.start}`];
    if (verbose) console.log(`shortestPathTo starting at ${startingRoom.locPath} ${Doors.showDoors(startingRoom.next)}`);
    // 3. Loop for all of the paths
    startingRoom = this.pathToVault(startingRoom, verbose, limit === 0 ? 99 : limit);
    while (startingRoom !== undefined && startingRoom.path.length > 0) {
      if (startingRoom.location === this.vault) {
        if (shortestLength === 0 || shortestLength > startingRoom.path.length) {
          shortestPath = startingRoom.path;
          shortestLength = shortestPath.length;
        }
      }
      if (verbose) console.log(`shortestPathTo re-starting at ${startingRoom.locPath} ${Doors.showDoors(startingRoom.next)}`);
      if (startingRoom.previous !== undefined) {
        startingRoom = this.pathToVault(startingRoom.previous, verbose, shortestLength);
      } else {
        break;
      }
    }
    return shortestPath;
  }

  longestPathTo(verbose = false, limit = 0): string {
    if (verbose) console.log(`shortestPathTo limit=${limit}`);
    // 1. Start with nothing
    let longestLength = 0;
    // 2. A very good place to start
    let startingRoom = this.grid[`${this.start}`];
    if (verbose) console.log(`longestPathTo starting at ${startingRoom.locPath} ${Doors.showDoors(startingRoom.next)}`);
    // 3. Loop for all of the paths
    startingRoom = this.pathToVault(startingRoom, verbose, limit === 0 ? 9999 : limit);
    while (startingRoom !== undefined && startingRoom.path.length > 0) {
      if (startingRoom.location === this.vault) {
        if (longestLength < startingRoom.path.length) {
          longestLength = startingRoom.path.length;
        }
      }
      if (verbose) console.log(`shortestPathTo re-starting at ${startingRoom.locPath} ${Doors.showDoors(startingRoom.next)}`);
      if (startingRoom.previous !== undefined) {
        startingRoom = this.pathToVault(startingRoom.previous, verbose, limit === 0 ? 9999 : limit);
      } else {
        break;
      }
    }
    return `${longestLength}`;
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.longestPathTo(verbose, limit);;
    }
    return this.shortestPathTo(verbose, limit);
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                         d o o r s . t s                        end
// ======================================================================
