# Tilt Enriched Archetype Profiles
### Evidence-Mapped from UX Research | For Synthetic Agent Training

> **How to use this document:** Each profile is a complete behavioral and emotional specification for one user type. Quotes are verbatim from real users. Friction points are sourced. Contradictions are flagged explicitly — do not smooth them over; they are the most important training signal.

---

## ARCHETYPE 1: CRISIS
### *"Something went wrong."*

**Internal definition:** Reactive, emotional, urgent. Needs money fast. First-time or rare user.

---

### VERBATIM QUOTES

> *"I had like 50 bucks in my bank account. That was the first domino and everything else just kind of fell apart from there."*
— Runeda, EarnIn user (Nasdaq/NerdWallet interview)

> *"I looked for loans but because of my bad credit, I wasn't qualified for any and then out of nowhere, this app appeared to me and I enrolled, answered a few questions, gave my information and there it was.. Bad credit saving money."*
— Hatchetface81, Tilt App Store ⭐⭐⭐⭐⭐

> *"I'm writing this review to extend my eternal gratitude. I had managed to get into a bad patch of my life where I was nearly going to lose my job and my home... In my desperate search for answers, I stumbled upon this app. All I needed was about $400 to make the difference and break even. I prayed for this daily and I was blessed."*
— EarnIn App Store reviewer

> *"Fast money transfer! Emergency funds! It's like asking mom for money!"*
— Tilt Trustpilot

> *"Thank you [Tilt] for giving me a chance when nobody else would."*
— Kris M., tilt.com testimonial (March 2025)

---

### EMOTIONAL ARC

**Before opening the app — Panic + shame spiral**
The triggering event (car repair, rent due, utility shutoff, food for children) has already happened. The user has likely already exhausted their other options: checked their bank balance multiple times, considered asking family, maybe Googled "emergency loan bad credit." By the time they open the app store, they are in acute stress. Shame is present but secondary to urgency.

**During onboarding — Tense hope**
Every screen is experienced as a potential rejection or delay. The user is simultaneously desperate for approval and braced for disappointment. "What's the catch" anxiety is high. Any fee disclosure at this stage lands as a betrayal rather than a business term.

**At advance offer — Relief or collapse**
If the offer meets or approaches the need: overwhelming relief, physical release, intense brand loyalty formed in seconds. If the offer is $10 against a $300 emergency: the product has failed this user even though it technically worked. The emotional response is disproportionate to the dollar amount because the stakes were existential.

**After funds arrive — Gratitude + exhaustion**
The crisis is resolved. The emotional tone shifts to gratitude, sometimes expressed with religious language ("blessed," "prayed," "eternal gratitude"). The user is not yet thinking about repayment.

**At repayment — Variable**
If smooth: neutral, forgotten. If auto-debit misfires and overdraft occurs: the gratitude is instantly reversed into the most intense betrayal response in the entire customer lifecycle.

---

### SPECIFIC FRICTION POINTS

**1. The instant fee they didn't expect**
Crisis users need money NOW — standard 1–3 day delivery is functionally useless for a rent-due or car-broken situation. But they also didn't budget for the instant delivery fee ($1–$8 on top of the $8 subscription). They discover it mid-flow, already committed.
- *Evidence source:* Finder.com review aggregation; internal competitor table (Albert forces instant at $5.99 on $17 advance; Brigit forces instant at $2.99 on $20)

**2. The advertised maximum vs. first-time offer gap**
Marketing shows "$400" or "$500." First-time offer is frequently $10–$100. For a Crisis user whose emergency requires a specific dollar amount, this isn't a disappointment — it's a product failure.
- *"I am rating this app 2 stars for now due to I did have to pay 8 bucks for the first month just to get an advance of 10 dollars."* — April Workman, App Store ⭐⭐
- *Evidence:* Average Tilt first-time advance ~$100; Dave average $73; FTC consumer complaint on Dave: "I only was able to get 25.00. Not very helpful."

**3. State eligibility not disclosed before subscription charge**
Crisis users don't read terms carefully — they're in crisis. Discovering that cash advance isn't available in their state after being charged $8 is experienced as a scam.
- *"Empower allowed me to subscribe knowing that Cash Advance—the main feature promoted—was not available in [my state]. That was the only reason I signed up."* — BBB complaint

**4. Onboarding length during a real emergency**
Tilt: 12 screens signup + 6 CA enrollment. Dave: 20 screens. Albert: 24 screens. Crisis users report time pressure as its own source of anxiety. Each additional screen is a barrier.

---

### COMPETITOR RESPONSES THIS ARCHETYPE NOTICES

**EarnIn:** No subscription fee removes the $8-for-$10 shock entirely. First interaction is purely value delivery. Crisis users who've used EarnIn cite this as the reason they recommend it.
- *"Very trust worthy app! No hidden agendas, no hassle, it just works!"* — EarnIn reviewer

**Earnin's clean design + privacy explanation:** Specifically praised for explaining *why* payroll linking is needed. Crisis users are already suspicious; this explanation converts.

