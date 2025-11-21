# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:24:29 2024

@author: X1 Carbon Gen 7
"""

import matplotlib.pyplot as plt

Units = float(input('Your units is: '))
SellPrice = float(input('Your selling price per unit is: '))
Variable = float(input('Variable cost per unit is: ' ))
Fixed = float(input('Fixed cost for this year is: ' ))
TargetProfit = float(input('Target Profit for this year is: ' ))

# -------------------------------------------- in Power Point
# Your units is: 1000
# Your selling price per unit is: 2000
# Variable cost is: 800
# Fixed cost for this year is: 1200000
# Target Profit for this year is: 100000

# -------------------------------------------- in Excel
# Your units is: 2000
# Your selling price per unit is: 60
# Variable cost is: 45
# Fixed cost for this year is: 240000
# Target Profit for this year is: 100000



CM_Ratio = SellPrice-Variable  # Contribution Margin Ratio 
CM = Units*SellPrice - Units*Variable # Contribution Margin

print (f'\n\n Your Contribution Margin per unit is:  {CM:.2f}' )
NC = CM - Fixed # Net income
print (f'\n\n Your Net Income per unit is:  {NC:.2f}' )
NumberofUnits = (Fixed + TargetProfit) / CM_Ratio

BEP = Fixed/CM_Ratio # Break-Even Point
BEPS = Fixed/(CM_Ratio/SellPrice) # Break-Even Point in Sales

print (f'\n Your break even point in units is:  {BEP:.2f} ' 
       + f'\n\n Your break even point in total sales dollars is:  {BEPS:.2f}')


# Fixed Costs
plt.plot([0, Fixed],[Fixed, Fixed + 2 * BEP], color='red', label='Fixed Costs')
# Total Costs (Fixed + Variable)
plt.plot([0, 2 * BEP],[Fixed, Fixed + Variable * 2 * BEP], color='orange',label='Total Costs (Fixed + Variable)')
# Revenue
plt.plot([0, 2 * BEP],[0, SellPrice * 2 * BEP], color='green',label='Revenue')

# Break-Even Point
plt.plot([BEP]*2,[0, BEPS], color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6)
plt.plot([0, BEP],[BEPS]*2, color='black', linestyle='--', lw=1 ,marker = 'o', markerfacecolor = 'red', markersize = 6)

plt.scatter(NumberofUnits, Fixed+BEPS+TargetProfit, c ="blue", linewidths = 2, marker ="*", label='Target Profit: 100.000 (USD)')

plt.legend()
plt.title('Break-Even Analysis by Rinez')
plt.ylabel('Sales in Dollars')
plt.xlabel('Units Sold')

plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xlim(right=2*BEP)
plt.show()






