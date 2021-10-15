"""Position Sizing Algorithm
	Based on Volatility of asset
	Calculate 20 day ATR(N)
	
	Nifty 1 contract = 50 shares
	1 point move gains 50 rupees with no leverage
	value = 50 * 15000=750000
	Buying value = 187500
	Calculate dollar volatility-N * Dollar per point = 150 *50 = 7500
	Unit = 1% of Account / Dollar Volatility
	Capital- 20,00,000
	10% = 20000/7500=2
	ATR - 150 """

from backtrader.utils import AutoOrderedDict
rets = AutoOrderedDict()
counts = AutoOrderedDict()
counts.total = 0
hit_desc = ('Mesures the frequency in percent that each pivot was hit over the course of the time period analyzed\n')
rets['Hit']['Description'] = hit_desc
counts['Hit']['R1'] = 0
counts['Hit']['R2'] = 0
counts['Hit']['P'] = 0
counts['Hit']['S1'] = 0
counts['Hit']['S2'] = 0
print(counts)

# counts['DB']['S1 & R1'] = 0
# counts['DB']['S1 & R2'] = 0
# counts['DB']['S2 & R1'] = 0
# counts['DB']['S2 & R2'] = 0

print(counts)
