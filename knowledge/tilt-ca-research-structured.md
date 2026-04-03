# Tilt UX Knowledge Base
### Structured for Synthetic Agent Training | Source: Cash Advance Market Research Session 1

> **How to use this document:** Each section is designed to answer a specific question a synthetic user agent might need to reason from. Section 1 tells you *what users do*. Section 2 tells you *where they get stuck*. Section 3 tells you *how they feel*. Section 4 tells you *how they compare*. Section 5 tells you *who specifically they are*.

---

## SECTION 1: USER BEHAVIORAL PATTERNS BY JOURNEY STAGE

---

### STAGE 1 — AWARENESS
*How users discover cash advance apps and what they believe before they try*

**Discovery channels:**
- App store search (often after a triggering financial event)
- Word of mouth / peer referral ("a friend told me")
- Social media ads (which prominently display maximum advance amounts)
- Reddit threads on r/personalfinance, r/povertyfinance
- Google search for "emergency money" or "cash before payday"

**Pre-use mental models:**
- Most users do NOT frame it as borrowing. They frame it as "accessing money I've already earned," "borrowing from myself," or "a bridge."
- Users who've used payday loans previously see cash advance apps as the ethical upgrade — "no interest," "no credit check," "no shame."
- First-timers approach with skepticism: "Is this real? What's the catch?"
- The advertised maximum ($400 for Tilt, $500 for Dave, $750 for EarnIn) anchors their expectation of what they'll receive.

**Triggering events (from user evidence):**
- Internet bill cut off at 5am (Runeda, EarnIn user)
- Car repair needed to get to work
- Rent due before payday
- Utility shutoff notice
- Food for children (76% of hospitality EWA users cite food as primary reason — EBRI/Fourth, Fall 2024)
- Rent/housing (47% — EBRI/Fourth)
- "Everything just piled up at once"

**What users say at the awareness stage:**
- "I looked for loans but because of my bad credit, I wasn't qualified for any and then out of nowhere, this app appeared to me." — Hatchetface81, App Store ⭐⭐⭐⭐⭐
- "I downloaded about 20 Cash Advance Apps, Tilt was legit!" — Trustpilot
- "When you go to the payday loan, you are kind of watching your backs. Who's seeing me walk into this building?" — Lee, teacher (Nasdaq/NerdWallet interview)

**Behavioral signals:**
- 78% of cash advance app users are previous payday loan borrowers (DebtHammer)
- 65–67% of Americans live paycheck to paycheck (baseline condition)
- 37% can't cover a $400 emergency (Federal Reserve)
- Users compare 3–5+ apps before committing, often using Reddit for comparison

---

### STAGE 2 — ONBOARDING
*Signing up, connecting a bank account, understanding the product*

**What users expect:**
- Simple, fast signup
- Immediate access to the advance they came for
- To know how much they can borrow BEFORE they're charged anything
- No surprises on fees

**What actually happens:**
- Subscription ($8/month) is charged at or before the advance is offered
- First advance offered is frequently $10–$50, far below the advertised maximum
- Bank connection via Plaid can fail silently or block progress
- State eligibility for cash advance may not be disclosed until after subscription enrollment
- Pay frequency detection may be wrong, setting incorrect repayment dates from the start
- Some users are required to open an Empower/Tilt bank account to receive their advance (after approval)

**Onboarding UX observations (from internal competitor analysis):**
- Tilt: 12 screens for signup, 6 for CA enrollment, 14-day free trial
- Dave: 20 screens (most complex), 4 for CA, 7:16 completion time
- Albert: 24 screens (longest), 5:45 completion, small font + survey-heavy
- MoneyLion: 15 screens, 4:44, overwhelms users with options
- Earnin: 16 screens, 4:21, clean design with clear privacy explanations
- Brigit: 13 screens, 6:22, requires pre-Plaid confirmation checklist (account 2mo+ old, $1,500+/month deposits)

**User quotes — Onboarding:**
- "I did have to pay 8 bucks for the first month just to get an advance of 10 dollars, I'm a bit confused on that and pretty turned off about it due to the fact that I have used other apps like Dave and Albert and their fees are no where near that high, Dave's is somewhere around $1.99 or $2.99 a month and Albert I believe was free or $4.99 if you wanted to explore other features on the app." — April Workman, App Store ⭐⭐
- "Was approved for $400 advance. They have bank info but state i have to add my bank card. Problem is their app has a glitch that won't allow you to add. They are aware of glitch but have no eta on it. Must take out empower bank account and move direct deposit to get advance. They lied for hours before I finally realized its a scam to get you to open their bank account and send your deposits to them. RUN!!!!" — Michelle Anderson, Trustpilot ⭐
- "Empower allowed me to subscribe knowing that Cash Advance—the main feature promoted—was not available in [my state]. That was the only reason I signed up, not for budgeting tools or spend tracking." — BBB complaint
- "The criteria for a cash advance is written specifically for people that wouldn't even need a cash advance in the first place. You have to maintain a $50 balance for so many days for 4 pay periods. So, why would I borrow $50 if I could keep $50 in my account?" — ComplaintsBoard
- "The app incorrectly shows I'm paid monthly when I'm actually paid bimonthly, and customer support could not fix it. The chatbot kept repeating the same canned response with no option to reach a real person, which was frustrating." — Nicholas Baldwin, Trustpilot ⭐

**Behavioral signals:**
- Users abandon onboarding if asked for SSN without understanding why
- Users who see an advance estimate before giving payment info convert at higher rates
- Confusion between "Empower checking account" and "bank connection" is a recurring trap

---

### STAGE 3 — FIRST ADVANCE
*Requesting, receiving, and emotionally processing the first advance*

**What users expect:**
- The advertised maximum, or close to it
- Immediate delivery
- No additional fees beyond subscription
- A frictionless experience from request to receipt

**What actually happens:**
- Average first-time advance: ~$100 (Tilt internal data); ~$73 (Dave); ~$70 (Cleo)
- Instant delivery requires a fee ($1–$8 for Tilt; $3.99–$5.99 for EarnIn; $5.99 for Albert)
- Standard delivery is 1–3 business days (not the same day the user typically needs the money)
- Albert does not allow users to opt for standard delivery — instant is forced, fee mandatory
- Some apps default to instant with fee, hiding the free option (MoneyLion)

**The relief experience (when it works):**
- Users describe a literal physical/emotional release
- Speed is the #1 driver of first-impression satisfaction
- Being approved when no other option existed generates intense brand loyalty

**User quotes — First advance:**
- "I linked my new debit card and within a matter of seconds they transferred the money. I mean it literally was that fast." — Google Play ⭐⭐⭐⭐⭐
- "Bad credit saving money.. Because of Empower, I was able to pay a bill on time which saved my credit score from dropping even lower... the best part is you don't have to repay it all on the next paycheck like a payday loan.. they break up the payments up to 4 installments which is extremely helpful." — Hatchetface81, App Store ⭐⭐⭐⭐⭐
- "Thank you [Tilt] for giving me a chance when nobody else would." — Kris M., tilt.com testimonial (March 2025)
- "To be honest, I downloaded about 20 Cash Advance Apps, Tilt was legit! I RECOMMEND it EVERYONE!!" — Trustpilot
- "Fast money transfer! Emergency funds! It's like asking mom for money!" — Trustpilot
- "No one likes having to borrow money from friends or family! Now I can just borrow from myself through Tilt! It was so fast and easy and the money was in my account!" — Trustpilot
- "I had a surprise car repair and didn't know how I'd make rent. EarnIn let me access my pay instantly. It was a lifesaver." — EarnIn user
- "[After internet bill crisis] I prayed for this daily and I was blessed." — EarnIn App Store review
- "I feel like they should be a little more transparent and honest about the fee... I didn't see anything about a monthly fee until I checked my bank account and saw it deducted." — Brigit user

