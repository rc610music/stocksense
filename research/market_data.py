"""CoinGecko REST snapshot adapter. Not a streaming or executable quote feed."""
import json
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen
ASSETS={'CHIP':'usd-ai','XRP':'ripple','ADA':'cardano','XLM':'stellar','XTZ':'tezos','DOGE':'dogecoin','SHIB':'shiba-inu'}
def normalize(symbol,payload,now=None,max_age=120):
    symbol=symbol.upper()
    if symbol not in ASSETS: raise ValueError('Unsupported token')
    item=payload.get(ASSETS[symbol])
    if not isinstance(item,dict): raise ValueError('Missing provider record')
    price,epoch=item.get('usd'),item.get('last_updated_at')
    if isinstance(price,bool) or not isinstance(price,(int,float)) or price<=0: raise ValueError('Invalid USD quote')
    if isinstance(epoch,bool) or not isinstance(epoch,int) or epoch<=0: raise ValueError('Missing source timestamp')
    observed=now or datetime.now(timezone.utc)
    if observed.tzinfo is None: raise ValueError('Timezone required')
    age=observed.timestamp()-epoch
    quality='clock_conflict' if age < -5 else ('fresh' if age<=max_age else 'stale')
    return {'symbol':symbol,'provider_id':ASSETS[symbol],'provider':'CoinGecko','quote_currency':'USD','price':price,'source_updated_at':datetime.fromtimestamp(epoch,timezone.utc).isoformat(),'observed_at':observed.astimezone(timezone.utc).isoformat(),'age_seconds':round(age,2),'quality_state':quality,'source_url':'https://www.coingecko.com/en/coins/'+ASSETS[symbol],'data_class':'delayed_rest_snapshot_not_executable_quote'}
def fetch_spot(symbol,timeout=8,max_age=120):
    symbol=symbol.upper()
    if symbol not in ASSETS: raise ValueError('Unknown or ambiguous token')
    query=urlencode({'ids':ASSETS[symbol],'vs_currencies':'usd','include_last_updated_at':'true'})
    req=Request('https://api.coingecko.com/api/v3/simple/price?'+query,headers={'User-Agent':'StockSense-TIVF/0.3','Accept':'application/json'})
    with urlopen(req,timeout=timeout) as response: data=json.load(response)
    return normalize(symbol,data,max_age=max_age)
