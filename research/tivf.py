"""TIVF v0.2: deterministic tokenomics arithmetic and freshness validation. No live-feed claims."""
from decimal import Decimal, InvalidOperation
from datetime import datetime, timezone

def number(value):
    try: n=Decimal(str(value))
    except (InvalidOperation,ValueError): raise ValueError("invalid numeric input")
    if not n.is_finite() or n<0: raise ValueError("input must be finite and nonnegative")
    return n

def metrics(price,circulating,total=None,maximum=None,future_circulating=None):
    p,c=number(price),number(circulating)
    if c==0: raise ValueError("circulating supply must be positive")
    t=number(total) if total is not None else None
    m=number(maximum) if maximum is not None else None
    if t is not None and t<c: raise ValueError("total below circulating")
    if m is not None and m<c: raise ValueError("maximum below circulating")
    if t is not None and m is not None and t>m: raise ValueError("total exceeds maximum")
    f=number(future_circulating) if future_circulating is not None else None
    if f is not None and f<c: raise ValueError("future below current")
    return {"market_cap":str(p*c),"fdv":str(p*m) if m is not None else None,"circulating_pct_max":str(c/m*100) if m is not None and m>0 else None,"supply_overhang_pct":str((m-c)/c*100) if m is not None else None,"future_supply_growth_pct":str((f-c)/c*100) if f is not None else None,"constant_cap_price":str(p*c/f) if f is not None and f>0 else None}

def freshness(event_time,observed_time,max_age_seconds):
    def parse(x):
        d=datetime.fromisoformat(x.replace("Z","+00:00"))
        if d.tzinfo is None: raise ValueError("timezone required")
        return d.astimezone(timezone.utc)
    age=(parse(observed_time)-parse(event_time)).total_seconds()
    if age < -5: return "clock_conflict"
    return "fresh" if age<=max_age_seconds else "stale"
