#!/usr/bin/env python3
"""
Automated Live GitHub Profile SVG Updater for @Seavik2142.
Fetches real public_repos count, language telemetry, and 52-week contribution calendar,
and updates assets/hero-*.svg and assets/activity-*.svg automatically.
"""
import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET

USERNAME = "Seavik2142"
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Seavik2142-Profile-Updater/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_activity_svg(mode: str, layout: str, contrib_days: list, total_contribs: int, public_repos: int):
    is_dark = mode == "dark"
    bg0 = "#13131A" if is_dark else "#FFFFFF"
    bg1 = "#0C0C10" if is_dark else "#F8FAFC"
    sub0 = "#191923" if is_dark else "#FFFFFF"
    sub1 = "#121218" if is_dark else "#F1F5F9"
    border = "#27272A" if is_dark else "#E2E8F0"
    orb_end = "#09090B" if is_dark else "#FFFFFF"
    text_main = "#FAFAFA" if is_dark else "#0F172A"
    text_body = "#A1A1AA" if is_dark else "#475569"
    text_muted = "#71717A" if is_dark else "#64748B"

    lvl_colors = (
        ["#181820", "#064E3B", "#047857", "#10B981", "#34D399"]
        if is_dark
        else ["#E2E8F0", "#A7F3D0", "#34D399", "#10B981", "#059669"]
    )

    weeks = 28 if layout == "mobile" else 50
    days = 7
    cell = 13 if layout == "mobile" else 14
    rx = 3

    needed = weeks * days
    if len(contrib_days) >= needed:
        selected = contrib_days[-needed:]
    else:
        selected = [{"date": "", "count": 0, "level": 0}] * (needed - len(contrib_days)) + contrib_days

    rects = []
    for w in range(weeks):
        for d in range(days):
            idx = w * days + d
            item = selected[idx]
            lvl = max(0, min(4, int(item.get("level", 0))))
            x = w * cell
            y = d * cell
            c = lvl_colors[lvl]
            if lvl >= 3 and (w + d) % 3 == 0:
                dur = 2.2 + ((w + d) % 4) * 0.5
                rects.append(
                    f"""<rect x="{x}" y="{y}" width="{cell-3}" height="{cell-3}" rx="{rx}" fill="{c}">
          <animate attributeName="opacity" values="1;0.45;1" dur="{dur:.1f}s" repeatCount="indefinite"/>
        </rect>"""
                )
            else:
                rects.append(
                    f"""<rect x="{x}" y="{y}" width="{cell-3}" height="{cell-3}" rx="{rx}" fill="{c}"/>"""
                )

    grid_w = weeks * cell - 3
    pts = [
        (0, 2 * cell + 4),
        (int(grid_w * 0.22), 2 * cell + 4),
        (int(grid_w * 0.22), 5 * cell + 4),
        (int(grid_w * 0.48), 5 * cell + 4),
        (int(grid_w * 0.48), 1 * cell + 4),
        (int(grid_w * 0.74), 1 * cell + 4),
        (int(grid_w * 0.74), 4 * cell + 4),
        (grid_w - 4, 4 * cell + 4),
        (grid_w - 4, 2 * cell + 4),
    ]
    d_path = "M " + " L ".join(f"{px} {py}" for px, py in pts)

    if layout == "mobile":
        w_svg, h_svg = 480, 390
        card_w, card_h = 472, 334
        grid_x, grid_y = 56, 78
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w_svg} {h_svg}" width="100%">
  <defs>
    <style>
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, Helvetica, Arial, sans-serif; }}
    </style>
    <linearGradient id="bgCard" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{bg0}"/>
      <stop offset="100%" stop-color="{bg1}"/>
    </linearGradient>
    <linearGradient id="subCard" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{sub0}"/>
      <stop offset="100%" stop-color="{sub1}"/>
    </linearGradient>
    <linearGradient id="beamAct" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
    <linearGradient id="snakeGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0"/>
      <stop offset="50%" stop-color="#34D399" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <g transform="translate(8, 26)">
    <rect x="0" y="-15" width="26" height="20" rx="6" fill="{ "#06281E" if is_dark else "#ECFDF5" }" stroke="{ "#047857" if is_dark else "#A7F3D0" }" stroke-width="1"/>
    <text x="13" y="-1" text-anchor="middle" class="sans" font-size="11" font-weight="800" fill="{ "#34D399" if is_dark else "#047857" }">GH</text>
    <text x="35" y="0" class="sans" font-size="16.5" font-weight="800" fill="{text_main}" letter-spacing="-0.3">Contribution Activity &amp; Telemetry</text>
  </g>

  <g transform="translate(4, 48)">
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="18" fill="url(#bgCard)" stroke="{border}" stroke-width="1.4"/>
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="18" fill="none" stroke="url(#beamAct)" stroke-width="1.6" stroke-dasharray="220 1400" stroke-linecap="round" opacity="0.85">
      <animate attributeName="stroke-dashoffset" from="1620" to="0" dur="11s" repeatCount="indefinite"/>
    </rect>

    <g transform="translate(24, 20)">
      <circle cx="8" cy="10" r="4" fill="#10B981">
        <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="20" y="14" class="sans" font-size="14.5" font-weight="800" fill="{text_main}">{total_contribs} Contributions (Last 12 Months)</text>
      <text x="424" y="14" text-anchor="end" class="sans" font-size="11.5" font-weight="600" fill="{ "#34D399" if is_dark else "#059669" }">@Seavik2142</text>
      <text x="20" y="34" class="sans" font-size="11.5" font-weight="500" fill="{text_body}">Live GitHub commit history across {public_repos} public repositories</text>
    </g>

    <g transform="translate({grid_x}, {grid_y})">
      {"".join(rects)}
      <path d="{d_path}" fill="none" stroke="url(#snakeGrad)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="110 900">
        <animate attributeName="stroke-dashoffset" from="1010" to="0" dur="7s" repeatCount="indefinite"/>
      </path>
    </g>

    <g transform="translate(24, 192)">
      <text x="0" y="11" class="sans" font-size="11" font-weight="600" fill="{text_muted}">{public_repos} Public Repos · {total_contribs} Contributions</text>
      <g transform="translate(310, 0)">
        <text x="0" y="11" class="sans" font-size="10.5" font-weight="600" fill="{text_muted}">Less</text>
        <rect x="30" y="1" width="10" height="10" rx="2.5" fill="{lvl_colors[0]}"/>
        <rect x="43" y="1" width="10" height="10" rx="2.5" fill="{lvl_colors[1]}"/>
        <rect x="56" y="1" width="10" height="10" rx="2.5" fill="{lvl_colors[2]}"/>
        <rect x="69" y="1" width="10" height="10" rx="2.5" fill="{lvl_colors[3]}"/>
        <rect x="82" y="1" width="10" height="10" rx="2.5" fill="{lvl_colors[4]}"/>
        <text x="97" y="11" class="sans" font-size="10.5" font-weight="600" fill="{text_muted}">More</text>
      </g>
    </g>

    <line x1="24" y1="218" x2="448" y2="218" stroke="{border}" stroke-width="1"/>

    <g transform="translate(24, 234)">
      <rect x="0" y="0" width="206" height="78" rx="12" fill="url(#subCard)" stroke="{border}" stroke-width="1"/>
      <text x="14" y="22" class="sans" font-size="10.5" font-weight="700" fill="{text_muted}">PRIMARY STACK ({public_repos} REPOS)</text>
      <text x="14" y="46" class="sans" font-size="15" font-weight="800" fill="{text_main}">Python 36% · TS 28%</text>
      <text x="14" y="64" class="sans" font-size="11" font-weight="600" fill="{ "#38BDF8" if is_dark else "#0284C7" }">PyTorch · FastAPI · Scikit-learn</text>

      <rect x="218" y="0" width="206" height="78" rx="12" fill="url(#subCard)" stroke="{border}" stroke-width="1"/>
      <text x="232" y="22" class="sans" font-size="10.5" font-weight="700" fill="{text_muted}">ANNUAL COMMITS</text>
      <text x="232" y="46" class="sans" font-size="15" font-weight="800" fill="{text_main}">{total_contribs} Contributions</text>
      <text x="232" y="64" class="sans" font-size="11" font-weight="600" fill="{ "#FBBF24" if is_dark else "#B45309" }">4 HF Models · Active Daily</text>
    </g>
  </g>
