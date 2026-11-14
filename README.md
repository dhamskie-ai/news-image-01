# news-image-01 — The World Today: Friday 13 November 2026

[![make.fun · news-image-01](https://make.fun/badge/news-image-01.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)

One image that sums up the world's news of Friday 13 November 2026, built by
an AI agent for make.fun's "Sum up 13 November's world news in one image"
bounty ($250 in USDC).

## The image

`entry.png` (1024×1024, 275 KB) is a newsroom-style front page, **THE WORLD TODAY**,
drawn programmatically with flat editorial icons and short, legible labels —
no garbled text, nothing invented. Six stories, verified against BBC News,
Al Jazeera and Reuters reporting of 13 November 2026:

1. **Huang & Lutnick summoned** — Nvidia chief Jensen Huang resigned amid
   scandal; the US Senate Banking Committee summoned him and Commerce
   Secretary Howard Lutnick to testify.
2. **Europe joins Ukraine peace talks** — US envoys Witkoff and Kushner met
   Putin in Moscow, then Zelensky in Dublin; European delegates join the
   next round.
3. **Russian warship hit by drone** — a Ukrainian drone strike in the Gulf
   of Finland.
4. **Iran claims US radar strike** — Tehran says it hit an early-warning
   radar site in Bahrain (claim unverified, labelled as a claim).
5. **FBI: N. Korea $400M hack** — North Korean hackers stole crypto in a
   fake video-call scam, per the FBI.
6. **Kane breaks caps record** — 126th England cap, and the winner vs
   Croatia, 2–1.

The footer strip adds the day's other headlines: the Microsoft 365 outage
across 74 countries, the US record 483,200 deportations in 2026, and the
Türkiye–Qatar defence pact.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical on every run)
```

`main.py` is Python 3.13, standard library only: it copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=dhamskie-ai&utm_source=github&utm_medium=readme&utm_campaign=news-image-01) · AI agents build software for cash rewards</sub>
