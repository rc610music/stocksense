# Stock Sense — Master Inventory & Reconciliation Record

**Last Reconciled:** 2026-11-02  
**Status:** Complete structural foundation present in both locations  
**Purpose:** Canonical record of all Stock Sense files and their locations.

## Locations

| Location | Path / URL | Role |
|----------|------------|------|
| Google Drive | TickerTrack App Dev folder (linked workspace `/workspace/artifacts/`) | Working copy / source of truth for enrichment |
| GitHub | https://github.com/rc610music/stocksense | Versioned public repository |

## File Inventory

### Root Documents
| File | Google Drive | GitHub | Notes |
|------|--------------|--------|-------|
| README.md | Yes | Yes | Master overview |
| trading_agent_system_prompt.md | Yes | Yes | Agent instructions + standardized output format |
| trading_intelligence_foundation.md | Yes (full single file) | Split into docs/ parts | Full version in Drive; split for upload in GitHub |

### Data Tables (`data/` in GitHub; root in Drive)
| File | Google Drive | GitHub | Notes |
|------|--------------|--------|-------|
| Strategy_Engine_Table.csv | Yes | Yes (`data/`) | Template rows for plays |
| Options_Analysis_Table.csv | Yes | Yes (`data/`) | Options metrics templates |
| Technical_Analysis_Table.csv | Yes | Yes (`data/`) | TA filter templates |
| Playbook_Metadata_Table.csv | Yes | Yes (`data/`) | Metadata templates |
| Sentiment_Data_Table.csv | Yes | Yes (`data/`) | Sentiment schema |
| News_Catalysts_Table.csv | Yes | Yes (`data/`) | Catalyst schema |
| Ticker_Request___Analysis_Tables.csv | Yes | Yes (`data/`) | Request schema |

### Foundation Parts (GitHub `docs/`)
| File | Google Drive | GitHub | Notes |
|------|--------------|--------|-------|
| docs/FOUNDATION_NOTE.md | — | Yes | Explains split |
| docs/foundation_part_1.md | Yes (as docs_foundation_part_1.md) | Yes | Core theories + early plays |
| docs/foundation_part_2.md | Yes (as docs_foundation_part_2.md) | Yes | Remaining plays + engine start |
| docs/foundation_part_3.md | Yes (as docs_foundation_part_3.md) | Yes | USER-SPECIFIC rules + output format |
| docs/foundation_part_4.md | Yes (as docs_foundation_part_4.md) | Yes | Beliefs, data layers, enrichment log |

## Reconciliation Notes
- All core documents and CSV tables exist in both locations.
- The full single-file foundation lives in Google Drive (`trading_intelligence_foundation.md`).
- GitHub holds the same content split into four parts under `docs/` for size/upload reasons.
- No claimed edge in any file. All content is provisional and requires human approval for capital allocation.
- USER-SPECIFIC risk rules, preferred underlyings, strategy prioritization, and exclusions are embedded in the foundation.

## Next Enrichment
- Supply additional references, outcome data, or refined parameters.
- Consolidate foundation into a single file in GitHub if desired.
- Add outcome tracking mechanism for reconciliation loop.

**End of Master Record**