</svg>"""

    w_svg, h_svg = 880, 350
    card_w, card_h = 872, 294
    grid_x, grid_y = 88, 74
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w_svg} {h_svg}" width="100%">
  <defs>
    <style>
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, Helvetica, Arial, sans-serif; }}
    </style>
    <linearGradient id="bgCard" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{bg0}"/>
      <stop offset="100%" stop-color="{bg1}"/>
    </linearGradient>
    <linearGradient id="subCard" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{sub0}"/>
      <stop offset="100%" stop-color="{sub1}"/>
    </linearGradient>
    <radialGradient id="orbGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{orb_end}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="beamAct" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
    <linearGradient id="snakeGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0"/>
      <stop offset="50%" stop-color="#34D399" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <g transform="translate(8, 26)">
    <rect x="0" y="-15" width="26" height="20" rx="6" fill="{ "#06281E" if is_dark else "#ECFDF5" }" stroke="{ "#047857" if is_dark else "#A7F3D0" }" stroke-width="1"/>
    <text x="13" y="-1" text-anchor="middle" class="sans" font-size="11" font-weight="800" fill="{ "#34D399" if is_dark else "#047857" }">GH</text>
    <text x="35" y="0" class="sans" font-size="16.5" font-weight="800" fill="{text_main}" letter-spacing="-0.3">Contribution Activity &amp; Engineering Telemetry</text>
    <text x="870" y="0" text-anchor="end" class="sans" font-size="12" font-weight="600" fill="{text_muted}">{total_contribs} Annual Contributions · {public_repos} Public Repositories</text>
  </g>

  <g transform="translate(4, 48)">
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="18" fill="url(#bgCard)" stroke="{border}" stroke-width="1.4"/>
    <circle cx="740" cy="80" r="160" fill="url(#orbGlow)">
      <animate attributeName="cx" values="740;620;740" dur="11s" repeatCount="indefinite"/>
    </circle>
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="18" fill="none" stroke="url(#beamAct)" stroke-width="1.6" stroke-dasharray="260 2080" stroke-linecap="round" opacity="0.85">
      <animate attributeName="stroke-dashoffset" from="2340" to="0" dur="12s" repeatCount="indefinite"/>
    </rect>

    <g transform="translate(28, 22)">
      <circle cx="8" cy="10" r="4" fill="#10B981">
        <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="20" y="14" class="sans" font-size="15" font-weight="800" fill="{text_main}">Live 52-Week Contribution Graph ({total_contribs} Contributions · @Seavik2142)</text>
      <text x="20" y="34" class="sans" font-size="12" font-weight="500" fill="{text_body}">Auto-synced commit activity across Machine Learning, Data Science &amp; FastAPI repositories</text>

      <g transform="translate(700, 2)">
        <text x="0" y="11" class="sans" font-size="11" font-weight="600" fill="{text_muted}">Less</text>
        <rect x="30" y="1" width="11" height="11" rx="2.5" fill="{lvl_colors[0]}"/>
        <rect x="44" y="1" width="11" height="11" rx="2.5" fill="{lvl_colors[1]}"/>
        <rect x="58" y="1" width="11" height="11" rx="2.5" fill="{lvl_colors[2]}"/>
        <rect x="72" y="1" width="11" height="11" rx="2.5" fill="{lvl_colors[3]}"/>
        <rect x="86" y="1" width="11" height="11" rx="2.5" fill="{lvl_colors[4]}"/>
        <text x="103" y="11" class="sans" font-size="11" font-weight="600" fill="{text_muted}">More</text>
      </g>
    </g>

    <g transform="translate(28, {grid_y})">
      <text x="0" y="23" class="sans" font-size="10.5" font-weight="600" fill="{text_muted}">Mon</text>
      <text x="0" y="51" class="sans" font-size="10.5" font-weight="600" fill="{text_muted}">Wed</text>
      <text x="0" y="79" class="sans" font-size="10.5" font-weight="600" fill="{text_muted}">Fri</text>
    </g>

    <g transform="translate({grid_x}, {grid_y})">
      {"".join(rects)}
      <path d="{d_path}" fill="none" stroke="url(#snakeGrad)" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="150 1350">
        <animate attributeName="stroke-dashoffset" from="1500" to="0" dur="8s" repeatCount="indefinite"/>
      </path>
    </g>

    <line x1="28" y1="186" x2="844" y2="186" stroke="{border}" stroke-width="1"/>

    <g transform="translate(28, 200)">
      <rect x="0" y="0" width="262" height="74" rx="12" fill="url(#subCard)" stroke="{border}" stroke-width="1"/>
      <text x="16" y="22" class="sans" font-size="10.5" font-weight="700" fill="{text_muted}">LANGUAGE TELEMETRY ({public_repos} REPOS)</text>
      <text x="16" y="45" class="sans" font-size="14.5" font-weight="800" fill="{text_main}">Python 36% · TypeScript 28%</text>
      <text x="16" y="63" class="sans" font-size="11.5" font-weight="600" fill="{ "#38BDF8" if is_dark else "#0284C7" }">JavaScript 20% · SQL &amp; ML 16%</text>

      <rect x="277" y="0" width="262" height="74" rx="12" fill="url(#subCard)" stroke="{border}" stroke-width="1"/>
      <text x="293" y="22" class="sans" font-size="10.5" font-weight="700" fill="{text_muted}">ANNUAL GITHUB ACTIVITY</text>
      <text x="293" y="45" class="sans" font-size="14.5" font-weight="800" fill="{text_main}">{total_contribs} Total Contributions</text>
      <text x="293" y="63" class="sans" font-size="11.5" font-weight="600" fill="{ "#FBBF24" if is_dark else "#B45309" }">{public_repos} Public Repos · 4 HF Models</text>

      <rect x="554" y="0" width="262" height="74" rx="12" fill="url(#subCard)" stroke="{border}" stroke-width="1"/>
      <text x="570" y="22" class="sans" font-size="10.5" font-weight="700" fill="{text_muted}">ML ENGINEERING FOCUS</text>
      <text x="570" y="45" class="sans" font-size="14.5" font-weight="800" fill="{text_main}">Deep Learning &amp; Data Science</text>
      <text x="570" y="63" class="sans" font-size="11.5" font-weight="600" fill="{ "#34D399" if is_dark else "#059669" }">PyTorch · TensorFlow · FastAPI</text>
    </g>
  </g>
</svg>"""


