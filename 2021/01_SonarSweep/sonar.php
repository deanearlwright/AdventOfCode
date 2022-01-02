<?php
$lines = file("./input.txt", FILE_IGNORE_NEW_LINES+FILE_SKIP_EMPTY_LINES);
// $lines = array(199, 200, 208, 210, 200, 207, 240, 269, 260, 263);
$previous = 999999;
$count = 0;
foreach ($lines as $l) {
  $num = intval($l);
  if ($num > $previous) {
    $count = $count + 1;
  }
  $previous = $num;
}
echo "Answer to Advent of Code 2021 day 1 part 1 is $count.\n";
?>