**Chime SpotMe:** Zero fees, instant coverage — but the $200 cap and ecosystem lock-in means it often doesn't cover the actual crisis amount.

**What Tilt has that competitors don't (for this archetype):**
The installment repayment option is a genuine structural advantage. Crisis users who've been burned by lump-sum payday loan repayments respond strongly to "you don't have to repay it all at once."
- *"the best part is you don't have to repay it all on the next paycheck like a payday loan.. they break up the payments up to 4 installments which is extremely helpful... payday loans that have to be paid back all at once put me back where I started."* — Hatchetface81, App Store

---

### CONTRADICTIONS & COMPLICATIONS

**⚠ CONTRADICTION 1: "First-time or rare user" assumption may be too narrow**
The research shows many Crisis users become Liquidity Stabilizers immediately after their first use — not because their situation improved, but because the first advance left their paycheck depleted, requiring another advance 3 days later. The archetype definition treats Crisis as a stable identity. It may be better understood as an *entry state* that most users pass through, not a permanent type.
- *"[After the internet bill], that setback meant Runeda had to borrow again just 3 days later for gas, and 4 days after that for a utility bill. Which meant her next paycheck was smaller, which meant she ended up borrowing again 3 more times over the next week."* — Runeda's cycle (Nasdaq)

**⚠ CONTRADICTION 2: The dignity driver is as strong as the urgency driver**
The internal definition emphasizes speed and urgency. But the evidence consistently shows that *privacy* and *dignity* are co-equal motivators — often the deciding factor between apps (and between apps and payday loans). A Crisis user who could get faster money from a payday loan may still choose Tilt specifically because it's private.
- *"When you go to the payday loan, you are kind of watching your backs. Who's seeing me walk into this building? But the cash advance, uh, apps, it's private. There's this huge social stigma against people who are poor. Everyone I know is in debt. But we have to pretend like we're not. And there's a lot of shame wrapped up in that."* — Lee, teacher

**⚠ CONTRADICTION 3: Crisis users don't experience themselves as borrowers**
The internal framing positions this archetype as someone who "needs money fast." But users actively resist the "borrowing" frame — they frame it as accessing earned money, or "borrowing from myself." This distinction matters for copy, UX language, and agent simulation. A Crisis user who hears "loan" language may disengage.
- *"No one likes having to borrow money from friends or family! Now I can just borrow from myself through Tilt!"* — Tilt Trustpilot

---

## ARCHETYPE 2: LIQUIDITY STABILIZER
### *"I need breathing room."*

**Internal definition:** Paycheck-to-paycheck, repeat user. Needs predictability.

---

### VERBATIM QUOTES

> *"Been using Empower/Tilt for about 3 years now. I definitely depend on my advances every month and they always seem to come at a time when I need them the most. My only complaint is the sudden drop in my cash advance amount like over a year ago. I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due."*
— paigecash, App Store ⭐⭐⭐⭐

> *"You don't have room to breathe, it's like you can't breathe. Every dollar is accounted for. It leaves no room for error."*
— Runeda, EarnIn user (Nasdaq/NerdWallet interview)

> *"I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either."*
— Tomika Wright

> *"It helps me out a lot but why does my amount keep decreasing. But overall it's great."*
— Tilt Trustpilot

> *"Been paying 8$ a month after that for 2 years, and now I owe late payments, empower tilt is the worst they have stolen a ton of money out of my account."*
— Joshua Tillery, Trustpilot ⭐

---

### EMOTIONAL ARC

**Baseline state — Low-grade chronic anxiety**
The Liquidity Stabilizer is not in crisis. They are in the condition *before* crisis — perpetually. Every dollar is allocated. Any unexpected variable (late paycheck, car issue, medical copay) creates a cascade. The advance isn't relief from a specific event; it's the structural buffer that makes the month survivable.

**When opening the app — Routine with vigilance**
Not panic. Not hope. Routine — but with a background watchfulness: *Will the amount be there? Will it be enough? Has anything changed?* The emotional register when opening the app is closer to checking a utility account than to a crisis intervention.

**When the advance is confirmed at expected amount — Exhale**
Brief, functional relief. Not euphoria. The crisis was prevented rather than resolved. This user doesn't write glowing 5-star reviews after their 20th advance — the experience has to fail before they'll write anything.

**When the limit drops unexpectedly — Betrayal + helplessness**
This is the moment that generates the most detailed, most damaging public reviews. The Liquidity Stabilizer has built their budget around their limit. A silent drop from $175 to $75 doesn't just disappoint — it breaks a system they depend on, with no warning and no explanation. The fact that customer service also cannot explain it transforms frustration into a deep sense of institutional betrayal.

**When auto-debit causes overdraft — Worst-case scenario**
The overdraft cascade is devastating specifically to this archetype because their margin is already zero. A $35 overdraft fee — let alone three — can be more damaging than the original advance amount. This user doesn't have a buffer to absorb it.

**Long-term — Exhaustion and resignation**
The Liquidity Stabilizer knows they're in the cycle. They may not know how to exit. The emotional register over months and years shifts from relief to resignation: *"This is just how it is."*

