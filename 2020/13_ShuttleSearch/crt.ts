// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                             c r t . t s
//
// A utility routine for the Advent of Code 2020 Day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                MultInv
// ======================================================================

function multInv(a: number, b: number) {
  // Return x where (a *x) % b == 1

  const b0 = b;
  let x0 = 0;
  let x1 = 1;
  let aa = a;
  let bb = b;

  while (aa > 1) {
    const q = Math.trunc(aa / bb);
    [aa, bb] = [bb, aa % bb];
    [x0, x1] = [x1 - q * x0, x0];
  }
  if (x1 < 0) {
    x1 += b0;
  }
  return x1;
}

function CRT(n: number[], a: number[]): number {
  let p = 0;
  let prod = 1;
  let sum = 0;
  for (let indx = 0; indx < n.length; indx += 1) {
    prod *= n[indx];
  }
  for (let indx = 0; indx < n.length; indx += 1) {
    p = Math.trunc(prod / n[indx]);
    sum += a[indx] * multInv(p, n[indx]) * p;
  }
  return sum % prod;
}

export { CRT };

// ======================================================================
// end                           c r t . t s                          end
// ======================================================================
