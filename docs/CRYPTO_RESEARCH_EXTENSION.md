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
