"""Draw the 19 November 2026 newspaper front page (build time only)."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font; never overflows."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill, spacing=4, max_lines=None):
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def main():
    img = Image.new("RGB", (W, H), "#fdfcf7")
    d = ImageDraw.Draw(img)
    mx = 36
    cw = W - 2 * mx

    # Masthead
    title = font(SERIF, 68)
    d.text((W // 2, 30), "THE WORLD TODAY", font=title, fill="#111111",
           anchor="ma")
    d.line([(mx, 112), (W - mx, 112)], fill="#111111", width=3)
    d.line([(mx, 118), (W - mx, 118)], fill="#111111", width=1)
    sub = font(SANS, 20)
    d.text((W // 2, 128), "Thursday 19 November 2026  •  One image, six stories",
           font=sub, fill="#333333", anchor="ma")

    # Lead story
    ly, lh = 162, 218
    d.rectangle([mx, ly, W - mx, ly + lh], fill="#e8eef5", outline="#1a3a5c", width=2)
    x = mx + 20
    y = ly + 12
    d.text((x, y), "LEAD  •  DIPLOMACY  •  SHENZHEN", font=font(SANS_B, 15),
           fill="#b03a2e")
    y += 26
    y = para(d, x, y, "Trump, Xi and Putin to hold rare trilateral talks at APEC",
             font(SANS_B, 33), cw - 40, "#111111", spacing=2, max_lines=2)
    y += 4
    para(d, x, y,
         "The leaders of the United States, China and Russia are set to meet "
         "on the sidelines of the APEC summit in Shenzhen, the White House "
         "confirmed. Nuclear arms control is expected to top the agenda, "
         "after the New START treaty expired in February.",
         font(SANS, 19), cw - 40, "#222222", spacing=3, max_lines=4)

    # Stories 2-5 in a 2x2 grid
    stories = [
        ("CONFLICT  •  GULF",
         "US and Iran exchange fire again as Gulf attacks widen",
         "US forces struck a missile launch site on Iran's Qeshm Island "
         "on 17 November, after Iran hit a US radar site in Bahrain. On "
         "18 November Iran struck a US base in Kuwait and Bahrain again."),
        ("CULTURE  •  GAMING",
         "Gamers enter Vice City as GTA VI begins global rollout",
         "After a 13-year wait, Grand Theft Auto VI arrives with enormous "
         "hype and expectation, opening to players around the world."),
        ("BUSINESS  •  TECH",
         "Nvidia halts H-series chip shipments to China",
         "Acting chief Colette Kress told an earnings call the firm no "
         "longer ships Hopper chips to mainland China, days after founder "
         "Jensen Huang resigned. She also promised earlier pay rises."),
        ("EUROPE  •  UKRAINE",
         "EU proposes \u20ac45 billion loan for Ukraine",
         "The European Commission plans to borrow on capital markets to "
         "cover Ukraine's projected budget gap, to be repaid after Russia "
         "pays reparations, the Financial Times reported."),
    ]
    gy, gh, gap = 396, 172, 16
    col_w = (cw - gap) // 2
    for i, (kick, head, summ) in enumerate(stories):
        cx = mx + (i % 2) * (col_w + gap)
        cy = gy + (i // 2) * (gh + gap)
        d.rectangle([cx, cy, cx + col_w, cy + gh], outline="#999999", width=1)
        ix, iy = cx + 14, cy + 10
        d.text((ix, iy), kick, font=font(SANS_B, 13), fill="#b03a2e")
        iy += 22
        iy = para(d, ix, iy, head, font(SANS_B, 21), col_w - 28,
                  "#111111", spacing=2, max_lines=2)
        iy += 2
        para(d, ix, iy, summ, font(SANS, 15), col_w - 28, "#333333",
             spacing=2, max_lines=4)

    # Story 6, full width
    sy = 756
    d.rectangle([mx, sy, W - mx, sy + 96], fill="#f4ead8", outline="#8a6d3b", width=1)
    y = sy + 10
    d.text((mx + 16, y), "SCIENCE  •  SPACE", font=font(SANS_B, 13), fill="#b03a2e")
    y += 22
    y = para(d, mx + 16, y, "Voyager 1 believed to reach a light-day from Earth",
             font(SANS_B, 21), cw - 32, "#111111", spacing=2, max_lines=1)
    para(d, mx + 16, y,
         "After almost 50 years in space, NASA's Voyager 1 probe likely passed "
         "the milestone at about 05:16 EST; NASA will confirm it at a news "
         "conference today.",
         font(SANS, 15), cw - 32, "#333333", spacing=2, max_lines=2)

    # Briefs strip
    by = 868
    d.rectangle([mx, by, W - mx, by + 104], fill="#1a3a5c")
    d.text((mx + 16, by + 8), "IN BRIEF", font=font(SANS_B, 15), fill="#ffd966")
    briefs = ("Fed minutes: most officials expect further rate hikes.  •  "
              "Cyclone Akvan likely to cross the coast between Machilipatnam "
              "and Puri.  •  Democrats nominate Hakeem Jeffries, set to be "
              "the first Black Speaker of the House.  •  Australia sanctions "
              "Israeli settlers over West Bank expansion.  •  Ben Duckett "
              "hits 133 as England press Australia in the third ODI.")
    para(d, mx + 16, by + 32, briefs, font(SANS, 15), cw - 32, "#ffffff",
         spacing=3, max_lines=4)

    # Footer
    d.line([(mx, 986), (W - mx, 986)], fill="#111111", width=1)
    d.text((W // 2, 992), "Built for make.fun  •  news-image-20261119  •  Sources: SOURCES.md",
           font=font(SANS, 13), fill="#555555", anchor="ma")

    img.save("entry.png")
    print("saved entry.png", img.size, img.mode)


if __name__ == "__main__":
    main()