**Behavioral signals:**
- Users who receive funds within minutes become active word-of-mouth promoters
- Users who receive far less than expected ($10 on a $400 promise) rarely become repeat users
- Installment repayment option, when noticed at first advance, is cited as a differentiating positive
- Many users don't read fee disclosures; they discover fees by checking their bank statement

---

### STAGE 4 — REPEAT USE
*Returning to the app after first repayment; developing usage habits*

**What users expect:**
- Increasing advance limits over time as trust is established
- Stable, predictable limits they can plan around
- The same smooth experience as the first time

**What actually happens:**
- Some users see limit increases quickly (e.g., "$10 → increased really fast" — Trustpilot)
- Many loyal users experience unexplained limit decreases after months of perfect repayment
- App-hopping begins when one app's limit is insufficient — 53% use multiple apps in year 1 (CRL)
- Average returning customer advance: $174 (Tilt internal data)
- The product becomes a fixture in monthly budgeting, often replacing other financial tools
- 75% of EWA users took out a new advance on the same day or day after repayment (CRL)

**The cycle formation pattern:**
- Month 1–2: Emergency use, grateful, one-time mindset
- Month 3–6: Routine use, "it's part of my system now"
- Month 6–18: Dependency, advance is pre-spent before payday arrives
- Month 18+: Either entrapment (can't stop because each paycheck is depleted) or deliberate churn

**User quotes — Repeat use:**
- "Been using Empower/Tilt for about 3 years now. I definitely depend on my advances every month and they always seem to come at a time when I need them the most. My only complaint is the sudden drop in my cash advance amount like over a year ago. I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due." — paigecash, App Store ⭐⭐⭐⭐
- "It helps me out a lot but why does my amount keep decreasing. But overall it's great." — Trustpilot
- "This is a great app. At first, I was unaware there was a monthly subscription charge but it's a LOT cheaper than any app I've researched!" — Google Play ⭐⭐⭐⭐⭐
- "It just went completely out of control, and I was having to live off the borrowing apps." — Smith (Nasdaq/NerdWallet interview, on using 7–8 apps simultaneously)
- "You don't have room to breathe, it's like you can't breathe. Every dollar is accounted for. It leaves no room for error." — Runeda, EarnIn user
- "I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either." — Tomika Wright
- "I received 3 advances, which were all repaid on time and automatically with my checking account. All of a sudden, I'm unable to get any advances and a message saying 'unknown error' appears in the app and customer support has no idea and nothing they say works." — Google Play ⭐
- "I'm on my 4th advance with Empower and they still have not offered me more than $25." — Google Play (via Millennial Money)
- "It's also dangerous to get into this cycle of living beyond your means. I can draw $1000 from my next paycheck and it's dangerous to have your next paycheck instantly depleted and then you have to keep using it to not run out of money." — EarnIn App Store review
- "I also like the fact that they don't pressure you for 'tips' like other cash advance apps do." — paigecash, App Store

**Behavioral signals:**
- Average EWA user takes 27 transactions/year (vs. 8 for payday loan consumer)
- High-frequency users = 38% of users but 86% of all advances (CRL)
- 50% of active users accessed advances at least monthly in 2022
- 53% borrowed from multiple apps during first year
- 57% of hospitality EWA users used apps to avoid borrowing from friends/family

---

### STAGE 5 — REPAYMENT
*Auto-debit, timing, and the aftermath*

**What users expect:**
- Repayment will come out on or after payday
- They'll be notified before repayment occurs
- They can reschedule if needed
- No surprise deductions or overdraft consequences

**What actually happens:**
- Auto-debit sometimes fires before the expected deposit clears
- Repayment amount is pulled even when account balance is insufficient
- Overdraft fees from the bank compound the problem ($35 × multiple occurrences)
- Dave: manual repayment not allowed until 3 days before due date
- MoneyLion: repayment screen is hard to locate in app
- Brigit: offers one-time repayment extension option (differentiator)
- Some users can't repay and the account becomes "charged off," affecting credit; subscription charges continue even after charge-off

**User quotes — Repayment:**
- "Empower autodebited my bank account. They got paid, but I got an overdraft fee. I communicated with some 8-10 people at Empower, the last one, 'Lord', asked for a screenshot of my account, but never got back to me. This has been going on for 5 days, with no response from Empower. The overdraft had a domino effect on my bank account, resulting in additional overdrafts. None of this would have happened, but after months of successful repayments, Empower dropped my advance limit from $200 to $75! I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!" — Victor A, Trustpilot ⭐
- "On Dec 31 2025 I was debited $27.00 from a $50.00 advance. Afterwards, I was also debited on Jan 11 2026 $53.00 and on Jan 30 2026 $53.00 which I paid in full. My account has been overdrawn since Dec 30 2025 because my payment was not updated by the company named Tilt." — BBB complaint
- "During the change from Empower to Tilt, the app immediately pulled back a payment after an advance. Needing the advance, I did another draw, even though that meant paying for the draw again. Found out that the payment for the draw was not credited, even though they reset the draw amount available, and now I have double payments due at the end of the month. AND THERE IS NO OPTION FOR CUSTOMER SUPPORT CONTACT ON THE APP/WEBSITE." — Google Play ⭐
- "Account was charged off, could no longer take advances. Fair. Paid the collection agency. However, they continued to take their sub fee of $8 every month for 6 months despite the account no longer being eligible for the service. After months of back and forth, calls and emails, they offered me half of what they took despite not offering the service I'm paying for. Which is, you know, illegal." — Google Play ⭐
- "I opened an Empower (Thrive) account in 2024, I used cash advances and never missed one payment. All of a sudden they switched to Tilt and updated the app and every single one of my payments have failed stating 'Unfortunately, your account is not eligible, please use another account'. I have attempted to make OVER 50 payments on the app in the past 3 months." — BBB complaint
- "31% struggled to repay as scheduled; 17% skipped another bill to repay; 4% borrowed from a different app to repay the first." — DebtHammer survey data

**Behavioral signals:**
- Users who experience overdraft caused by Tilt's auto-debit become the loudest detractors on review platforms
- The overdraft domino effect is the most financially harmful outcome and the one most likely to generate regulatory complaints
- Users in the repayment friction zone are most likely to contact support, where they often encounter the chatbot wall (→ Stage 6)

---

### STAGE 6 — SUPPORT
*What happens when something goes wrong*

**What users expect:**
- A human who can fix the problem quickly
- Resolution within 24 hours for financial-harm issues
- Confirmation that their issue has been received and is being addressed

**What actually happens:**
- Chatbot-first, human-last (or never) support model
- Scripted, copy-paste responses that do not address the specific problem
- No in-app path to a live human for most issue categories
- Email responses that are generic or delayed
- No escalation path for financial-harm emergencies (overdrafts, blocked accounts, missing funds)
- After rebrand: some users found NO customer support option existed on the new app/website

**User quotes — Support:**
- "Customer service zero help. They just spout out prefabricated script. I cannot get my money back from Empower." — ComplaintsBoard
- "They read scripts and will just disconnect the chat whenever you as the customer are right." — ComplaintsBoard
- "The chatbot kept repeating the same canned response with no option to reach a real person, which was frustrating." — Nicholas Baldwin, Trustpilot ⭐
- "I communicated with some 8-10 people at Empower, the last one, 'Lord', asked for a screenshot of my account, but never got back to me. This has been going on for 5 days, with no response from Empower." — Victor A, Trustpilot ⭐
- "Customer service tells me it's issues with plaid connecting to my account and it will be fixed within 48 hours. That was 6 weeks ago. Funny no other app using plaid and my bank account has any issue." — ComplaintsBoard
- "I've been trying to resolve this for months. I've requested to close my account and I'm still waiting. Yet, they keep trying to hit my account for the monthly subscription fee. I do NOT recommend this app!" — Google Play ⭐
- "The app doesn't register anything. Login button stays gray and unusable. I have uninstalled/reinstalled at least 5 times... I contacted Empower customer service and they keep sending auto bot letters saying they working on it. This has been going on for weeks." — Rebecca Labosky, Trustpilot ⭐
- "Since they changed to Tilt, support doesn't exist." — WalletHub
- "AND THERE IS NO OPTION FOR CUSTOMER SUPPORT CONTACT ON THE APP/WEBSITE." — Google Play ⭐ [caps in original]
- "No one seems to understand English, and their advice was to just cancel my subscription. Done. Garbage app." — Google Play ⭐

**Behavioral signals:**
- Users who hit the support wall immediately escalate to BBB, Trustpilot, ComplaintsBoard — where they write the most detailed and damaging reviews
- Support failure on a financial-harm issue (overdraft, missing funds) converts a distressed user into an active detractor
- The "cancel and you owe money" loop is the most common reason users contact the BBB

---

## SECTION 2: FRICTION POINTS & EVIDENCE

---

### FRICTION POINT 1: The $8-for-$10 Shock
**What it is:** First-time users pay an $8 subscription fee only to receive a $10–$50 advance — a negative ROI on the first interaction.

**Evidence:**
- "I did have to pay 8 bucks for the first month just to get an advance of 10 dollars, I'm a bit confused on that and pretty turned off about it." — April Workman, App Store ⭐⭐
- "They cold-heartedly trap people into paying $11 or so a month in hopes they might qualify for advances in the future." — ComplaintsBoard
- Internal data: average first-time advance ~$100; many users receive $10–$50 on first draw
- Dave comparison: $1.99–$2.99/month subscription vs. Tilt's $8

**Journey stage:** Onboarding → First advance
**Severity:** CRITICAL

---

### FRICTION POINT 2: Advertised Maximum vs. Reality
**What it is:** Marketing leads with "$400" (Tilt), "$500" (Dave), "$750" (EarnIn) — none of which reflect the typical first-advance amount.

**Evidence:**
- Average first-time Tilt advance: ~$100 (internal)
- Average Dave advance: ~$73; FTC documented consumer: "I only was able to get 25.00. Not very helpful."
- FTC consumer on Dave: "got 2 small cash advances and paid them OFF ON TIME. They kept promising 500 for the past month and NEVER delivered."
- "They claim to offer up to $250 for cash advances. They watch your account activity and act like they know what's going on. They assume they know where your money comes from and offer you one amount one week and a lower amount the following week after paying them back the full amount early." — ComplaintsBoard
- "I'm on my 4th advance with Empower and they still have not offered me more than $25." — Google Play (via Millennial Money)
- Cleo: first-timers receive ~$70 despite $250 advertised max

**Journey stage:** Awareness → First advance
**Severity:** CRITICAL

---

### FRICTION POINT 3: Opaque Limit Decreases
**What it is:** Advance limits decrease suddenly and without explanation, often after many months of perfect repayment, with no pathway to restore the original limit.

**Evidence:**
- "I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due." — paigecash, App Store ⭐⭐⭐⭐
- "after months of successful repayments, Empower dropped my advance limit from $200 to $75!" — Victor A, Trustpilot ⭐
- "It helps me out a lot but why does my amount keep decreasing." — Trustpilot
- "False advertising... They assume they know where your money comes from and offer you one amount one week and a lower amount the following week after paying them back the full amount early. Then they lowered it by half." — ComplaintsBoard

**Journey stage:** Repeat use
**Severity:** CRITICAL

---

### FRICTION POINT 4: Overdraft Domino Effect
**What it is:** Auto-debit fires at the wrong time (before paycheck deposits), causing an overdraft that triggers additional overdraft fees, leaving users in a worse financial position than before they took the advance.

**Evidence:**
- "Empower autodebited my bank account. They got paid, but I got an overdraft fee... The overdraft had a domino effect on my bank account, resulting in additional overdrafts... I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!" — Victor A, Trustpilot ⭐
- "the app sets repayments before payday, expecting a $15 bank hit unless the date is shifted" — CashAdvanceApps.com
- "On Dec 31 2025 I was debited $27.00 from a $50.00 advance. Afterwards, I was also debited on Jan 11 2026 $53.00 and on Jan 30 2026 $53.00 which I paid in full. My account has been overdrawn since Dec 30 2025." — BBB complaint
- 31% of users struggled to repay as scheduled; 17% skipped another bill to repay (DebtHammer)

**Journey stage:** Repayment
**Severity:** CRITICAL

---

### FRICTION POINT 5: Cancellation Trap
**What it is:** Users who want to stop the service cannot easily cancel; they encounter subscription charges continuing after cancellation requests, requirements to pay balances before account closure, and chatbot loops.

**Evidence:**
- "I've deleted and unsubscribed from the app but still being charged." — BBB
- "when I try to cancel my account I'm told I owe money... I shouldn't be charged for keeping a service that I don't use or want." — Kyra Rose, Trustpilot ⭐
- "they continued to take their sub fee of $8 every month for 6 months despite the account no longer being eligible for the service." — Google Play ⭐
- "I've been trying to resolve this for months. I've requested to close my account and I'm still waiting." — Google Play ⭐
- "Tilt (firmly empower) has continuously been charging my account for $8 dollars subscriptions in which I have numerous emails requesting that they no longer bill me and they continue to do so." — BBB
- "Will take a 'SUBSCRIPTION' fee right outa your damn account without your permission!!!!!!!! Cost me 30 bucks at Chase to keep their greedy little fingers outa my account!!!" — G.K.J., Trustpilot ⭐
- FTC sued Brigit (Nov 2023, $18M) specifically for "difficult cancellation" — same pattern industry-wide

**Journey stage:** Support / Churn
**Severity:** CRITICAL

---

### FRICTION POINT 6: Support Black Hole
**What it is:** Customer service is chatbot-driven with scripted responses; no human escalation path for financial-harm situations; users with urgent financial emergencies are left unresolved for days or weeks.

**Evidence:**
- "Customer service zero help. They just spout out prefabricated script." — ComplaintsBoard
- "They read scripts and will just disconnect the chat whenever you as the customer are right." — ComplaintsBoard
- "I communicated with some 8-10 people at Empower... This has been going on for 5 days, with no response from Empower." — Victor A, Trustpilot ⭐
- "The chatbot kept repeating the same canned response with no option to reach a real person." — Nicholas Baldwin, Trustpilot ⭐
- "AND THERE IS NO OPTION FOR CUSTOMER SUPPORT CONTACT ON THE APP/WEBSITE." — Google Play ⭐
- "since they changed to Tilt, support doesn't exist." — WalletHub
- "the copy/paste soulless response this review will get be 100% by far the most they've ever acknowledged me" — Brigit user (same pattern)

**Journey stage:** Support
**Severity:** CRITICAL

---

### FRICTION POINT 7: Rebrand Technical Failures
**What it is:** The August 2025 Empower→Tilt rebrand caused widespread technical failures — broken payment processing, locked accounts, lost verification states, inaccessible repayment screens, and missing support channels.

**Evidence:**
- "All of a sudden they switched to Tilt and updated the app and every single one of my payments have failed stating 'Unfortunately, your account is not eligible, please use another account'. I have attempted to make OVER 50 payments on the app in the past 3 months." — BBB
- "During the change from Empower to Tilt, the app immediately pulled back a payment after an advance... now I have double payments due at the end of the month." — Google Play ⭐
- "Empower was a wonderful service however when they decided to rebrand thats when all of the trouble started. I would advise anyone that is unsatisfied to close their account because I can gaurantee with all of the issues its not going to get any better." — Renee Lindsey, Trustpilot ⭐

**Journey stage:** Repeat use / Support
**Severity:** CRITICAL

---

### FRICTION POINT 8: Subscription Charged Before Eligibility Confirmed
**What it is:** Users are charged the $8 subscription before the app has confirmed they qualify for an advance — or while simultaneously denying their advance request.

**Evidence:**
- "Tilt IMMEDIATELY takes money out of your account if you link a bank account when applying for a cash advance. They immediately deny you for the advance... and they still fraudulently take funds from customers." — BBB
- "Empower allowed me to subscribe knowing that Cash Advance—the main feature promoted—was not available in [my state]." — BBB
- "They charged me for services I didn't receive. They are stealing." — BBB (re: $8 fee taken, $250 advance never received)

**Journey stage:** Onboarding
**Severity:** CRITICAL

---

### FRICTION POINT 9: Pay Frequency Misdetection
**What it is:** The automated system incorrectly identifies a user's pay schedule, resulting in wrong repayment dates and blocked advances — and support cannot manually correct it.

**Evidence:**
- "The app incorrectly shows I'm paid monthly when I'm actually paid bimonthly, and customer support could not fix it." — Nicholas Baldwin, Trustpilot ⭐
- Brigit noted as differentiator for offering manual payday override (internal competitor analysis)
- Internal competitor analysis recommendation: "Verified or Editable Paydays: Some competitors allow users to confirm or adjust their next payday to better align with their real-world income cadence"

**Journey stage:** Onboarding → Repayment
**Severity:** Significant

---

### FRICTION POINT 10: Plaid Connection Fragility
**What it is:** Bank connection via Plaid fails silently or intermittently, blocking advance access for weeks while support offers only "wait 48 hours" responses — indefinitely.

**Evidence:**
- "Customer service tells me it's issues with plaid connecting to my account and it will be fixed within 48 hours. That was 6 weeks ago." — ComplaintsBoard
- "I have uninstalled/reinstalled at least 5 times... I contacted Empower customer service and they keep sending auto bot letters saying they working on it. This has been going on for weeks." — Rebecca Labosky, Trustpilot ⭐
- "I updated my information in the Tilt app and had no problem for 3 months. Suddenly, it says I need to verify my account, but it keeps sending the verification code to my old email." — WalletHub

**Journey stage:** Onboarding / Repeat use
**Severity:** Significant

---

### FRICTION POINT 11: The Eligibility Catch-22
**What it is:** The users most in need of an advance (low or negative balance, irregular income) are systematically excluded by eligibility requirements designed around financial stability.

**Evidence:**
- "The criteria for a cash advance is written specifically for people that wouldn't even need a cash advance in the first place. You have to maintain a $50 balance for so many days for 4 pay periods." — ComplaintsBoard
- "The irony is that if I HAD money in my bank account, the necessity to use Float Me wouldn't exist." — FloatMe user, App Store
- "if your account is in the negative by over $50 dollars in the negative they won't send the advance." — Google Play (Tilt user)
- Brigit requires 2+ paychecks deposited before first advance; $1,500+/month deposit minimum (internal analysis)

**Journey stage:** Eligibility / Onboarding
**Severity:** Significant

---

### FRICTION POINT 12: Instant Delivery Fee Opacity
**What it is:** Users who need money urgently (the entire reason they're using the app) often don't realize they'll pay an additional fee for immediate delivery — and standard delivery can take 1–3 business days.

**Evidence:**
- Tilt: $1–$8 instant fee (on top of $8 subscription)
- Albert: forces instant transfer; cannot opt out; $5.99 fee on a $17 advance cited as extreme
- Brigit: forces instant; $2.99 on a $20 advance
- MoneyLion: defaults to instant with fee; no-fee option is harder to find
- "At first, I was unaware there was a monthly subscription charge but it's a LOT cheaper than any app I've researched!" — Google Play (positive framing, but revealing that fees are discovered post-fact)
- EarnIn requires 13 additional clicks and 17 messages to get an advance without a tip

**Journey stage:** First advance / Repeat use
**Severity:** Significant

---

## SECTION 3: EMOTIONAL MOMENTS

---

### HIGH: The Rescue Moment
**When it occurs:** Immediately after a successful first advance deposits
**Emotional register:** Overwhelming gratitude, relief, physical release, loyalty formed instantly

**Verbatim user language:**
- "I prayed for this daily and I was blessed." — EarnIn App Store reviewer
- "It's like asking mom for money!" — Tilt Trustpilot
- "Fast money transfer! Emergency funds!" — Tilt Trustpilot
- "No one likes having to borrow money from friends or family! Now I can just borrow from myself through Tilt!" — Tilt Trustpilot
- "I'm so lost for words, this is an awesome app. You can count on them when you need fast, easy, and reliable cash." — Tyra S., tilt.com (January 2025)
- "I feel like they should be a little more transparent and honest about the fee... I didn't see anything about a monthly fee until I checked my bank account." — Brigit user [note: even here, the advance itself was a positive]
- "I had a surprise car repair and didn't know how I'd make rent. EarnIn let me access my pay instantly. It was a lifesaver." — EarnIn user
- "I'm writing this review to extend my eternal gratitude." — EarnIn App Store reviewer
- "It's almost like endorphins." — Lee, teacher (DailyPay user, Nasdaq interview)
- "Thank you for giving me a chance when nobody else would." — Kris M., tilt.com (March 2025)
- "I felt appreciated and could just be myself and no worries of being abused or embarrassed or belittled." — Tilt Trustpilot

**Design note:** This moment is the emotional peak of the entire user journey. Everything in the UX should protect and amplify it.

---

### HIGH: The Dignity Moment
**When it occurs:** When a user realizes they can solve a financial problem without involving family, friends, or a physical loan office
**Emotional register:** Pride, relief, restored self-respect

**Verbatim user language:**
- "No one likes having to borrow money from friends or family! Now I can just borrow from myself through Tilt!" — Tilt Trustpilot
- "I felt appreciated and could just be myself and no worries of being abused or embarrassed or belittled." — Tilt Trustpilot
- "When you go to the payday loan, you are kind of watching your backs. Who's seeing me walk into this building? But the cash advance, uh, apps, it's private. There's this huge social stigma against people who are poor. Everyone I know is in debt. But we have to pretend like we're not. And there's a lot of shame wrapped up in that." — Lee, teacher (Nasdaq/NerdWallet interview)
- 57% of hospitality EWA users said the app helped them avoid borrowing from friends and family (EBRI/Fourth survey)

---

### HIGH: The "Finally Someone Trusted Me" Moment
**When it occurs:** After being rejected by banks, credit cards, or traditional lenders — approval by Tilt feels personal and meaningful
**Emotional register:** Deep gratitude, trust, loyalty

**Verbatim user language:**
- "I looked for loans but because of my bad credit, I wasn't qualified for any and then out of nowhere, this app appeared to me." — Hatchetface81, App Store ⭐⭐⭐⭐⭐
- "thank you so much for taking a chance on me and trusting that I'll pay back the money that was loaned to me." — Hatchetface81, App Store
- "Thank you [Tilt] for giving me a chance when nobody else would." — Kris M., tilt.com

---

### LOW: The First Fee Shock
**When it occurs:** When user checks their bank account and finds $8 missing before they've received any value
**Emotional register:** Confusion transitioning to distrust

**Verbatim user language:**
- "I did have to pay 8 bucks for the first month just to get an advance of 10 dollars, I'm a bit confused on that and pretty turned off about it." — April Workman, App Store ⭐⭐
- "Will take a 'SUBSCRIPTION' fee right outa your damn account without your permission!!!!!!!! Cost me 30 bucks at Chase to keep their greedy little fingers outa my account!!!" — G.K.J., Trustpilot ⭐
- "They took 5$ out of my account every week until it reached 105$... I've been paying 8$ a month after that for 2 years, and now I owe late payments, empower tilt is the worst they have stolen a ton of money out of my account." — Joshua Tillery, Trustpilot ⭐

---

### LOW: The Limit Drop Betrayal
**When it occurs:** When a loyal, on-time user sees their advance limit cut without warning or explanation
**Emotional register:** Confusion, then indignation, then helplessness (no one can explain it)

**Verbatim user language:**
- "I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due." — paigecash, App Store ⭐⭐⭐⭐
- "after months of successful repayments, Empower dropped my advance limit from $200 to $75! I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!" — Victor A, Trustpilot ⭐

---

### LOW: The Overdraft Cascade
**When it occurs:** When auto-debit fires before paycheck arrives, triggering bank overdraft fees that exceed the original advance
**Emotional register:** Panic, rage, sense of victimization

**Verbatim user language:**
- "I am disabled, recently got out of the hospital to a mess! Empower autodebited my bank account... The overdraft had a domino effect on my bank account, resulting in additional overdrafts... I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!" — Victor A, Trustpilot ⭐
- "My account has been overdrawn since Dec 30 2025 because my payment was not updated by the company named Tilt." — BBB complaint

---

### LOW: The Tip Pressure Moment (competitor — EarnIn/Dave)
**When it occurs:** When a user is navigating to complete an advance and encounters dark patterns pressuring a "tip"
**Emotional register:** Anger, feeling manipulated, betrayal of trust

**Verbatim user language:**
- "The audacity. I am here to borrow money. I don't have any to give you." — Runeda, EarnIn user (Nasdaq interview)
- "I turned on the overdraft protection shield and without my knowledge it tipped the app automatically which is supposed to be optional... that felt like a violation of my trust." — EarnIn reviewer
- "I feel deceived by it, it's crazy. It's absolutely insane." — Lee, teacher (on discovering true cost of EWA)
- EarnIn documented: animated child made sad when user reduces tip; 13 additional clicks required to avoid tipping; 17 messages about tipping importance (NCLC)
- Dave: FTC found animated child made sad when users reduced tips; $68M from tips in one year

---

### LOW: The Support Wall
**When it occurs:** When a user with an urgent financial problem reaches the chatbot and cannot get a human
**Emotional register:** Helplessness, rage, desperation

**Verbatim user language:**
- "Customer service zero help. They just spout out prefabricated script. I cannot get my money back from Empower." — ComplaintsBoard
- "They read scripts and will just disconnect the chat whenever you as the customer are right." — ComplaintsBoard
- "AND THERE IS NO OPTION FOR CUSTOMER SUPPORT CONTACT ON THE APP/WEBSITE." — Google Play ⭐ [caps in original]

---

### LOW: The Dependency Recognition
**When it occurs:** When a user realizes, usually mid-cycle, that they can no longer reach payday without an advance — they are structurally dependent
**Emotional register:** Shame, exhaustion, trapped feeling

**Verbatim user language:**
- "You don't have room to breathe, it's like you can't breathe. Every dollar is accounted for. It leaves no room for error." — Runeda, EarnIn user
- "It just went completely out of control, and I was having to live off the borrowing apps." — Smith (7–8 apps simultaneously)
- "I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either." — Tomika Wright
- "It's dangerous to have your next paycheck instantly depleted and then you have to keep using it to not run out of money." — EarnIn App Store reviewer
- "[After the internet bill], that setback meant Runeda had to borrow again just 3 days later for gas, and 4 days after that for a utility bill. Which meant her next paycheck was smaller, which meant she ended up borrowing again 3 more times over the next week." — Runeda's cycle documented (Nasdaq)

---

## SECTION 4: COMPETITOR INSIGHTS

---

### DAVE — What Users Say

**Positive:**
- Low subscription fee ($1.99–$2.99/month) vs. Tilt's $8
- Referral program: 20% boost on next advance for referring a friend
- Budgeting tools included
- Clear value prop messaging during onboarding ("safety, trust, member success")

**Negative:**
- FTC sued Dave (November 2024) for misleading consumers about advance amounts and undisclosed fees/tips
- Average advance: $73 despite $500 advertised maximum
- "tricked me into opening a checking account (no clear exit)" — internal competitor analysis
- Manual repayment not allowed until 3 days before due date
- After clicking repayment notification, settlement screen hard to find
- Advance amount shown ($50), then removed later without explanation
- Animated child made sad when users reduced tips (FTC complaint)
- $68 million from tips in one year — tip pressure is structural
- 3–5 day delivery without paying a fee
- Recent App Store score: 3.4 (declining)

**User quotes:**
- FTC consumer: "They keep promising 500 for the past month and NEVER delivered."
- FTC consumer: "[Dave] claims you can borrow up to 500.00 dollars. But, I only was able to get 25.00. Not very helpful."
- "I decided I will be closing my account with Dave" — Reddit user after "weird charges"

**Tilt opportunity vs. Dave:** No-tip policy; installment repayment; higher subscription converts to better perceived value if advance amounts are competitive

---

### BRIGIT — What Users Say

**Positive:**
- Repayment extension: one-time option to delay payment due date (unique feature)
- Auto-advances: sends cash automatically when low balance detected
- Progress indicator in onboarding
- $15 referral bonus
- Edit payday: manual payday override option
- Shows "future eligibility" when clicked on locked amounts
- Affiliate partner marketplace in-app

**Negative:**
- FTC $18M settlement (November 2023) for deceptive "free" marketing and difficult cancellation
- $8.99–$15.99/month — highest subscription in category
- Offer evaluation took 60+ seconds
- Requires 2+ paychecks deposited; $1,500+/month minimum — strict eligibility
- Forces instant transfer; no free standard delivery option ($2.99 on $20 CA)
- Cancellation is difficult and deliberately obfuscated
- Copy-paste support responses

**User quotes:**
- "their service all around is just abysmal.. you need to re-enter your debit card info constantly (and takes days to update), their customer service support is garbage if not, just straight up nonexistent. The copy/paste soulless response this review will get be 100% by far the most they've ever acknowledged me.. you have REQUEST to have your account back to a free service from a 10$ month sad excuse of a service.. REQUEST TO DEACTIVATE YOUR ACCOUNT.. like what universe are they in?" — Brigit App Store reviewer
- "I feel like they should be a little more transparent and honest about the fee... I didn't see anything about a monthly fee until I checked my bank account and saw it deducted. Not a huge deal to some, but apps like Earnin charge absolutely no fees. You can tip IF YOU WANT to." — Brigit reviewer

**Tilt opportunity vs. Brigit:** No-interest, no-tip positioning; repayment extension feature worth testing (identified in internal analysis); auto-advance feature worth testing

---

### EARNIN — What Users Say

**Positive:**
- No monthly subscription — highest trust signal in category
- Optional tips (though dark patterns exist)
- Up to $750/pay period ($150/day)
- Clean, simple design
- Clear privacy explanation for payroll linking
- Employment verification creates stronger underwriting (GPS/work email)
- Social proof: "3.8 million users" cited prominently
- Debit card optional during onboarding

**Negative:**
- Requires employment verification — excludes gig workers, irregular employment
- $3.99–$5.99 instant transfer fee (on top of $0 subscription — effective cost comparison complex)
- Tips are technically optional but dark-patterned: 13 clicks to avoid, 17 messages about importance
- Doesn't work with PayPal, Varo, Venmo
- $150/day limit even though $750/period is available — creates multi-day friction in emergencies
- Tips collected 73% of the time

**User quotes:**
- "2025 has been hard, man... I don't think my family and I would even be remotely okay without EarnIn. It's been more than an app it's been a lifeline." — EarnIn Trustpilot
- "I've used this for 6 months now. I never pay fees, I just tip $2 when I can. Honestly the best alternative to payday loans." — EarnIn reviewer
- "Very trust worthy app! No hidden agendas, no hassle, it just works!" — EarnIn reviewer
- "Terrible now. They tell you you're approved for a certain amount (say 400-500) but won't let you withdraw it all in one day, it has to be done over a span of several days." — EarnIn reviewer (recent decline)
- "The audacity. I am here to borrow money. I don't have any to give you." — Runeda, on EarnIn tip pressure

**Tilt opportunity vs. EarnIn:** No-tip model is Tilt's strongest differentiator here; eligibility for users without traditional employment is a significant advantage; installment repayment is a structural advantage

---

### MONEYLION — What Users Say

**Positive:**
- No subscription for basic access
- Up to $1,000 with RoarMoney account + direct deposit
- Lowest instant transfer fees ($0.49–$8.99)
- Boost feature: community members can help each other increase CA limits
- Flexible disbursement destinations (other debit cards)
- New CA available immediately after repayment
- Any-amount manual repayment
- In-app walkthrough on first open
- Referral program in onboarding

**Negative:**
- CFPB sued for Military Lending Act violations
- Best features require RoarMoney account (not transparent upfront)
- App experience "feels overwhelming; lots of screens to tap through"
- Website UI feels clunky
- Repayment screen hard to locate
- Defaults to instant (with fee); no-fee option buried
- SSN required during onboarding
- 2–5 business days free delivery (slowest in category)
- Eligibility logic unclear

**Tilt opportunity vs. MoneyLion:** Simpler, less overwhelming UX; transparency about eligibility; faster standard delivery

---

### ALBERT — What Users Say

**Positive:**
- Up to $1,000 advance (highest max alongside MoneyLion)
- "Smart Money" savings feature
- Privacy Promise during onboarding
- Referral incentive at onboarding
- Alerts when cash advance becomes available
- Investing feature (unique differentiator)
- Partial advance: can access remainder later

**Negative:**
- $14.99–$39.99/month — highest fees in category
- Must activate "Smart Money" to become eligible for cash advance (hidden gating)
- No offer shown after connecting bank — users wait without feedback
- Forces instant transfer; cannot opt for free standard delivery
- $5.99 instant fee on a $17 advance = 35% effective cost
- Repayment not via debit card
- Small font, survey-heavy screens
- Recent App Store score: 2.7 — steepest decline in category

**User quotes:**
- "A scam, do not download. They will steal your money saying it's an investment then will never give it back." — Albert Trustpilot reviewer

**Tilt opportunity vs. Albert:** Lower fees; no hidden feature gating; clearer offer after bank connection; debit card repayment option

---

### CHIME SPOTME — What Users Say

**Positive:**
- $0 monthly fee — highest trust signal
- Instant overdraft coverage
- No fees whatsoever
- Simplest product in category
- Credit building tools
- MyPay: up to $500 for flat $2 fee (new)

**Negative:**
- Requires Chime checking account + $200+/month direct deposit — high barrier
- $200 cap (SpotMe) is too low for many emergencies
- Locked into Chime ecosystem entirely

**Tilt opportunity vs. Chime:** Higher advance amounts; works with existing bank accounts; no ecosystem lock-in

---

### CLEO — What Users Say

**Positive:**
- AI chatbot personality — users enjoy the conversational interface
- Up to $250 ($500 with Builder plan)
- Roast Mode / Hype Mode — gamified financial coaching with humor

**Negative:**
- First-timers receive ~$70 despite $250 advertising
- $1–$19.99/month; $3.99–$14.99 instant fee
- Recent App Store score: 2.9 (sharp decline from 4.5)
- Chatbot personality praised; advance product increasingly criticized

**Tilt opportunity vs. Cleo:** No-tip, no-dark-pattern trust; more transparent first-advance amount; better customer support (table stakes)

---

### FLOATME — What Users Say

**Positive:**
- Low cost: $1.99/month
- Simple, low-friction product

**Negative:**
- Max $50 — lowest in category by far
- Balance-check eligibility: users with low balances (the target user) often denied
- No credit building

**User quotes:**
- "There are times when my main accounts get SO low (we're in the middle of a pandemic) that an extra $20 offered by FM would make all the difference in the world... With the restrictions shown on the app with regard to bank balances, that check to see if you have money in your account or not, will automatically deny your request for a $20 float. The irony is that if I HAD money in my bank account, the necessity to use Float Me wouldn't exist." — FloatMe App Store reviewer

---

### CROSS-COMPETITOR: What Reddit Users Say About the Category

- Tilt/Empower consistently mentioned as "one of the best options" on Reddit positive threads
- Subscription-charge-while-ineligible is the most common negative Empower/Tilt complaint on Reddit
- Difficulty unlinking bank accounts is a second major Reddit complaint
- EarnIn described as the "most trustworthy" due to no subscription
- "Which cash advance app is best" threads consistently compare: EarnIn (no fees), Dave (low fee, high max), Brigit (auto-advance), Empower/Tilt (solid all-around, $8 fee)
- From multi-app user on Gerald: "All in all I've tried a lot of these apps... Dave, Bridget, Albert, Empower, Cleo, and Cash-App have all given me a far better experience in the past. At least they actually deliver what they promise and in a timely fashion."

---

## SECTION 5: ARCHETYPE-SPECIFIC FINDINGS

> **Note on archetypes:** The original research identified 4 archetypes. Per this brief's instruction, findings are mapped here to 5 archetypes: **Crisis**, **Liquidity Stabilizer**, **Hybrid**, **Credit Builder**, and **Optimizer**. Mapping is based on behavioral and motivational evidence from the research.

---

### ARCHETYPE 1: THE CRISIS USER
*"I need money right now or something catastrophic happens"*

**Profile:**
- First-time or infrequent user
- Triggered by a specific, acute emergency: rent, car repair, utility shutoff, medical bill
- Emotionally: panic → desperate hope → intense relief or intense disappointment
- Does NOT think of themselves as someone who "uses cash advance apps" — this is a one-time thing
- Deeply affected by the privacy/dignity dimension — refuses payday loans due to stigma

**Behavioral evidence:**
- 76% of hospitality EWA users cite food as primary reason for first use; 47% cite rent/housing (EBRI/Fourth)
- 77% of workers would face financial difficulty if paycheck delayed one week
- 37% of US adults can't cover $400 emergency (Federal Reserve)
- Discovery is reactive: user searches "emergency money app" or "cash before payday" in a stressful moment
- Speed to funds is the singular metric — everything else is secondary

**Specific journey friction:**
- Onboarding length is felt acutely — every screen is a delay from solving the crisis
- Any fee surprise is devastating: "I needed $300 and I'm paying $8 for $10?"
- If the advance amount doesn't cover the emergency, the product failed — even if technically it worked
- State eligibility gap: user discovers cash advance isn't available in their state after paying subscription
- Waiting 1–3 business days is not viable — must pay the instant fee (which they didn't budget for)

**Representative verbatim quotes:**
- "I had like 50 bucks in my bank account. That was the first domino and everything else just kind of fell apart from there." — Runeda, EarnIn user
- "thank you so much for taking a chance on me and trusting that I'll pay back the money that was loaned to me." — Hatchetface81, App Store
- "I prayed for this daily and I was blessed." — EarnIn App Store reviewer
- "I'm so lost for words, this is an awesome app. You can count on them when you need fast, easy, and reliable cash." — Tyra S., tilt.com
- "Fast money transfer! Emergency funds! It's like asking mom for money!" — Tilt Trustpilot
- "I feel like they should be a little more transparent and honest about the fee... I didn't see anything about a monthly fee until I checked my bank account." — Brigit user

**What Tilt does right for this archetype:**
- Instant delivery option
- No-interest framing
- No credit check
- Works with existing bank account (no ecosystem lock-in)
- Installment repayment reduces payday-evaporation risk

**What Tilt does wrong for this archetype:**
- $8 subscription charged before/alongside $10 first advance
- Advance amount far below emergency amount needed
- State eligibility not disclosed upfront
- Instant delivery fee not visible until after commitment

---

### ARCHETYPE 2: THE LIQUIDITY STABILIZER
*"I use this every month to smooth out the gaps — it's part of my system"*

**Profile:**
- Long-term user (6+ months, often 2–3+ years)
- Uses advance predictably every pay cycle
- Has mentally incorporated the advance into their monthly budget
- Advance is pre-spent — the paycheck arrives already partially depleted
- NOT thinking of stopping: "I depend on this"
- Single parent, hourly worker, or fixed-income more likely

**Behavioral evidence:**
- Average returning customer advance: $174 (Tilt internal)
- 50% of active EWA users accessed advances at least monthly in 2022
- 75% took new advance same day or day after repayment (CRL)
- High-frequency users: 38% of users, 86% of all advances (CRL)
- Average user takes 27 EWA transactions/year

**Specific journey friction:**
- Limit decrease is devastating — they budget around their limit. A drop from $175 to $75 disrupts their entire month.
- Repayment timing failure (auto-debit before paycheck) causes overdraft cascades
- App outages, rebrand failures, Plaid disconnections block access at critical moments
- Subscription charges continuing when account is ineligible or during account closure

**Representative verbatim quotes:**
- "Been using Empower/Tilt for about 3 years now. I definitely depend on my advances every month and they always seem to come at a time when I need them the most. My only complaint is the sudden drop in my cash advance amount like over a year ago. I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due." — paigecash, App Store ⭐⭐⭐⭐
- "You don't have room to breathe, it's like you can't breathe. Every dollar is accounted for. It leaves no room for error." — Runeda, EarnIn user
- "I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either." — Tomika Wright
- "I received 3 advances, which were all repaid on time and automatically with my checking account. All of a sudden, I'm unable to get any advances and a message saying 'unknown error' appears in the app and customer support has no idea." — Google Play ⭐
- "Been paying 8$ a month after that for 2 years, and now I owe late payments, empower tilt is the worst they have stolen a ton of money out of my account." — Joshua Tillery, Trustpilot ⭐

**What Tilt does right for this archetype:**
- Installment repayment prevents full paycheck evaporation
- No-tip policy vs. EarnIn/Dave (explicitly valued)
- Credit monitoring adds perceived value beyond the advance
- Advance reliability (when it works) creates habitual loyalty

**What Tilt does wrong for this archetype:**
- Zero transparency on limit change algorithm
- No proactive communication before limit decreases
- Subscription keeps charging even during service failures
- Auto-debit timing doesn't adapt to actual deposit timing
- No future eligibility indicator ("your limit may increase on [date]")

---

### ARCHETYPE 3: THE HYBRID
*"I use this sometimes for emergencies and sometimes just to smooth things out — it depends on the month"*

**Profile:**
- Moderate user frequency (monthly or bi-monthly, not every pay cycle)
- Uses advance for specific situations, not as structural budget tool
- More financially stable than Liquidity Stabilizer but still periodically cash-constrained
- May also have a credit card but it's maxed or reserved for larger purchases
- More likely to be comparison-shopping / app-hopping

**Behavioral evidence:**
- 53% borrowed from multiple apps during first year (CRL)
- Nearly 50% of borrowers used multiple companies in the same month (CRL)
- App-hopper: uses Dave for high amount, Brigit for auto-advance protection, Tilt for reliable mid-range
- More likely to read and post Reddit reviews; more analytically engaged

**Specific journey friction:**
- Fee structure comparison is more active — $8/month is evaluated monthly
- App-switching creates repayment complexity (multiple auto-debits can collide)
- They notice when the advance amount doesn't grow despite good repayment history
- More likely to cancel if a competitor offers equivalent value at lower cost

**Representative verbatim quotes:**
- "It just went completely out of control, and I was having to live off the borrowing apps." — Smith (7–8 apps simultaneously)
- "I am rating this app 2 stars for now due to I did have to pay 8 bucks for the first month just to get an advance of 10 dollars... Dave's is somewhere around $1.99 or $2.99 a month and Albert I believe was free or $4.99." — April Workman, App Store ⭐⭐
- "All in all I've tried a lot of these apps... Dave, Bridget, Albert, Empower, Cleo, and Cash-App have all given me a far better experience in the past." — Gerald App Store reviewer
- "I've used this for 6 months now. I never pay fees, I just tip $2 when I can. Honestly the best alternative to payday loans." — EarnIn user (active comparator mindset)

**What Tilt does right for this archetype:**
- No-tip policy is clearly superior to Dave/EarnIn
- 14-day free trial enables low-commitment trial
- Credit monitoring and budgeting add ancillary value that keeps them subscribed in off months

**What Tilt does wrong for this archetype:**
- $8/month is hardest to justify in months where no advance is taken
- No "pause subscription" option documented
- Limit opacity makes planning impossible — they can't reliably know how much they can access

---

### ARCHETYPE 4: THE CREDIT BUILDER
*"I'm using this as a stepping stone — I want to fix my credit and eventually not need this"*

**Profile:**
- Motivated by financial improvement, not just immediate need
- Views Tilt as a transitional tool, not a permanent fixture
- Engages with credit monitoring, budgeting tools, and savings features
- May have been explicitly told by a credit counselor or article to try cash advance apps
- More responsive to "earn your way up" limit increase framing

**Behavioral evidence:**
- [INFERENCE — limited direct evidence in this dataset; behavioral patterns inferred from product feature engagement]
- Tilt's own product suite (credit monitoring, AutoSave, Thrive Line of Credit, Tilt credit cards) is explicitly designed for this archetype
- Albert's "Smart Money" savings feature gates CA eligibility — targets this archetype
- Some users explicitly mention wanting to "rebuild credit": "help you rebuild your credit!! I promise you!!" — App Store reviewer
- Installment repayment appeals specifically because it "doesn't put me back where I started"

**Specific journey friction:**
- Confusion between Cash Advance and Thrive Line of Credit products
- Not understanding how limit increases are earned
- Savings features pulling from account unexpectedly
- Credit building features hidden below the fold vs. cash advance primary CTA

**Representative verbatim quotes:**
- "This app will help you rebuild your credit!! I promise you!!" — App Store ⭐⭐⭐⭐⭐
- "This was just the first time using, but applying and connecting to my bank was very fast and the advance was super fast! I love how they don't let you go overboard. From what I've seen so far, they are here to help you with advances within reason, help you to save money and eventually get a line of credit, and help you rebuild your credit at the same time." — App Store ⭐⭐⭐⭐⭐
- "the best part is you don't have to repay it all on the next paycheck like a payday loan.. they break up the payments up to 4 installments which is extremely helpful, especially when I don't make a great amount of money.. payday loans that have to be paid back all at once put me back where i started." — Hatchetface81, App Store ⭐⭐⭐⭐⭐
- "Once I found out about paying myself first, it was a game changer for me." — Tomika Wright (escape from cycle narrative)
- "A good payment history leads to an increase in your accessible funds. It monitors my spending and credit score as well. $8 a month is well worth the convenience." — WalletHub reviewer

**What Tilt does right for this archetype:**
- Credit monitoring included in subscription
- Installment repayment is structurally better for credit health than lump-sum
- AutoSave feature aligns with self-improvement motivation
- Thrive Line of Credit and Tilt credit card create a clear upgrade path
- No-interest framing ("you're not in debt, you're bridging")

**What Tilt does wrong for this archetype:**
- No visible progress indicators toward limit increases
- No "you're on track for a limit increase in X days" messaging
- Credit builder journey is fragmented across products
- Savings feature can pull from account unexpectedly, undermining trust in the product that's supposed to help them build financial health

---

### ARCHETYPE 5: THE OPTIMIZER
*"I've figured out the system — I use multiple apps strategically to maximize available liquidity"*

**Profile:**
- Heavy user who has learned the rules and games them
- Uses 2–7+ apps simultaneously
- Calculates effective APR and chooses strategically
- Highly sensitive to fee changes, policy changes, eligibility shifts
- Likely to post detailed Reddit reviews; most influential in community recommendations
- Often the person who found out about revocation of ACH authorization from a Reddit thread

**Behavioral evidence:**
- 53% use multiple apps in year 1 (CRL); power users run 5–8 simultaneously
- "I've tried almost everything" framing appears across many reviews
- Researches apps on Reddit before downloading
- Often triggered to switch by a policy change or trust violation (limit drop, fee increase)
- Most likely to file BBB/Trustpilot complaint when wronged (high investment in platform)

**Specific journey friction:**
- Multiple auto-debits from different apps can collide, triggering overdraft
- Apps detecting other apps and reducing limits accordingly (documented concern, CFPB)
- Eligibility requirements differ subtly — managing multiple sets of rules is cognitively taxing
- Fee calculation: "$8/month Tilt + $4 instant fee + $2.99 EarnIn tip + $1.99 FloatMe = $17/month for $300 total capacity"

**Representative verbatim quotes:**
- "It just went completely out of control, and I was having to live off the borrowing apps." — Smith (7–8 apps simultaneously)
- "I've been very impressed!! And take it from someone who has tried almost everything." — App Store ⭐⭐⭐⭐⭐
- "To be honest, I downloaded about 20 Cash Advance Apps, Tilt was legit! I RECOMMEND it EVERYONE!!" — Trustpilot
- "I decided I will be closing my account with Dave" — Reddit user (comparative, evaluative mindset)
- "I learned about Empower, now Tilt, a couple of weeks ago... I looked for loans but because of my bad credit, I wasn't qualified for any" — Hatchetface81 [note: even first-timers can be in Optimizer mindset if they researched extensively]
- From Reddit-aggregated EarnIn sentiment: "I've used this for 6 months now. I never pay fees, I just tip $2 when I can. Honestly the best alternative to payday loans." [Fee-optimization mindset]

**What Tilt does right for this archetype:**
- Competitive advance amount ($400 max, $174 returning average)
- Installment repayment allows stacking across multiple apps without full paycheck depletion
- No-tip policy reduces total cost vs. Dave/EarnIn
- Budgeting tools help track across multiple accounts

**What Tilt does wrong for this archetype:**
- $8/month subscription is the highest fixed cost; Optimizers evaluate this hard
- Opaque eligibility algorithm makes it impossible to predict or optimize limit
- No referral program to optimize social value
- No flexible disbursement to alternate accounts (MoneyLion's differentiator)
- Subscription-while-ineligible is a known trap; Optimizers document and share this widely

---

## APPENDIX: MARKET CONTEXT REFERENCE DATA

### Demographics
- Target market: Millennials and Gen Z (18–44), predominantly hourly/gig workers
- 80%+ of EWA users are hourly or gig workers
- 79% of Cash App users have FICO scores below 600
- 78% of cash advance app users are previous payday loan borrowers (DebtHammer)
- 33%+ of Americans have signed up for at least one cash advance app

### Financial baseline
- 65–67% of Americans live paycheck to paycheck
- 59% lack savings to cover a $1,000 emergency
- 77% of workers would face financial difficulty if paycheck delayed one week
- 37% of U.S. adults can't cover a $400 emergency (Federal Reserve)

### Usage patterns
- Average EWA transaction: $106
- Average annual funds accessed per user: $3,000
- Average transactions per user per year: 27
- 75% took new advance same day or day after repayment
- 38% of users = 86% of all advances (high-frequency segment)
- 53% borrowed from multiple apps in year 1

### Repayment struggles
- 31% struggled to repay as scheduled (DebtHammer)
- 17% skipped another bill to repay the advance
- 4% borrowed from a different app to repay the first

### Regulatory signals
- CFPB flip-flopped: 2024 proposal said EWA IS credit (109.5% illustrative APR); Dec 2025 opinion under Vought says NOT credit
- 6 federal court decisions in 2025 found EWA products ARE loans
- *Vickery v. Empower Finance Inc.* — Northern District of California, 2025
- FTC sued Dave (Nov 2024) for deceptive practices
- FTC settled with Brigit (Nov 2023, $18M) for deceptive marketing and cancellation difficulty
- CFPB sued MoneyLion for Military Lending Act violations
- Connecticut forced providers out with 36% APR cap, then built EWA framework (June 2025)
- 12+ states have enacted EWA-specific laws

### Tilt/Empower company snapshot
- Founded: 2016, San Francisco
- Founder: Warren Hogarth (ex-Sequoia Capital)
- Users: 3M+ active subscribers, 5M+ total customers
- Profitable since 2022
- Post-money valuation: ~$797M (August 2025)
- Total equity: ~$174.5M (Sequoia, Initialized Capital, Icon Ventures, Defy Partners)
- Rebranded Empower → Tilt: August 2025
- Products: Cash Advance ($10–$400), Thrive Line of Credit ($200–$1,000), Tilt Credit Cards (Aug 2025, WebBank), budgeting, AutoSave, credit monitoring
- Subscription: $8/month
- Avg first-time advance: ~$100 | Avg returning: ~$174 | Approval rate: ~75%
- Operations: US + Mexico

### Industry-wide App Store score trends (recent vs. lifetime)
| App | Lifetime | Recent | Trend |
|-----|---------|--------|-------|
| Tilt | 4.8 | 3.1 | ↓↓ |
| Dave | 4.8 | 3.4 | ↓↓ |
| Brigit | 4.8 | 3.8 | ↓ |
| Chime | 4.8 | 4.5 | ↓ (recovery) |
| Albert | — | 2.7 | ↓↓↓ |
| Cleo | 4.5 | 2.9 | ↓↓↓ |
| EarnIn | 4.8 | ~4.5 | stable |