<?php
$lines = file("./input.txt", FILE_IGNORE_NEW_LINES+FILE_SKIP_EMPTY_LINES);
//$lines = array("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2");
$position = 0;
$depth = 0;
foreach ($lines as $l) {
    $cmd = explode(" ", $l);
    $num = intval($cmd[1]);
    if ($cmd[0] == 'forward') {
        $position = $position + $num;
    } elseif ($cmd[0] == 'down') {
        $depth = $depth + $num;
    } elseif ($cmd[0] == 'up') {
        $depth = $depth - $num;
    } else {
        echo "unknown command ", $l;
    }
}
$answer = $position * $depth;
echo "<p>Answer to Advent of Code 2021 day 2 part 1 is $answer.</p>";

$position = 0;
$depth = 0;
$aim = 0;
foreach ($lines as $l) {
    $cmd = explode(" ", $l);
    $num = intval($cmd[1]);
    if ($cmd[0] == 'forward') {
        $position = $position + $num;
        $depth = $depth + $aim * $num;
    } elseif ($cmd[0] == 'down') {
        $aim = $aim + $num;
    } elseif ($cmd[0] == 'up') {
        $aim = $aim - $num;
    } else {
        echo "unknown command ", $l;
    }
}
$answer = $position * $depth;
echo "<p>Answer to Advent of Code 2021 day 2 part 2 is $answer.</p>";
?>

