import unittest
from tivf import metrics,freshness
class TestTIVF(unittest.TestCase):
 def test_chip(self):
  x=metrics("0.0276",2_000_000_000,10_000_000_000,10_000_000_000)
  self.assertEqual(x["market_cap"],"55200000.0000")
  self.assertEqual(x["circulating_pct_max"],"20.0")
  self.assertEqual(x["supply_overhang_pct"],"400")
 def test_future(self):
  x=metrics("0.10",100,125,125,125)
  self.assertEqual(x["future_supply_growth_pct"],"25.00")
  self.assertEqual(x["constant_cap_price"],"0.08")
 def test_no_max(self): self.assertIsNone(metrics(1,100)["fdv"])
 def test_bad(self):
  for x in ["NaN",-1,"Infinity"]:
   with self.assertRaises(ValueError): metrics(x,100)
  with self.assertRaises(ValueError): metrics(1,200,100)
 def test_staleness(self):
  self.assertEqual(freshness("2026-11-16T10:00:00Z","2026-11-16T10:00:40Z",30),"stale")
  self.assertEqual(freshness("2026-11-16T10:00:00Z","2026-11-16T10:00:10Z",30),"fresh")
 def test_clock(self): self.assertEqual(freshness("2026-11-16T10:01:00Z","2026-11-16T10:00:00Z",30),"clock_conflict")
if __name__=="__main__": unittest.main()
