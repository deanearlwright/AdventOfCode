<?php
$lines = file("./input.txt", FILE_IGNORE_NEW_LINES+FILE_SKIP_EMPTY_LINES);
// $lines = array(199, 200, 208, 210, 200, 207, 240, 269, 260, 263);
$count = 0;
for ($index = 0; $index + 3 < count($lines); $index = $index + 1) {
    $num_index = intval($lines[$index]);
    $num_three = intval($lines[3+$index]);
    if ($num_three > $num_index) {
        $count = $count + 1;
    }
}
echo "Answer to Advent of Code 2021 day 1 part 2 is $count.\n";
?>

