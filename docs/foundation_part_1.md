# Stock Sense — Trading Intelligence Foundation
**Status:** STRUCTURAL FOUNDATION — modular, extensible, ready for enrichment  
**Purpose:** Canonical knowledge base for trading strategies, tactics, theories, practices, and beliefs. Designed for agent use and continuous enrichment from multiple external sources.  
**Last Updated:** 2026-10-25  
**Provenance Rule:** Every claim must carry a confidence label. Never treat this file as absolute truth. No edge is assumed without evidence.

## Confidence Labels
- **VERIFIED**: Directly proven by primary source, data, or reproducible evidence.
- **SUPPORTED**: Strong evidence or consensus from reputable sources; not independently proven here.
- **INFERRED**: Logically derived from other material; not directly observed.
- **UNVERIFIED**: Claimed or expected but unchecked.
- **CONFLICTING**: Evidence disagrees.
- **USER-SPECIFIC**: Preference, belief, or constraint supplied by operator.

## 1. Core Theories & Frameworks
*(Standard professional frameworks. Label and limitations required.)*

| Theory / Framework | Summary | Key Trading Implications | Limitations / Failure Modes | Confidence | Source(s) |
|--------------------|---------|---------------------------|-----------------------------|------------|-----------|
| Risk Management Primacy | Survival and position sizing dominate long-term results more than entry timing. | Size positions so that a sequence of losses does not impair capital. Fixed fractional or volatility-adjusted sizing. | Ignoring correlation or gap risk can still cause large drawdowns. | SUPPORTED | Standard risk literature |
| Regime Dependence | Markets alternate between trending, mean-reverting, and high-volatility states. Strategies have conditions. | Filter setups by regime (trend strength, volatility regime, liquidity). Do not force a strategy outside its regime. | Regime detection lags; false regime calls are common. | SUPPORTED | Trend-following / adaptive systems literature |
| Behavioral Biases | Participants systematically deviate from pure rationality (loss aversion, overconfidence, herding, narrative bias). | Watch for crowded narratives, extreme sentiment, and post-event overreactions. Use as contextual overlay, not primary signal. | Biases are not constant; markets can remain irrational longer than expected. | SUPPORTED | Behavioral finance consensus |
| Limited EMH | Prices incorporate public information with varying speed and completeness. Short-term inefficiencies can exist; persistent edge is rare and decays. | Prefer process and risk control over claims of consistent alpha. Treat any edge as temporary and requiring ongoing validation. | Easy to overfit past inefficiencies. | SUPPORTED | Market efficiency literature |
| Market Microstructure | Order flow, liquidity, spreads, and participant types affect short-term price formation. | Higher spreads, low volume, or thin books increase slippage and gap risk. Prefer liquid instruments for most strategies. | Microstructure effects are instrument- and time-specific. | SUPPORTED | Market microstructure basics |

## 2. Tactics & Playbook Entries
*(Maps to Strategy_Engine_Table.csv. Use template for every play.)*

### Play Type Template
- **Play ID / Name**:
- **Regime Conditions** (volatility, trend, liquidity, etc.):
- **Entry Zone / Criteria**:
- **Exit / Target**:
- **Invalidation / Stop**:
- **Risk / Reward Guideline**:
- **Position Sizing Rule**:
- **Required Data Inputs** (from tables):
- **Common Failure Modes**:
- **Confidence**:
- **Source**:

### Example Structural Plays (no claimed edge)
**Play: Trend Continuation (skeleton)**  
- Regime: Clear higher-timeframe trend, moderate volatility, adequate liquidity.  
- Entry: Pullback to moving average zone or break of minor structure with volume.  
- Exit: Measured move or trailing structure.  
- Invalidation: Close beyond structure or opposite MA.  
- R/R: Minimum 1.5:1 after costs.  
- Sizing: Fixed fractional or ATR-based.  
- Inputs: sma_20/sma_50/ema_20, volume, trend_summary (Technical_Analysis_Table).  
- Failure modes: Regime change, false break, liquidity gap.  
- Confidence: INFERRED (template only).  

*(Add concrete plays from external references as they are supplied.)*

### Options Strategy Plays (structured templates — no claimed edge)
All require liquid underlyings, defined risk preferred, IV rank context, and explicit invalidation. Confidence: INFERRED (templates only).

**Play: Cash-Secured Put**  
- Regime: Neutral to mildly bullish, adequate IV, liquid options.  
- Entry: Sell put at chosen delta/strike; reserve full cash.  
- Exit: Close at target premium capture, or accept assignment.  
- Invalidation: Underlying breaks below technical support or thesis invalidates.  
- R/R: Premium received vs. downside to strike (after costs).  
- Sizing: Cash reserved = strike × 100 × contracts.  
- Inputs: Options_Analysis_Table (strike, iv, delta, bid/ask), Technical_Analysis_Table for support.  
- Failure modes: Sharp gap down, IV expansion, assignment on further decline.  

**Play: Covered Call**  
- Regime: Neutral to mildly bullish, long stock held, adequate IV.  
- Entry: Sell call against long shares at chosen delta.  
- Exit: Close at premium target or let expire; accept assignment if called.  
- Invalidation: Underlying breaks support or thesis changes.  
- R/R: Premium + remaining upside to strike.  
- Sizing: Limited by shares owned.  
- Inputs: Options_Analysis_Table (strike, iv, delta), stock position.  
- Failure modes: Strong rally past strike, opportunity cost, gap up.  

**Play: Iron Condor**  
- Regime: Range-bound, elevated IV preferred, liquid chain.  
- Entry: Sell OTM put spread + sell OTM call spread.  
- Exit: Close at profit target or when wings threatened.  
- Invalidation: Price approaches short strike or breaks expected range.  
- R/R: Credit received vs. width of wings (defined).  
- Sizing: Max loss = wing width – credit.  
- Inputs: Options_Analysis_Table (strikes, iv, delta, bid/ask spreads).  
- Failure modes: Breakout, IV expansion, wide fills.  

**Play: Collar**  
- Regime: Long stock, desire for downside protection with reduced cost.  
- Entry: Long stock + buy protective put + sell call.  
- Exit: Unwind on thesis change or at expiration management.  
- Invalidation: Thesis invalidates or protection no longer needed.  
- R/R: Limited upside (call) and limited downside (put).  
- Sizing: Matches stock position.  
- Inputs: Options_Analysis_Table for both legs.  
- Failure modes: Cost of put exceeds call premium, opportunity cost on upside.  

**Play: Credit Spread (Bull Put / Bear Call)**  
- Regime: Directional bias with defined risk preferred over naked.  
