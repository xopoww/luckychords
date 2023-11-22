#!/usr/bin/env python3

import random
import time
import itertools


def note(code):
    all_notes = [
        "C", "C#", "D", "D#", "E",
        "F", "F#", "G", "G#", "A",
        "A#", "B"
    ]
    return all_notes[code%len(all_notes)]


ROOTS=[
    0,  # C
    2,  # D
    4,  # E
    5,  # F
    7,  # G
    9,  # A
    11, # B
]


def major(root):
    return (root, root+4, root+4+3), ""


def minor(root):
    return (root, root+3, root+3+4), "m"


def dim(root):
    return (root, root+3, root+3+3), " dim"


def aug(root):
    return (root, root+4, root+4+4), " aug"


QUALITIES=[
    major,
    minor,
    dim,
    aug
]


COMBINATIONS=list(itertools.product(ROOTS, QUALITIES))


def chord_repr(root, quality):
    codes, suffix = quality(root)
    chord = note(root) + suffix
    return "%-6s (%s)" % (chord, ", ".join([note(code) for code in codes]))


def main():
    N_CHORDS = 4
    print("Your lucky chords are:")
    got=set()
    while len(got) < N_CHORDS:
        root, quality = random.choice(COMBINATIONS)
        cr = chord_repr(root, quality)
        if cr not in got:
            got.add(cr)
            print(f'{len(got)}. {cr}')


if __name__ == "__main__":
    random.seed(time.monotonic())
    main()