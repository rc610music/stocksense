# Stock Sense

Institutional-grade trading intelligence engine for defined-risk options and equity strategies.

## Overview
Stock Sense provides a structured, evidence-graded knowledge base, strategy playbooks, risk rules, and multi-layer market analysis framework. All content is provisional; no edge is claimed. Human approval required for capital allocation.

## Core Documents
- `docs/trading_intelligence_foundation.md` — Canonical knowledge base (theories, practices, USER-SPECIFIC rules, play templates, advanced forecasting engine)
- `docs/trading_agent_system_prompt.md` — Agent instructions and standardized output format

## Data Tables
CSV templates in `data/`:
- Strategy_Engine_Table.csv
- Options_Analysis_Table.csv
- Technical_Analysis_Table.csv
- Playbook_Metadata_Table.csv
- Sentiment_Data_Table.csv
- News_Catalysts_Table.csv
- Ticker_Request___Analysis_Tables.csv

## Key Rules (USER-SPECIFIC)
- Max risk per trade: 1.5–2.0% NAV
- Preferred DTE: 30–45
- IV Rank regime filters
- Defined-risk preferred; naked excluded unless covered
- Preferred underlyings: SPY, QQQ, IWM, AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA

## Status
Structural foundation complete. Ready for enrichment and agent integration.
