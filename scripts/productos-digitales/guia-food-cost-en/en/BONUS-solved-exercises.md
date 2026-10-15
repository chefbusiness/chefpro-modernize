# 12 Solved Food Cost and Menu Engineering Exercises

**Bonus of the "Food Cost + Menu Engineering Guide" Pack · Built on the Data From the Eight Excel Tools**

*John Guerrero · AI Chef Pro · aichef.pro*

Twelve exercises, each with the problem, a step-by-step solution and a table, all worked on the same sample menu the eight Excel tools in this pack use. There isn't a single invented number: every figure comes from a cell you can open and check. Do each exercise with your own data next to it and, in two afternoons, you will have your menu costed, classified and priced.

**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide**

---

## Table of Contents

1. **Gross Quantity and Cost With Trim Loss** — from the net quantity in the recipe to the quantity you actually have to buy, and from there to the cost of the line.
2. **Yield Test With Byproducts** — what a clean pound costs when you put the trimmings to use and what it costs when you don't.
3. **Actual Food Cost for a Month** — beginning inventory plus purchases minus ending inventory, and the percentage over net sales.
4. **The Same Dish Through the Four Methods** — cost factor, target margin, market price and perceived value applied to the same plate cost.
5. **Tax on a Drink, Channel by Channel** — the same bottle served dine-in and sold for takeout: two tax treatments and two prices for the guest.
6. **Classifying a Category With Kasavana & Smith** — popularity threshold, weighted average margin and the four quadrants, inside a single category.
7. **The Same Group Under Miller and Pavesic** — why two models looking at the same dishes reach different conclusions.
8. **Goal Value for Two Dishes** — one index per dish against the target of its category, no quadrants.
9. **Third-Party Delivery Repricing With Packaging and a Price Ceiling** — commission on the price, packaging per dish and the highest price the app will bear.
10. **Glass or Bottle** — the same wine served two ways: what changes in the percentage and what changes in the dollars.
11. **A Month's Prime Cost and Its Traffic Light** — adding product and labor with employer payroll taxes and benefits included, and comparing it to the target for your format.
12. **Prix Fixe Menu: The Mix Decides the Margin** — the same menu at the same price with three different splits of what guests choose.

---

## 1. Gross Quantity and Cost With Trim Loss

### The Problem and the Data

We take the tenderloin line from the "Cost Card" sheet of recipe-cost-card.xlsx: one portion calls for 0.49 lb (7.76 oz, or 0.22 kg) of net product, with 12.0% trim loss in the prep done before cooking, and the supplier invoices the tenderloin at $7.17 per lb ($15.80 per kg), pre-tax. The exercise asks two questions that come up on every recipe cost card: how much you have to buy as purchased so that, after the trim loss is discarded, you are left with the net quantity the recipe calls for; and what that line costs inside the card.

The trap is in the wording of trim loss. When someone says a piece "has 12.0% trim loss," the temptation is to take the net quantity and add 12.0% on top, as if trim loss were an extra tacked on at the end. It isn't. It is the share of the as-purchased piece that is lost along the way, and you have to buy more to make up for it, not just add a percentage to what you already have. That difference separates a recipe cost card that reflects what the kitchen really paid from one that understates the plate cost.

### The Solution, Step by Step

The formula is the same for any line: gross quantity equals net quantity divided by one minus the trim loss, with the trim loss written as a decimal. Applied to the tenderloin (net quantity 0.49 lb, trim loss 12.0%), that division gives the gross quantity to buy: 0.55 lb (8.82 oz, or 0.25 kg), the figure shown on the "Cost Card" sheet of recipe-cost-card.xlsx and in the table below.

The cost of the line is not calculated on the net quantity, which is what reaches the plate, but on the gross quantity, which is what was actually bought: gross quantity times pre-tax price per unit. With 0.55 lb of gross quantity at $7.17 per lb, the tenderloin line costs $3.95 pre-tax, the figure that closes that row in the table below. If you work in kilos, as UK and Australian kitchens do, the check is the same: 0.25 kg at $15.80 per kg is $3.95.

Now the error to get rid of. If you add the trim loss on top of the net quantity (0.49 lb plus 12.0% is about 0.54 lb, or 8.69 oz) and treat that as the gross quantity, the number comes out below the 0.55 lb you really need, and the line cost drops to $3.89 instead of the real $3.95: the kitchen buys too little and records a plate that costs less than it really does to produce. The difference is only six cents on this line, but it repeats on every line, every portion and every service. The sweet potato line, with 18.0% trim loss, reaches its gross quantity (0.49 lb, or 0.22 kg) the same way, and the total cost of the card, pre-tax, $5.67, is only correct if every line has been costed at gross and not at net.

A note on tax. The prices in this exercise are pre-tax. In recipe-cost-card.xlsx the "Tax rate (%)" cell starts at 0%, and you should leave it there unless a supplier invoice really does charge you tax that you cannot recover: in that case, the tax you pay on supplies is part of the cost of the line, and you type the rate in. If you run a business in the UK, Canada or Australia and you are registered for VAT or GST/HST, the tax you pay on your purchases is recovered on your return, so it stays out of the plate cost.

### How to Read the Result

What separates the correct recipe cost card from the wrong one is not a theoretical nuance: it is asking the supplier for the quantity you need, or running short in the middle of service, and recording a cost that exists for real instead of one that exists only on paper. The figure that comes out of the division (0.55 lb for the tenderloin, 0.49 lb for the sweet potato) is the one that goes straight into the order; buying less leaves the line short, and ordering extra "just in case" doesn't solve the problem, it only hides it. The procedure doesn't change from one line to the next, no matter how much the trim loss or the price changes: always divide the net quantity by one minus the trim loss and multiply the result by the price. That is what holds the total cost of the card, pre-tax, at $5.67.

That total cost is also the number that moves from the card to the menu when you set the selling price: if the gross quantity feeding it is wrong on even one line, the selling price inherits the same error from the first step. Checking the gross quantity of every line before you close the card is, of all the tasks in this chapter, the one that takes the least time and protects the margin the most, portion after portion, every time the dish leaves the kitchen.

**The Card Lines, With the Gross Quantity Calculated**

| Ingredient | Net Quantity/Portion | Trim Loss (%) | Gross Quantity to Buy | Price/Unit Pre-Tax ($) | Line Cost Pre-Tax ($) |
|---|---|---|---|---|---|
| Iberico pork tenderloin | 0.49 lb | 12.0% | 0.55 lb | $7.17 | $3.95 |
| Iberico pork belly (crispy) | 0.07 lb | 5.0% | 0.07 lb | $5.22 | $0.36 |
| Sweet potato | 0.40 lb | 18.0% | 0.49 lb | $0.73 | $0.35 |
| Butter | 0.02 lb | 0.0% | 0.02 lb | $4.04 | $0.13 |
| Heavy cream (35% fat) | 0.03 L | 0.0% | 0.03 L | $3.40 | $0.10 |
| Onion | 0.09 lb | 12.0% | 0.11 lb | $0.43 | $0.04 |
| Pedro Ximénez wine (for the sauce) | 0.03 L | 0.0% | 0.03 L | $9.80 | $0.29 |
| Beef stock | 0.06 L | 0.0% | 0.06 L | $2.20 | $0.13 |
| Extra virgin olive oil | 0.01 L | 0.0% | 0.01 L | $7.20 | $0.11 |
| Arugula sprouts | 0.02 lb | 10.0% | 0.02 lb | $5.44 | $0.13 |
| Salt, pepper, thyme and paprika (allocated) | 0.02 lb | 0.0% | 0.02 lb | $2.72 | $0.06 |

*Prices are per lb for the lines in pounds and per liter for the lines in liters. Quantities are rounded to two decimals; the line costs are calculated from the unrounded quantities, so multiplying the rounded figures by hand can differ by a few cents.*

---

## 2. Yield Test With Byproducts

### The Problem and the Data

