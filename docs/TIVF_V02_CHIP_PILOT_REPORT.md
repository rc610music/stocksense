# TIVF v0.2 — CHIP pilot research and validation (2026-11-16)

Status: research pilot, NOT a deployed live-data service or investment recommendation.

## Source evidence
- CoinGecko https://www.coingecko.com/en/coins/usd-ai: indicative CHIP price ~$0.02758, 2B circulating, 10B total/max, ~$55.16M market cap, ~$275.8M FDV; provider-reported values fluctuate.
- CoinMarketCap https://coinmarketcap.com/currencies/usd-ai/: approximately $0.0278, 2B circulating, 10B max. Source comparison broadly corroborates the supply figure, not on-chain proof.
- DefiLlama https://defillama.com/protocol/usd-ai: as of 2026-11-16 TVL ~$157.27M, active loans ~$305.4M, 30-day fees ~$2.67M, protocol revenue ~$267k. Different metrics must not be added or conflated with CHIP tokenholder revenue.
- Official USD.AI https://usd.ai/blog/usdai-foundation-chip: CHIP governance, staking/backstop, no entitlement to protocol revenue.
- Official USD.AI https://usd.ai/blog/chip-governance-is-live: governance live as of 2026-10-19.
- Official portal https://app.usd.ai/chip: no equity/ownership/claim on protocol assets; stake/backstop risk.

## Calculated snapshot
Using $0.0276, 2B circulating, 10B maximum: market cap $55.2M, FDV $276M, circulating fraction 20%, supply overhang 400% of circulating. Overhang is NOT a forecast of selling pressure. Do not assume all 8B noncirculating tokens unlock soon.

## Preliminary verdict
Verified via multiple aggregators: reported circulating and max supply, broad price range. Officially documented: governance and backstop functions; no automatic claim on revenue. Protocol activity exists per DefiLlama. Not yet verified: chain-level cross-chain reconciliation, token-holder beneficial ownership, complete vesting calendar, effective circulating float, staking reward economics, smart-contract permissions, verified exchange order-book streaming. Withhold numeric quality score and investment rating until these are reconciled.

## Test evidence
Deterministic research/tivf.py and research/test_tivf.py: six local unittest cases passed on 2026-11-16 (supply math, future scenario, undefined max, invalid values, freshness, clock conflict). This is NOT live feed integration testing. Run: python -m unittest discover -s research -p 'test_*.py' -v.

## Next engineering gates
1. Locate actual StockSense app source (this repo is research docs/templates) before UI integration.
2. Implement provider adapters with event timestamps, data lineage, fallback, rate limits, and conflict states.
3. Reconcile CHIP contracts and vesting/unlock events against primary sources; compare XRP/ADA and an unlock-heavy token.
4. Test stream latency, outages, ticker collisions, reorgs and stale data on a preview environment.
5. Only then consider skill packaging, alerts and out-of-sample alpha evaluation.
