/* eslint-disable linebreak-style */
// ======================================================================
// All in a Single Night
//   Advent of Code 2015 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r o u t e s . j s
//
// A solver for the Advent of Code 2015 Day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Routes
// ======================================================================

class Routes {
  // Object for All in a Single Night

  constructor(options) {
    // Create a Routes object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.cities = {};
    this.number = 0;
    this.shortest = null;
    this.distance = null;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.cities = {};
    this.number = 0;
    const pattern = /([A-Z][A-Za-z]+) to ([A-Z][A-Za-z]+) = ([0-9]+)/;

    // 2. Loop for each line of the input
    text.forEach((line) => {
      // 3. Decompose input line into cities and distance
      const match = line.match(pattern);
      if (match) {
        const startCity = match[1];
        const endCity = match[2];
        const distance = parseInt(match[3], 10);

        // 4. Add to cities dictionary
        this.addCities(startCity, endCity, distance);
        this.addCities(endCity, startCity, distance);
      } else {
        // eslint-disable-next-line no-console
        console.log('Unable to parse input', line);
      }
    });
  }

  addCities(fromCity, toCity, distance) {
    if (!(fromCity in this.cities)) {
      this.cities[fromCity] = {};
      this.number += 1;
    }
    this.cities[fromCity][toCity] = distance;
  }

  verifyDistance(route) {
    const cities = route.split(' -> ');
    if (cities.length !== this.number) {
      return -1;
    }
    return this.calculateDistance(cities);
  }

  calculateDistance(cities) {
    let distance = 0;
    for (let i = 0; i < cities.length - 1; i += 1) {
      distance += this.cities[cities[i]][cities[i + 1]];
    }
    return distance;
  }

  findShortRoute(startAt, maximum = null, distance = 0, cities = null) {
    // 1. If there are no cities, there are no routes
    if (this.number === 0) {
      return null;
    }
    // 2. If we have been to all cities, return list if distance less than maximum (if any)
    const beenTo = cities === null ? [startAt] : cities.slice(0);
    if (beenTo.length === this.number) {
      if (maximum === null || distance < maximum) {
        return beenTo;
      }
      return null;
    }
    // 3. Loop for all cities from this one calculating final distances
    let shortestDistance = maximum;
    let shortestRoute = null;
    Object.keys(this.cities[startAt]).forEach((next) => {
      const delta = this.cities[startAt][next];
      const newDistance = distance + delta;
      if ((!beenTo.includes(next))
       && (shortestDistance === null || newDistance < shortestDistance)) {
        beenTo.push(next);
        const route = this.findShortRoute(next, shortestDistance, newDistance, beenTo);
        if (route != null) {
          const routeDistance = this.calculateDistance(route);
          if (shortestDistance === null || routeDistance < shortestDistance) {
            shortestDistance = routeDistance;
            shortestRoute = route.slice(0);
          }
        }
        beenTo.pop();
      }
    });
    return shortestRoute;
  }

  findLongRoute(startAt, minimum = null, distance = 0, cities = null) {
    // 1. If there are no cities, there are no routes
    if (this.number === 0) {
      return null;
    }
    // 2. If we have been to all cities, return list if distance less than maximum (if any)
    const beenTo = cities === null ? [startAt] : cities.slice(0);
    if (beenTo.length === this.number) {
      if (minimum === null || distance > minimum) {
        return beenTo;
      }
      return null;
    }
    // 3. Loop for all cities from this one calculating final distances
    let longestDistance = minimum;
    let longestRoute = null;
    Object.keys(this.cities[startAt]).forEach((next) => {
      const delta = this.cities[startAt][next];
      const newDistance = distance + delta;
      if (!beenTo.includes(next)) {
        beenTo.push(next);
        const route = this.findLongRoute(next, longestDistance, newDistance, beenTo);
        if (route != null) {
          const routeDistance = this.calculateDistance(route);
          if (longestDistance === null || routeDistance > longestDistance) {
            longestDistance = routeDistance;
            longestRoute = route.slice(0);
          }
        }
        beenTo.pop();
      }
    });
    return longestRoute;
  }

  findSortestRoute() {
    // 1. Start with nothing
    let shortestDistance = null;
    let shortestRoute = null;
    // 1. If there are no cities, there are no routes
    if (this.number === 0) {
      return null;
    }
    // 2. Loop for all the possible starting cities
    Object.keys(this.cities).forEach((startAt) => {
      const route = this.findShortRoute(startAt, shortestDistance);
      if (route != null) {
        const routeDistance = this.calculateDistance(route);
        if (shortestDistance === null || routeDistance < shortestDistance) {
          shortestDistance = routeDistance;
          shortestRoute = route.slice(0);
        }
      }
    });
    return shortestRoute;
  }

  findLongestRoute() {
    // 1. Start with nothing
    let longestDistance = null;
    let longestRoute = null;
    // 1. If there are no cities, there are no routes
    if (this.number === 0) {
      return null;
    }
    // 2. Loop for all the possible starting cities
    Object.keys(this.cities).forEach((startAt) => {
      const route = this.findLongRoute(startAt, longestDistance);
      if (route != null) {
        const routeDistance = this.calculateDistance(route);
        if (longestDistance === null || routeDistance > longestDistance) {
          longestDistance = routeDistance;
          longestRoute = route.slice(0);
        }
      }
    });
    return longestRoute;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Determine the shortest route
    const route = this.findSortestRoute();
    // 2. If there is no solution, say so
    if (route === null) {
      return null;
    }
    // 3. Else, Return the solution for part one
    return this.calculateDistance(route);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    // 1. Determine the longest route
    const route = this.findLongestRoute();
    // 2. If there is no solution, say so
    if (route === null) {
      return null;
    }
    // 3. Else, Return the solution for part two
    return this.calculateDistance(route);
  }
}

module.exports.Routes = Routes;
// ======================================================================
// end                        r o u t e s . j s                       end
// ======================================================================