---

### SPECIFIC FRICTION POINTS

**1. Unexplained limit decreases after perfect repayment**
This is the defining friction for this archetype. They have the most to lose from limit drops and the least capacity to absorb them.
- *"I was getting $175 and then it suddenly dropped to $75 for no reason, and it stayed that way consistently for over a year and I have no idea why and customer service could not give any insight either. My income, bills and deposits have never changed and I've always paid my advances on time when they're due."* — paigecash, App Store
- *"after months of successful repayments, Empower dropped my advance limit from $200 to $75! I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!"* — Victor A, Trustpilot ⭐

**2. Auto-debit overdraft cascade**
The repayment fires before the paycheck deposits. The Liquidity Stabilizer has no buffer to absorb the resulting overdraft fee. Then a second overdraft fee. Then the advance limit drops because the account went negative.
- *"Empower autodebited my bank account. They got paid, but I got an overdraft fee... The overdraft had a domino effect on my bank account, resulting in additional overdrafts... I now have 3 overdraft fees of $35, and a negative bank balance of over $395!!"* — Victor A, Trustpilot ⭐

**3. Subscription charges during service failures**
Being charged $8/month while the advance is inaccessible (due to technical failure, rebrand issues, or account hold) is experienced as the app taking money from someone who has none to spare.
- *"they continued to take their sub fee of $8 every month for 6 months despite the account no longer being eligible for the service. After months of back and forth, calls and emails, they offered me half of what they took despite not offering the service I'm paying for. Which is, you know, illegal."* — Google Play ⭐
- *"Been paying 8$ a month after that for 2 years, and now I owe late payments."* — Joshua Tillery, Trustpilot ⭐

**4. Rebrand-induced payment failures**
For a user who has built repayment into their monthly routine, a rebrand that breaks payment processing is catastrophic.
- *"All of a sudden they switched to Tilt and updated the app and every single one of my payments have failed stating 'Unfortunately, your account is not eligible, please use another account'. I have attempted to make OVER 50 payments on the app in the past 3 months."* — BBB complaint

**5. The dependency recognition trap**
The Liquidity Stabilizer intellectually understands the cycle but feels structurally unable to exit it. Each repayment depletes the next paycheck, requiring the next advance.
- *"I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either."* — Tomika Wright
- 75% of EWA users took out a new advance on the same day or the day after repayment (CRL data)

---

### COMPETITOR RESPONSES THIS ARCHETYPE NOTICES

**Brigit's repayment extension:** The one-time option to delay repayment date is specifically designed for this archetype's core anxiety — that the timing will be off. Liquidity Stabilizers who've used Brigit cite this as a meaningful differentiator.
- Internal competitor analysis: *"Extensions Offered: Option to extend the payment due date after taking an advance"*

**Brigit's auto-advance feature:** Automatically sends cash when a low balance is detected. For a Liquidity Stabilizer, this is deeply attractive — it removes the cognitive load of monitoring.
- Internal analysis: *"Auto advances: Feature to send cash automatically when detected low account."*

**MoneyLion's immediate re-advance after repayment:** New CA available immediately after repayment — eliminates the wait between cycles. Liquidity Stabilizers notice this because the gap between repayment and next advance is a vulnerability window.
- Internal analysis: *"Availability of CA: New cash advance made available immediately after repayment."*

**Brigit's "future eligibility" indicator:** When an amount is locked, clicking it shows when eligibility might return. This is exactly what paigecash needed for 13 months and never got from Tilt.

---

### CONTRADICTIONS & COMPLICATIONS

**⚠ CONTRADICTION 1: "Needs predictability" — but Tilt's algorithm is structurally unpredictable**
The internal definition correctly identifies predictability as the core need. But the product's limit algorithm is opaque by design. There is no mechanism by which a Liquidity Stabilizer can predict, manage, or restore their limit. This is not a UX gap — it's a product architecture conflict with the archetype's defining need.

**⚠ CONTRADICTION 2: This archetype is aware of the cycle and often ashamed of it**
The internal definition focuses on the financial pattern. The evidence shows a strong emotional layer: these users know they're dependent, feel shame about it, and would exit if they could. They are not naively trapped — they are structurally trapped. This matters for agent simulation: a Liquidity Stabilizer is not a passive user; they are an active person who has tried and failed to change their situation.
- *"I got tired of my paychecks being short after taking the advance, but then I sometimes couldn't make it to the next payday either."* — Tomika Wright

**⚠ CONTRADICTION 3: Long-term loyal users generate the worst reviews when things go wrong**
The assumption might be that loyal users = advocates. The evidence shows the opposite pattern: Liquidity Stabilizers who have been using the app for 2–3 years write the most detailed, most damaging negative reviews when a limit drops or a payment fails. Their investment in the product makes the betrayal proportionally larger.
- paigecash: 4 stars for 3 years of use, but the review is primarily about the unexplained limit drop
- Victor A: The review reads like a case study because this user had tracked every interaction

