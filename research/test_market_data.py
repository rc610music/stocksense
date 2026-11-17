import unittest
from datetime import datetime,timezone
from market_data import normalize,ASSETS
class MarketDataTests(unittest.TestCase):
 now=datetime.fromtimestamp(1800000000,timezone.utc)
 def payload(self,t=1799999990,price=.03): return {'usd-ai':{'usd':price,'last_updated_at':t}}
 def test_chip_identity(self): self.assertEqual(ASSETS['CHIP'],'usd-ai')
 def test_fresh(self): self.assertEqual(normalize('CHIP',self.payload(),self.now)['quality_state'],'fresh')
 def test_stale(self): self.assertEqual(normalize('CHIP',self.payload(1799999000),self.now)['quality_state'],'stale')
 def test_future_clock(self): self.assertEqual(normalize('CHIP',self.payload(1800000100),self.now)['quality_state'],'clock_conflict')
 def test_missing_timestamp(self):
  with self.assertRaises(ValueError): normalize('CHIP',{'usd-ai':{'usd':.03}},self.now)
 def test_bad_price(self):
  with self.assertRaises(ValueError): normalize('CHIP',self.payload(price=0),self.now)
 def test_unknown_symbol(self):
  with self.assertRaises(ValueError): normalize('FAKE',self.payload(),self.now)
 def test_no_record(self):
  with self.assertRaises(ValueError): normalize('CHIP',{},self.now)
if __name__=='__main__': unittest.main()