We start with a whole sea bass bought at a known AP weight and a known purchase price per pound. After breaking it down in the kitchen (removing the head, bones and skin) you are left with a clean EP weight, smaller than the AP weight, and that is what is actually served on the plate. The same fish also gives you usable trimmings: head, bones and skin that don't go straight into the compost bin but are set aside, weighed and given a use value, meaning what they are worth once turned into stock or another preparation that puts them to use. These four data points (AP weight, purchase price per pound, clean weight and byproduct use value) are the minimum record for each piece that goes through this test, and they are what the "Yield Test" sheet of yield-and-trim-loss.xlsx records, piece by piece. The goal isn't to find out how much a sea bass weighs: it is to decide, with those four data points, whether it pays to buy it whole and break it down in-house or whether you come out ahead ordering it already cleaned from the supplier.

### The Solution, Step by Step

First, calculate the yield: clean weight divided by AP weight. For this sea bass the operation gives 51.7%, meaning a little over half of what you buy ends up as usable meat, and the rest is head, bones, skin and trim.

Second, the purchase cost: AP weight times price per pound. For this fish, 2.65 lb at $6.76 per lb ($14.90 per kg) comes to $17.88, the real cash outlay for the whole fish, before the knife touches it.

Third, the net cost per clean pound without using the byproduct: the purchase cost divided by the clean weight, with nothing subtracted. The result is $13.08 per lb ($28.84 per kg), and that is the figure to set against the menu price of the sea bass dish, not the purchase price per pound on the supplier's invoice.

Fourth, the net cost per clean pound using the byproduct: you subtract the byproduct's use value from the purchase cost and divide the result by the clean weight again. With that subtraction, the net cost drops to $12.53 per lb ($27.63 per kg). The distance between the two net costs is what the byproduct contributes when someone separates it and finds a use for it in the kitchen before it spoils; when nobody does, that contribution ends up in the compost bin.

### How to Read the Result

The number that really matters when you set the selling price is not the purchase price per pound on the invoice: it is the net cost per clean pound, because it reflects what each pound that reaches the guest really costs. Compared with the price per pound of the whole piece, the net cost without using the byproduct carries an extra cost of $6.32 per lb ($13.94 per kg), and even after crediting the byproduct the clean pound still costs $5.77 more per lb ($12.73 per kg) than the pound you bought. That difference is what you pay for the part of the sea bass that ends up in the compost bin instead of on the plate: the lower the yield of a piece, the more of that extra cost lands on the pounds you do sell.

Put in the context of the other tests on the same sheet, this sea bass sits somewhat below the weighted average yield of the whole set, which is 60.5% (19.07 kg of clean weight out of 31.50 kg of AP weight, or 42.04 lb out of 69.45 lb): in the table that follows this exercise there are pieces that make better use of their AP weight and others that make worse use of it, and the criterion for deciding whether a piece is worth buying whole is that comparison, not an isolated number. The same table shows tests where the byproduct weighs even more in the decision: the savings from using the shrimp heads, for example, come to $0.65 per lb ($1.43 per kg), a figure that over time, on a high-priced item you buy often, adds up very differently than on a piece you only work now and then. Altogether, the use value of the byproducts across the ten tests in the table reaches $5.15, proof that setting aside the trimmings and putting them to use is not a symbolic gesture: it is a line you track with the same discipline as any other cost on the menu.

**Ten Tests With the Cost of the Clean Pound, With and Without Using the Trimmings**

| Product | AP Weight (lb) | EP (Clean) Weight (lb) | Byproducts (lb) | Use Value ($/lb) | Net Cost, Byproduct Not Used ($/lb) | Net Cost, Byproduct Used ($/lb) | Savings ($/lb) |
|---|---|---|---|---|---|---|---|
| Whole sea bass (2.65 lb) | 2.65 | 1.37 | 0.66 | $1.13 | $13.08 | $12.53 | $0.55 |
| Whole hake | 5.29 | 2.87 | 1.21 | $1.13 | $9.88 | $9.40 | $0.48 |
| Beef tenderloin (whole piece) | 4.63 | 4.08 | 0.26 | $2.72 | $13.64 | $13.47 | $0.18 |
| Whole free-range chicken | 4.85 | 3.31 | 0.99 | $0.82 | $3.59 | $3.35 | $0.24 |
| Lamb (shoulder) | 3.53 | 2.98 | 0.00 | $0.00 | $7.09 | $7.09 | $0.00 |
| Heirloom tomato | 11.02 | 9.70 | 0.00 | $0.00 | $1.96 | $1.96 | $0.00 |
| Artichoke | 11.02 | 4.19 | 0.00 | $0.00 | $3.46 | $3.46 | $0.00 |
| Sweet potato | 11.02 | 9.04 | 0.00 | $0.00 | $0.88 | $0.88 | $0.00 |
| Mussels (in the shell) | 11.02 | 2.20 | 0.00 | $0.00 | $5.90 | $5.90 | $0.00 |
| White shrimp (whole) | 4.41 | 2.31 | 1.10 | $1.36 | $20.73 | $20.09 | $0.65 |

---

## 3. Actual Food Cost for a Month

### The Problem and the Data

