#!/usr/bin/env python3
"""Build the TikTok Whiz swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/TIKTOK_WHIZ_Swipe")

qs = sorted(glob.glob(os.path.join(PKG, "Transcript/ttw_[0-9a-z]*_Q*.md")))
vsls = sorted(glob.glob(os.path.join(PKG, "Transcript/ttw_vsl_*.md")))
yts = sorted(glob.glob(os.path.join(PKG, "Transcript/ttw_yt_*.md")))

CONFIG = {
    "SITE": "TikTok Whiz — TikTok Shop Inner Circle",
    "CREATOR": "TikTok Whiz",
    "ADS_KEY": "tiktok_whiz",
    "FUNNEL_IDS": ["F015"],
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/TIKTOK_WHIZ_Swipe",
    "BLURB": "A TikTok Shop <b>seller</b> offer — deliberately positioned against the affiliate "
             "route everyone else sells. Application-gated, with an 11-part pre-webinar FAQ and "
             "a YouTube channel doing the heavy lifting on belief.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "FAQ + video transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("FAQ videos", "11"),
        ("FAQ runtime", "26m"),
        ("YouTube pulled", "4"),
        ("YouTube runtime", "63m"),
        ("Total captured", "1h 34m"),
        ("Gate", "Typeform"),
        ("Platform", "Zoom"),
        ("Price", "not observed"),
    ],

    "OFFER": [
        ("Product", "TikTok Whiz Inner Circle — TikTok Shop <i>seller</i>, not affiliate"),
        ("Positioning", "Explicitly against the affiliate route: &ldquo;DON'T Start TikTok Shop "
                        "Affiliate — Be a Seller Instead&rdquo;"),
        ("Core deliverable", "12-module, 100-video masterclass — which he downplays as "
                             "&ldquo;a small portion of the actual program&rdquo;"),
        ("Real deliverable", "The support and systems layer around the course"),
        ("Gate", "Typeform application after the masterclass, then a booked call"),
        ("Event", "Zoom webinar, Sunday"),
        ("Price", '<span class="tag warn">not yet observed</span> — behind the application'),
    ],

    "FINDINGS": [
        ("Positioned against the obvious offer",
         "Everyone in this niche sells the affiliate route. His hero YouTube video is "
         "&ldquo;Why I Quit TikTok Shop Affiliate&rdquo; and another is &ldquo;DON'T Start TikTok "
         "Shop Affiliate — Be a Seller Instead.&rdquo; He converts the category's most common "
         "offer into his own differentiator."),
        ("He devalues his own course on purpose",
         "&ldquo;It's not just a course — in fact it's such a small portion of the actual "
         "program.&rdquo; Naming 12 modules and 100 videos and then dismissing them makes the "
         "support layer the thing being bought, which is far harder to price-compare."),
        ("Q1 refuses to answer the speed question",
         "&ldquo;You're not going to like this answer&rdquo; — then puts the timeline entirely on "
         "the buyer's own action. Same structural move as Miss Affiliate's 90-day video: decline "
         "the number, keep the credibility."),
        ("A legal-risk FAQ, disclaimed",
         "Q11 covers copyright, trademarks and product design, opening with &ldquo;I'm not an "
         "attorney, this is not legal advice.&rdquo; He tackles the objection that would stop a "
         "serious buyer, and hedges it explicitly."),
        ("YouTube carries the belief-building",
         "Four long-form videos totalling 63 minutes, including a $132,625-in-30-days case study, "
         "are embedded straight into the confirmation page. The funnel borrows credibility from "
         "an owned channel rather than building it all inside the webinar."),
        ("Application before price",
         "A Typeform gate sits between the masterclass and the call, so price is never shown to "
         "unqualified traffic."),
    ],

    "FUNNEL": [
        ("Masterclass opt-in", "ttwhizprogram.com/masterclass-opt-in…",
         "Name, email, <b>phone</b>. Zoom-hosted."),
        ("Confirmation", "ttwhizprogram.com/masterclass-confirmation…",
         "<b>11 FAQ videos + 2 VSLs + 4 YouTube embeds</b> all on one page."),
        ("Application", "pjb9yue2ih1.typeform.com/to/MITUqQQ2", "Qualification gate."),
        ("Call confirmed", "ttwhizprogram.com/call-confirmed-q", "Post-booking."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Pre-webinar FAQ — Q1 to Q11", qs),
        ("On-page VSLs", vsls),
        ("YouTube long-form", yts),
    ],

    "SLIDE_PAGES": [],

    "VIDEOS": [
        ("11 &times; Wistia FAQ (Q1&ndash;Q11)", 1566, "694 MB", "Pre-webinar objection handling."),
        ("ttw_vsl_1.mp4", 284, "60 MB", "Primary Vidalytics VSL on the confirmation page."),
        ("ttw_vsl_2.mp4", 110, "24 MB", "Secondary Vidalytics VSL."),
        ("YouTube &times; 4", 3828, "520 MB",
         "$132k/30-day case study, &ldquo;Why I Quit Affiliate&rdquo;, "
         "&ldquo;Be a Seller Instead&rdquo;, millionaire Q&amp;A."),
    ],

    "ANALYSIS": """
<div class="note"><b>The one idea here.</b> He does not compete inside his category — he
disqualifies the category's default offer. In a market saturated with TikTok Shop
<i>affiliate</i> programs, his lead asset is a video called &ldquo;Why I Quit TikTok Shop
Affiliate.&rdquo; That is a positioning move, not a copy move.</div>

<h2 class="sec">The pre-webinar page is doing three jobs at once</h2>
<div class="tablewrap"><table>
<tr><th>Layer</th><th>Asset</th><th>Job</th></tr>
<tr><td>Objection</td><td>11 Wistia FAQ videos, 26m</td><td>Pre-answer the sales conversation</td></tr>
<tr><td>Belief</td><td>4 YouTube long-forms, 63m</td><td>Borrow credibility from an owned channel</td></tr>
<tr><td>Urgency</td><td>2 Vidalytics VSLs</td><td>Drive attendance at the Sunday session</td></tr>
</table></div>
<p>Nearly 90 minutes of consumption offered between opt-in and event. Compare with our own
pre-class window, which is currently SMS nudges and nothing to watch.</p>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Disqualify the default</h3><p>Our category's default is &ldquo;become a UGC
creator, pitch brands.&rdquo; There is a version of this where we name what does not work about
the standard advice and position the Hybrid Model against it, rather than presenting it as one
more UGC course.</p></div>
<div class="card"><h3>Devalue the course, sell the layer</h3><p>Naming the module count and then
calling it the small part removes the price comparison against every $497 course. Ours is
similarly a support-and-system offer sold against content-only competitors.</p></div>
<div class="card"><h3>Answer the legal question out loud</h3><p>His Q11 handles copyright and
trademarks head-on with a disclaimer. Serious buyers ask serious questions; answering them
filters for exactly the buyer worth having.</p></div>
<div class="card"><h3>Refuse the speed number</h3><p>&ldquo;You're not going to like this
answer.&rdquo; Naming the discomfort before delivering it makes a non-answer land as honesty.</p></div>
</div>

<h2 class="sec">Still missing</h2>
<p>Price and the full pitch sit behind the Typeform application and the Sunday Zoom session.
Both are real live events, so neither can be pulled the way Richard Yu's and Karla Marie's
were.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
