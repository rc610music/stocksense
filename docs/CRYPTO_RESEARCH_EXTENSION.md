# StockSense Cryptocurrency Research Extension — implementation specification
Date: 2026-11-13
Status: Specification only; live application not modified.

## Goal
Extend the EXISTING StockSense application and its Scout research workflows to support cryptocurrencies alongside stocks, ETFs and options. Do not build a parallel app. Preserve existing equity/ETF/options workflows and avoid Supabase.

## Initial user watchlist
CHIP (USD.AI), XRP, XLM, ADA, XTZ, DOGE, SHIB. These are user-identified holdings; quantities and cost basis must be verified before portfolio calculations. CHIP is USD.AI's governance/utility token (verify token identity by provider ID and contract address).

## Requirements
1. Asset type selector: All / Stocks / ETFs / Crypto / Options; global lookup resolves asset class and aliases, with disambiguation for reused tickers. Search by name, ticker, provider ID, and where relevant chain + contract.
2. Quote adapters with source, observed_at timestamp, currency, staleness, and explicit errors. Prefer provider IDs over ticker-only lookup. Never fabricate quotes or silently reuse stale quotes.
3. Crypto research detail: spot price, 1h/24h/7d/30d/1y performance, market cap, FDV, circulating/max supply, 24h volume, liquidity, volatility, drawdown, exchange availability, and verifiable news/catalysts. Gracefully mark missing fields.
4. Token fundamentals: chain, token standard, utility, tokenomics, issuance/unlocks, governance, staking and smart-contract risks, regulatory and counterparty risks, official links. Separate sourced facts from inference.
5. Portfolio: manual units, cost basis, fees and transactions, mark-to-market, P/L, weights, category exposure, alerts; never infer units or purchase price from a cropped screenshot. No auto-trading.
6. Scout AI research: thesis, bullish/bearish scenarios, time horizons, risks, confidence, cited evidence, source freshness, and explicit uncertainty. Do not confuse equity dividend yields with staking APY or protocol incentives.
7. Charts: OHLCV where available, technical indicators with timeframe and data coverage; mark 24/7 crypto markets and UTC boundaries.
8. Security: keep provider credentials server-side, use caching and rate-limit handling, test bad tickers and unsupported tokens; no wallet private keys required.
9. Mobile responsive UI including Galaxy Z Fold inner/outer viewport; preserve existing StockSense styling preferences (avoid square block-style feature title fonts).

## Acceptance tests
- All seven assets resolve to correct distinct tokens, especially CHIP/USD.AI.
- Query for XRP returns a sourced, timestamped USD quote and clear unavailable state on provider failure.
- Ticker collisions present a choice instead of choosing incorrectly.
- Holdings and cost basis persist; P/L computes accurately with fees; screenshots do not trigger invented balances.
- Crypto search and research work on mobile; existing stock, ETF and options searches still pass.
- No Supabase dependency or new parallel application.
- Isolated preview verified before production changes.

## Implementation dependency
The rc610music/stocksense GitHub repository currently contains research docs and CSV templates, not the live app source. Locate the actual StockSense application source/deployment, then implement there. This file is NOT evidence of deployed functionality.


## Market data freshness and evidence contract (v0.2, 2026-11-15)
Targets below are design SLOs contingent on provider availability, entitlements and rate limits, NOT claims of currently deployed feeds.
- Quotes/trades: target 5–30s age for liquid pairs; order-book depth: 5–15s; on-chain transfer alerts: 1–5m after indexing; supply/unlock changes: event-triggered with daily reconciliation; protocol metrics: hourly or best supported cadence; news/security/governance: monitored on available feeds. Each asset/provider can have a different cadence.
- Every observation must contain asset_id, chain_id/contract (if relevant), provider, source_url or provider record, exchange/venue, quote_currency, value, unit, event_time, provider_time, fetched_at, observed_at, age_seconds, coverage, and quality_state (live/delayed/cached/stale/missing/conflicted). Keep raw payload reference and normalization version for auditability.
- Quote timestamp cannot be replaced by fetch timestamp. Never label a delayed REST snapshot 'real time'. Exchange timestamps and clock drift must be normalized to UTC. Avoid comparing unaligned quotes.
- Use websocket streaming where supported, REST polling with bounded backoff otherwise; cross-check prices with a second independent venue/source. Reject outliers with documented rules and retain disagreements for review. Detect zero/negative/NaN prices, crossed books, missing bids/asks, thin liquidity, and wash-volume concerns.
- If primary feed is stale, fall back to another provider and label the switch. If all feeds fail, show last verified quote with timestamp and STALE label or no quote, never a synthetic live number.
- Token supply reconciliation: compare verified contract state/chain indexer with issuer vesting schedules and independent aggregators; distinguish circulating, unlocked, treasury, bridged, burned, and economically liquid supply. Store snapshot block number, chain finality, and any assumptions. Do not double-count bridged/wrapped supply.
- Alert rules require materiality thresholds, deduplication, evidence links, and rate limits; distinguish transfer to exchange from a confirmed sale, and announced unlock from circulating supply increase.

## Competitive edge: measurable research, not guaranteed alpha
- Define hypotheses in advance (e.g., verified unlock plus deteriorating order-book depth predicts elevated downside risk) and benchmark against simple price momentum and buy-and-hold, with predeclared horizons and outcomes.
- Run event-time backtests with point-in-time datasets, fees, spread, slippage, liquidity constraints, survivorship bias checks, token migrations, and delistings. Prevent look-ahead and data leakage.
- Use chronological train/validation/test splits and walk-forward out-of-sample testing. Report hit rate, precision/recall, calibration, drawdown, risk-adjusted return and sample size with uncertainty intervals; avoid cherry-picked examples.
- Paper-trade and monitor drift before considering any execution workflow. No autonomous trading, no promise of outperforming the market.
- Distinguish a verified finding from a hypothesis, a model estimate, and an actionable recommendation. Each report must state what would invalidate the thesis.

## Engineering verification gates
1. Simulated delayed feed: stale state is visible and no real-time claim survives.
2. Conflicting venues: provenance and conflict warning preserved; no silent averaging.
3. Reorg/bridged supply: chain finality and double-count safeguards.
4. Unsupported or duplicated ticker: no forced token match.
5. Backtest leakage: enforce point-in-time availability and fees/slippage.
6. Provider outage/rate limit: bounded retries and graceful degradation.
7. Regression: equity, ETF, options and crypto lookups still work.
8. Only label the system 'live verified' after actual deployed endpoint and feed tests; docs/tests alone are not live integration.
