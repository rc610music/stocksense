- Entry: Sell nearer strike, buy further OTM strike.  
- Exit: Close at premium target or manage if challenged.  
- Invalidation: Price breaches short strike or technical level.  
- R/R: Credit vs. spread width.  
- Sizing: Max loss = width – credit.  
- Inputs: Options_Analysis_Table (strikes, iv, delta, greeks, spreads).  
- Failure modes: Directional move against, IV rise, poor fills.  

**Play: Debit Spread**  
- Regime: Directional conviction, limited capital or defined risk desired.  
- Entry: Buy nearer strike, sell further strike.  
- Exit: Close at target or time/IV decay threshold.  
- Invalidation: Price fails to move toward target or thesis breaks.  
- R/R: Max profit (width – debit) vs. debit paid.  
- Sizing: Debit paid = max risk.  
- Inputs: Options_Analysis_Table.  
- Failure modes: Slow move, IV crush, time decay.  

**Play: Wheel (CSP → Assignment → Covered Call)**  
- Regime: Systematic income + potential entry on names willing to own.  
- Entry: Start with cash-secured put; if assigned, sell covered calls.  
- Exit: Cycle continues until position closed or criteria no longer met.  
- Invalidation: Fundamental or technical thesis on the underlying breaks.  
- R/R: Cumulative premium vs. capital at risk.  
- Sizing: Cash and share constraints as above.  
- Inputs: Both CSP and CC fields.  
- Failure modes: Prolonged decline after assignment, opportunity cost.  

**Play: LEAP (Long-term Call or Put)**  
- Regime: Longer-term directional thesis, lower theta relative to short-dated.  
- Entry: Buy deep or moderate ITM/ATM LEAP.  
- Exit: Scale or close on target or thesis change; roll if needed.  
- Invalidation: Thesis breaks or time/IV erodes value excessively.  
- R/R: Leverage vs. premium at risk.  
- Sizing: Premium paid = max risk.  
- Inputs: Options_Analysis_Table (longer expiration, delta, iv).  
- Failure modes: Wrong direction, IV crush, capital tied up.  

**Play: Swing (Equity or Options Overlay)**  
- Regime: Multi-day to multi-week directional move, clear structure.  
- Entry: Technical or catalyst-driven zone.  
- Exit: Target or trailing invalidation.  
- Invalidation: Structure break.  
- R/R: Minimum defined after costs.  
- Sizing: Fixed fractional.  
- Inputs: Technical_Analysis_Table + optional Options_Analysis_Table overlay.  
- Failure modes: Regime shift, gap risk, overholding.  

OTM selection, high-IV filters, and favorable greeks (delta for direction, theta for sellers, vega awareness) are overlays on the above, not standalone plays. All require liquidity (tight spreads) and explicit human approval for capital allocation.

### Additional Requested Templates (no claimed edge)
Confidence: INFERRED (templates only). Apply USER-SPECIFIC rules above.

**Play: Calendar Spread**  
- Regime: Low to normal IV (IV Rank < 30 preferred), term structure favoring near-term decay, neutral to mild directional bias.  
- Entry: Sell nearer-term option (30–45 DTE), buy longer-term option (60–90 DTE) at the same or nearby strike.  
- Exit: Close at profit target, when short leg decays sufficiently, or if thesis changes.  
- Invalidation: Price moves significantly away from strike or IV term structure inverts unfavorably.  
- R/R: Net debit vs. potential profit from differential decay; defined risk.  
- Sizing: Debit paid within 1.5–2% NAV limit.  
- Inputs: Options_Analysis_Table (both expirations, iv, delta, theta, bid/ask).  
- Failure modes: Large directional move, IV crush on long leg, poor fills on multi-leg.  

**Play: Long Butterfly**  
- Regime: Expected low volatility / range-bound, pin potential near expiration or heavy open interest/POC levels, adequate liquidity.  
- Entry: Buy lower strike, sell 2× middle strike, buy higher strike (typically equidistant); preferred 30–45 DTE. Target 0.30–0.50 risk-to-reward ratios.  
- Exit: Close at profit target or before significant gamma risk near expiration.  
- Invalidation: Price moves outside wings or volatility expands sharply.  
- R/R: Max profit near body vs. net debit; defined risk.  
- Sizing: Net debit within risk limit.  
- Inputs: Options_Analysis_Table (three strikes, iv, greeks, spreads).  
- Failure modes: Price fails to pin, wide spreads, early exit needed on move.  

**Play: Earnings IV-Crush (Post-Earnings)**  
- Regime: Post-earnings only; elevated IV that is expected to contract; liquid chain. Avoid pre-earnings long premium.  
- Entry: After earnings release and initial reaction; sell premium (credit spreads, iron condors, or short premium defined-risk) if IV remains elevated and range is plausible. Enter wide, defined-risk credit spreads or iron condors expiring immediately after the announcement ONLY if implied move is priced significantly higher than the 8-quarter average historical move.  
- Exit: Close on IV crush target or premium capture (align with 50% / 80% rules). Exit within 30–60 minutes of market open post-announcement to capture volatility collapse.  
- Invalidation: Unexpected continuation move or further IV expansion.  
- R/R: Credit received vs. defined wing risk.  
- Sizing: Within 1.5–2% NAV and underlying allocation limits.  
- Inputs: Options_Analysis_Table (post-event iv, delta, bid/ask), News_Catalysts_Table for earnings confirmation.  
- Failure modes: Earnings surprise magnitude exceeds expected move, continued directional follow-through, poor liquidity.  

These templates inherit all USER-SPECIFIC filters (delta, DTE, IV rank, underlyings, exclusions).