A month on the menu closes with four numbers you need on the table before you talk about food cost: the inventory valued at the start of the period (the beginning inventory, what was left after the physical count that closed the previous period), the purchases that came in on invoices during the month, the inventory valued at the end (the ending inventory, after that same month's count) and the net sales invoiced over those same dates, excluding sales tax and tips. None of the four replaces another: buying is not the same as consuming.

The table below walks through that calculation month by month. In January, ingredient usage closed at $28,400 on net sales of $89,600, for a food cost of 31.7%. Carried through the twelve months of the year, cumulative purchases were $396,100, cumulative actual usage $395,400, the year's net sales $1,232,200 and the year's food cost 32.1%, against the target food cost on the dashboard, set at 30%. The exercise is to calculate actual usage and compare it with what purchases alone would tell you.

### The Solution, Step by Step

The formula doesn't change from one month to the next: usage equals beginning inventory plus purchases minus ending inventory. You apply it in three moves.

- Start from the valued inventory with which the previous month closed, which serves as this month's beginning inventory.
- Add the purchases recorded in the period, taken from each supplier's invoice, never from the delivery slip.
- Subtract the valued inventory after this month's closing physical count, the ending inventory.

What is left after that subtraction is the period's actual ingredient usage, what really went through the kitchen and the bar. Food cost comes from dividing that usage by the net sales of the same period.

Applied to January, the sequence delivers the $28,400 usage already mentioned, and that usage divided by net sales of $89,600 gives the food cost of 31.7%. The same mechanics, kept up for twelve months, put the year's actual usage at $395,400 against cumulative purchases of $396,100: two figures very close, but not the same, and the difference between them is exactly what the value of the storeroom changed over that stretch.

### How to Read the Result

The usual mistake is to accept the purchases as if they were usage, because it is the number that arrives first: the supplier's invoice is there as soon as you pay it, and actual usage only appears after the physical count. That shortcut always misleads you in the direction the storeroom has moved.

When ending inventory comes in higher than beginning inventory, with a fuller storeroom than at the start, purchases exceed actual usage, because part of what you bought hasn't left the storeroom yet. Treating purchases as usage inflates food cost: it looks worse than it is, and it can lead you to touch prices or portions over a problem that is really piled-up inventory, not cost.

When ending inventory comes in lower than beginning inventory, with the storeroom emptying out, the opposite happens: actual usage exceeds purchases, because you have spent product paid for in earlier months. Here the shortcut hides the problem, because the food cost calculated on purchases comes out better than it really is, right when the storeroom is running down.

The year illustrates it on a small scale: purchases, $396,100, sit above actual usage, $395,400, a sign that the storeroom ended the year slightly fuller than it started (beginning inventory $9,700, ending inventory $10,400). Both January's 31.7% and the year's 32.1% sit above the dashboard's target food cost, 30%, with the calculation always made on actual usage and never on what was bought: it is the only way the comparison with the target means what it says it means.

**From Stock to Usage, Month by Month**

| Month | Beginning Inventory ($) | Purchases ($) | Ending Inventory ($) | Usage ($) | Net Sales ($) | Food Cost (%) |
|---|---|---|---|---|---|---|
| January | $9,700 | $28,100 | $9,400 | $28,400 | $89,600 | 31.7% |
| February | $9,400 | $27,000 | $9,100 | $27,300 | $84,100 | 32.5% |
| March | $9,100 | $30,700 | $9,500 | $30,300 | $95,200 | 31.8% |
| April | $9,500 | $31,400 | $9,200 | $31,700 | $100,400 | 31.6% |
| May | $9,200 | $34,700 | $9,700 | $34,200 | $107,900 | 31.7% |
| June | $9,700 | $37,700 | $9,000 | $38,400 | $110,700 | 34.7% |
| July | $9,000 | $38,100 | $9,400 | $37,700 | $116,200 | 32.4% |
| August | $9,400 | $34,400 | $8,700 | $35,100 | $99,600 | 35.2% |
| September | $8,700 | $32,600 | $9,500 | $31,800 | $105,500 | 30.1% |
| October | $9,500 | $31,800 | $9,200 | $32,100 | $102,700 | 31.3% |
| November | $9,200 | $30,500 | $9,700 | $30,000 | $97,900 | 30.6% |
| December | $9,700 | $39,100 | $10,400 | $38,400 | $122,400 | 31.4% |
| TOTAL / AVERAGE |  | $396,100 |  | $395,400 | $1,232,200 | 32.1% |

---

## 4. The Same Dish Through the Four Methods

### The Problem and the Data

The exercise takes a high-cost dish: the ribeye, the cut that on any menu concentrates the highest raw-material spend per portion. The "By Dish" sheet of menu-pricing-calculator.xlsx records, for this dish, its plate cost (the one that already comes out of the recipe costing you have loaded in the rest of the pack), the target food cost set for the whole menu, a target margin in dollars that protects the absolute profit of this particular piece, and two references that don't come out of any internal calculation: the market price, what the ribeye can hold up against what direct competitors charge, and the perceived value price, the ceiling the guest is willing to pay for that cut in that restaurant. The menu's target food cost is 30%, the same percentage applied to every other dish on the sheet, from the croquettes to this ribeye. With those four starting points, the sheet solves the same dish four different ways, and what each one returns is what you compare in the table below.

### The Solution, Step by Step

The four routes start from the same cost and arrive at four different menu prices:

- **A · Cost Factor:** the plate cost is divided by the target food cost. With a 30% target food cost, the ribeye's menu price by this route climbs to $49.33.
- **B · Target Margin:** the target margin in dollars is added to the plate cost. By this route the ribeye's menu price lands at $25.30, and it is this price, not the cost factor's, that the sheet marks as the one chosen for the menu.
- **C · Market Price:** you take the price direct competitors already sustain and, with that as the input, calculate the food cost you would get by selling at that figure.
- **D · Perceived Value:** the same logic, taking as the input the ceiling the guest is willing to pay for that cut in that restaurant.

With the chosen price of $25.30, the ribeye's final food cost lands at 58.5%: far above the 30% target. The chosen price also sits below what this dish carries on the menu today, $32.70, so the exercise leaves you with a decision to make. With the croquettes, a low-cost dish, the same exercise gives a different result: the cost factor menu price is $7.00, close to the $8.60 they already carry on the menu today, so there the factor opens no gap against what the business already charges.

### How to Read the Result

The cost factor doesn't work for the ribeye, and that is not a flaw in the sheet: it is the limit of the method itself. The factor multiplies the cost by a fixed constant, designed so that food cost comes out the same on every dish on the menu, and that sameness only makes commercial sense in the low and mid cost range, where the result falls within what guests already pay out of habit. On a high-cost dish like the ribeye, the same constant pushes the price far above what the market price and the perceived value price are willing to hold up, and that is where the target margin method takes back control: it fixes the profit in dollars and lets the food cost move, even up to that 58.5% that on any other dish would call for an immediate review. It isn't that the ribeye is a bad dish: it's that on high-cost dishes food cost stops being the indicator that rules, and the contribution margin in dollars that each portion leaves takes over. Comparing the ribeye with the croquettes helps fix the idea: on a low-cost dish, the cost factor price and the target margin price tend to converge, which is why the cost factor shortcut works there; on a high-cost dish the same shortcut stops holding up, and you have to solve the price through the margin route, always checked against what the market price and the perceived value price are willing to accept.

**The Four Methods on the Same Menu**

| Dish | Plate Cost ($) | A · Cost Factor Menu Price ($) | B · Target Margin Menu Price ($) | Food Cost at Market Price (%) | Food Cost at Perceived Value (%) | Chosen Menu Price Pre-Tax ($) |
|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $7.00 | $8.60 | 23.0% | 21.8% | $7.00 |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $12.00 | $10.10 | 32.1% | 28.5% | $12.00 |
| Garlic shrimp | $6.90 | $23.00 | $13.40 | 39.7% | 37.1% | $13.40 |
| Broken eggs with potatoes and chistorra sausage | $2.40 | $8.00 | $8.90 | 26.1% | 22.7% | $8.00 |
| Local cheese board | $5.20 | $17.33 | $11.70 | 33.2% | 31.3% | $17.33 |
| Confit artichokes with ham | $3.10 | $10.33 | $9.60 | 30.6% | 26.8% | $10.33 |
| Roasted tomato soup with basil | $1.20 | $4.00 | $7.70 | 18.5% | 15.9% | $7.56 |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $18.90 | $16.17 | 30.4% | 28.3% | $18.68 |
| Confit cod in pil-pil sauce | $7.40 | $24.67 | $17.90 | 34.6% | 32.3% | $17.90 |
| Dry-aged beef burger with fries | $4.30 | $14.33 | $14.80 | 33.3% | 29.8% | $12.92 |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $20.67 | $16.70 | 35.7% | 33.2% | $16.70 |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $49.33 | $25.30 | 37.7% | 36.2% | $25.30 |
| Salt-baked sea bass | $8.90 | $29.67 | $19.40 | 37.1% | 34.6% | $19.40 |
| Free-range roast chicken with potatoes | $3.70 | $12.33 | $14.20 | 31.0% | 27.2% | $11.94 |
| Seasonal vegetable lasagna | $2.60 | $8.67 | $13.10 | 24.8% | 21.7% | $10.49 |
| Seared bluefin tuna tataki with sesame | $9.60 | $32.00 | $20.10 | 37.3% | 35.1% | $20.10 |
| Creamy cheesecake | $1.30 | $4.33 | $5.50 | 20.8% | 19.7% | $6.61 |
| Caramelized torrija with ice cream | $1.10 | $3.67 | $5.30 | 21.3% | 18.9% | $5.83 |
| Chocolate lava cake | $1.60 | $5.33 | $5.80 | 23.9% | 22.4% | $7.13 |
| Prepared seasonal fruit | $1.40 | $4.67 | $5.60 | 34.6% | 29.6% | $4.73 |

---
## 5. Tax on a Drink, Channel by Channel

### The Problem and the Data

The house red on the "Wines" sheet of beverage-cost-menu.xlsx, a young Tempranillo, has a bottle menu price of $13.60 pre-tax when it's served in the dining room, and the bottle costs you $3.90 to buy, also pre-tax. The exercise asks three questions about that one bottle: what the guest at the table pays, how much of that payment is actually yours, and how much you keep when the same bottle, at the same menu price, goes out on a third-party delivery order instead. The purchase cost doesn't move from one channel to the next: $3.90 is $3.90 whether a server opens the bottle at the table or a courier carries it out the door. Your menu doesn't split prices by channel either (the wine has one single pre-tax price), and that's exactly where it pays to look closely at what happens next, when that one price turns into a different amount in your pocket in each channel. One condition comes before any number: alcohol is licensed locally, so whether a bottle can leave the building at all, sealed, to go or on an app, is a question for your license before it's a question for your margin.

### The Solution, Step by Step

In the US, the $13.60 on the menu is before tax, and the sales tax is added on the bill. With the round 10% this guide uses as an illustrative rate (your combined state and local rate is the one that counts), the guest at the table pays $14.96: $13.60 for the wine and $1.36 of sales tax. Those $1.36 aren't yours: you only collect them, and they never count as sales. So your beverage cost is $3.90 ÷ $13.60 = 28.7%, the same figure the "Wines" sheet shows for the bottle, and the bottle leaves you $9.70 of margin. Work it out on the $14.96 the guest paid and you'd read a 26.1% beverage cost and an $11.06 margin that don't exist. Takeout, where your license lets a sealed bottle go out the door, works the same way on tax: the same $13.60, the same sales tax on top, as long as your state or city charges the same rate on takeout; check it instead of assuming it, because some states and cities add a meals tax. Canada usually works like the US, with GST or HST added on the bill.

Third-party delivery is where the channel changes what you keep, and tax has nothing to do with it. The guest still pays $13.60 plus sales tax, but the app takes its commission off the selling price: at the 30% the simulator uses, $4.08 of the $13.60 goes to the platform and you keep $9.52, so the beverage cost on the same bottle climbs from 28.7% to 41.0% and the margin drops from $9.70 to $5.62, before you spend a cent on packaging. That's why the nine-cell tax matrix on the "Inputs" sheet of multichannel-repricing-simulator.xlsx stays at 0% for a US or Canadian menu: you type pre-tax prices and leave your sales tax out of it, because the simulator reads every price as including the rate in its cell. The UK is where tax itself moves with the channel, and where the item matters as much as the channel. Prices there are printed with 20% VAT included, so the same bottle printed at 16.32 on the premises leaves you 16.32 ÷ 1.20 = 13.60. Most cold takeaway food is zero-rated, but soft drinks, confectionery and crisps never join that zero rate: a can of cola printed at 2.76 pays 20% whether it's drunk at the table or goes out with a cold sandwich, so it nets 2.30 in both channels, while the sandwich beside it in the bag pays nothing (the detail lives in VAT Notices 709/1 and 701/14 on gov.uk). In the simulator, a UK operator types 20%, and 0% only where their cold takeaway food is zero-rated; the soft drink column never drops to zero. In Australia, the 10% GST is already inside every printed price, whatever the channel: a bottle printed at 14.96 carries 1.36 of GST (one eleventh) and nets 13.60, and that's the 10% you type in the simulator.

### How to Read the Result

The purchase cost of the bottle is identical in every channel: $3.90 pre-tax, whether the server pours it or a courier carries it. What moves is what comes off the price before it reaches you, and that movement has a consequence that usually goes unnoticed on the menu. The sales tax the guest pays on top is never yours, in any channel, so it never belongs in your percentages; the commission, on the other hand, comes straight out of your share. If you keep the same menu price on the app for convenience (one price, one label for the same bottle), the beverage cost goes from 28.7% to 41.0% and the margin falls from $9.70 to $5.62. The purchase cost hasn't gone up a cent and yet the margin on that sale drops, purely because of the channel the guest chose. That's why each channel's price gets set on the pre-tax menu price and on what that channel takes off it: to keep the same $9.70 and the same 28.7% on delivery, the bottle needs $19.43 pre-tax on the app ($13.60 ÷ 0.70), a figure you then check against the app's ceiling price, exactly as the simulator does with every dish. In the UK the same rule works item by item: one printed price across channels leaves a different net on a cold sandwich eaten in (20% VAT) than taken away (zero-rated), but the same net on the cola, which stays at 20% either way. Book the whole cold order as zero-rated and you'd count the full 2.76 as sales, 0.46 of VAT that isn't yours, and read a 19.9% beverage cost on the can instead of the real 23.9%. Applying each channel's real deduction to each item, instead of dragging one final price from one channel to the next, is what keeps the difference from eating your margin without anyone having decided it.

**The Same Bottle, Two Channels: What the Guest Pays and What You Keep**

| Wine | Bottle Menu Price Pre-Tax ($) | Illustrative Sales Tax (%) | Guest Pays With Tax, Any Channel ($) | Delivery App Commission (%) | You Keep on Delivery, Pre-Tax ($) |
|---|---|---|---|---|---|
| House red (young Tempranillo) | $13.60 | 10% | $14.96 | 30% | $9.52 |
| Rioja Crianza | $19.10 | 10% | $21.01 | 30% | $13.37 |
| Ribera del Duero Roble | $21.80 | 10% | $23.98 | 30% | $15.26 |
| Rueda Verdejo | $14.50 | 10% | $15.95 | 30% | $10.15 |
| Rias Baixas Albariño | $22.70 | 10% | $24.97 | 30% | $15.89 |
| Cava Brut Nature | $18.20 | 10% | $20.02 | 30% | $12.74 |
| Navarra Rosé | $12.70 | 10% | $13.97 | 30% | $8.89 |
| Pedro Ximénez dessert wine | $27.30 | 10% | $30.03 | 30% | $19.11 |


---

## 6. Classifying a Category With Kasavana & Smith

### The Problem and the Data

Before you trust the label the matrix puts next to each dish, it's worth working it out by hand once, with a single category, to see where each word comes from. Take the starters category as it appears on the "Data" sheet of menu-engineering-matrix.xlsx: 7 dishes, 1,730 units sold over the period the analysis covers and a weighted average contribution margin of $7.46 per unit. Those are the three starting figures, and you don't need a single other one to reproduce the model's logic.

The model behind the exercise is Kasavana and Smith's (1982): it sets how much each dish weighs within the sales of its own category against how much margin it leaves, and that double comparison produces one of four labels. What's still missing to close the calculation dish by dish (the units sold and the margin of each dish on its own, no longer those of the whole category) is exactly what the table after this text gives you, with the category's threshold next to every row.

### The Solution, Step by Step

With the category's three figures you can rebuild the whole procedure in four steps, the same ones the matrix applies to every category on the menu:

- Each dish's menu mix is its weight within the category: the units that particular dish sells over the 1,730 units all the starters add up to. It's a share within the category, not within the whole menu, which is why the same number of sales weighs differently depending on which category the dish falls into.
- The category's popularity threshold comes from applying the 70% factor (the same one that runs the whole matrix, also stored on the "Data" sheet) to the share each dish would get if units were split evenly among the category's 7 dishes: that 70% multiplied by one over the number of dishes. A dish with a menu mix above that threshold counts as popular within its category; below it, it doesn't.
- Each dish's contribution margin is compared with the category's weighted average contribution margin, those $7.46 per unit. Above the average, the dish leaves more margin than the starters as a whole; below it, it leaves less.
- The label comes from crossing the two comparisons, not from reading them one at a time: high popularity with a high margin is a Star; high popularity with a low margin, a Plowhorse; low popularity with a high margin, a Puzzle; and low popularity with a low margin, a Dog.

Applied to the whole menu (not just the starters), the result on the "Kasavana-Smith" sheet of menu-engineering-matrix.xlsx is 6 Stars, 6 Plowhorses, 5 Puzzles and 3 Dogs. It's the same logic we just applied by hand to the starters, repeated category by category until the whole menu is done; the next table gives the dish-by-dish detail, with each dish's menu mix, margin and threshold next to its label.

### How to Read the Result

A dish's label isn't a property of the dish on its own: it depends on the set of dishes it shares a category with at the moment you calculate it. The threshold is built on the number of dishes in the category and each dish's menu mix is measured on that same category's total units, so taking a dish off the menu (or adding a new one) changes both denominators at once. The dishes that stay haven't sold a single unit more or less, but their menu mix is recalculated on a different total and the category's weighted average margin shifts too, so a dish that sits just above the threshold today can fall below it the next time you review the menu, without anything in its own sales having changed. That's why it pays to repeat this calculation every time you change a category's lineup, not only when the menu price or the cost of a particular dish changes: pulling the dish with the worst label out of a category doesn't always help the others, because it can push the threshold or the average to a point that hurts another dish that was safe until then.

**The Classification Dish by Dish, With Its Category Threshold Alongside**

| Dish | Category | Units | Menu Mix in Category (MM%) | Threshold (%) | CM ($) | Classification |
|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | Starters | 420 | 24.3% | 10.0% | $6.50 | Plowhorse |
| Heirloom tomato salad with tuna belly and scallions | Starters | 310 | 17.9% | 10.0% | $8.20 | Star |
| Garlic shrimp | Starters | 260 | 15.0% | 10.0% | $8.60 | Star |
| Broken eggs with potatoes and chistorra sausage | Starters | 380 | 22.0% | 10.0% | $7.40 | Plowhorse |
| Local cheese board | Starters | 90 | 5.2% | 10.0% | $8.40 | Puzzle |
| Confit artichokes with ham | Starters | 120 | 6.9% | 10.0% | $7.80 | Puzzle |
| Roasted tomato soup with basil | Starters | 150 | 8.7% | 10.0% | $6.00 | Dog |
| Iberico pork tenderloin with sweet potato purée | Mains | 340 | 16.8% | 7.8% | $11.63 | Star |
| Confit cod in pil-pil sauce | Mains | 190 | 9.4% | 7.8% | $11.70 | Star |
| Dry-aged beef burger with fries | Mains | 460 | 22.8% | 7.8% | $9.30 | Plowhorse |
| Creamy rice with Iberico pork secreto and mushrooms | Mains | 270 | 13.4% | 7.8% | $10.20 | Plowhorse |
| Dry-aged bone-in ribeye (17.64 oz) | Mains | 110 | 5.4% | 7.8% | $17.90 | Puzzle |
| Salt-baked sea bass | Mains | 80 | 4.0% | 7.8% | $12.90 | Puzzle |
| Free-range roast chicken with potatoes | Mains | 300 | 14.9% | 7.8% | $9.00 | Plowhorse |
| Seasonal vegetable lasagna | Mains | 140 | 6.9% | 7.8% | $8.80 | Dog |
| Seared bluefin tuna tataki with sesame | Mains | 130 | 6.4% | 7.8% | $12.80 | Puzzle |
| Creamy cheesecake | Desserts | 520 | 46.4% | 17.5% | $4.60 | Star |
| Caramelized torrija with ice cream | Desserts | 210 | 18.8% | 17.5% | $4.40 | Plowhorse |
| Chocolate lava cake | Desserts | 330 | 29.5% | 17.5% | $4.60 | Star |
| Prepared seasonal fruit | Desserts | 60 | 5.4% | 17.5% | $3.10 | Dog |


---

## 7. The Same Group Under Miller and Pavesic

### The Problem and the Data

The exercise starts from a group of dishes on the menu, with three figures already settled on their recipe cost cards: food cost %, contribution margin per unit and units sold in the period. They're the same figures you've already worked with separately in the Miller matrix and in the Pavesic matrix; here they're crossed dish by dish, to see what happens when two models that start from the same cost and the same menu price give the same dish a different label. What changes is the second axis: each dish's weight in total units sold, or the contribution margin it leaves multiplied by those units. That volume-weighted margin is the figure that separates one model from the other, and it's worth keeping in mind before you look at the table below, with Miller and Pavesic side by side on the same menu.

### The Solution, Step by Step

Both paths start from the same pair of figures (food cost % and contribution margin) but cross a different second axis. Miller (1980) sets food cost % against each dish's popularity, its weight in total units sold: high or low popularity, high or low food cost, four quadrants. On this group it hands out 8 Winners (high popularity and low food cost) and 5 Losers (low popularity and high food cost), with a weighted average food cost of 26.9% across the Winners. In qualitative terms, Miller's is the first matrix model to cross food cost with the menu mix, the direct forerunner of the Kasavana and Smith matrix you've worked with throughout the rest of this pack.

Pavesic (1983) takes the same food cost % but changes the second axis: instead of popularity, in comes the contribution margin weighted by each dish's units sold, not the unit margin of a single portion. Swapping the individual margin for the weighted one is, in qualitative terms, the correction Pavesic makes to Miller: two dishes with the same popularity can leave different dollars in the register depending on what each unit sold is worth, a nuance that disappears if you only count portions. With that new axis the split changes: 7 Prime dishes (low food cost and high weighted margin) and 6 Problems (high food cost and low weighted margin), with a total weighted contribution margin of $21,408 across the Primes.

Put the two splits side by side and only 3 dishes keep the best label across all four readings at once (Winner under Miller, Prime under Pavesic, with Kasavana & Smith and Goal Value agreeing, without a single crack). At the other end there are 12 dishes where three or four readings don't match: a dish can come out a Winner on popularity and a Problem on weighted margin, or a Loser for selling little and a Prime because each unit leaves a high margin. In those 12, the label changes with the model, and they're the ones that deserve a second look before you touch the menu price or take a dish off the menu.

### How to Read the Result

When Miller and Pavesic disagree on a dish, it isn't a calculation error: it's the warning that the dish has a food cost % that doesn't match the dollars it actually leaves in the register. Food cost % is a ratio to the menu price and, on its own, says nothing about the volume moving behind it; weighted contribution margin does, because it multiplies what each unit leaves by how many of them sell. A dish with a modest food cost % can look healthy at a glance and still contribute little weighted margin if it barely gets ordered; and one with a higher food cost % can carry a good share of the menu's total contribution margin if it sells a lot, even though its percentage alone flags it as suspect.

The decision isn't about picking one model and throwing out the other, but about using the disagreement as a filter: when they agree, the dish calls for no urgent action; when they disagree, look at that dish's menu price, cost and volume before you touch it, because the percentage alone (without knowing how many units go out and how much contribution margin they leave) can lead you to raise a price that already works or to keep one that's dragging the numbers down.

**Miller and Pavesic on the Same Dish, Side by Side**

| Dish | Category | Miller | Pavesic | Readings Off | Diagnosis |
|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | Starters | Winner | Prime | 1 | Popular with a low margin: raise the price or cut the cost. |
| Heirloom tomato salad with tuna belly and scallions | Starters | Winner | Prime | 0 | All four readings agree on the best label: keep it, feature it on the menu and protect the recipe and the supplier. |
| Garlic shrimp | Starters | Marginal | Standard | 3 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Broken eggs with potatoes and chistorra sausage | Starters | Winner | Prime | 1 | Popular with a low margin: raise the price or cut the cost. |
| Local cheese board | Starters | Loser | Problem | 4 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Confit artichokes with ham | Starters | Marginal | Sleeper | 4 | Healthy food cost % but little added to total margin: give it visibility before you remove it. |
| Roasted tomato soup with basil | Starters | Marginal | Sleeper | 4 | Healthy food cost % but little added to total margin: give it visibility before you remove it. |
| Iberico pork tenderloin with sweet potato purée | Mains | Winner | Prime | 0 | All four readings agree on the best label: keep it, feature it on the menu and protect the recipe and the supplier. |
| Confit cod in pil-pil sauce | Mains | Marginal | Problem | 3 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Dry-aged beef burger with fries | Mains | Winner | Prime | 1 | Popular with a low margin: raise the price or cut the cost. |
| Creamy rice with Iberico pork secreto and mushrooms | Mains | Marginal | Standard | 3 | The readings disagree: each method measures two of the three variables (popularity, dollar margin and food cost %). Decide with the one that hurts most this month. |
| Dry-aged bone-in ribeye (17.64 oz) | Mains | Loser | Problem | 4 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Salt-baked sea bass | Mains | Loser | Problem | 4 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Free-range roast chicken with potatoes | Mains | Winner | Prime | 1 | Popular with a low margin: raise the price or cut the cost. |
| Seasonal vegetable lasagna | Mains | Marginal | Sleeper | 4 | Healthy food cost % but little added to total margin: give it visibility before you remove it. |
| Seared bluefin tuna tataki with sesame | Mains | Loser | Problem | 4 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Creamy cheesecake | Desserts | Winner | Prime | 0 | All four readings agree on the best label: keep it, feature it on the menu and protect the recipe and the supplier. |
| Caramelized torrija with ice cream | Desserts | Winner | Sleeper | 3 | Popular with a low margin: raise the price or cut the cost. |
| Chocolate lava cake | Desserts | Marginal | Standard | 2 | High CM with a weak food cost %: protect the dollar margin, review the price, don't remove it. |
| Prepared seasonal fruit | Desserts | Loser | Problem | 4 | Rarely ordered, high food cost % and little added to total margin: a candidate to remove or to rework from the ground up. |


---
## 8. Goal Value for Two Dishes

### The Problem and the Data

This exercise takes two dishes from the same menu category and applies the Hayes and Huffman (1985) index, the model the trade knows as Goal Value. Each dish brings three numbers of its own: its food cost percentage, its pre-tax menu price and the units sold in the period you are analyzing. Those three numbers, dish by dish, are what the table below collects. On top of that come two percentages that don't change from one dish to the next, because they describe the cost structure of the whole business, not of the individual recipe: labor cost as a share of sales, set at 32% for this exercise, and all other variable costs as a share of sales (utilities, maintenance, card processing fees and the like), set at 10%. These two figures go into the calculation for every dish on the menu the same way; what sets one dish apart from another is its own food cost, its own menu price and its own volume. With those five inputs (three from the dish, two from the house) the index is ready to calculate, with no outside market or competitor data needed.

### The Solution, Step by Step

The calculation repeats the same way for every dish in the category, and before you touch a single dish you have to set the target for the group:

- First, calculate the category target: the weighted average food cost of all the dishes in that category, weighting each one by its share of the group's units sold. The logic is the same one that produces the weighted average food cost of the whole menu (32.7%, according to the "Data" sheet of `menu-engineering-matrix.xlsx`), only applied to the group instead of the whole business: a dish that sells a lot weighs more in that average than one that barely leaves the kitchen, wherever its food cost happens to sit.
- With the category target set, each dish adds the labor cost and the other variable costs (the 32% and 10% of the house) to its own food cost, which gives the combined weight of the three variable costs on its pre-tax menu price.
- That combined weight is then compared against the same calculation run with the category target in place of the dish's own food cost, and the result of that comparison, adjusted for the dish's sales volume within its group, is the index: a single number that replaces the old quadrant matrix (stars, plowhorses, puzzles and dogs) with one figure you can rank, dish by dish and category by category.

The procedure doesn't change from one category to another: the only thing that varies is the target, because each category is weighted with its own dishes and its own sales.

### How to Read the Result

The index has no units: it is not a percentage, not a dollar amount, not a score out of ten. It is a relative number, and it only means something when compared with the target of its own category; you don't compare it across categories or against the average food cost of the whole menu. A starter and a dessert can end up with similar indexes without that meaning anything, because each category is weighed against itself: it has its own menu price, its own volume and its own reference food cost.

The only thing the index tells you, dish by dish, is whether that dish sits above or below the target set by its own category. Applied to the whole menu in this exercise, the result leaves 9 dishes above their category target and 11 below, according to the "Goal Value" sheet of `menu-engineering-matrix.xlsx`. That 9-and-11 split doesn't yet tell you which category is driving the imbalance or which dish to review first. That is what the next table is for: it sets each dish against the target of its own group, so you can see, category by category, where there is margin to recover without touching the menu price and where the problem is volume, not cost.

**Each Dish's Index Against Its Category Target**

| Dish | Menu Price Pre-Tax ($) | Food Cost (%) | Dish Goal Value | Category Target Goal Value | Reading |
|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $8.60 | 24.4% | 916.77 | 503.30 | Above target |
| Heirloom tomato salad with tuna belly and scallions | $11.80 | 30.5% | 698.83 | 503.30 | Above target |
| Garlic shrimp | $15.50 | 44.5% | 301.50 | 503.30 | Below target |
| Broken eggs with potatoes and chistorra sausage | $9.80 | 24.5% | 942.31 | 503.30 | Above target |
| Local cheese board | $13.60 | 38.2% | 149.42 | 503.30 | Below target |
| Confit artichokes with ham | $10.90 | 28.4% | 276.68 | 503.30 | Below target |
| Roasted tomato soup with basil | $7.20 | 16.7% | 372.00 | 503.30 | Below target |
| Iberico pork tenderloin with sweet potato purée | $17.30 | 32.8% | 997.46 | 543.03 | Above target |
| Confit cod in pil-pil sauce | $19.10 | 38.7% | 428.07 | 543.03 | Below target |
| Dry-aged beef burger with fries | $13.60 | 31.6% | 1,128.64 | 543.03 | Above target |
| Creamy rice with Iberico pork secreto and mushrooms | $16.40 | 37.8% | 556.17 | 543.03 | Above target |
| Dry-aged bone-in ribeye (17.64 oz) | $32.70 | 45.3% | 250.85 | 543.03 | Below target |
| Salt-baked sea bass | $21.80 | 40.8% | 177.24 | 543.03 | Below target |
| Free-range roast chicken with potatoes | $12.70 | 29.1% | 779.39 | 543.03 | Above target |
| Seasonal vegetable lasagna | $11.40 | 22.8% | 433.58 | 543.03 | Below target |
| Seared bluefin tuna tataki with sesame | $22.40 | 42.9% | 251.98 | 543.03 | Below target |
| Creamy cheesecake | $5.90 | 22.0% | 860.31 | 436.37 | Above target |
| Caramelized torrija with ice cream | $5.50 | 20.0% | 351.12 | 436.37 | Below target |
| Chocolate lava cake | $6.20 | 25.8% | 488.70 | 436.37 | Above target |
| Prepared seasonal fruit | $4.50 | 31.1% | 50.01 | 436.37 | Below target |

*Goal Value is a unitless index: it is not a dollar amount, even though the sheet displays it with two decimals.*


---

## 9. Third-Party Delivery Repricing With Packaging and a Price Ceiling

### The Problem and the Data

The exercise starts from a dish whose recipe costing is already solved: the croquettes. The delivery channel adds two variables to the plate cost that the dining room never sees, the platform's commission and the packaging for the order, and it also sets a price ceiling: the limit above which the customer stops ordering the dish on the app. Here is the starting data:

- Plate cost of the croquettes: $2.10.
- Dine-in menu price, pre-tax: $8.60.
- Channel commission: 30%.
- Packaging per order: $1.75, with an average of 2.5 dishes per order.
- Packaging per dish: $0.70.
- Delivery price ceiling: $11.60.

The 30% commission in this exercise sits inside the 15% to 35% range commonly cited for delivery platforms, depending on the area, the plan you sign and who handles the delivery. And it is rarely the only cost: packaging can move on its own between $1.35 and $2.15 per order, some platforms ask for visibility discounts of between 20% and 30%, and performance penalties can add up to 2 more points of commission. These are extras that are almost never in plain sight when you sign the contract.

### The Solution, Step by Step

The first step adds the plate cost of the croquettes and the packaging that belongs to each dish. That gives you the effective cost, the real number you have to cover when the order walks out the door in its packaging, not just with the finished dish.

The second step checks what happens if you charge the same price on delivery as in the dining room. The effective food cost is the effective cost divided by the menu price times one minus the commission, in other words, divided by what the restaurant actually keeps from the price once the platform takes its percentage. With the dine-in price untouched, the "Menu" sheet of `multichannel-repricing-simulator.xlsx` puts the croquettes' effective food cost at 46.5%, far above the channel's target food cost of 40%. That makes it plain: the dine-in price doesn't work for the delivery channel without a second look.

The third step flips the formula: instead of starting from the price to arrive at the food cost, you start from the target food cost to arrive at the price. The required price is the effective cost divided by the product of the target food cost and one minus the commission. For the croquettes, that calculation sets the required price at $10.00: the minimum price at which, after the 30% commission, the dish's delivery food cost falls back to the 40% you are aiming for.

### How to Read the Result

The last step is no longer calculation, it is a decision: compare the required price with the price ceiling. For the croquettes, a required price of $10.00 against a ceiling of $11.60 leaves plenty of room, so the dish goes into the delivery channel without pushing the price to the limit your customer will tolerate, and it stays on the delivery menu at that recalculated price.

The same test repeats dish by dish, and the table below sets out, as summarized in the "Summary" sheet of `multichannel-repricing-simulator.xlsx`, the result for the whole menu: 12 dishes viable on delivery against 8 you need to exclude or rework. When the required price exceeds the ceiling, the answer is not to raise the price to the limit and hope it holds: that just passes the problem to the customer, who stops ordering the dish. The real way out is to pull the dish from the delivery channel, leaving it for the dining room only, where the food cost does work, or to rework it: lower the plate cost, adjust the portion or swap an ingredient until the required price fits back under the ceiling. And repeat the calculation every time your terms with the platform change, because the commission and the costs stacked on top of it move with your area, your plan and the promotion of the moment.

**The Menu on the Delivery Channel: Required Price Against Price Ceiling**

| Dish | Plate Cost ($) | Dine-In Menu Price Pre-Tax ($) | Delivery Food Cost (%) | Required Menu Price ($) | Price Ceiling ($) | Viable? |
|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $8.60 | 46.5% | $10.00 | $11.60 | Yes |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $11.80 | 52.1% | $15.36 | $15.90 | Yes |
| Garlic shrimp | $6.90 | $15.50 | 70.0% | $27.14 | $20.90 | No: exclude or rework |
| Broken eggs with potatoes and chistorra sausage | $2.40 | $9.80 | 45.2% | $11.07 | $13.20 | Yes |
| Local cheese board | $5.20 | $13.60 | 62.0% | $21.07 | $18.40 | No: exclude or rework |
| Confit artichokes with ham | $3.10 | $10.90 | 49.8% | $13.57 | $14.70 | Yes |
| Roasted tomato soup with basil | $1.20 | $7.20 | 37.7% | $6.79 | $9.70 | Yes |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $17.30 | 52.6% | $22.75 | $23.40 | Yes |
| Confit cod in pil-pil sauce | $7.40 | $19.10 | 60.6% | $28.93 | $25.80 | No: exclude or rework |
| Dry-aged beef burger with fries | $4.30 | $13.60 | 52.5% | $17.86 | $18.40 | Yes |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $16.40 | 60.1% | $24.64 | $22.10 | No: exclude or rework |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $32.70 | 67.7% | $55.36 | $44.10 | No: exclude or rework |
| Salt-baked sea bass | $8.90 | $21.80 | 62.9% | $34.29 | $29.40 | No: exclude or rework |
| Free-range roast chicken with potatoes | $3.70 | $12.70 | 49.5% | $15.71 | $17.10 | Yes |
| Seasonal vegetable lasagna | $2.60 | $11.40 | 41.4% | $11.79 | $15.40 | Yes |
| Seared bluefin tuna tataki with sesame | $9.60 | $22.40 | 65.7% | $36.79 | $30.20 | No: exclude or rework |
| Creamy cheesecake | $1.30 | $5.90 | 48.4% | $7.14 | $8.00 | Yes |
| Caramelized torrija with ice cream | $1.10 | $5.50 | 46.8% | $6.43 | $7.40 | Yes |
| Chocolate lava cake | $1.60 | $6.20 | 53.0% | $8.21 | $8.40 | Yes |
| Prepared seasonal fruit | $1.40 | $4.50 | 66.7% | $7.50 | $6.10 | No: exclude or rework |


---

## 10. Glass or Bottle

### The Problem and the Data

Opening a wine by the glass is a decision you make with a calculator in hand, not on dining-room instinct. The case is the house red: a standard 750 ml bottle, sold by the glass as well as by the full bottle, with a pre-tax purchase price of $3.90. The restaurant has set one menu price for the bottle and a different one for the single glass, and the gap between what the wine costs and what you charge produces the margin and, with it, the beverage cost of each format. The figures that the "Wines" sheet of `beverage-cost-menu.xlsx` records for this wine are the following: the bottle yields 5.0 glasses (750 ml ÷ 5 = 150 ml, or 5.07 fl oz, per glass), the cost per glass is $0.78, the margin per bottle is $9.70 and the margin per glass is $2.22. The beverage cost of the whole bottle is 28.7%, that of the glass is 26.0%, and the target set for the wines on the menu is 30%. The weighted average of all the wines, using the actual sales weight of each label, comes in at 30.2%, slightly above target, but not a deviation that calls for reviewing the whole wine list.

### The Solution, Step by Step

The first step is to split the bottle into the glasses you actually pour: 5.0 for each purchase unit. The cost per glass comes from dividing the purchase price by those glasses, which is why $3.90 spread over 5.0 glasses gives the $0.78 on the card. From there the rest is reading, not calculating: the margin per bottle ($9.70) and the margin per glass ($2.22) come from subtracting the cost from the corresponding menu price, one for the full bottle and one for the single glass, and both are already solved in the template. Beverage cost follows the same path in percentage form: cost over menu price gives the bottle's 28.7% and the glass's 26.0%. That difference is the effect of selling the same raw material in a portion with a better price per ounce: the single glass carries its own cost better than the sealed bottle does. Put in the context of the entire wine list, the weighted 30.2% against the 30% target says that, even though this label does better when opened by the glass, the list as a whole still needs the same purchasing and costing discipline as any other category on the menu.

### How to Read the Result

The percentage improves with the glass: going from 28.7% to 26.0% beverage cost is an efficiency gain on paper. But the dollar margin per opened bottle (the $9.70 each unit supposedly generates) only materializes if all 5.0 glasses find a buyer before the wine oxidizes or comes off the list. Over-pouring, leaving a glass off the check as a comp, or dumping what is left of a bottle that has been open for several days all eat into that difference without any sheet recording it: the spreadsheet keeps showing a 26.0% beverage cost on the glass while the real bottle, the one actually opened at the bar, earns less margin than the card promises. That is why the floor's yardstick is not just to compare the glass percentage against the bottle's, but to track how many glasses of each opened bottle actually get served. As a market reference, bear in mind that it comes from a US industry aggregate with no breakdown by type of drink, and that the range in the aggregate from getbackbar.com and purimax.com (2026) puts target beverage cost at 15% to 22% for spirits and cocktails, 20% to 26% for draft beer, 24% to 28% for bottled or canned beer, and 18% to 24%, with an average of 20%, as an overall target on drink sales. The house red, at 26.0% by the glass, sits inside that same band, although the figure that rules when you set prices on your own menu is still the internal 30% target for wines, not the average of another drink category.

**Bottle and Glass of the Same Wine, With Margin and Percentage**

| Wine | Bottle Menu Price Pre-Tax ($) | Glass Menu Price Pre-Tax ($) | Glasses per Bottle | Cost per Glass ($) | Bottle Margin ($) | Glass Margin ($) | Bottle Beverage Cost (%) | Glass Beverage Cost (%) |
|---|---|---|---|---|---|---|---|---|
| House red (young Tempranillo) | $13.60 | $3.00 | 5.0 | $0.78 | $9.70 | $2.22 | 28.7% | 26.0% |
| Rioja Crianza | $19.10 | $4.10 | 5.0 | $1.22 | $13.00 | $2.88 | 31.9% | 29.8% |
| Ribera del Duero Roble | $21.80 | $4.50 | 5.0 | $1.48 | $14.40 | $3.02 | 33.9% | 32.9% |
| Rueda Verdejo | $14.50 | $3.20 | 5.0 | $0.84 | $10.30 | $2.36 | 29.0% | 26.2% |
| Rias Baixas Albariño | $22.70 | $4.80 | 5.0 | $1.58 | $14.80 | $3.22 | 34.8% | 32.9% |
| Cava Brut Nature | $18.20 | $3.90 | 5.0 | $1.12 | $12.60 | $2.78 | 30.8% | 28.7% |
| Navarra Rosé | $12.70 | $2.90 | 5.0 | $0.74 | $9.00 | $2.16 | 29.1% | 25.5% |
| Pedro Ximénez dessert wine | $27.30 | $4.00 | 8.0 | $1.44 | $15.80 | $2.56 | 42.1% | 35.9% |


---

## 11. A Month's Prime Cost and Its Traffic Light

### The Problem and the Data

The exercise starts from a closed month: net sales for the period (after discounts, before sales tax and tips), raw material consumption, gross wages and other labor costs, the part that doesn't go through payroll but is still part of keeping a team on. To the gross wages you have to add employer payroll taxes and benefits, set in the dashboard at 33% (a model input: replace it with your own figure). One third piece of data is missing before you calculate anything: the prime cost target for the format, which is not the same for full service (65%) as for counter or self-service (55%). These are two different yardsticks, not a minor variation on the same number.

The month is August, with net sales of $99,600. The remaining lines (raw material consumption, gross wages, other labor costs) are already loaded in the "Monthly" sheet of `prime-cost-dashboard.xlsx`, and from them comes the full labor cost for the month, payroll taxes and benefits included: $34,517. With net sales, labor cost and the format's target as your yardstick, the exercise has everything it needs.

### The Solution, Step by Step

The solution follows the order of the sheet itself. First you build the labor cost: gross wages, multiplied by one plus the employer payroll taxes and benefits (the 33% already mentioned), plus the other labor costs. That sum, never the gross payroll on its own, is what gets compared with sales: leaving out the payroll taxes and benefits by oversight doesn't change what the business pays, but it does falsify the traffic light. For August, that build-up comes to $34,517.

With labor cost closed, the second step is to divide each line by the month's net sales. Food cost comes from putting raw material consumption over those net sales: 35.2% in August. Labor cost comes from putting the full labor cost, the $34,517 you just built, over the same base: 34.7%. Since both are measured on the same net sales, they add up with no adjustment at all: prime cost is food cost plus labor cost, 35.2% plus 34.7%, which the sheet resolves to 69.9%. By definition, prime cost is those two lines together over the net sales of the same period.

### How to Read the Result

August's 69.9% gets read against the target of your format, not against an abstract number. With full service the target is 65%, so August lands above target, exactly as the sheet flags it. It also pays to look at the year to date: prime cost for the year is 63.4%, within range, which makes August's problem a one-off and not a drift across the whole year.

That same 69.9% would mean something different at a counter or in self-service, because that format's target is not 65% but 55%, a tougher yardstick for the same two lines. The reason is not that a counter costs less in the abstract, but that it spreads its spending differently. According to a 2026 European industry study, labor cost as a share of net sales runs 30% to 35% with integrated table service, and 15% to 25% with partial service such as self-service or a counter: the staff needed to carry the dish to the table, collect payment and clear is not the staff behind a counter where the guest does much of the legwork. Along the same lines, Toast, "How to Calculate Prime Cost" (2026), puts the expected prime cost at 60% to 65% for full service and 55% to 60% for quick service (QSR): the ceiling drops because the weight of labor drops, not because food cost has to be squeezed harder.

That is why a 69.9% prime cost in a full-service dining room and that same 69.9% at a counter don't call for the same correction. In the dining room, with a labor cost of 34.7% already within range, the room for improvement is in food cost: trim loss, yields and the recipe costing of each dish, before you touch the staffing. At a counter, with a much lower labor target, that same 34.7% would already be out of range by itself, and the fix would look first at shifts and team sizing. Reading the traffic light without looking at the format almost always leads you to correct the line that isn't the problem.

**The Twelve Months With Their Prime Cost and Reading**

| Month | Labor Cost With Payroll Taxes and Benefits ($) | Food Cost (%) | Labor Cost (%) | Prime Cost (%) | Target (%) | Reading |
|---|---|---|---|---|---|---|
| January | $29,988 | 31.7% | 33.5% | 65.2% | 65.0% | Above target |
| February | $29,918 | 32.5% | 35.6% | 68.0% | 65.0% | Above target |
| March | $30,919 | 31.8% | 32.5% | 64.3% | 65.0% | On target |
| April | $31,255 | 31.6% | 31.1% | 62.7% | 65.0% | On target |
| May | $32,256 | 31.7% | 29.9% | 61.6% | 65.0% | On target |
| June | $33,656 | 34.7% | 30.4% | 65.1% | 65.0% | Above target |
| July | $34,657 | 32.4% | 29.8% | 62.3% | 65.0% | On target |
| August | $34,517 | 35.2% | 34.7% | 69.9% | 65.0% | Above target |
| September | $31,920 | 30.1% | 30.3% | 60.4% | 65.0% | On target |
| October | $31,255 | 31.3% | 30.4% | 61.7% | 65.0% | On target |
| November | $30,919 | 30.6% | 31.6% | 62.2% | 65.0% | On target |
| December | $34,398 | 31.4% | 28.1% | 59.5% | 65.0% | On target |
| TOTAL / AVERAGE | $385,658 | 32.1% | 31.3% | 63.4% | 65.0% | On target |


---

## 12. Prix Fixe Menu: The Mix Decides the Margin

### The Problem and the Data

The exercise starts from a prix fixe menu: a single selling price that bundles several courses, each with two or three options to choose from. The menu price is $13.18 pre-tax, which is $14.50 once the illustrative 10% sales tax is added at the register. On top of that sit fixed costs of $0.55 per menu (table bread, coffee and the included drink, the part of mise en place and structure that doesn't change whatever the guest orders). The pack closes the month with 100 menus served, the figure the result is projected on.

Each course has its own recipe costing, and what decides how much the course costs is not the cost of a single dish but the weight of each option in what actually gets ordered: the mix. The exercise compares three splits of that mix at the same selling price and the same costs: a base mix, the one observed in the dining room, and two scenarios that shift demand inside the menu itself. Scenario A shifts it toward the higher-cost options; scenario B, toward the cheaper ones. That is the starting data: one price, fixed costs and three different mixes for the same options.

### The Solution, Step by Step

The first step is already settled in the statement: the reference is the $13.18 pre-tax menu price, which is what everything that follows is measured on, never the $14.50 the guest pays at the register (that figure only adds the illustrative sales tax; if your market prints tax-inclusive prices, divide the tax out first).

The second step is the average cost of each course, calculated by adding up the cost of each option multiplied by its weight in the mix: if an option is ordered more often, it weighs more in the average; if almost nobody picks it, it barely moves the number even if it is the most expensive. You repeat this course by course, once for each of the three splits.

The third step adds up the average costs of all the courses and adds the fixed cost per menu, which gives the total cost of the menu in each scenario: $5.63 with the base mix, $5.93 in scenario A and $5.35 in scenario B. Three different menu costs for the same selling price, just because what gets ordered changes.

With that total cost you solve for the last two figures: food cost, which is the total cost over the pre-tax menu price, and the margin per menu, which is the pre-tax menu price minus the total cost. The base mix leaves a food cost of 42.7% and a margin of $7.55 per menu; scenario A raises food cost to 45.0%; scenario B lowers it to 40.6%. The last step multiplies that margin by the 100 menus served per month and gives the month's margin for each split, as the table below shows: $754.93 with the base mix, $725.18 in scenario A and $782.93 in scenario B (the sheet works with unrounded margins, which is why the cents differ slightly from $7.55 × 100).

### How to Read the Result

The menu price doesn't move at any point in this exercise: the $13.18 pre-tax, $14.50 with the illustrative tax, is the same in the base mix and in both scenarios, and still the month's margin changes noticeably between the costliest split to serve and the cheapest. That is what a set menu demonstrates: the result is not decided by the printed price, it is decided by what the guest ends up choosing among the options on offer.

Put another way, the food cost of this menu is not a number you calculate once and forget: it is an average that gets recalculated every time the mix changes, and that mix moves with decisions within reach of the kitchen and the floor (the order of the options in each course, how they are described, which ones are recommended at the table), not with raising the selling price. That is why the exercise doesn't look for an acceptable margin in the abstract: it looks at the distance between scenario A and scenario B at the same price, because that distance is the lever to work before you even think about touching the menu.

**The Same Menu and the Same Price, Three Results Depending on the Mix**

| Item | Base Mix | Scenario A | Scenario B |
|---|---|---|---|
| Average Cost of First Courses ($) | $1.26 | $1.37 | $1.18 |
| Average Cost of Main Courses ($) | $3.23 | $3.39 | $3.06 |
| Average Cost of Desserts ($) | $0.59 | $0.62 | $0.56 |
| Fixed Costs per Menu ($) | $0.55 | $0.55 | $0.55 |
| Total Average Menu Cost ($) | $5.63 | $5.93 | $5.35 |
| Menu Food Cost (%) | 42.7% | 45.0% | 40.6% |
| Contribution Margin per Menu ($) | $7.55 | $7.25 | $7.83 |
| Margin on Menus Served per Month ($) | $754.93 | $725.18 | $782.93 |


---


---

## About the Author and Terms of Use

John Guerrero is CEO of AI Chef Pro and founder of ChefBusiness Group. He has worked in kitchens since he was 17 and has been a hospitality consultant since 2010, advising on the opening of more than 200 venues, including MICHELIN-starred restaurants in Spain and across Europe. More about his work at johnguerrero.es.

**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide · info@aichef.pro**

*This guide is a professional working document, not tax, legal or accounting advice. The tax rates it mentions are illustrative and sit in editable cells of the spreadsheets precisely because they change: if the rate changes, you change the cell and the whole workbook recalculates. The costs, menu prices, margins and percentages are example values taken from the eight Excel templates that come with this pack, and they are there for you to replace with your own: none of them is a forecast of your results or a pricing recommendation. How a specific transaction is classified for tax purposes, such as what counts as a restaurant service versus a sale of goods, or which rate applies to a given product, depends on the facts of that transaction. Before you change your menu, the price of a dish or the tax rate you charge, check with your accountant or tax advisor.*
