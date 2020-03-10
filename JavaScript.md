# Advent of Code in JavaScript

### Introduction

The company I work for, [Novetta](https://www.novetta.com/careers/), is a sponsor of the December coding puzzle site, [Advent of Code](https://adventofcode.com/).  I participated in the 2019 event in near real time.  I didn't get every puzzle completed on the day it was announced but I was generally able to catch up on the weekends.  

I did the puzzles for 2019 in [python3](https://www.python.org/) using the [Wingware Wing IDE](https://wingware.com/) for python.  I have been using both python and Wingware for years and am very comfortable with both.  After doing the puzzle for 2019 and went back and did the ones from 2017.  Again I used python and Wingware.

I wanted to go on to the other years of the Advent of Code, but having done two years worth in python, I wanted to try using other languages.  At work I mainly use [Go](https://golang.org/) for server code and [React](https://reactjs.org/) for the front end.  I have the advantage of working with several talented front end developers so I  haven't had to do much on that side.  I decided to do year 2015 of Advent of Code in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) to improve my JS coding skills.

### The technology Stack

In addition to changing the programming language, I would also be changing the IDE and the testing framework.  The Advent of Code puzzles come with the example data and results.  If your code can correctly solve the puzzle using the example data you can be pretty sure that it can solve the puzzle given the real data.  So doing [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) is a good way to work through the puzzles.

##### IDE: Visual Studio Code

While there are a number of good IDEs for developing JavaScript solutions, I narrowed my choice to [Visual Studio Code](https://code.visualstudio.com/).  Walking around the office, I found most of the developers using VSC so it seemed to be the one to use.  

I had already installed VSC for some work with Go but I remove it and installed the latest version.  Microsoft has a [page](https://code.visualstudio.com/docs/nodejs/nodejs-tutorial) specifically for working with Node.js in Visual Studio Code.  The first step is to [download](https://nodejs.org/en/download/) and install node and npm.  In March 2020, this got me node version 12.16.1 and npm 6.13.4.

The next part of the tutorial walk through creating a Hello World application.   After that it goes through using [express](https://expressjs.com/) as a framework for building an running applications.  Express defines itself as a "Fast, unopinionated, minimalist web framework for Node.js".  But since, the Advent of Code problems will be run as command line applications, I decided not to use express or any of the many [alternatives](https://alternative.me/express-js).

##### TTD: Jest

Rigorous testing should be part of every project.  It should be easy to do and integrated into the IDE.  For the Advent of Code, I choose to use [Jest](https://jestjs.io/).  There are a number of other testing frameworks such as [Jasmine](https://jasmine.github.io/) and [Mocha](https://mochajs.org/) but they use jest where I work so I wanted to get more experience with it.

```
npm install jest --global
```

LINT: eslint

Code is code but readable code is better code.  Following a style guide, puts some limitations on your code which hopefully make it easier to read, understand, and get right.  For javascript, one of the popular style guides is from [Airbnb](https://github.com/airbnb/javascript).  

From helpful [page](https://travishorn.com/setting-up-eslint-on-vs-code-with-airbnb-javascript-style-guide-6eb78a535ba6)

1.  `cd coding-directory`
2. `npm init -y`
3. `npm i -D eslint eslint-config-airbnb-base eslint-plugin-import`
4. npm i -D eslint eslint-config-standard eslint-plugin-import eslint-plugin-node eslint-plugin-promise eslint-plugin-standard
5. Create `.eslintrc.js`: `module.exports = { "extends": "airbnb-base" };`
6. In VS Code, `Ctrl + Shift + X`
7. Search `ESLint`
8. Install ESLint
9. Restart VS Code