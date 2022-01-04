<?php
$lines = file("./input.txt", FILE_IGNORE_NEW_LINES+FILE_SKIP_EMPTY_LINES);
//$lines = array("00100", "11110", "10110", "10111", "10101", "01111",
//               "00111", "11100", "10000", "11001", "00010", "01010");
$counts = array_fill(0, strlen($lines[0]), 0);
foreach ($lines as $l) {
    $bits = str_split($l);
    for ($indx = 0; $indx < count($bits); $indx++) {
        if ($bits[$indx] == '1') {
            $counts[$indx]++;
        }
    }
}
$gamma = 0;
$epsilon = 0;
$half = count($lines) / 2;
for ($indx = 0; $indx < count($counts); $indx++) {
    if ($counts[$indx] > $half) {
        $gamma = $gamma * 2 + 1;
        $epsilon = $epsilon * 2;
    } else {
        $gamma = $gamma * 2;
        $epsilon = $epsilon * 2 + 1;
    }
}
$answer = $gamma * $epsilon;
echo "<p>Answer to Advent of Code 2021 day 3 part 1 is $answer.</p>";

// Part 2: oxygen
$xlines = (array)clone(object)$lines;
$indx = 0;
while (count($xlines)> 1) {
    $half = count($xlines) / 2;
    $count = 0;
    foreach ($xlines as $l) {
        if ($l[$indx] == '1') {
            $count++;
        }
    }
    if ($count >= $half) {
        $bit = '1';
    } else {
        $bit = '0';
    }
    $keep = array();
    foreach ($xlines as $l) {
        if ($bit == $l[$indx]) {
            array_push($keep, $l);
        }
    }
    $xlines = (array)clone(object)$keep;
    $len = count($xlines);
    $indx++;
}
$oxygen = bindec($xlines[0]);

// Part 2: co2
$xlines = (array)clone(object)$lines;
$indx = 0;
while (count($xlines)> 1) {
    $half = count($xlines) / 2;
    $count = 0;
    foreach ($xlines as $l) {
        if ($l[$indx] == '0') {
            $count++;
        }
    }
    if ($count <= $half) {
        $bit = '0';
    } else {
        $bit = '1';
    }
    $keep = array();
    foreach ($xlines as $l) {
        if ($bit == $l[$indx]) {
            array_push($keep, $l);
        }
    }
    $xlines = (array)clone(object)$keep;
    $len = count($xlines);
    $indx++;
}
$co2 = bindec($xlines[0]);
echo "<p>oxygen is $oxygen, co2=$co2</p>";
$answer = $oxygen * $co2;
echo "<p>Answer to Advent of Code 2021 day 3 part 2 is $answer.</p>";
?>

