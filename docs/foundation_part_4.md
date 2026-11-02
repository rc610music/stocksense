## 4. Beliefs, Heuristics & Known Biases
| Belief / Heuristic | Rationale | Counter-Evidence or Risk | Confidence | Source |
|--------------------|-----------|---------------------------|------------|--------|
| Process over prediction | Consistent risk control and process compound better than accurate forecasts. | Strong trends can reward pure prediction for periods. | SUPPORTED | Risk management consensus |
| Edge decays | Any observed short-term inefficiency tends to diminish once widely known. | Some structural edges persist longer in less efficient markets. | SUPPORTED | Market efficiency literature |
| Liquidity matters | Thin markets amplify slippage and gap risk. | Highly liquid markets can still gap on news. | SUPPORTED | Microstructure basics |

## 5. Data Layers & Catalyst Taxonomy
*(Maps to existing tables.)*

### Catalyst Categories (News_Catalysts_Table / Sentiment_Data_Table)
- Earnings & guidance: High short-term volatility; typical decay 1–5 sessions.
- Macro / rates / policy: Broader regime impact; slower decay.
- Sector / industry news: Relative strength shifts.
- Liquidity / flow events: Can create temporary dislocations.
- Reliability note: Most catalysts are already partially priced; surprise magnitude matters more than the event itself. Label all as contextual overlays.

### Technical & Options Overlays
- Technical_Analysis_Table fields (rsi, macd, sma_20, sma_50, ema_20, volume, trend_summary): Use as regime and confirmation filters, not standalone signals. No pattern is assumed to have reliable edge without evidence.
- Options_Analysis_Table (iv, delta, theta, gamma, bid/ask, strike): IV rank and expected move for context; spreads for liquidity; greeks for risk definition. Prefer defined-risk structures unless explicitly authorized.
- Explicit rule: Technical patterns and options metrics are inputs, not guarantees.

## 6. Integration with Existing Tables
| Table | Purpose | How Intelligence Uses It |
|-------|---------|---------------------------|
| Strategy_Engine_Table.csv | Core play definitions (play_type, entry_zone, exit_target, support/resistance, risk_reward_ratio, final_recommendation) | Populate from §2 templates |
| Playbook_Metadata_Table.csv | Metadata, summaries, PDF links | Link sources and notes |
| Technical_Analysis_Table.csv | TA signals (rsi, macd, SMAs/EMAs, volume, trend_summary) | Regime and confirmation filters |
| Options_Analysis_Table.csv | Options metrics (strike, type, bid/ask, iv, delta, theta, gamma, spread_suggestion) | Risk definition and liquidity overlay |
| Sentiment_Data_Table.csv | Sentiment inputs | Contextual weighting only |
| News_Catalysts_Table.csv | News events | Timing and impact context |
| Ticker_Request___Analysis_Tables.csv | Per-ticker requests | Input contract for analysis |

## 7. Agent Usage Instructions
When using this intelligence:
1. Grade every claim (use confidence labels). Never present INFERRED or UNVERIFIED as fact.
2. Separate observation from inference.
3. Require explicit risk parameters, position-size logic, and invalidation before any recommendation.
4. Flag insufficient data, high-uncertainty setups, or regime mismatch.
5. Prefer minimal, reversible actions and liquid instruments.
6. Reconcile against realized outcomes periodically and demote or update failing elements.
7. Never invent edge or certainty. Human approval required for consequential actions.
8. Map recommendations to the corresponding table columns so outputs remain structured.

## 8. Enrichment Log
| Date | Source | Sections Updated | Notes |
|------|--------|------------------|-------|
| 2026-10-25 | Initial skeleton | All | Modular foundation created |
| 2026-10-25 | Standard professional frameworks | §§1,3,4,5,7 | Added core theories, practices, data-layer rules, and agent instructions. All labeled. No claimed proprietary edge. Ready for external enrichment. |
| 2026-10-25 | Starter CSV rows + system prompt | Tables + new file | Added TEMPLATE rows to Strategy, Technical, Options, and Playbook CSVs. Created trading_agent_system_prompt.md. |
| 2026-10-25 | Options strategy set | §2 | Added structured templates for CSP, Covered Call, Iron Condor, Collar, Credit/Debit Spreads, Wheel, LEAP, Swing. No edge claimed. |
| 2026-10-25 | USER-SPECIFIC parameters + requested templates | §3 + §2 | Integrated operator risk rules, delta/DTE/IV filters, preferred underlyings, prioritization, and exclusions. Added Calendar, Long Butterfly, and Earnings IV-Crush templates. |
| 2026-10-25 | Advanced Market Intelligence & Forecasting Engine | §9 | Added multi-layer regime/macro, structural/technical, expanded trade design rules, and standardized output format. All contextual; no edge claimed. |

---

**Next Actions for Operator:**
- Supply specific strategies, books, research, or user-defined rules to expand §1–§2 and §4.
- Define risk tolerance, preferred instruments, timeframes, and forbidden strategies (USER-SPECIFIC).
- Populate CSV tables with concrete play data once rules are agreed.
- Add outcome tracking mechanism for reconciliation loop.
