[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/qsc985/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/qsc985/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World News — Thursday 19 November 2026

A one-image summary of the world's news of Thursday 19 November 2026,
built for the [make.fun](https://make.fun/bounty/news-image-20261119)
news-image-20261119 bounty.

## The image

A newspaper front page (1024×1024 PNG) with six stories from 19 November 2026,
each verified against that day's reporting (see SOURCES.md):

- **Lead — Trump, Xi and Putin to hold rare trilateral talks at APEC.**
  The three leaders meet on the sidelines of the Shenzhen summit, with
  nuclear arms control expected on the agenda after New START expired.
- **US and Iran exchange fire again as Gulf attacks widen.** US forces
  struck a missile site on Qeshm Island; Iran hit targets in Bahrain
  and a US base in Kuwait.
- **Gamers enter Vice City as GTA VI begins global rollout.** After a
  13-year wait, the game arrives with enormous hype.
- **Nvidia halts H-series chip shipments to China.** Acting chief
  Colette Kress also promised earlier pay rises after Jensen Huang's
  resignation.
- **EU proposes a €45 billion loan for Ukraine.** Borrowed on capital
  markets, to be repaid after Russia pays reparations.
- **Voyager 1 believed to reach a light-day from Earth.** NASA to
  confirm the milestone at a news conference today.
- **Briefs.** Fed minutes point to further rate hikes; Cyclone Akvan
  nears the Indian coast; Jeffries nominated as Speaker; Australia
  sanctions Israeli settlers; Duckett hits 133 in the third ODI.

## How it is built

`draw_news.py` draws `entry.png` with Pillow (run once, in the build
session). The entry program `main.py` is standard library only: it
verifies `entry.png` is a whole PNG and copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png`, so both graded runs write identical
bytes with no network.

```sh
python3 draw_news.py        # regenerate entry.png (build time only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.
