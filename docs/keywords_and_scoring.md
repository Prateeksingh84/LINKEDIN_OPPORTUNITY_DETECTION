# Keywords & Scoring Logic

This document explains which keywords are used to detect agency/marketing opportunity posts, and how the scoring logic works for qualifying & prioritizing them.

---

## Keywords / Phrases to Detect Opportunity

Search for posts (case-insensitive) containing phrases like:

- “looking for agency”  
- “need marketing help”  
- “seeking branding partner”  
- “hiring digital agency”  
- “looking for a digital agency”  
- “need agency”  
- “agency required”  
- “seeking marketing support”  
- “need help with marketing”  
- “looking for marketing agency”  
- “RFP” / “request for proposal”  
- “budget for marketing”  
- “urgent marketing help”  
- “immediately”, “ASAP”, “within 30 days”, “this week”  

You may combine keywords (e.g. AND/OR) for more precise matching.

---

## Scoring Logic

To qualify and prioritize leads, we compute a score (0-100) based on several components. Here’s how:

| Component | Weight (Max Points) | What to Measure | Example / Rules |
|---|---|---|---|
| **Company Size / Revenue** | up to ~30 | Firmographic data (employee count, revenue) | > $50M → 30, $10-50M → 20, $1-10M → 10, < $1M → 5, unknown → moderate default. |
| **Engagement** | up to ~25 | Likes + Comments + Shares (or generic engagement) | Use log scale; if many likes/comments → higher score; cap at limit. |
| **Urgency / Timeline** | up to ~20 | Presence of urgency words: “ASAP”, “urgent”, “within X days/weeks” | If “ASAP” or “immediately” → full points; weaker signals less. |
| **Budget Indicators** | up to ~15 | Explicit presence of budget terms (“$”, “₹”, “budget”, “Series A”, “funded”) | Explicit numeric budget gets full; vague signals get partial; none → zero. |
| **Role of Poster / Signal of Decision Maker** | up to ~10 | Poster’s title or role (Founder, CEO, Head of Marketing etc.) | If senior leadership → full; mid-level → half; unknown → low. |

---

## Scoring & Thresholds

- **Total score** is sum of all components, capped at 100.  
- **Qualification threshold**: e.g. score ≥ 40 → “qualified”.  
- **High priority threshold**: e.g. score ≥ 70 → “high priority”.  

These thresholds can be tuned depending on dataset / industry.

---

## Examples

| Sample Post | Engagement | Firmographics | Urgency | Budget | Poster Role | Total Score | Priority |
|---|---|---|---|---|---|---|---|
| *“Looking for agency to run social campaigns — Budget $20k/month, start ASAP.”* | High | Mid-sized company | Urgent | Numeric budget | Decision-maker | ~80-90 | High |
| *“Need help with marketing.”* | Low | Small company | None | None | Manager | ~30-40 | Unqualified / Low |
| *“Seeking branding partner. Series A funding.”* | Medium | Startup with funding | Within 30 days | Funding mentioned | Founder / CMO | ~60-70 | Medium-High |

---

## Tuning Tips

- Adjust weights according to your priorities (e.g., if budget is most important, increase budget weight).  
- Examine false positives / negatives on your dataset; e.g., posts that score high but are irrelevant. Fine-tune keywords / filters.  
- For simulation mode, lower thresholds so you see some output.  
- Consider language / regional variations (e.g. local terms for “agency”, currency symbols).