**⚠ CONTRADICTION 4: 38% of users generate 86% of advances — but this segment is underserved by UX**
This archetype represents the majority of Tilt's revenue (by advance volume). Yet the UX delivers no tools for this archetype: no limit transparency, no repayment scheduling flexibility, no advance impact modeling. The highest-value users are served by the least tailored experience.

---

## ARCHETYPE 3: HYBRID
### *"I need liquidity now but want to build long term."*

**Internal definition:** Occasional CA user, improving behavior, thinking about credit.

---

### VERBATIM QUOTES

> *"I am rating this app 2 stars for now due to I did have to pay 8 bucks for the first month just to get an advance of 10 dollars, I'm a bit confused on that and pretty turned off about it due to the fact that I have used other apps like Dave and Albert and their fees are no where near that high, Dave's is somewhere around $1.99 or $2.99 a month and Albert I believe was free or $4.99 if you wanted to explore other features on the app."*
— April Workman, App Store ⭐⭐

> *"This was just the first time using, but applying and connecting to my bank was very fast and the advance was super fast! I love how they don't let you go overboard. From what I've seen so far, they are here to help you with advances within reason, help you to save money and eventually get a line of credit, and help you rebuild your credit at the same time."*
— App Store ⭐⭐⭐⭐⭐ (recent)

> *"A good payment history leads to an increase in your accessible funds. It monitors my spending and credit score as well. $8 a month is well worth the convenience."*
— WalletHub reviewer

> *"It just went completely out of control, and I was having to live off the borrowing apps."*
— Smith, Nasdaq/NerdWallet interview [cautionary self-awareness the Hybrid fears becoming]

> *"Be responsible and [Tilt] is here when you need them. Simple."*
— Dawn B., tilt.com testimonial (January 2025)

---

### EMOTIONAL ARC

**Before opening the app — Considered discomfort**
The Hybrid doesn't open the app in pure panic. There's a gap — a bill coming due, an expense that arrived at a bad time — and they've assessed their options. The advance is a considered choice, not a desperation move. But there's still discomfort: they'd prefer not to need it.

**During onboarding — Evaluative and comparison-aware**
The Hybrid has likely researched at least one or two alternatives. They're evaluating value while going through the flow. Fee disclosures are noticed and compared. The $8 subscription is run against competitors' fees in real time.

**At advance offer — Pragmatic acceptance or principled rejection**
If the amount works and the fee feels fair relative to their need: quiet acceptance. If the fee-to-advance ratio is wrong (paying $8 for $10): this archetype is more likely to abandon than to accept and complain. They have alternatives.

