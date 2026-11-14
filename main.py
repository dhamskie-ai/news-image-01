# News-image-01 entry: copies the image beside this file to /output/entry.png.
# The image is a one-page news infographic summing up Friday 13 November 2026:
# Huang & Lutnick summoned by the US Senate, Europe joining the Ukraine peace
# talks, a drone hitting a Russian warship, Iran's claimed strike on a US radar
# in Bahrain, the FBI's $400M North Korea crypto-hack case, and Harry Kane's
# England caps record - plus the day's other headlines in the footer strip.
# Python 3.13, standard library only; deterministic (a plain file copy).
# The output is byte-identical on every run: no timestamps, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
