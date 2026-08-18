#!/usr/bin/env python3
"""TikTok Whiz — the whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P = f"{S}/TikTok_Whiz - TikTok_Shop_Masterclass - 2026-07-30/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 31 July 2026",
    "TITLE": "TikTok Whiz — the whole business, wired",
    "BLURB": "A TikTok Shop <b>seller</b> offer positioned deliberately against the affiliate "
             "route everyone else in the niche sells. The confirmation page does three jobs at "
             "once: 11 objection videos, 4 YouTube long-forms, and 2 VSLs &mdash; roughly 90 "
             "minutes of consumption before the event. Price sits behind a Typeform gate.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry",
            "title": "Masterclass opt-in",
            "url": "ttwhizprogram.com/masterclass-opt-in…",
            "img": f"{P}/01_Masterclass_opt-in/20260730T103944Z__screenshot_fullpage.png",
            "max_h": 950,
            "note": "&ldquo;Launch a profitable TikTok Shop in 2026.&rdquo; Name, email and "
                    "<b>phone</b>. Zoom-hosted, Sunday.",
        },
        "conf": {
            "col": 2, "y": 120, "lane": "ever", "step": "Confirmation",
            "title": "Confirmation — the consumption page",
            "url": "ttwhizprogram.com/masterclass-confirmation…",
            "img": f"{P}/02_Masterclass_confirmation/20260730T103952Z__screenshot_fullpage.png",
            "max_h": 1500,
            "note": "<b>11 Wistia FAQ videos + 2 Vidalytics VSLs + 4 YouTube embeds</b> on one "
                    "page. Nearly 90 minutes of material between opt-in and event.",
        },
        "app": {
            "col": 4, "y": 120, "lane": "paid", "step": "Qualify",
            "title": "Application (Typeform)",
            "url": "pjb9yue2ih1.typeform.com/to/MITUqQQ2",
            "img": f"{P}/03_Application_Typeform/20260730T104011Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "The gate. Price is never shown to traffic that has not passed it.",
        },
        "booked": {
            "col": 5, "y": 120, "lane": "paid", "step": "Booked",
            "title": "Call confirmed",
            "url": "ttwhizprogram.com/call-confirmed-q",
            "img": f"{P}/04_Call_confirmed_page/20260730T104017Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "Post-booking confirmation.",
        },
    },

    "DATA": {
        "faq": {
            "col": 3, "y": 120, "lane": "ever", "step": "Pre-webinar",
            "title": "Q1&ndash;Q11 — the FAQ library",
            "kv": [("Videos", "11"), ("Runtime", "26m"),
                   ("Longest", "Q8, 5m01s"), ("Q1", "how fast can I sell"),
                   ("Q8", "why us vs others"), ("Q11", "copyright &amp; trademarks")],
            "note": "Q1 opens &ldquo;you're not going to like this answer&rdquo; and puts the "
                    "timeline entirely on the buyer's own action.",
        },
        "yt": {
            "col": 3, "y": 1250, "lane": "ever", "step": "Belief",
            "title": "YouTube doing the convincing",
            "kv": [("Videos", "4"), ("Runtime", "63m"),
                   ("Hero", "$132,625 in 30 days"),
                   ("Anti-hook", "Why I Quit Affiliate"),
                   ("Position", "Be a Seller Instead")],
            "note": "Long-form embedded straight into the funnel. Credibility borrowed from an "
                    "owned channel rather than built inside the webinar.",
        },
        "offer": {
            "col": 6, "y": 120, "lane": "paid", "step": "The offer",
            "title": "Inner Circle",
            "kv": [("Course", "12 modules, 100 videos"),
                   ("His framing", "&ldquo;a small portion&rdquo;"),
                   ("Real product", "support + systems"),
                   ("Price", "not yet observed")],
            "note": "He names the module count then dismisses it, which removes the comparison "
                    "against every $497 course in the niche.",
        },
    },

    "EDGES": [
        ("optin", "conf"), ("conf", "faq"), ("conf", "yt", "v", "#34d399"),
        ("faq", "app"), ("app", "booked"), ("booked", "offer"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Masterclass → application → call"},
        {"x": X[1], "y": 2400, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_position", "x": X[1] + 10, "y": 2460, "state": "yes",
         "cond": "Positions against the category default",
         "body": "Everyone in this niche sells TikTok Shop <i>affiliate</i>. His lead assets are "
                 "<b>&ldquo;Why I Quit TikTok Shop Affiliate&rdquo;</b> and <b>&ldquo;DON'T "
                 "Start TikTok Shop Affiliate &mdash; Be a Seller Instead&rdquo;</b>. He turns "
                 "the category's most common offer into his own differentiator rather than "
                 "competing inside it.",
         "ev": "VERIFIED · 2 of the 4 embedded YouTube videos, both pulled"},
        {"id": "b_devalue", "x": X[3] + 10, "y": 2460, "state": "yes",
         "cond": "Devalues his own course on purpose",
         "body": "&ldquo;It's not just a course &mdash; in fact it's such a small portion of the "
                 "actual program.&rdquo; Naming 12 modules and 100 videos and then dismissing "
                 "them makes the support layer the thing being bought, which cannot be "
                 "price-compared against a course.",
         "ev": "VERIFIED · Q8 transcript"},
        {"id": "b_legal", "x": X[5] + 10, "y": 2460, "state": "unver",
         "cond": "Serious buyer asks about copyright → answered, disclaimed",
         "body": "Q11 covers copyright, trademarks and product design, opening &ldquo;I'm not an "
                 "attorney, this is not legal advice&rdquo;. Answering the question that stops a "
                 "serious buyer filters for exactly the buyer worth having.",
         "ev": "VERIFIED as present · legal accuracy not assessed"},
        {"id": "b_gate", "x": X[7] + 10, "y": 2460, "state": "dq",
         "cond": "Application gate before price",
         "body": "A Typeform sits between the masterclass and the call. Price never reaches "
                 "unqualified traffic, and the qualification questions are not visible without "
                 "submitting.",
         "ev": "PARTIALLY VERIFIED · form captured, not submitted"},
    ],

    "LEGEND": [("event", "Entry"), ("ever", "Pre-webinar consumption"),
               ("paid", "Qualification → call")],
}

if __name__ == "__main__":
    build(CONFIG)