**During active use — Monitoring and self-awareness**
The Hybrid is watching themselves. They notice if they're using the app more than they intended. They're aware of the cycle risk (Smith's story is their cautionary tale) and actively manage against it. They check their credit score more than other archetypes.

**At repayment — Completion-focused**
Repaying on time matters to this archetype not just for access to the next advance, but because they understand it may affect their credit profile and limit growth. Repayment is an investment, not just a debt clearance.

**Long-term — Graduation aspiration**
The Hybrid wants to need this product less over time. "Eventually get a line of credit" is cited explicitly. They frame the advance as a transitional tool.

---

### SPECIFIC FRICTION POINTS

**1. The fee-to-advance ratio on first use**
The Hybrid is comparison-aware. They know what competitors charge. A $8 subscription against a $10 first advance fails this archetype's value calculus specifically — they will do the math.
- *"I did have to pay 8 bucks for the first month just to get an advance of 10 dollars... Dave's is somewhere around $1.99 or $2.99 a month."* — April Workman, App Store ⭐⭐

**2. No visible progress toward limit increases**
The Hybrid's long-term thinking means they want to see that good behavior is building toward something. No indicator of limit trajectory is a specific pain point for them — not just because it's opaque, but because it removes their sense of agency.
- Internal analysis recommendation: *"Future Eligibility Indicators: Some apps give users a sense of when they may next qualify or when their advance amount might increase."*

**3. App-stacking collision**
The Hybrid is more likely than any other archetype to use multiple apps simultaneously — and more likely to experience the repayment collision that results. They are also more aware that this behavior is risky.
- *"It just went completely out of control, and I was having to live off the borrowing apps."* — Smith [the Hybrid's fear, not yet their reality]
- CRL data: 53% borrowed from multiple apps in year 1; nearly 50% used multiple companies in same month

**4. No pause or reduce subscription option**
The Hybrid may go 2–3 months without needing an advance. In those months, the $8 subscription feels like dead spend. No documented "pause subscription" feature means they must choose between paying for nothing or canceling entirely (which risks losing their established limit and history).

**5. Confusing product architecture**
Tilt offers Cash Advance + Thrive Line of Credit + Tilt Credit Cards. The Hybrid, who is thinking about credit building, wants to understand the relationship between these products. There is no documented UX that explains this progression.

---

### COMPETITOR RESPONSES THIS ARCHETYPE NOTICES

**Brigit's explicit intent prompt at onboarding:** Asks users whether they're interested in cash advance or credit building — then routes accordingly. The Hybrid would appreciate this acknowledgment that they might be both.
- Internal analysis: *"User Intent Prompt: Asked user whether they were interested in cash advance or credit building."*

**Albert's "Smart Money" and investing features:** Albert positions itself as a full financial health product. The Hybrid's credit-awareness makes them receptive to this framing — even if Albert's execution is criticized.
- Internal analysis: *"Unique Differentiator: Allows for investing, 'Smart Money' feature"*

**MoneyLion's cross-sell at activation:** Surfaces credit building, savings, and other financial tools immediately after first advance. The Hybrid responds to this because it validates their "this is a stepping stone" mental model.
- Internal analysis: *"Cross Sell: Incentivizes checking account signup with higher CA limit (up to $1k)."*

**EarnIn's no-subscription trust signal:** For the Hybrid evaluating value, EarnIn's zero-subscription model is the most rational first choice. Tilt needs to convert Hybrids who've already considered EarnIn.

---

### CONTRADICTIONS & COMPLICATIONS

**⚠ CONTRADICTION 1: "Improving behavior" may be aspirational rather than behavioral**
The internal definition implies the Hybrid is actively improving their financial habits. The evidence suggests many users in this archetype *intend* to improve but are structurally constrained from doing so. The aspiration is real; the behavioral change is rare without an income increase or external intervention.
- Documented exit paths from the cycle: income increase, legal self-education (ACH revocation), deliberate behavior change. All three require external catalysts, not just intention.

**⚠ CONTRADICTION 2: The Hybrid is the archetype most likely to become a Liquidity Stabilizer**
The line between "occasional user thinking about credit" and "repeat user who depends on advances" is thinner than the archetype suggests. Smith's story — "it just went completely out of control" — reads like a Hybrid who became a Liquidity Stabilizer without intending to. The agent should model this transition risk.

**⚠ CONTRADICTION 3: "Thinking about credit" but often not engaging with credit features**
The Hybrid notices credit monitoring as a value signal, but there's limited evidence they actively use budgeting or credit tools. The engagement may be shallow — they like that the feature exists more than they use it.

---

## ARCHETYPE 4: CREDIT BUILDER
### *"I want to move forward but don't trust myself yet."*

**Internal definition:** Low-mid credit score, approval-anxious, long-term thinker.

---

### VERBATIM QUOTES

> *"This app will help you rebuild your credit!! I promise you!!"*
— App Store ⭐⭐⭐⭐⭐

> *"This was just the first time using, but applying and connecting to my bank was very fast and the advance was super fast! I love how they don't let you go overboard. From what I've seen so far, they are here to help you with advances within reason, help you to save money and eventually get a line of credit, and help you rebuild your credit at the same time."*
— App Store ⭐⭐⭐⭐⭐

> *"I learned about Empower, now Tilt, a couple of weeks ago and so far this app has helped me pay bills when I absolutely had no money left.. I looked for loans but because of my bad credit, I wasn't qualified for any... Because of Empower, I was able to pay a bill on time which saved my credit score from dropping even lower... thank you so much for taking a chance on me and trusting that I'll pay back the money that was loaned to me."*
— Hatchetface81, App Store ⭐⭐⭐⭐⭐

> *"They will NOT make you overdrawn, ever. So give it a try!! I have been very impressed!! And take it from someone who has tried almost everything. This is the place to get small advances, a reasonable line of credit and save money all at the same time!!"*
— App Store ⭐⭐⭐⭐⭐

> *"Once I found out about paying myself first, it was a game changer for me."*
— Tomika Wright (breakthrough moment, documented in Nasdaq interview)

---

### EMOTIONAL ARC

**Before opening the app — Approval anxiety + shame**
The Credit Builder has been rejected before. Banks said no. Credit cards said no. Maybe a prior cash advance app said no. They approach Tilt expecting rejection and bracing for it. The "no credit check" signal is not just a convenience feature — it is emotionally significant. It removes the mechanism by which they've been judged and found lacking.

**During onboarding — Hypervigilant**
Every data field is an opportunity for the app to discover a reason to reject them. They answer questions carefully, anxiously. The Plaid bank connection step is particularly loaded — giving a financial app access to your account history when that history is the source of shame requires real trust.

**At approval — Profound relief + disbelief**
Being approved when you expected rejection creates a disproportionately positive emotional response. "Thank you for taking a chance on me" is Credit Builder language — the advance is experienced as an act of trust, not just a transaction.

**During repayment — Investment mindset**
The Credit Builder repays carefully, on time, because they understand (or hope) that this behavior is building toward something. They are more likely to check whether their limit has increased after repayment than other archetypes.

**When progress is invisible — Demoralization**
If good repayment behavior doesn't produce a visible signal (limit increase, credit score improvement, milestone acknowledgment), the Credit Builder interprets the silence as evidence that their effort isn't working. This is different from the Liquidity Stabilizer's frustration — it's closer to demoralization.

**Long-term — Aspiration for graduation**
"Eventually get a line of credit" is the explicit goal. The Credit Builder is using the advance as a stepping stone and wants to see the path ahead.

---

### SPECIFIC FRICTION POINTS

**1. No visible progress indicators toward limit increases or credit improvement**
The Credit Builder's entire motivation is forward motion. Without a progress indicator — "your limit may increase after 2 more on-time repayments" or "your credit score improved X points" — good behavior feels unrewarded and the goal feels invisible.
- *"It finally went back up to $100 just recently which I'm thankful for."* — paigecash (3 years, no explanation of why or when)
- Brigit differentiator: *"Displays Amount Not Eligible: indicates future eligibility when clicked."*
- Internal analysis recommendation: *"Future Eligibility Indicators: Some apps give users a sense of when they may next qualify or when their advance amount might increase."*

**2. Approval anxiety during onboarding without advance amount preview**
The Credit Builder doesn't know if they'll be approved or for how much until after they've committed. Showing an estimated advance range before subscription enrollment would convert this archetype at higher rates and reduce demoralization at offer stage.
- *"No offer shown after connecting bank."* — Albert internal analysis (named as a negative)

**3. Low first advance relative to need**
The Credit Builder often has a specific, tangible goal (paying a bill that will protect their credit score). A $10 advance against a $200 bill doesn't solve the problem they came to solve.
- *"Because of Empower, I was able to pay a bill on time which saved my credit score from dropping even lower."* — Hatchetface81 [this worked; the evidence also shows many users don't get enough]

**4. AutoSave pulling from account unexpectedly**
The Credit Builder is attracted to savings features — but an unexpected AutoSave deduction from a thin account can trigger the overdraft they were trying to avoid. The feature that's supposed to help them can hurt them.
- App Store reviewer: *"A note on the savings acct part of it: If you don't have the funds, Empower will not draw the money from your account until you have enough funds."* [positive signal — but many users don't know this before it concerns them]

**5. Confusion between advance and credit products**
Tilt offers Cash Advance, Thrive Line of Credit, and a credit card. The Credit Builder wants to understand this progression and can't find it explained clearly in the UX.

---

### COMPETITOR RESPONSES THIS ARCHETYPE NOTICES

**Brigit's explicit credit building track:** Asks upfront whether the user wants cash advance or credit building. For the Credit Builder, being seen as someone with a credit goal — not just someone who needs emergency money — is meaningful.

**Albert's "Privacy Promise" and "Smart Money":** The Privacy Promise during onboarding directly addresses approval anxiety. Smart Money's savings mechanism aligns with the Credit Builder's self-improvement mindset — even if gating eligibility behind it is criticized.
- Internal analysis: *"Security: 'Privacy Promise' shared to build trust."*

**MoneyLion's credit-building tools and Boost feature:** The community Boost feature — where users can help each other increase their CA — resonates with Credit Builders' long-term orientation. It signals that progress is social and supported, not just algorithmic.

**EarnIn's employment verification approach:** For Credit Builders with stable employment, EarnIn's work-email verification creates a stronger sense of deserving access — "I earned this." For Credit Builders in gig work or non-traditional employment, it's exclusionary.

---

### CONTRADICTIONS & COMPLICATIONS

**⚠ CONTRADICTION 1: This archetype has the least direct evidence in the research dataset**
Most verbatim quotes that map here are from users who mention credit improvement as a secondary benefit, not as their primary stated motivation. The Credit Builder as a distinct motivational type is partially inferred. The research captures their *outcomes* (credit score improved, limit increased) more than their *intent* at the point of use. More targeted research on this archetype's onboarding decision-making is needed.

**⚠ CONTRADICTION 2: "Long-term thinker" in tension with the app's short-term product design**
The Credit Builder is oriented toward the future. Tilt's UX is oriented toward the present advance. There is no documented journey or UX path that takes a Credit Builder from first advance → credit milestone → product graduation. The credit monitoring feature exists, but it appears to sit alongside the advance product rather than being connected to it.

**⚠ CONTRADICTION 3: "Don't trust myself yet" may mean they resist features that require self-discipline**
The internal definition includes "don't trust myself yet" as a tension. The evidence suggests this self-awareness is protective — users like Hatchetface81 explicitly value that the app "doesn't let you go overboard." But it also means this archetype may resist AutoSave or savings features because engaging with them requires trusting that the deductions won't hurt them. Opt-in design matters more for this archetype than any other.

**⚠ CONTRADICTION 4: Approval anxiety may make them over-grateful in ways that mask product problems**
Hatchetface81's review is 5 stars and reads as a product success — but the underlying situation (bad credit, no other options, dependent on a $400 advance) is the same structural vulnerability as Runeda's. The Credit Builder's gratitude at being approved can suppress legitimate complaints, making them appear more satisfied than they are. For synthetic agent simulation, the agent should model the gap between expressed satisfaction and underlying financial precarity.

---

## ARCHETYPE 5: OPTIMIZER
### *"I want my money to work harder."*

**Internal definition:** Financially stable, strategic, rewards-focused.

---

### VERBATIM QUOTES

> *"To be honest, I downloaded about 20 Cash Advance Apps, Tilt was legit! I RECOMMEND it EVERYONE!!"*
— Tilt Trustpilot [systematic evaluation before commitment]

> *"I've been very impressed!! And take it from someone who has tried almost everything. This is the place to get small advances, a reasonable line of credit and save money all at the same time!!"*
— App Store ⭐⭐⭐⭐⭐

> *"A good payment history leads to an increase in your accessible funds. It monitors my spending and credit score as well. $8 a month is well worth the convenience."*
— WalletHub reviewer [explicit ROI calculation]

> *"I've used this for 6 months now. I never pay fees, I just tip $2 when I can. Honestly the best alternative to payday loans."*
— EarnIn App Store reviewer [fee-optimization mindset, competitor]

> *"It just went completely out of control, and I was having to live off the borrowing apps."*
— Smith, Nasdaq/NerdWallet interview [the Optimizer's nightmare scenario — system went wrong]

---

### EMOTIONAL ARC

**Before opening the app — Research mode**
The Optimizer does not download Tilt after a crisis. They find it through Reddit comparison threads, review aggregators, or fintech newsletters. They've already evaluated 3–5 alternatives and identified Tilt's specific value proposition within the competitive set.

**During onboarding — Efficient and impatient**
The Optimizer wants to get to the product as fast as possible. Every unnecessary screen is friction. They notice and evaluate every design choice: "Why is this required? What is this data used for?" They read the fee structure carefully before committing.

**During active use — Systematic monitoring**
They track their limit, their repayment history, their credit score change. They may have a spreadsheet. They know their effective monthly cost. They calculate whether the advance is cheaper than a credit card cash advance or an overdraft fee.

**When a competitor does something better — Active comparison**
The Optimizer will switch apps, add apps, or publicly document the difference. They are the most likely to post detailed Reddit reviews. They are also the most likely to discover workarounds (ACH revocation to stop subscription charges) and share them.

**When the system works — Quiet satisfaction**
No euphoria. The advance was expected, the fee was calculated, the outcome was as modeled. Positive reviews from this archetype tend to be systematic ("this is what it does well, this is what it doesn't").

**When the system fails — Forensic anger**
The Optimizer's negative reviews are the most detailed in the dataset. Victor A's Trustpilot review — tracking every support contact, naming the agent, documenting the overdraft cascade — is Optimizer behavior. They treat service failures as documentation opportunities.

---

### SPECIFIC FRICTION POINTS

**1. $8/month subscription with no pause option**
The Optimizer calculates: months with no advance = $8 for zero value. No documented pause-subscription feature means they either pay for nothing or risk losing their established profile.
- *"$8 a month is well worth the convenience."* — WalletHub [positive, but this user IS getting consistent value; the Optimizer is more sensitive to months when they don't]

**2. No referral program**
Every competitor has a referral program. Dave offers 20% boost on next advance. Brigit offers $15. Albert offers $50 for referrals. Tilt has none documented. The Optimizer — who has recommended Tilt to others ("RECOMMEND it EVERYONE!!") — gets no reward for this behavior.
- Internal analysis: *"Stronger Referral Incentives: Many competitors use referrals to drive growth."*

**3. Opaque limit algorithm with no optimization pathway**
The Optimizer wants to understand and influence the variables that determine their limit. Tilt's "250+ non-traditional financial health signals" model provides no visibility. There is no documented way to actively increase one's limit — only waiting and hoping.

**4. No flexible disbursement to alternate accounts**
MoneyLion allows editing disbursement destination (other debit cards). Tilt requires a linked bank account. The Optimizer who runs multiple financial accounts wants control over where funds land.
- Internal analysis: *"Flexible Destination: Allows editing destination (e.g., other cards) for CA disbursement."* [MoneyLion positive]

**5. Multi-app collision risk**
The Optimizer using 3–5 apps simultaneously faces timing conflicts between auto-debits. They understand the risk but may not have tools to manage it.
- CRL data: 53% use multiple apps in year 1; nearly 50% used multiple companies in same month
- *"It just went completely out of control, and I was having to live off the borrowing apps."* — Smith [Optimizer who lost control of the system]

---

### COMPETITOR RESPONSES THIS ARCHETYPE NOTICES

**EarnIn's no-subscription model:** The Optimizer's ROI calculation is most favorable to EarnIn — $0 fixed cost, tip-optional, up to $750/period. For an Optimizer with stable employment (required by EarnIn), this is the rational first choice.
- *"I've used this for 6 months now. I never pay fees, I just tip $2 when I can. Honestly the best alternative to payday loans."* — EarnIn reviewer

**Dave's 20% referral boost:** Directly rewards the Optimizer's natural behavior (recommending apps to their network). Tilt offers nothing equivalent.
- Internal analysis: *"Referral Program: 20% boost on next advance for referring a friend."* [Dave positive]

**MoneyLion's community Boost feature:** Users helping each other increase CA limits — a social optimization mechanic. The Optimizer finds this compelling even if it requires additional engagement.
- Internal analysis: *"Boost Feature: Allows helping others increase their CA."*

**Brigit's repayment extension:** The Optimizer values system flexibility. A one-time extension option is a risk management tool they want in their toolkit even if they rarely use it.

**Earnin's social proof framing:** "3.8 million users" — the Optimizer responds to scale as a trust and validation signal.

---

### CONTRADICTIONS & COMPLICATIONS

**⚠ CONTRADICTION 1: "Financially stable" does not match the evidence profile**
This is the most significant definitional problem in the archetype set. The research does not surface users who are genuinely financially stable using cash advances strategically. Every user who exhibits Optimizer *behaviors* (app comparison, fee calculation, system-building) does so from a position of financial constraint — not stability.

Smith ("7–8 apps simultaneously") is the clearest Optimizer behavior in the dataset — and his story is one of financial collapse, not optimization from a position of strength. The Optimizer's tools (multi-app stacking, fee comparison, Reddit research) are used by users who are desperate to wring more capacity from a constrained system — not by users who are comfortable and strategically managing wealth.

**Recommendation:** Reframe "financially stable" as "financially sophisticated" or "system-aware." The Optimizer's defining characteristic is their approach (analytical, strategic, comparative), not their financial baseline.

**⚠ CONTRADICTION 2: "Rewards-focused" may not be the right core tension**
No evidence found of cash advance users using these products for rewards in the traditional sense (points, cashback, miles). The Optimizer's "rewards" are: higher advance limits, lower fees, faster access, referral bonuses. These are not rewards — they are optimization of a cost-and-access system. The frame may need adjustment.

**⚠ CONTRADICTION 3: The Optimizer is the archetype most likely to document and escalate**
Victor A's 8–10 support contacts, named agents, and detailed overdraft timeline; the BBB complainant who tracked 50+ payment attempts — these are Optimizer behaviors. But the assumption might be that Optimizers are satisfied, strategic users. The evidence shows Optimizers become the most dangerous detractors when the product fails them, because they document everything.

**⚠ CONTRADICTION 4: This archetype may not exist at meaningful scale in Tilt's current user base**
The Optimizer archetype assumes a user with enough financial stability to be "strategic" rather than reactive. Given that 37% of U.S. adults can't cover a $400 emergency, 78% of cash advance users are former payday loan users, and 79% have sub-600 FICO scores — the truly financially stable Optimizer may be a small segment. This archetype may be better understood as an *aspiration state* that Liquidity Stabilizers and Hybrids reach toward, rather than a distinct, stable user type.

---

## CROSS-ARCHETYPE FINDINGS

### Patterns that appear across all five archetypes

**1. The "not a loan" reframe is universal**
Every archetype resists the word "loan." They use: "bridging," "borrowing from myself," "accessing what I earned," "emergency funds." UX language that uses "loan," "borrow," or "debt" creates friction regardless of archetype.

**2. The privacy/dignity driver is underweighted across all internal definitions**
All five archetypes are motivated in part by avoiding the social exposure of traditional borrowing. This is not unique to the Crisis user. The Liquidity Stabilizer doesn't want their family to know they depend on advances every month. The Credit Builder doesn't want to be judged for their credit score. The Optimizer doesn't want to appear financially unsophisticated. Privacy-as-dignity is a through-line, not an archetype-specific trait.

**3. Support quality determines whether any archetype stays or leaves**
Positive first experiences (fast funds, no surprises) generate loyalty across all archetypes. But the support experience at the first failure point is the moment that determines long-term retention. A chatbot wall at a financial-harm moment converts advocates into detractors regardless of archetype.

**4. The subscription-while-denied pattern is universally destructive**
No archetype accepts being charged for a service they cannot access. This is not a price sensitivity issue — it's a fairness violation that triggers disproportionate anger and public complaint behavior.

**5. All archetypes want to need this product less**
Even the Liquidity Stabilizer, who structurally depends on advances, expresses aspiration toward financial independence. The product that helps users graduate — or at least progress — earns disproportionate loyalty. The product that simply extracts fees without visible progress loses users the moment an alternative appears.

---

## ARCHETYPE TRANSITION MAP

The evidence suggests archetypes are not stable. Users move between them — often in a direction the product doesn't intend.

```
CRISIS ──────────────────────────────────►  LIQUIDITY STABILIZER
         (first advance depletes paycheck;      (cycle established
          next advance needed within days)       within 30-90 days)

CREDIT BUILDER ──────────────────────────►  HYBRID
               (limit increases, credit          (now occasionally 
                score improves slightly)          using strategically)

HYBRID ──────────────────────────────────►  LIQUIDITY STABILIZER
       (income doesn't improve;                  (graduated from
        advance becomes structural)              occasional to routine)

OPTIMIZER ───────────────────────────────►  LIQUIDITY STABILIZER
           (system gets out of control;          (Smith: "7-8 apps, 
            stacking creates dependency)          out of control")

LIQUIDITY STABILIZER ────────────────────►  EXIT
                      (income increase,          (rare; requires
                       credit literacy,           external catalyst)
                       deliberate change)
```

**The critical unmodeled transition:** The most common path is Crisis → Liquidity Stabilizer, not Crisis → one-time user → exit. Product and agent design should account for this drift as a default, not an exception.