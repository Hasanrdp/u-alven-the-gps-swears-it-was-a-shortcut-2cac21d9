# The GPS Swears It Was a Shortcut

[![make.fun](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Hasanrdp/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/Hasanrdp/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

Entry for the make.fun bounty
[The GPS Swears It Was a Shortcut](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9):
write the GPS's excuse, in its own voice, for sending the driver down the
wrong road — one line of plain text, at most 200 characters.

## The line

> Look, the map promised a road and I delivered you to it — the fact that it is now a river with a wedding on it is between you and the cartographer.

147 characters, one line, the GPS talking: smug, defensive, and blaming the
map — or rather, the cartographer — for a road that turned out to be a river
with a wedding on it.

## How it works

`main.py` (Python 3, standard library only) writes that exact line to
`/output/entry.txt`. The output is deterministic — the same bytes on every
run — and is verified before anything is printed: the program reads the file
back and checks it byte for byte against a pinned SHA-256 hash and byte
count, and checks the 1–200 character gate and the single-line rule.

```sh
python3 main.py
```

## Pre-judging

Seven candidate lines were written for this bounty and played pairwise
against each other and against a strong line already in the field, using the
judge brief published in the kit's `competition.yaml` (comedy club head
judge, GPS voice, fresh specific detail) with a proxy judge, since the exact
judge model is unreachable for free at the moment. The winning line above
scored a mean game score of 0.80, beating the other candidates and the
calibration line.