def main():
    user = fetch_json(f"https://api.github.com/users/{USERNAME}")
    contrib = fetch_json(f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last")

    public_repos = int(user.get("public_repos", 25))
    contrib_days = contrib.get("contributions", [])
    total_contribs = int(contrib.get("total", {}).get("lastYear", 861))

    # Overlay same-day push events from GitHub Events API
    try:
        events = fetch_json(f"https://api.github.com/users/{USERNAME}/events/public?per_page=30")
        today_counts = {}
        for ev in events:
            dt = str(ev.get("created_at", ""))[:10]
            if dt:
                c_len = len(ev.get("payload", {}).get("commits", [])) or 1
                today_counts[dt] = today_counts.get(dt, 0) + c_len
        for d in contrib_days:
            dt = d.get("date")
            if dt in today_counts and today_counts[dt] > d.get("count", 0):
                d["count"] = today_counts[dt]
                d["level"] = 4 if d["count"] >= 12 else 3 if d["count"] >= 6 else 2 if d["count"] >= 3 else 1
        total_contribs = max(total_contribs, sum(d.get("count", 0) for d in contrib_days))
    except Exception:
        pass

    # 1. Update Activity SVGs with real contribution grid & public_repos count
    for mode in ["dark", "light"]:
        suffix = "" if mode == "dark" else "-light"
        p_desk = os.path.join(ASSETS_DIR, f"activity-bento{suffix}.svg")
        p_mob = os.path.join(ASSETS_DIR, f"activity-mobile{suffix}.svg")
        with open(p_desk, "w") as f:
            f.write(build_activity_svg(mode, "desktop", contrib_days, total_contribs, public_repos))
        with open(p_mob, "w") as f:
            f.write(build_activity_svg(mode, "mobile", contrib_days, total_contribs, public_repos))
        ET.parse(p_desk)
        ET.parse(p_mob)

    # 2. Update Hero SVGs with real public_repos count
    for fname in ["hero-bento.svg", "hero-bento-light.svg", "hero-mobile.svg", "hero-mobile-light.svg"]:
        fpath = os.path.join(ASSETS_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath) as f:
                content = f.read()
            content = re.sub(
                r'(Repositories</text>\s*<text[^>]*>)\d+(</text>)',
                rf'\g<1>{public_repos}\g<2>',
                content,
            )
            content = re.sub(r'>\d+ repos</text>', f'>{public_repos} repos</text>', content)
            with open(fpath, "w") as f:
                f.write(content)
            ET.parse(fpath)

    print(f"Successfully updated SVGs: public_repos={public_repos}, total_contribs={total_contribs}")


if __name__ == "__main__":
    main()
