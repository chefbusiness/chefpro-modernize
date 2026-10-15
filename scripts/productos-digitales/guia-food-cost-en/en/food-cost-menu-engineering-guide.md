# Food Cost + Menu Engineering Guide

**Recipe costing, menu pricing and menu profitability · US edition 2026**

*John Guerrero · AI Chef Pro · aichef.pro*

20 chapters, 8 Excel tools with live formulas and a bonus of 12 solved exercises to cost out your menu, put the right price on it and find out which dish pays the bills and which one quietly drains the register. This is not an opening guide: it is written for people who already serve every day. It is the US edition, with notes for operators in the UK, Canada and Australia wherever the rules differ. Every number you will read comes from the workbooks in this same pack, so the text and the spreadsheets always say the same thing; when you change a figure in Excel, the logic this document explains stays yours.

**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide**

---

## Table of Contents

1. **Who This Guide Is For (and What You Will Not Find Here)** — where we assume you start, a map from problem to chapter to tool, and the starter glossary.
2. **The Four Numbers That Run Your Menu** — food cost, contribution margin, prime cost and average check: which one rules each decision.
3. **Sales Tax, VAT and the Error That Breaks Your Food Cost %** — the tax matrix by channel and product type, and why the percentage is always calculated on net sales.
4. **The Real Purchase Cost: What Actually Belongs on the Invoice Line** — how tax shows up on a supplier invoice, which lines carry it and why recoverable input tax is not a cost.
5. **From AP to EP: Trim Loss, Yield and the Test That Replaces the Chart** — butchering, cooking and byproducts: how to measure your own trim loss and what a clean pound really costs you.
6. **The Recipe Cost Card That Survives an Audit** — edible quantity, trim loss, as-purchased quantity, plate cost and target price, line by line.
7. **Theoretical vs. Actual Food Cost: Where the Money Leaks** — actual usage from opening inventory, purchases and closing inventory, and the four causes of variance.
8. **Prime Cost: The Metric That Measures the Health of the Business** — product plus labor in a single number, with the 65% threshold and the 55% one for the bar.
9. **Four Ways to Price a Dish** — cost multiplier, target dollar margin, market price and perceived value.
10. **Pricing Psychology: What Is Proven and What Is Myth** — the decoy effect, descriptive names and price formatting, each with its study and its caveat.
11. **Menu Engineering I: Kasavana & Smith Done Right** — popularity by margin, the 70% rule split by category and what to do with each quadrant.
12. **Menu Engineering II: What the Classic Matrix Can't See** — Miller, Pavesic, Goal Value and LeBruto: three variables and no single method that measures them all.
13. **When the Methods Disagree: The Decision Protocol** — reading the four results at once, understanding the disagreement and choosing between reworking, repricing, redesigning or removing.
14. **Short Menus, Prix Fixe, Buffets and Banquets** — when the price is already set and the mix decides the margin: prix fixe lunch, buffet, hotel and catering.
15. **Multichannel: Dine-In, Takeout and Third-Party Delivery** — commission, packaging, tax by channel and price ceiling: how much to raise in each channel and which dish to leave out.
16. **Beverage Cost: The Bar as a P&L of Its Own** — glass versus bottle, draft, cocktails and tax by channel: the bar has its own targets.
17. **Batch Costing for Commissary Kitchens and Pastry** — batch yield, labor per hour, packaging and scaling: why the portion is not the unit.
18. **When Your Supplier Raises Prices: The Re-Costing Protocol** — triggers, calendar, where to look for prices and how to raise yours without losing the guest.
19. **The Full Case: One Entire Menu, Start to Finish** — the sample menu walked end to end: cost card, matrix, pricing, multichannel and 90-day plan.
20. **When Your Spreadsheet Falls Short** — the criteria for jumping from the spreadsheet to software and AI agents, with the math in front of you.

---

## 1. Who This Guide Is For (and What You Will Not Find Here)

### What We Assume You Know and What We Don't

This guide starts where other guides stop: the menu is already printed, the doors are open and your food cost is giving you a number you don't trust. You will not find a single line here about permits, build-out, startup costs or business plans. If that is what you need, you need a different resource; if you already operate and want to understand why your contribution margin doesn't add up, keep reading.

We assume you know what a recipe card is, that you have heard of recipe costing (working out what each dish costs to make) and that you understand a percentage of sales. What we do not assume is judgment: when that percentage is an alarm bell, which analysis tool fits which symptom, and how to make a menu decision with data in hand instead of gut feeling. That is what this document adds.

The pack comes in two pieces with different jobs. The Food Cost Kit Pro holds the templates by business format and the daily control system: that is where the recipe cards, yields and purchase tracking live. This guide brings the decision framework and the eight menu analysis tools. If you own both, you are not doing the same work twice: each one solves a different layer of the problem, and the cross-references between them are flagged throughout the text so the jump is immediate.

The common thread through every chapter is a sample menu that appears in all eight workbooks of the pack. It is a modeled case, not a real client or an identifiable business: the data is consistent from one file to the next and calibrated so the tools show representative situations, not ideal ones. That menu has 20 dishes, sells 4,870 units a month and generates $59,029 in net sales over the reference period, with a weighted average food cost of 32.7%. Those numbers live in the "Data" sheet of menu-engineering-matrix.xlsx and they are the same ones you will see in every analysis: if the figure in the text and the figure in the sheet ever disagree, the sheet wins.

The pack works with a 30% food cost target, in line with the 25% to 35% range of sales that is commonly cited as healthy for restaurants, and with a 65% prime cost target, which is the active setting in the "Inputs" sheet of prime-cost-dashboard.xlsx. Those two thresholds are the starting point for every exercise; you can adjust them to your reality, and the dashboard is built to absorb that change without breaking a single formula.

A quick vocabulary note for readers outside the US, which is the only time the parenthetical will appear: the guide is written in US English, so you will read "takeout" (UK and Australia: takeaway), "prix fixe lunch" (UK: set menu), "POS" for the till system, and "food cost %" for the share of sales that goes to ingredients. If you work in pounds sterling or Canadian or Australian dollars, the logic does not change, and in the UK that same share is usually called GP % (gross profit, which is 100% minus food cost %). The rest of the time, a menu is a menu.

---

### Your Problem, Its Chapter and Its Tool

The fastest way into this guide is not page one but your symptom. The weighted average food cost of the sample menu is 32.7%, two and seven tenths of a point above the 30% target set in the "Cost Card" sheet of recipe-cost-card.xlsx. That gap can come from very different places: a star dish whose cost has shot up, a family of dishes dragging the average higher, a selling price nobody has revisited, or a mix of all three. Every cause has its tool, and every tool has its chapter.

The table below lays out that correspondence: the real problem in the first column, the chapter that covers it in the second, the file in the pack that solves it in the third. It is not a table of contents; it is an entry map for people who already know where it hurts and don't want to read what they don't need.

Some symptoms this guide does not cover because they belong to another layer of the business. The full cost structure of a restaurant, using the reference ranges the pack works with, puts labor in the 30% to 35% range of sales, rent between 5% and 10%, and overhead at an ideal close to 17%, which leaves a healthy EBITDA in the 10% to 13% band. Prime cost, which is product plus labor, is the first indicator of whether that structure is in balance, and that is why the pack's dashboard watches it against the 65% target. But labor cost, rent and overhead sit outside the scope of this guide: here we work on product and menu, which is where the operator has the most immediate room to maneuver and where menu engineering decisions show up in the next purchasing cycle.

What you will not find here, stated plainly: there is no step-by-step supplier negotiation (that material is in the Food Cost Kit Pro bonus, and we will point you to it when the time comes), there is no profitability analysis by shift or by sales channel, and there is no twelve-month projection built on the sample menu's data. The figures in the text are the ones in the sheets; you do the math with your own numbers, not with extrapolations from a modeled case.

### What This Guide Does and What the Food Cost Kit Pro Does

The starting point of this document is a menu that is already being served. There is not a paragraph here about permits, build-out, startup costs or business plans: if you need those, look for another tool. What there is, is a method for reading what that menu is doing with your money and for making decisions about it with judgment instead of intuition.

The division of labor inside the pack is precise, and it is worth understanding before you open any file. The Food Cost Kit Pro supplies the templates by business format (full-service restaurant, bar, institutional catering, delivery) and the daily control system: recipe cards, trim loss sheets, purchase log and a variance tracking dashboard. This guide supplies something else: the decision framework and the eight menu analysis tools that tell you which dishes carry the business, which ones weigh it down and which levers to pull first. If you have both, you don't duplicate work: the Kit produces the data and this guide interprets it.

The target food cost the pack works with is 30%, a figure that sits in the middle of the 25% to 35% range of sales commonly cited as healthy. The reference cost structure for a restaurant behind it looks like this: product around 30%, labor and integrated service between 30% and 35%, rent between 5% and 10%, and overhead between 13% and 20% of sales, which leaves a healthy EBITDA of between 10% and 13%; below 10%, the business needs restructuring. Inside that architecture, prime cost (product plus labor) is the indicator that concentrates most of the management effort, and the target the dashboard in the pack works with is 65%, set in the "Inputs" sheet of prime-cost-dashboard.xlsx.

The sample menu that runs through the whole pack is a modeled case, not a real client. It has 20 dishes, sells 4,870 units a month and closes the period with $59,029 in net sales and a weighted average food cost of 32.7%. Those numbers are in the "Data" sheet of menu-engineering-matrix.xlsx and they are the same in all eight workbooks: what changes from tool to tool is the angle from which that menu is analyzed, not the starting data. Always working on the same case lets you compare results across methods without losing the thread, and it lets you see clearly which decision changes when a single parameter changes. The opening-costs sheet of the Restaurant Financial Plan Kit Pro is not part of this pack: it is mentioned here only to make clear that it is not included, because it is the opening tool and this document starts where that one ends.

The table below collects, for each concrete problem you might bring, the chapter that covers it and the tool in the pack that solves it. Read it before moving on, because it marks the shortest path for wherever you are starting from.

---

### What We Call Things Here

This document is written in US English and uses trade terms the way they are used on the line and in the dining room. When the UK, Canada or Australia says something differently, the equivalent is given the first time it appears, and from then on the US form is used.

Recipe costing is the card that breaks a dish down into ingredients, as-purchased quantities, trim losses and the resulting unit cost. From here on, "recipe cost card" and "plate cost" are the forms used throughout the document. The menu is the full set of dishes the house offers for sale; "prix fixe menu" is reserved for the fixed-price format, which is a different way of selling with its own costing logic. "Dish" means any item on the menu, whether it is a starter, a main, a dessert or a bar preparation.

The terms we keep in English are the ones the trade has adopted without a clear substitute: food cost, prime cost, labor cost, beverage cost, third-party delivery, takeout and packaging. Likewise, "contribution margin" and "menu engineering" stay as they are, because they are the forms you will find in industry reports and in the foodservice courses you may already know, and the names of the classic methods (Kasavana & Smith, Miller, Pavesic, Goal Value) are never translated or altered.

The table that follows details which workbook in the pack solves each problem, with the exact file name and the sheet where the work starts.

**Your Problem, the Chapter That Covers It and the Tool That Solves It**

| If your problem is… | Chapter | Tool in the pack |
|---|---|---|
| I don't know if my food cost is calculated correctly | 3 and 4 | recipe-cost-card.xlsx |
| I buy a lot and don't know how much reaches the plate | 5 | yield-and-trim-loss.xlsx |
| I have to rebuild a dish's recipe card | 6 | recipe-cost-card.xlsx |
| My actual food cost doesn't match the theoretical | 7 | prime-cost-dashboard.xlsx |
| I sell a lot and don't make money | 8 | prime-cost-dashboard.xlsx |
| I don't know what price to put on a new dish | 9 and 10 | menu-pricing-calculator.xlsx |
| I don't know which dish to cut from the menu | 11, 12 and 13 | menu-engineering-matrix.xlsx |
| I want to build a prix fixe menu | 14 | menu-engineering-matrix.xlsx |
| Delivery leaves me less than it looks like | 15 | multichannel-repricing-simulator.xlsx |
| I don't know if the bar makes or loses money | 16 | beverage-cost-menu.xlsx |
| My supplier raised prices and I don't know what to adjust | 18 | menu-pricing-calculator.xlsx |
| I have the diagnosis and I'm not acting on it | 19 and 20 | 90-day-action-plan.xlsx |

*All eight workbooks share the same sample menu, so you can jump to the chapter that interests you without losing the thread of the numbers.*


---

## 2. The Four Numbers That Run Your Menu

### Food Cost Percentage: What It Measures and What It Doesn't

Food cost percentage measures the share of the net selling price that goes to raw materials. That is all it measures. It does not measure how many dollars hit the register, it does not measure whether your kitchen takes twenty minutes to make that dish, and it does not measure whether the dish sells ten times a month or two hundred. Confusing what it measures with what it decides is the most expensive mistake you can make when reviewing a menu.

The healthy range for restaurants is commonly cited at 25% to 35% of sales, with a market average around 30%. That range is not universal: the starting point changes with the format. Traditional full-service restaurants usually run between 28% and 32%, a small-plates bar between 28% and 35%, a pizzeria between 25% and 30%, a coffee shop between 20% and 28%, and fine dining can drop to 20-25% precisely because the high check absorbs the fixed cost per cover. None of those ranges is a goal in itself: they are references to tell you whether something deserves a second look.

The sample menu in the pack closes the month with a weighted average food cost of 32.7%, which is inside the healthy range. That 32.7% comes from the "Data" sheet of menu-engineering-matrix.xlsx and is calculated on the 4,870 units sold in the month, not on the simple average of the dishes on the menu. The simple average gives you a number that doesn't exist in the reality of the business: if a dish with a 40% food cost sells three times and another with a 28% food cost sells four hundred, the arithmetic average of the two percentages describes nothing that ever happened in that kitchen. Only weighting by units sold produces a figure you can compare with the month's $59,029 in net sales.

The percentage ranks the menu, helps you spot dishes with runaway cost and serves as an argument in supplier negotiations. But it does not pay a single bill. For that you need the next number.

### Contribution Margin: The Dollars That Land in the Register

A dish's contribution margin is what is left of its selling price once the raw material cost is subtracted. It is not profit: it has not yet paid for a single hour of labor, or the rent, or the electricity. It is the gross dollar that dish contributes to cover the rest of the structure. That distinction matters every time someone proposes pulling a dish because it "has a high food cost."

The thesis that governs this chapter is direct: the percentage ranks, the dollar pays. A dish with a 20% food cost that generates few dollars per unit can be a worse business than one with a high food cost that leaves many dollars per cover, as long as it sells often enough. A low percentage does not make up for a skimpy contribution margin multiplied by few units.

In the sample menu, the weighted average contribution margin is $8.16 per unit sold, also calculated on the month's 4,870 units, in the same "Data" sheet of menu-engineering-matrix.xlsx. Multiplying that margin by the units sold is not something you need to do here: the totals are already in the workbook. What is worth fixing in your mind is the criterion: when you evaluate whether a dish stays or leaves the menu, the variable that rules is contribution margin, not food cost. A dish that sells a lot and leaves a solid contribution margin holds up the books even if its cost percentage is above average. Pulling it because of the percentage, without looking at the dollars, is a diagnostic error.

The table below shows the monthly breakdown of the sample menu with both numbers by dish family.

### Prime Cost: Product and Labor on the Same Line

Prime cost adds up raw material cost and labor cost and expresses them together over sales. It is the number that keeps you from fooling yourself, because it captures the most common shell game in the kitchen: lowering food cost by increasing prep work. A restaurant that swaps a semi-prepared product for raw product can cut its raw material cost by several points and watch that saving reappear in full on the payroll, in overtime or in the need for an extra cook. Food cost improves on paper; prime cost doesn't move, or gets worse.

The reference structure puts labor cost between 30% and 35% of sales when service is integrated, with product cost around 30%, which places prime cost in a band that leaves room for rent, overhead and a healthy EBITDA of between 10% and 13%. Below 10% EBITDA, the structure needs review.

In the pack's dashboard, the "Monthly" sheet of prime-cost-dashboard.xlsx collects the whole year: net sales of $1,232,200, raw material cost over sales of 32.1%, labor cost of 31.3% and a resulting prime cost of 63.4%. The margin left after that prime cost is $451,142, which is the starting point for covering rent, utilities, overhead and whatever finally remains as operating income. The monthly dashboard with the detail of each line appears in the table below.

The usage rule for the three numbers is as follows. To decide whether a dish is pulled or kept on the menu, contribution margin rules: the dollars per unit sold and that dish's sales volume. To negotiate with suppliers or review trim loss and portions, food cost rules: the percentage gives you the argument and sets the target of the negotiation. To know whether the business as a whole can carry the cost structure it has, prime cost rules: it is the only number that puts product and labor on the same line and makes the shift between the two visible.

### Average Check and Margin per Cover

The percentage ranks; the dollar pays. That is the tension running through any menu that has gone a while without a review, and understanding it changes the criteria you use for pricing decisions.

Take the sample menu in the pack. The weighted average food cost is 32.7% ("Data" sheet of menu-engineering-matrix.xlsx), a number that, set against the industry reference, sits at the upper end of the healthy 25-35% range. Someone might read that 32.7% and conclude the menu has a problem. The table below will show that the right reading is more nuanced.

The weighted average contribution margin of that same menu is $8.16 per unit sold. Over 4,870 units a month and $59,029 in net sales, that margin is what funds everything that comes after: labor, rent, utilities and profit. Note that contribution margin has not paid any of those items yet; it is the starting point, not the result.

Now the edge case that justifies the thesis. A dish with a 20% food cost on a low selling price can leave fewer dollars per cover than a dish with a 34% food cost on a high selling price. The first one's percentage is "cleaner" on paper, but the second puts more absolute margin into the register every time it leaves the kitchen. If you decide by looking only at the percentage, you can end up pulling exactly the dish that contributes most to covering the fixed costs.

The pre-tax average check in the starting month of the 90-day plan is $27.40 ("Tracking KPIs" sheet of 90-day-action-plan.xlsx) and the contribution margin per cover at that same point is $18.10. Those two numbers are read together: the first says how much the house takes in per guest; the second, how much is left available to cover the structure before the guest pays the check and walks out.

The weighted average contribution margin and the weighted average food cost of the menu are always calculated on the units actually sold, not on the simple average of the dishes on the menu. The simple average gives the same weight to a dish that sells three times a day as to one that sells three times a month, and it produces a number that corresponds to no operating reality. The "Data" sheet of menu-engineering-matrix.xlsx applies the weighting by units: the result is the 32.7% and the $8.16 cited here, and they are the only ones that make sense for making decisions.

---

### Which One Rules Each Decision

Prime cost is the number that stops the most common form of self-deception in the kitchen: cutting food cost by adding prep work. When a semi-prepared product is replaced by raw ingredients, the cost of goods goes down, but prep time goes up, and that shows up on the payroll. The saving doesn't disappear; it moves from one line to another. Prime cost catches it because it adds food cost and labor cost into a single indicator.

In the sample menu, the raw material cost over the year's sales is 32.1% and labor cost is 31.3%, which gives a prime cost of 63.4% ("Monthly" sheet of prime-cost-dashboard.xlsx). On annual net sales of $1,232,200, the margin after prime cost is $451,142. That margin has to cover rent, utilities and overhead and still leave an operating profit. The reference structure the pack works with puts product around 30%, labor between 30% and 35% and overhead at an ideal near 17%, with a healthy EBITDA of between 10% and 13%; below that threshold, the business needs restructuring. The table below lets you read month by month whether prime cost is staying in the control zone or whether either of its two legs is drifting.

The food cost range varies by format. Fine dining usually works between 20% and 25%, traditional full-service between 28% and 32%, a small-plates bar between 28% and 35%, a pizzeria between 25% and 30% and a coffee shop between 20% and 28%. Those ranges are indicative and depend on the check, the level of preparation and the real sales mix, not on the printed menu.

The rule of use works out like this:

- To decide whether a dish is pulled or kept on the menu, contribution margin rules: it is the only indicator that measures what that dish contributes in real dollars every time it sells.
- To go negotiate with a supplier, food cost rules: it is the percentage that reflects the weight of that raw material on sales and the one that justifies, or doesn't, a bigger purchase volume in exchange for a lower price.
- To know whether the business can carry its cost structure, prime cost rules: it is the sum of the two largest controllable lines and the first indicator to deteriorate when something goes wrong in the kitchen or on the floor.

None of the three numbers is dispensable, and none replaces the other two.

**The Monthly Dashboard: Food Cost, Labor Cost and Prime Cost (prime-cost-dashboard.xlsx, "Monthly" Sheet)**

| Month | Net Sales ($) | Food Cost (%) | Labor Cost (%) | Prime Cost (%) | Target (%) | Reading |
|---|---|---|---|---|---|---|
| January | $89,600 | 31.7% | 33.5% | 65.2% | 65.0% | Above target |
| February | $84,100 | 32.5% | 35.6% | 68.0% | 65.0% | Above target |
| March | $95,200 | 31.8% | 32.5% | 64.3% | 65.0% | On target |
| April | $100,400 | 31.6% | 31.1% | 62.7% | 65.0% | On target |
| May | $107,900 | 31.7% | 29.9% | 61.6% | 65.0% | On target |
| June | $110,700 | 34.7% | 30.4% | 65.1% | 65.0% | Above target |
| July | $116,200 | 32.4% | 29.8% | 62.3% | 65.0% | On target |
| August | $99,600 | 35.2% | 34.7% | 69.9% | 65.0% | Above target |
| September | $105,500 | 30.1% | 30.3% | 60.4% | 65.0% | On target |
| October | $102,700 | 31.3% | 30.4% | 61.7% | 65.0% | On target |
| November | $97,900 | 30.6% | 31.6% | 62.2% | 65.0% | On target |
| December | $122,400 | 31.4% | 28.1% | 59.5% | 65.0% | On target |
| TOTAL / AVERAGE | $1,232,200 | 32.1% | 31.3% | 63.4% | 65.0% | On target |

*The last row is the year's total and its percentages are weighted, not the average of the twelve months: a weak month counts for what it sells, not for one twelfth.*

**The Three Families on the Sample Menu (menu-engineering-matrix.xlsx, "Data" Sheet)**

| Family | Dishes | Units Sold | Share of Menu Mix (%) | Weighted Avg. Contribution Margin ($) | Weighted Avg. Food Cost (%) | Net Sales for the Month ($) |
|---|---|---|---|---|---|---|
| Starters | 7 | 1,730 | 35.5% | $7.46 | 30.7% | $18,636 |
| Mains | 9 | 2,020 | 41.5% | $10.80 | 35.6% | $33,854 |
| Desserts | 4 | 1,120 | 23.0% | $4.48 | 23.2% | $6,539 |


---
## 3. Sales Tax, VAT and the Error That Breaks Your Food Cost %

### Which Number Your Food Cost % Is Calculated On

Recipe costing always works on the price net of tax, never on what the guest ends up paying. In the US that sounds obvious, because the menu is printed before tax and the sales tax only appears on the check. The mistake creeps in later, when someone pulls a sales figure that already has the tax inside it and divides the plate cost by it. The result is a food cost % lower than the real one, and that's the worst direction an error can take, because it tells you the dish is doing better than it is.

The "Cost Card" sheet of recipe-cost-card.xlsx shows it precisely. The plate cost of the dish is $5.67 and its menu price is $17.30, before tax. Now add sales tax at a round 10% for the example (your real rate is your state rate plus your county and city rates, and some places add a meals tax on top): the guest pays $19.03, and $1.73 of that is sales tax. The real food cost of the dish, calculated on the $17.30 menu price, is 32.8%. Divide by $19.03 instead and the percentage drops to 29.8%: three points better on paper without anything having improved in the kitchen. That $1.73 was never yours. You collect it for your state and pay it over, so it isn't sales and it never belongs in a ratio.

There's a second error that shows up less often but bends the number just as much, and it sits on the cost side: getting the tax on your purchases wrong. Suppose the invoices behind this card's ingredients carried $0.56 of tax in total. In the US there's nothing to get back, because sales tax you pay on supplies is a cost of doing business: if you really paid that $0.56, the plate really costs $6.23 and its food cost really is 36.0%. In the UK, Canada and Australia it depends on registration. A business registered for VAT, GST or HST reclaims the tax on its purchases, so that tax isn't a cost of the plate, and adding it would push the cost to $6.23 and the food cost to 36.0%, 3.2 points above the real 32.8%. Three points of food cost aren't a detail: they're wrong menu decisions, price increases nobody needed, or dishes cut that were actually making money. The contribution margin of the dish at today's menu price is $11.63, and that figure is only reliable if the cost and the price are both stated the right way.

The rule fits on one line: the price net of tax in the denominator, and in the numerator everything you pay and can't get back.

### The Tax Matrix: Three Channels by Three Product Types

Tax on what you sell is where the US, the UK, Canada and Australia differ most, and a workbook set up with the wrong logic will mislead you. In the US there's no national sales tax: each state sets its own rate, and counties and cities add theirs. Restaurant and bar sales are usually taxed at the combined state and local rate, and some states and cities add a meals tax, so check yours. Canada works the same way at the table: menu prices are usually shown before tax and the tax is added on the bill. Federal GST is 5%, participating provinces charge one combined HST rate instead, and other provinces may add their own tax (PST, or the QST in Quebec); how that provincial tax treats restaurant meals depends on the province.

The UK and Australia work the other way around. In the UK, printed prices must include VAT, and the standard rate is 20%. In Australia, GST of 10% applies to restaurant meals and the prices on the menu include it. In both countries the number on the menu is not your sales: your sales are what's left once you take the tax out.

The UK is also the clearest case of a rate that changes with the channel. Food and drink consumed on the premises and hot takeaway food pay the 20% standard rate; most cold takeaway food is zero-rated, but not soft drinks, confectionery or crisps. That's why the "Inputs" sheet of multichannel-repricing-simulator.xlsx doesn't hold one tax rate but nine: three channels (dine-in, takeout and third-party delivery) by three product types (food, soft or sweetened drinks, and alcoholic drinks). The table at the end of this chapter shows them as they ship.

The operational consequence is immediate. If your delivery menu copies the dine-in menu without adjusting prices, the margin per channel isn't the same. In a country where the printed price includes the tax, the net price behind the same printed figure moves with the rate each channel carries. In the US, where the menu is pre-tax, the gap between channels comes from elsewhere (packaging, platform commissions), and the multichannel chapter works it through with the repricing simulator. Either way, the starting point is having the right rate in each cell. That's why the rates sit in editable cells with a note on the "Inputs" sheet, and the workbook's formulas read them with INDEX and MATCH: if a rate changes tomorrow, you change the value in that one cell and the whole workbook recalculates without touching a single formula.

### Dine-In: The Guest's Check Is Not Your Sales

The error that distorts food cost the most isn't in the recipe costing: it happens earlier, in the denominator. In dine-in, the guest's check is your menu prices plus the sales tax plus the tip. Divide the plate cost by that total and you get a percentage lower than the real one, and that's the worst direction for the error to run, because it makes you believe the margin holds when it doesn't. Food cost is always calculated on the price before tax, which in the US is simply the price printed on your menu.

The danger zone is the POS report. Your POS gives you more than one "sales" number, and the biggest one (total collected, total payments, whatever your system calls it) has the sales tax and the tips inside it. Before you divide anything, find the line that excludes both: net sales, after discounts and before tax and tips. Tips never count as sales. A mandatory service charge is a different animal: in the US it's revenue that you then pay out as wages, so book it on its own line and keep it out of food sales. The "Cost Card" sheet of recipe-cost-card.xlsx carries the dish this guide keeps coming back to: a plate cost of $5.67 against a menu price of $17.30 gives a real food cost of 32.8%. If you divided by the $19.03 the guest pays at a 10% sales tax, the percentage would drop and give you an artificially comfortable reading. The table at the end of this chapter shows how much that comfort can cost.

In the UK, dine-in has its own logic, and it covers the whole check: food and drink consumed on the premises pay the same 20% standard rate. The glass of wine, the gin and tonic and the draft beer carry exactly the same VAT as the main course. Because the printed price includes that VAT, you take it out before any ratio: net price = printed price ÷ 1.20. The same dish, printed at 20.76 in a UK pub, nets 20.76 ÷ 1.20 = 17.30. In Australia, GST is one eleventh of the printed price: a menu showing 19.03 carries 1.73 of GST and a net price of 17.30. Same dish, same net price, three different printed numbers.

The contribution margin of the dish at today's menu price is $11.63, calculated on the $17.30 net price. That's the figure that feeds menu engineering. A margin calculated on the price with tax in it would look $1.73 bigger in the US (the guest's $19.03 minus the $5.67 plate cost is $13.36) and would lead to the wrong menu decisions.

### Takeout and Delivery: Where the Rate Can Change

When the food leaves the dining room, the tax question changes, and how much it changes depends on where you are. In the US the rate on a takeout or third-party delivery order is whatever your state and city apply, and some states and cities add a meals tax, so check whether your takeout rate matches your dine-in rate instead of assuming it. In Canada, how provincial tax treats restaurant meals depends on the province: check that too.

In the UK the line is drawn by law between food eaten on the premises and food taken away, and a delivery order is food that leaves the premises too. Two things decide the rate of a takeaway item:

- Hot takeaway food stays at the 20% standard rate, exactly as if it were eaten at the table.
- Most cold takeaway food is zero-rated, but the exceptions matter: soft drinks, confectionery and crisps are not zero-rated. The can of cola that goes out with a zero-rated cold item doesn't follow it to 0%.

Here's what that does to a margin. Take a cold item printed at 6.00 that qualifies as zero-rated cold takeaway food, with a plate cost of 1.80. Eaten on the premises, it nets 6.00 ÷ 1.20 = 5.00 and runs a 36.0% food cost. Taken away, there's no VAT to take out, it nets the full 6.00 and runs 30.0%. Same item, same printed price, six points of food cost apart. The "Inputs" sheet of multichannel-repricing-simulator.xlsx holds the three channels and the three product types in editable cells with a note, and every price and margin in the workbook reads its rate from there, so a UK site sets the takeout and delivery rows once and the whole simulator follows.

The practical upshot in a VAT or GST country: if the delivery menu is the same as the dine-in menu, the margin per channel isn't the same, because the tax inside each printed price changes the net price your food cost is calculated on. How to build different prices per channel without breaking the guest's sense of value is the problem the multichannel chapter takes on.

### The Same Dish With and Without Tax: How Many Points You're Making Up

Food cost is the plate cost divided by the price net of tax. Divide it by a price with the tax inside and the result comes out lower than the real one, and that's the worst direction the error can take: it makes you believe the dish is doing better than it is.

Take the card on the "Cost Card" sheet of recipe-cost-card.xlsx. The plate cost is $5.67. The menu price before tax is $17.30. The real food cost of the dish at that price is 32.8%. So far, so good. The error appears when someone takes the price with tax and uses it as the denominator without stripping the tax out. In the US, at a 10% sales tax, that's the guest's $19.03, and the food cost shows 29.8%: three points you made up. In the UK the error is bigger, because the tax is too: the printed 20.76 gives 27.3% instead of 32.8%, five and a half points that don't exist. Turned into GP %, the figure UK kitchens use, the dish looks like a 72.7% GP when it really runs 67.2%. In Australia, the printed 19.03 gives the same false 29.8% as the US check. The difference isn't cosmetic; it's the distance between a well-founded decision and a badly calibrated menu.

The second error, on the cost side, is getting the tax on the ingredients wrong. With the same example as before, $0.56 of tax on this card's purchases would take the apparent plate cost to $6.23, and dividing that by the $17.30 net price gives a food cost of 36.0%, 3.2 points above 32.8%. In the US, if that tax was really charged and paid, 36.0% is the truth, because there's nothing to reclaim. For a business registered for VAT or GST/HST, the tax on purchases isn't a cost: it comes back on the return, and including it in the recipe costing double-counts money the tax authority gives back to you. The second table at the end of this chapter shows both readings side by side so the difference leaves no room for doubt.

The contribution margin of the dish at today's menu price is $11.63. That's the figure that feeds menu engineering: if the food cost denominator has tax in it, the contribution margin is distorted too, and the classification of your dishes in the menu engineering matrix loses its reliability.

### Why the Tax Rate Lives in a Cell, Not Inside the Formula

The tax map of a restaurant isn't flat, and it isn't the same in two cities. In the US, the rate on your sales is set by your state plus your county and city, some places add a meals tax, and rates change. In the UK, the 20% standard rate covers everything consumed on the premises, alcohol included: the glass of wine and the draft beer carry the same rate as the main course.

Outside the dining room, the picture changes. In the UK, takeaway splits between hot food at the 20% standard rate and most cold food at zero, with soft drinks, confectionery and crisps left out of the zero rate. In Canada, the GST or HST sits on top of the menu price as it does in the US, and how provincial tax treats restaurant meals depends on the province. In Australia, a 10% GST applies to restaurant meals and is already included in every price on the menu.

One workbook has to work for all four, and the only way to do that honestly is to keep the rates out of the formulas. The table below shows the rates by channel and product type as they're set up on the "Inputs" sheet of multichannel-repricing-simulator.xlsx: dine-in food, dine-in soft drinks and dine-in alcohol; the same three for takeout; and the same three for third-party delivery. They ship at 0%, the US default, so the simulator works on pre-tax menu prices, which is exactly how a US menu is printed. A UK pub types 20% and 0% where they apply; an Australian cafe types 10%.

Those values live in editable cells with a source note, and the workbook's formulas read them with INDEX and MATCH. If a rate changes tomorrow, you change the value in the matching cell of the "Inputs" sheet and the whole workbook recalculates without touching a single formula. Writing the rate inside the formula, on the other hand, forces you to hunt down every calculation that uses it, and in a workbook with recipe cost cards, repricing and margin simulation by channel, that manual hunt is where the silent error starts.

**The Tax Matrix: Channel by Product Type (multichannel-repricing-simulator.xlsx, "Inputs" sheet)**

| Channel | Food | Soft drink or sweetened drink | Alcoholic drink |
|---|---|---|---|
| Dine-in | 0.0% | 0.0% | 0.0% |
| Takeout | 0.0% | 0.0% | 0.0% |
| Third-party delivery | 0.0% | 0.0% | 0.0% |

*All nine cells are editable and ship at 0%, the US default: the simulator then works on pre-tax menu prices. In Canada, leave them at 0% and price before tax as in the US. In the UK, type 20% for dine-in and hot takeaway food and 0% where your cold takeaway food is zero-rated (soft drinks, confectionery and crisps are not); each channel has one food cell, so if your takeaway mixes hot and cold food, use the rate that covers most of it. In Australia, type 10%.*

**Tax on Purchases: When It's a Cost and When It Isn't (worked example on the "Cost Card" sheet, recipe-cost-card.xlsx)**

| Item | Value |
|---|---|
| Tax on this card's ingredients, example ($) | $0.56 |
| Plate cost with that tax included ($) | $6.23 |
| Food cost % with that tax included — right only if you can't reclaim it | 36.0% |

*In the US, sales tax you pay on supplies is a cost: if it's on the invoice, it's in the plate cost. In the UK, Canada and Australia, a registered business gets that tax back: it's cash flow, not cost, and this card's food cost stays at 32.8%. Counting it pushes the food cost up without anyone having spent a dollar more.*


---

## 4. The Real Purchase Cost: What Actually Belongs on the Invoice Line

### Three Numbers on Every Invoice Line

When the vendor's delivery invoice arrives, every line can carry three different amounts: the line amount before tax, the tax charged on it (if any) and the line total. Which of the three is your cost comes down to a single question: do you get that tax back? In the US the answer is no. Sales tax you pay on supplies is a cost of doing business, so whatever tax a vendor charges you belongs in the cost of the line. Whether a vendor charges it on a given line depends on your state, and the rules for goods you buy to resell vary from state to state. In the UK, Canada and Australia the answer is yes, as long as you're registered: the VAT or GST/HST on your purchases comes back to you, so the cost of the line is the amount before tax.

The sample invoice on the "Invoice & Tax Check" sheet of recipe-cost-card.xlsx shows the method. Its lines add up to $768.40 before tax; at the US default of 0% the tax column shows $0.00 and the invoice total the vendor collects is $768.40. If you type the rates your supplier charged, the sheet separates the tax line by line, and for a registered business in the UK, Canada or Australia the difference between the pre-tax amounts and the invoice total is exactly what comes back on the VAT return or as input tax credits or GST credits. The table at the end of this chapter breaks the invoice down line by line.

The recipe costing rule is a single one and admits no exceptions under normal conditions: you cost from what you actually pay and can't get back. Where the tax comes back, putting it on the cost card means counting the same expense twice. The "Cost Card" sheet of recipe-cost-card.xlsx makes the point with the guide's own numbers: the plate cost before tax is $5.67, and if the card's ingredients carried $0.56 of tax, the plate cost with it would rise to $6.23. For a registered business, the right food cost of the dish is 32.8%, and counting the reclaimable tax as cost takes it to a wrong 36.0%. For a US kitchen that really paid that tax, 36.0% is the right one. That difference in percentage points isn't an accounting nuance: it's the distance between a well-calibrated price decision and a badly calibrated one.

Outside the US there's a case where the rule flips, and you want to know it before you set up the cards. If your business isn't registered for VAT or GST/HST, the tax on your purchases doesn't come back, so it becomes a real cost and goes into the recipe costing, just as in the US. Whether you're registered, or should be, is a question for your accountant: it's not a decision for the chef or the front-of-house manager, and this chapter doesn't go into the registration rules, because the thresholds change (gov.uk, the CRA's small-supplier rules and business.gov.au carry the current figures).

Packaging deserves its own paragraph because it causes confusion all the time. A delivery box, a paper cup or a paper bag isn't food: it's packaging, and it arrives on its own invoice line. Whether that line carries tax, and at what rate, can differ from the food lines, depending on your state in the US or on the rate your supplier charges in the UK, Canada or Australia. The fact that a plate of food travels inside the box doesn't turn the box into food. They're two different lines on the invoice and two different lines on the cost card. Whoever costs a delivery plate without separating the packaging from the food is mixing two different costs and distorting the plate's food cost.

---

### The Closed List: What Goes Into the Cost of an Invoice Line

Purchase cost isn't decided by feel or by broad category. There's a closed list of what can show up on a delivery invoice line, and each item on it has a fixed place. Anything that isn't on the list stays off the cost card, with no gray zone and no generous interpretation.

These are the items on that closed list:

- The pre-tax line amount, quantity times unit price: always in.
- Sales tax charged on the line in the US: in. There's nothing to reclaim, so it's part of what the product costs you.
- VAT or GST/HST you reclaim as a registered business in the UK, Canada or Australia: out. It comes back as input VAT on your VAT return, as input tax credits in Canada or as GST credits in Australia.
- VAT or GST/HST when you're not registered: in, exactly like US sales tax.
- Credits for shorted, damaged or returned items: subtracted from the line before you cost anything.
- Packaging and disposables (takeout containers, cups, bags): a cost of the takeout or delivery plate, but on their own line, never folded into the price of an ingredient.
- Cleaning supplies, smallwares and anything else that never reaches the plate: out of food cost entirely; they belong in your operating supplies.

Nothing else. The pair that trips people up is the second and third items together: the same taxed line is a cost for a restaurant in Ohio and cash flow for a VAT-registered pub in Manchester. The food, the vendor and the invoice can be identical; what changes is whether the tax comes back. And when you're not sure whether a vendor charges tax on a line or how they show it, ask the vendor how they bill it on their own invoice rather than guessing.

The moment that changes your cost cards is a change in your own situation: registering for VAT or GST/HST, a vendor that starts charging sales tax on a line it didn't tax before, a second location in a different state. It has a direct consequence on the cards: any card built under the old setup has to be reviewed so that its cost reflects what you pay now, not what you paid then. The table at the end of this chapter sums up what goes into the cost in each case, from the "Invoice & Tax Check" sheet of recipe-cost-card.xlsx.

### A Sample Delivery Invoice, Line by Line

When a vendor's invoice arrives with goods of different kinds on it, the first job is to separate the lines before you carry a single number over to the recipe cost card. The sample invoice that comes with this section, reproduced in the table below, adds up to $768.40 before tax, $0.00 of tax at the US default and an invoice total of $768.40. Those three figures come from the "Invoice & Tax Check" sheet of recipe-cost-card.xlsx, and you can check them line by line against a real invoice of your own.

The invoice mixes three kinds of goods because the vendor delivers food, beverages and packaging together. What goes into the cost from each line depends on where you are:

- **US** — the line total. The sheet ships at 0% on every line, so the line amount and the line total match. If your vendor charges sales tax on a line, type its rate there. Say the containers on line 7 came with sales tax at an illustrative 8%: the tax would be $6.08, the line total $82.08 and the invoice total $774.48. That $82.08 is what the containers cost you, because there's nothing to reclaim. Whether a line is taxed at all depends on your state, and the rules for goods bought to resell vary from state to state.

- **UK, Canada and Australia, registered** — the pre-tax line amount. Type the rate your supplier charged on each line: in the UK, lines can carry the 20% standard rate, the 5% reduced rate or the 0% zero rate; in Canada, the 5% GST or your province's HST; in Australia, 10% GST, which applies to most goods and services. The sheet shows the tax you'll reclaim and the total you pay, and the cost card takes the line from the pre-tax amount.

- **UK, Canada and Australia, not registered** — the line total, exactly as in the US: you pay the tax and nothing comes back, so it's part of the cost.

Packaging needs special attention here too. The delivery box isn't food: it's a cardboard or plastic container for carrying food, and it sits on its own line even though the plate inside it is food. The same goes for single-use cutlery, paper bags and presentation trays that aren't part of the food itself. When a vendor delivers kitchen goods and packaging on the same invoice, you get one document with different kinds of cost on it, and splitting it by category before you file it (food, beverage, packaging) is the only way to close the month without errors. That's how food cost, beverage cost and packaging each get the right number and, in VAT and GST countries, how your reclaimable tax adds up on the return.

### Reclaimable Tax Is Cash Flow, Not Cost: Where It Goes and Where It Doesn't

The recipe costing rule fits in one line: you cost from what you can't get back. For a business registered for VAT or GST/HST, the tax on purchases is reclaimed on the return, so it isn't a real cost of the business but an advance the tax authority gives back when it's offset against the tax you collect on your sales. Putting it on the cost card is counting it twice: once on the card and once on the return. In the US there's no return to offset it against: sales tax you pay on supplies is a cost, and if it's on the invoice it belongs on the card.

Run the numbers on the "Cost Card" sheet of recipe-cost-card.xlsx. The plate cost before tax is $5.67. If the tax on that plate's ingredients came to $0.56, adding it would give a plate cost of $6.23 with the tax inside. The right food cost of the dish for a registered business, calculated on the net price, is 32.8%. Start from $6.23 instead and the food cost rises to a wrong 36.0%. That difference in percentage points isn't a technicality: it shifts the price decision, the break-even point and any comparison between dishes on the menu. And if you're a US kitchen that really paid that $0.56, the reasoning flips but the discipline is the same: the cost card has to carry what you actually pay.

There is, however, a case where the reclaim no longer applies: when a business in the UK, Canada or Australia isn't registered, the tax on its purchases doesn't come back, so it becomes a real cost and goes into the recipe costing. Whether you have to register depends on your turnover against a threshold, and settling it is your accountant's job, not the cost card's. If there's any doubt about whether you can reclaim, talk to your accountant before you set up the formulas on the "Cost Card" sheet, because switching the approach halfway through the year forces you to recalculate every card you've already closed.

The table below, from the "Invoice & Tax Check" sheet of recipe-cost-card.xlsx, shows the full invoice with the tax columns broken out and the pre-tax amount of each line, so you can repeat the reading with any invoice from your regular vendor.

**What Goes Into the Cost of a Taxed Line, by Country (recipe-cost-card.xlsx, "Invoice & Tax Check" sheet)**

| Where you buy | What goes into the cost |
|---|---|
| US | The line total, tax included. Sales tax you pay on supplies is a cost: there's nothing to reclaim. Whether a vendor charges it on a given line depends on your state, and resale rules vary by state. |
| UK, Canada and Australia, registered for VAT or GST/HST | The pre-tax line amount. The tax comes back as input VAT on your VAT return (UK), input tax credits (Canada) or GST credits (Australia). |
| UK, Canada and Australia, not registered | The line total, tax included, as in the US: with nothing to reclaim, the tax is a cost. |

**A Delivery Invoice, Line by Line (recipe-cost-card.xlsx, "Invoice & Tax Check" sheet, US default)**

| # | Item | Quantity | Unit | Unit price pre-tax ($) | Line amount pre-tax ($) | Tax rate (%) | Tax ($) | Line total ($) |
|---|---|---|---|---|---|---|---|---|
| 1 | Iberico pork tenderloin | 26.46 | lb | $7.17 | $189.60 | 0% | $0.00 | $189.60 |
| 2 | Heirloom tomatoes | 44.09 | lb | $1.72 | $76.00 | 0% | $0.00 | $76.00 |
| 3 | Extra virgin olive oil | 25.0 | L | $7.20 | $180.00 | 0% | $0.00 | $180.00 |
| 4 | Aged sheep's milk cheese | 8.82 | lb | $8.39 | $74.00 | 0% | $0.00 | $74.00 |
| 5 | Red wine (750 ml bottle) | 24.0 | each | $6.10 | $146.40 | 0% | $0.00 | $146.40 |
| 6 | Cola (can) | 48.0 | each | $0.55 | $26.40 | 0% | $0.00 | $26.40 |
| 7 | Takeout containers (case) | 2.0 | case | $38.00 | $76.00 | 0% | $0.00 | $76.00 |
|  | INVOICE TOTAL |  |  |  | $768.40 |  | $0.00 | $768.40 |

*The column that goes into recipe costing is the line total in the US, where tax on supplies is a cost, and the pre-tax line amount where you reclaim VAT or GST/HST. Quantities and prices show two decimals; the sheet multiplies the unrounded values, so a hand check can differ by a few cents.*


---
## 5. From AP to EP: Trim Loss, Yield and the Test That Replaces the Chart

### The Three Losses That Aren't the Same: Trim, Cooking and Waste

Trim loss isn't an industry percentage you copy from a chart on the internet and apply to every product in the same category. It's a number that belongs to your supplier, your purchase size and the way your crew cleans. Two kitchens that receive the same whole sea bass from the same dock can get different yields depending on the size of the fish, the knife they use and how strictly they remove the skin. That means the reference chart that comes with this chapter, the one you'll find in the "My Trim Loss Table" sheet of yield-and-trim-loss.xlsx, is only a temporary starting point until you have your own measurements.

It pays to separate three things that the trade lumps under one word. Trim loss is what happens cold, on the cutting board, before the product ever meets heat: bones, skin, outer leaves, shells, peels. Cooking loss is the weight the cleaned product loses once heat is applied: the liquid a roast gives up in the oven, the shrinkage of a steak on the flat-top, a muscle contracting in the steamer. Waste is the loss that shouldn't exist and still does: product that expires, product that gets cut badly and can't be plated, product that goes in the trash because the mise en place was too big. All three eat margin, but they're managed differently and recorded at different moments.

The most common mistake in recipe costing is applying only the trim loss and forgetting the cooking loss. If a roast free-range chicken loses 28.0% of its weight in the oven (a figure from the "Cooking Loss Test" sheet of yield-and-trim-loss.xlsx) and the whole bird also has its own trim loss, anyone who applies only one of the two numbers is under-costing the dish. The average cooking loss across the tests recorded in that same sheet is 27.3%, which tells you cooking isn't a minor adjustment: in many categories it's a second loss of a size comparable to the trim loss, and it applies on top of the first one, not instead of it.

---

### The Yield Test Protocol, Step by Step

The yield test takes a scale, the same day and the real piece you buy from your usual supplier. Weighing a different size or using a sample piece won't do: the number has to come from the product that actually comes through your back door.

The procedure is three weighings of the same piece:

- Weigh the product as it arrives from the supplier, uncleaned. That's the AP weight (as purchased).
- Clean it the way your kitchen normally does and weigh the cleaned product, ready to cook. That's the EP weight (edible portion).
- Collect separately everything that has use value (heads, bones, meaty trimmings, usable outer leaves) and weigh that too. That's the weight of the usable byproduct.

Three measurements of the same piece, on the same day, written into the "Yield Test" sheet of yield-and-trim-loss.xlsx. Across the 10 products measured in that sheet, the total AP weight purchased was 69.45 lb and the total cleaned weight obtained was 42.04 lb, which gives a weighted average yield of 60.5% and a weighted average trim loss of 39.5%. The total purchase cost of those tests was $237.35.

Out of those numbers comes the figure that goes onto the recipe cost card: the Q-factor. It's the inverse of the yield, and its job is to turn the net quantity you need for one portion into the gross quantity you have to buy. If whole sea bass yields 51.7%, its Q-factor is 1 divided by 0.517. That number, which the sheet calculates automatically, is what multiplies the EP weight in the recipe to give you the purchase weight. Without it, every recipe cost card understates the quantity that really leaves the walk-in.

The net cost per clean pound of sea bass, without using the byproduct, is $13.08 ($28.84 per kg), and once you use the byproduct the gap between the AP price and the cost of a clean pound is $5.77 per lb. That gap is what disappears from your margin when recipe costing is done on the AP purchase price instead of on the cost of the clean pound. Artichoke, with a yield of 38.0%, and mussels in the shell, with a yield of 20.0%, show in the table below just how far the purchase price and the real cost in use can sit from each other.

---

### What to Do With the Byproduct: Heads, Bones and Trimmings

Using the byproduct lowers the net cost of the clean pound, but only if the use value you assign to it is real. The condition is specific: that byproduct has to replace something you were going to buy. If shrimp heads become a stock that replaces a packaged stock you would otherwise have ordered from your supplier, the saving is real and you can put a number on it. If that stock gets made because "we don't throw anything away" and then never goes into a recipe, or ends up in the trash anyway, the use value you assigned is fictional and your recipe costing is inflated.

In the tests recorded in the "Yield Test" sheet, the total use value of the byproducts comes to $5.15. That's not a trivial figure inside a $237.35 purchase lot, but it doesn't change the cost dramatically either: what it changes is precision. Sea bass with the byproduct used costs $12.53 per clean pound against $13.08 without it. The saving from using the shrimp heads is $1.43. Those amounts only hold if the kitchen has a specific recipe that consumes that byproduct on a regular basis, and if the stock or preparation that comes out of it actually replaces a purchase.

The rule for recording use value is the cost of what it replaces, not the selling price of some hypothetical dish you could make from those trimmings. If the sea bass bones go into a fish stock that replaces a purchased fish stock, the use value is the price of that purchased stock for the quantity you get. If there's no direct replacement, the use value is zero and the net cost of the clean pound is calculated with no discount.

The "My Trim Loss Table" sheet of yield-and-trim-loss.xlsx shows where your measuring stands today: 6 categories already have your own measurement and 6 categories still use the reference chart. The goal isn't to measure every category at once, but to swap the reference for your own number each time you place an order that matters, until the reference chart is just a leftover backstop and no longer the main source for your recipe costing.

### The Cost of the Clean Pound and the Q-Factor

Trim loss isn't an industry percentage: it's the result of your supplier, your purchase size and the hands of whoever does the cleaning. Two kitchens that receive the same whole sea bass on the same Tuesday can get different yields because one fillets it by machine and the other by knife, because one buys larger fish and the other works with smaller ones, or simply because the cook doing the breakdown has ten years behind him and the one next door has ten weeks. A trim loss chart copied from the internet reflects an average of conditions that aren't yours, and applying it in your recipe costing means accepting a starting error that compounds on every card.

The correct protocol takes three measurements of the same piece, on the same day. You weigh the product as it arrives from the supplier: that's the AP weight. You clean it with the kitchen's usual procedure, with no shortcuts and no special care, because what you're measuring is the real process, not the ideal one. You weigh the cleaned product, ready to portion: that's the usable EP weight. And you weigh separately everything that can be reused (heads, bones, skins, trimmings with use value), because that byproduct has an assigned cost and changes the final calculation. Without those three measurements there's no test; with two out of three you're estimating, not measuring.

The "Yield Test" sheet of yield-and-trim-loss.xlsx records the results for 10 products measured with that protocol. The total AP weight purchased in the tests was 69.45 lb; the cleaned weight obtained, 42.04 lb. The weighted average yield for that set is 60.5%, which equals a weighted average trim loss of 39.5%. The total purchase cost of the tests came to $237.35, and the use value assigned to the recovered byproducts adds up to $5.15.

Whole sea bass is the case that best illustrates the jump between purchase price and real cost. Its yield in the test is 51.7%: of every pound that comes through the back door, a little over half reaches the plate. With no byproduct used, the net cost per clean pound of sea bass is $13.08. Using the heads and bones for a stock that replaces something you would have bought, that cost drops to $12.53 per lb ($27.63 per kg). The difference between the AP price per pound and the net cost of the clean pound is $5.77: that's the extra cost that disappears from the card when you work with the purchase price instead of the real cost.

The number that travels to the recipe cost card is the Q-factor, the inverse of the yield. If the yield is 51.7%, the Q-factor is 1 divided by 0.517. That factor converts the net quantity the recipe asks for into the gross quantity you have to buy: if the portion needs 6.35 oz (180 g) of cleaned product, you multiply by the factor and get the weight you'll see on the delivery invoice. Skip that step and your recipe costing understates the cost of every plate, systematically.

The decision to use the byproduct deserves a clear rule: shrimp heads, sea bass bones or the outer leaves of an artichoke only pay off if the use value you assign to them is real. Real use value means that stock, that broth or that garnish replaces something you would otherwise buy. If the fish stock is made from the bones but the kitchen also buys packaged fish stock because the volume falls short, the saving is partial and has to be calculated that way. The shrimp heads, for example, generate a saving of $1.43 in the test: that figure is only valid if the bisque or the oil made from them replaces a real purchase, not if it gets made because "we don't throw anything away" and ends up in the bin anyway.

Cooking loss is a different number and it applies on top of trim loss, never in its place. The free-range roast chicken loses 28.0% of its weight during cooking, according to the "Cooking Loss Test" sheet of yield-and-trim-loss.xlsx; the average cooking loss across the tests recorded in that same sheet is 27.3%. Anyone who applies only trim loss is costing the clean pound before it goes into the oven, and anyone who applies only cooking loss ignores what was lost at the cutting board. The two losses are independent, measured separately and chained on the card: first you work out how much to buy to get the recipe's EP weight, then you adjust that net weight for the loss heat introduces.

### Your Trim Loss Table: When You Can Stop Using the Reference

The trim loss charts for professional kitchens that circulate in manuals and training resources are approximate by design. The ranges they list are wide precisely because they aggregate very different conditions (sizes, suppliers, techniques, receiving temperatures), and none of those ranges comes with a source that tells you which kitchens it was measured in or with what protocol. They're good for a first estimate when you have no data of your own, and for nothing else.

The table below shows the trim loss table from the "My Trim Loss Table" sheet of yield-and-trim-loss.xlsx with two separate columns: the reference range and your own measurement. Right now, 6 categories already have your own measurement and 6 categories still use the reference. That proportion is where you stand today, not the goal: every category that moves from the reference column to your own measurement narrows the margin of error in your recipe costing.

The criterion for deciding what to measure first isn't purchase volume in pounds, it's the impact on your menu's cost. Artichoke has a yield of 38.0% in the test, and mussels in the shell come in at only 20.0%: two products where the difference between using the reference and using your own number can move the plate cost in a meaningful way. If those two show up in high-volume dishes, measuring before estimating isn't a technical refinement, it's an economic decision.

How often you review depends on how much the product varies. A seasonal vegetable changes size and supplier several times a year; a frozen tuna loin with a fixed spec can stay stable for months. The "My Trim Loss Table" sheet has a last-measured date column precisely so the review becomes a purchasing habit and not a one-off task: when the supplier or the size changes, you repeat the test before updating the card, not after you spot the deviation at month-end close.

**Ten Yield Tests With Their Clean-Pound Cost (yield-and-trim-loss.xlsx, "Yield Test" sheet)**

| Product | AP weight (lb) | AP price/lb ($) | Clean weight (lb) | Yield (%) | Trim loss (%) | Q-factor | Net cost, byproduct not used ($/lb) | Net cost, byproduct used ($/lb) |
|---|---|---|---|---|---|---|---|---|
| Whole sea bass (2.65 lb) | 2.65 | $6.76 | 1.37 | 51.7% | 48.3% | 1.94 | $13.08 | $12.53 |
| Whole hake | 5.29 | $5.35 | 2.87 | 54.2% | 45.8% | 1.85 | $9.88 | $9.40 |
| Beef tenderloin (whole piece) | 4.63 | $12.02 | 4.08 | 88.1% | 11.9% | 1.14 | $13.64 | $13.47 |
| Whole free-range chicken | 4.85 | $2.45 | 3.31 | 68.2% | 31.8% | 1.47 | $3.59 | $3.35 |
| Lamb (shoulder) | 3.53 | $5.99 | 2.98 | 84.4% | 15.6% | 1.19 | $7.09 | $7.09 |
| Heirloom tomato | 11.02 | $1.72 | 9.70 | 88.0% | 12.0% | 1.14 | $1.96 | $1.96 |
| Artichoke | 11.02 | $1.32 | 4.19 | 38.0% | 62.0% | 2.63 | $3.46 | $3.46 |
| Sweet potato | 11.02 | $0.73 | 9.04 | 82.0% | 18.0% | 1.22 | $0.88 | $0.88 |
| Mussels (in the shell) | 11.02 | $1.18 | 2.20 | 20.0% | 80.0% | 5.00 | $5.90 | $5.90 |
| White shrimp (whole) | 4.41 | $10.89 | 2.31 | 52.5% | 47.5% | 1.90 | $20.73 | $20.09 |

**Your Trim Loss Table: Reference Range and Your Own Measurement (yield-and-trim-loss.xlsx, "My Trim Loss Table" sheet)**

| Category | Reference minimum (%) | Reference maximum (%) | Your measured trim loss (%) | Trim loss you use (%) | Where the number comes from |
|---|---|---|---|---|---|
| Meats (bone-in/fatty cuts) | 15.0% | 30.0% |  | 22.5% | Reference range |
| Beef tenderloin (trimming) | 10.0% | 15.0% | 11.9% | 11.9% | Your measurement |
| Whole fish | 45.0% | 55.0% | 48.3% | 48.3% | Your measurement |
| Fish loins/fillets | 5.0% | 12.0% |  | 8.5% | Reference range |
| Leafy greens | 10.0% | 15.0% |  | 12.5% | Reference range |
| Vegetables and produce (general) | 10.0% | 25.0% |  | 17.5% | Reference range |
| Artichoke | 55.0% | 65.0% | 62.0% | 62.0% | Your measurement |
| Mussels, snails, tripe | 80.0% | 85.0% | 80.0% | 80.0% | Your measurement |
| Whole shellfish (shrimp, langoustine) | 45.0% | 55.0% | 47.5% | 47.5% | Your measurement |
| Fruit | 15.0% | 30.0% |  | 22.5% | Reference range |
| Whole poultry | 28.0% | 35.0% | 31.8% | 31.8% | Your measurement |
| Cheeses, cured meats (rind/skin) | 3.0% | 8.0% |  | 5.5% | Reference range |

*The "Trim loss you use" column takes your own measurement the moment you type it in and, until you have one, falls back on the reference range. The last column always tells you where the number that's costing your plates comes from.*


---

## 6. The Recipe Cost Card That Survives an Audit

### What a Recipe Cost Line Needs to Be Auditable

A recipe cost card that holds up to an audit isn't the one with the most columns, it's the one that lets someone reconstruct every decision without asking whoever built it. For that, each ingredient line needs at least six fields: the ingredient name as it appears on the delivery invoice, the net quantity per portion, the trim loss percentage, the gross quantity to buy, the pre-tax price and the purchase tax rate in its own column.

Keeping the pre-tax price apart from the tax rate isn't bureaucracy. The card has to do two jobs at once: cost the portion, and reconcile the delivery invoice when the supplier's bill arrives. If the price you store already has the tax built in, the cost you calculate isn't comparable with what appears on your P&L, which always works with amounts before tax. And if the tax rate sits in its own column, any rule change (an ingredient that moves from one rate to another) gets fixed in a single field without touching the price or the cost formula.

The "portions this card yields" field deserves special attention. The card for the Iberico pork tenderloin with sweet potato purée that comes with this guide has that field set to 1, which means every ingredient is expressed per single portion. But in production cooking it's common to cost an entire preparation (a stock, a base sauce, a purée) and then divide by the number of portions it yields. That field is the divisor. Eyeballing the portion cost from a preparation of several pounds introduces rounding that builds up line by line and shows up at month-end as an unexplained gap between theoretical cost and actual cost. The "Cost Card" sheet of recipe-cost-card.xlsx solves this: you enter the total cost of the preparation and the number of portions, and the sheet does the division, not the cook on shift.

The mandatory fields of each line, summarized:

- Ingredient name exactly as it appears on the supplier's delivery invoice.
- Net quantity per portion, in pounds or liters, unrounded.
- Trim loss percentage, as a number between 0 and 1 or as a percentage depending on the convention you pick, but always the same across the whole card.
- Gross quantity to buy, calculated by formula, never by hand.
- Pre-tax price per purchase unit.
- Purchase tax rate, in its own column.
- Line cost excluding tax, the result of multiplying the gross quantity by the pre-tax price.

### Trim Loss Goes In by Dividing, Not by Multiplying

The most common mistake when building a card is calculating the gross quantity by adding the trim loss to the net quantity. The logic looks right: if I need 7.76 oz of cleaned product and trim loss is 12.0%, I add 12.0% of 7.76 oz and buy a little more. The problem is that this calculation applies the percentage to the clean weight, when trim loss happens on the AP weight. The result always comes up short, and the gap grows with higher trim loss percentages.

The correct formula is: gross quantity = net quantity divided by one minus the trim loss. With the data from the first line of the card, the net quantity is 7.76 oz (0.49 lb) and trim loss is 12.0%, which is 0.12 as a decimal. The operation is 7.76 oz divided by 0.88, which gives 8.82 oz (0.55 lb). That 8.82 oz is the gross quantity that appears in the "Cost Card" sheet of recipe-cost-card.xlsx. Had it been calculated by adding 12.0% of 7.76 oz, the result would have been 8.69 oz, a difference that looks small per ingredient but multiplies across every line, every service and every day of the year. If you buy by the kilo, as UK and Australian kitchens do, the per-kg prices behind those pound prices are $15.80 for the tenderloin, $11.50 for the belly, $8.90 for the butter and $0.95 for the onion.

The gross quantity for the sweet potato on that same card is 0.49 lb against a net quantity of 0.40 lb, which reflects its 18.0% trim loss: in this preparation the potato is bought whole and peeled in the kitchen. If the process changes (if you buy it already peeled and portioned, as part of the establishment's mise en place), the trim loss percentage drops and the gross quantity drops with it. The card isn't a static document: every time the supplier, the purchase format or the cleaning process changes, you check the trim loss column before you check the price.

A practical rule for auditing this column: if a line's trim loss is zero and the ingredient arrives whole or unprocessed, ask who is absorbing that loss. Either the supplier absorbs it in the price (which means the price per pound already carries the cost of the breakdown), or your P&L is absorbing it without anyone having decided that.

### From Plate Cost to Target Menu Price

The summary of the card is where the information turns into a decision. The total cost of the Iberico pork tenderloin with sweet potato purée card, pre-tax, is $5.67. Since the card is built for 1 portion, the plate cost is also $5.67. From there, the sheet applies the 30% target food cost set in the matching cell of the "Cost Card" sheet of recipe-cost-card.xlsx and calculates the target menu price, pre-tax: $18.90. Add the same illustrative 10% sales tax from chapter 3 and the target price the guest pays comes to $20.79.

So far, the card does what any recipe costing does. What turns it into a decision tool is the comparison with the price currently on the menu. The dish is on the menu at $17.30, pre-tax. At that price the real food cost climbs to 32.8% and the contribution margin (the difference between the menu price and the cost of the plate) is $11.63. The gap between the target price and the current price is $1.60, which works out to a needed increase of 9.3% over the current price.

Those two numbers, $1.60 and 9.3%, are what you take into the menu conversation. The card doesn't recommend raising the price automatically: it recommends that the decision be made with those numbers on the table, not on a gut feeling that "this dish doesn't make money." The table below, taken from the "Cost Card" sheet of recipe-cost-card.xlsx, shows the full summary with all the lines.

It's worth clarifying the scope of this card relative to the rest of the package. The "Cost Card" sheet of recipe-cost-card.xlsx is the base: it's there to build your judgment, understand the logic of trim loss and read the profitability summary. The Food Cost Kit Pro includes templates adapted to business formats with different menu structures (tasting menu, prix fixe, tapas bar), but you don't need them to work with the method this guide develops. With the base card and a clear method, any operation can audit its menu dish by dish.

### Comparing the Target Price With What's on the Menu Today

The summary of the card doesn't stop at the plate cost: it ends in the pricing decision. The "Cost Card" sheet of recipe-cost-card.xlsx calculates the target menu price from the target food cost set in the header, which in the Iberico pork tenderloin with sweet potato purée example is 30%. With a plate cost of $5.67 pre-tax, the target menu price pre-tax comes to $18.90, which with the illustrative 10% sales tax means $20.79 at the register. That's the price that sustains the margin the business needs.

The field that turns the card into a real management tool is the current menu price, which in this case is $17.30 pre-tax. The difference between the two values, $1.60, appears calculated in the "Cost Card" sheet next to the increase needed, expressed as a percentage of the current price: 9.3%. Those two figures are what you bring to the menu review meeting, not the bare cost. The real food cost produced by the current price is 32.8%, and the contribution margin left by each portion sold at that price is $11.63. Knowing the contribution margin falls below target isn't enough to make a decision; knowing how far to move the price, and stating it as a percentage of the current price, is what lets you judge whether the market will take the increase or whether you need to act on the cost side.

The card doesn't prescribe the decision: it informs it. A 9.3% increase may be workable in high season and not on a midday prix fixe menu. The dish may be a signature item that anchors the menu, and the business may choose to hold that food cost on purpose, offsetting it with higher-margin dishes. What can't happen is making that decision without knowing the number. The table below gathers the full summary, from plate cost to price difference, with all the fields just described.

If you need to adapt this structure to formats with several portions per preparation, to beverage costing, or to cards for sub-recipes that go in as an ingredient in other cards, the Food Cost Kit Pro includes templates specific to each type of business. This base card is enough to work the method this guide develops; the kit's templates are complementary and meant for people who have already absorbed the logic of the base card.

---

### Mistakes That Invalidate a Card

The most frequent and most silent mistake is calculating the gross quantity by multiplying the net quantity by the trim loss percentage and adding the result. With a net quantity of 7.76 oz and 12.0% trim loss, that calculation gives a gross quantity lower than the real one. The correct formula is to divide the net quantity by one minus the trim loss expressed as a decimal: 7.76 oz divided by 0.88 gives 8.82 oz, which is the gross quantity in the "Cost Card" sheet. The difference looks small on one line, but it builds up across every ingredient and the total cost of the card ends up understated, systematically. The table below shows the tenderloin line with both values side by side so the difference is visible.

Storing the pre-tax price on the ingredient line, and the purchase tax rate in its own column, isn't a formatting whim: it's what lets you use the same card to cost the dish and to reconcile the supplier's delivery invoice. If the purchase price is stored with tax included, the total cost of the card mixes the pre-tax amount with the tax, and comparing against the delivery invoice requires a conversion step that introduces errors. With the pre-tax price on the line and the rate in a separate column, any internal or external audit can rebuild the invoice total by multiplying by the matching rate, without touching the logic of the recipe costing.

The "portions this card yields" field solves another common problem: the rounding that shows up when you try to cost the portion directly by eye. The right practice is to cost the entire preparation and divide by the number of portions it produces. On the example card that field is 1, because the preparation is calculated for a single portion, but for a sauce, a stock or a dough that yields several units, the field can hold any whole number, and the plate cost the "Cost Card" sheet calculates will always be the result of dividing the total cost by that value, with no intermediate rounding.

Three situations invalidate a card even when the math is right: the recorded purchase price doesn't match your current supplier, the trim loss was estimated without a real weighing, and the portions field doesn't reflect the real yield of the preparation in the kitchen. All three have the same fix: the card is reviewed every time the purchase price of a relevant ingredient changes, and the trim loss is validated with a yield sheet signed by the cook in charge. A card with no last-review date and no assigned owner won't survive an audit, even if the gross quantity formula is right.

**The Card Lines, With Trim Loss Built In (recipe-cost-card.xlsx, "Cost Card" sheet)**

| # | Ingredient | Unit | Net quantity/portion | Price/unit pre-tax ($) | Trim loss (%) | Gross quantity to buy | Line cost pre-tax ($) |
|---|---|---|---|---|---|---|---|
| 1 | Iberico pork tenderloin | lb | 0.49 | $7.17 | 12.0% | 0.55 | $3.95 |
| 2 | Iberico pork belly (crispy) | lb | 0.07 | $5.22 | 5.0% | 0.07 | $0.36 |
| 3 | Sweet potato | lb | 0.40 | $0.73 | 18.0% | 0.49 | $0.35 |
| 4 | Butter | lb | 0.02 | $4.04 | 0.0% | 0.02 | $0.13 |
| 5 | Heavy cream (35% fat) | L | 0.03 | $3.40 | 0.0% | 0.03 | $0.10 |
| 6 | Onion | lb | 0.09 | $0.43 | 12.0% | 0.11 | $0.04 |
| 7 | Pedro Ximénez wine (for the sauce) | L | 0.03 | $9.80 | 0.0% | 0.03 | $0.29 |
| 8 | Beef stock | L | 0.06 | $2.20 | 0.0% | 0.06 | $0.13 |
| 9 | Extra virgin olive oil | L | 0.01 | $7.20 | 0.0% | 0.01 | $0.11 |
| 10 | Arugula sprouts | lb | 0.02 | $5.44 | 10.0% | 0.02 | $0.13 |
| 11 | Salt, pepper, thyme and paprika (allocated) | lb | 0.02 | $2.72 | 0.0% | 0.02 | $0.06 |

**The Card Summary: From Plate Cost to Menu Price (recipe-cost-card.xlsx, "Cost Card" sheet)**

| Item | Value |
|---|---|
| TOTAL CARD COST, pre-tax ($) | $5.67 |
| Plate cost, pre-tax ($) | $5.67 |
| Target menu price (pre-tax) ($) = plate cost ÷ target food cost | $18.90 |
| Tax rate (%), illustrative 10% (the workbook starts at 0%) | 10.0% |
| Target price WITH tax ($), what the guest pays | $20.79 |
| CURRENT menu price (pre-tax) ($) | $17.30 |
| Current price WITH tax ($), what the guest pays | $19.03 |
| REAL food cost at the current menu price (%) | 32.8% |
| Contribution margin at the current menu price ($) | $11.63 |
| Difference between target and current menu price ($) | $1.60 |
| Increase needed over the current menu price to reach the target (%) | 9.3% |

*Rows marked "(%)" are percentages; the rest are dollars. The target price comes from dividing the plate cost by the target food cost, which is an editable cell and not a number buried inside the formula. In the workbook the tax rate cell starts at 0%, so the "WITH tax" rows equal the pre-tax rows until you enter a rate; the 10% here is the same illustrative rate as chapter 3.*


---

## 7. Theoretical vs. Actual Food Cost: Where the Money Leaks

### The Two Food Costs and Why They Never Quite Match

Theoretical food cost is what it should have cost to produce everything you sold, worked out plate by plate from the recipe cost card. Actual food cost is what the kitchen really consumed during the period, worked out from inventory movement. The two will differ. That isn't a spreadsheet error: it's the norm, and the gap is your diagnosis.

On the "Data" sheet of menu-engineering-matrix.xlsx, the theoretical food cost of the sample menu comes out at 32.7%. The target on the "Cost Card" sheet of recipe-cost-card.xlsx is 30%. The raw-material cost over sales for the year on the "Monthly" sheet of prime-cost-dashboard.xlsx is 32.1%, with total net sales of $1,232,200 and actual ingredient consumption of $395,400. The dashboard's target, on the "Inputs" sheet of the same file, is also 30%. Three sources, three different numbers, and all three are correct: they measure different things. Commonly cited industry ranges put average food cost at around 30% of sales, with a healthy band of 25 to 35%. Sitting at 32.1% is not an alarm; sitting at 32.1% and climbing is.

The four causes that explain the gap between theoretical and actual, in the order they show up in most kitchens, are these:

- **Portions that don't match the card.** The recipe cost card says 6.35 oz of protein; the scale at the pass says something else. A little too much on every plate, multiplied by the covers you serve in a month, pushes actual food cost above theoretical without anyone having decided it.
- **Trim, waste and spoilage.** Product that comes in the back door and never reaches a plate: trim losses higher than the card assumes, product that expires before it rotates, or cooking loss that was never updated in the costing.
- **Comps and staff meals.** Everything that leaves the kitchen without generating a sale. If it isn't rung in under its own cost code, the system counts it as ingredient consumption and actual food cost rises with no apparent explanation.
- **Purchase prices that moved while nobody re-costed.** An ingredient gets more expensive, the card isn't updated, and the theoretical number keeps being calculated with the old price. To see how far prices have really moved, go to your own delivery invoices and your suppliers' price lists: the data is already on your desk. This guide gives you the method to read it.

What you watch is not the absolute value of any one month, but the trend. In January, actual food cost was 31.7% on net sales of $89,600, with the target set at 30%. A stable deviation around that level, month after month, tells you the card or the target needs a review, but there is no active leak. A deviation that grows every month tells you something has changed in operations or in purchase prices and you haven't found it yet.

---

### Actual Usage: Beginning Inventory, Purchases and Ending Inventory

Actual ingredient usage for a period comes from a single formula: beginning inventory plus purchases minus ending inventory. The result is what the kitchen consumed, regardless of what was sold. Without that closing count, what you get is a purchases-based food cost, which is a different number and misleads you the moment your storeroom goes up or down in level. If you buy more than usual in December to cover the first week of January, December's purchases-based food cost shoots up even though the kitchen ran normally; actual food cost, calculated with the ending inventory, corrects it.

On the dashboard, purchases for the year add up to $396,100 and actual ingredient consumption is $395,400. The difference, which the "Monthly" sheet of prime-cost-dashboard.xlsx shows month by month, reflects exactly that storeroom adjustment: stock hasn't changed significantly over the full year, but in individual months the distance between the two figures can matter. The table below shows that monthly breakdown.

The most useful routine is not a full weekly inventory, which few kitchens sustain in real life. What works is a short count of the ten items that carry the most weight in your total cost: the main proteins, seafood if you have it, and any ingredient whose price has changed recently. Those ten items usually explain most of the deviation. If you want to track at a finer level day to day, the Food Cost Kit Pro includes a control template with the columns you need to log receipts, usage and stock in real time, without building it from scratch.

### The Four Causes of the Deviation

Actual food cost for the period comes from a single formula: beginning inventory plus purchases minus ending inventory. The result is actual ingredient consumption. Without that closing count there is no actual food cost; what you have is a purchases-based food cost, which is something else and misleads you every time the storeroom goes up or down. On the "Monthly" sheet of prime-cost-dashboard.xlsx the difference is easy to see: purchases for the year add up to $396,100 and actual ingredient consumption is $395,400, on net sales of $1,232,200. That $700 gap reflects the change in stock between the first day of the year and the last; if someone had used purchases as a proxy for consumption, the percentage would have come out slightly distorted. The raw-material cost over sales that the dashboard produces is 32.1%, against a target food cost of 30% set on the "Inputs" sheet of the same workbook. That gap of 2.1 points isn't a spreadsheet error: it's a diagnosis with specific causes.

Commonly cited industry ranges put average food cost at around 30% of sales, with a healthy band between 25% and 35%. Sitting at 32.1% is not an emergency, but you do need to know why you're there and whether the trend is going up or down.

The causes of deviation between theoretical and actual food cost repeat themselves in almost every operation I work with, and they always show up in the same order of frequency:

- **Portions that don't match the card.** This is the most common cause. The recipe cost card sets a portion weight; the line serves another. A quarter of an ounce too much per plate (about 0.18 oz) on a high-volume item moves actual food cost by several tenths of a point a month, and nobody notices it at the pass.
- **Trim, waste and spoilage.** Product that comes into the storeroom and never reaches a plate has a cost but generates no sale. Poor rotation or an oversized order goes straight into actual consumption with nothing to match it on the sales side.
- **Comps and staff meals.** Every item that leaves the kitchen without a sale on the POS is actual consumption with no revenue to cover it. If you don't record it through a comps system or a staff-meal code, food cost absorbs that cost and the theoretical sheet never sees it.
- **Purchase prices that moved while nobody re-costed.** When a supplier updates its price list and the recipe cost card isn't touched, the theoretical food cost of the menu goes stale. The menu-engineering-matrix.xlsx shows a theoretical food cost of 32.7% for the sample menu; if purchase prices have risen since the last costing, that 32.7% is already optimistic. To know how far your input prices have moved, check your own delivery invoices and supplier price lists: the data is there, not in the head chef's memory.

What you watch is not the absolute value of any one month, but the trend. A stable deviation, month after month in the same range, tells you the business runs at a food cost that is structurally different from the theoretical one, and you have to decide whether to fix the operation or adjust the target. A deviation that keeps growing is a different conversation: something has changed, and you need to find it before it settles in.

---

### The Weekly Routine That Keeps It Under Control

A full inventory every week is unworkable in most kitchens with the staff they have. What works is the short count: the ten items that weigh most in your total cost. In any operation there is a small group of products, usually proteins and high-value preparations, that account for most of the consumption. Controlling those ten items rigorously every week gives you more information than an exhaustive count done in a hurry and full of errors.

The procedure is straightforward:

- Identify the ten items with the most weight in your usage, using the "Monthly" sheet of prime-cost-dashboard.xlsx as a base to see which purchase lines are the largest.
- Count the physical stock of those items every Monday before service, or on the slowest day of the week.
- Record the purchases received between that count and the previous one.
- Calculate partial usage: previous stock plus receipts minus current stock.
- Compare that partial usage with sales of those items over the same period, using the units sold from the POS.

If the partial usage of those ten items drifts consistently from what should have been consumed according to recipe-cost-card.xlsx, you've found the problem before a full month of losses piles up. The target food cost on that card is 30%; any signal that moves actual usage away from that threshold on a sustained basis deserves a review of the line portioning or the purchasing terms, not an improvised explanation at month-end.

If you want to track day by day without building the tool from scratch, the Food Cost Kit Pro includes the control template with the formulas already set up; this chapter doesn't develop it here because the kit already ships it ready to use. The table below shows the full path from stock to usage month by month, with the data from prime-cost-dashboard.xlsx, "Monthly" sheet: January, with net sales of $89,600 and an actual food cost of 31.7%, is the starting point for reading how the deviation evolves over the year.

**From Stock to Usage: Actual Food Cost Month by Month (prime-cost-dashboard.xlsx, "Monthly" Sheet)**

| Month | Net Sales ($) | Beginning Inventory ($) | Purchases ($) | Ending Inventory ($) | Usage ($) | Food Cost (%) |
|---|---|---|---|---|---|---|
| January | $89,600 | $9,700 | $28,100 | $9,400 | $28,400 | 31.7% |
| February | $84,100 | $9,400 | $27,000 | $9,100 | $27,300 | 32.5% |
| March | $95,200 | $9,100 | $30,700 | $9,500 | $30,300 | 31.8% |
| April | $100,400 | $9,500 | $31,400 | $9,200 | $31,700 | 31.6% |
| May | $107,900 | $9,200 | $34,700 | $9,700 | $34,200 | 31.7% |
| June | $110,700 | $9,700 | $37,700 | $9,000 | $38,400 | 34.7% |
| July | $116,200 | $9,000 | $38,100 | $9,400 | $37,700 | 32.4% |
| August | $99,600 | $9,400 | $34,400 | $8,700 | $35,100 | 35.2% |
| September | $105,500 | $8,700 | $32,600 | $9,500 | $31,800 | 30.1% |
| October | $102,700 | $9,500 | $31,800 | $9,200 | $32,100 | 31.3% |
| November | $97,900 | $9,200 | $30,500 | $9,700 | $30,000 | 30.6% |
| December | $122,400 | $9,700 | $39,100 | $10,400 | $38,400 | 31.4% |
| TOTAL / AVERAGE | $1,232,200 |  | $396,100 |  | $395,400 | 32.1% |

*Compare the purchases and usage columns: when they differ, what changed is the storeroom, and using purchases as if they were usage would have given you a false food cost that month.*


---

## 8. Prime Cost: The Metric That Measures the Health of the Business

### What Prime Cost Adds Up and Why You Look at Both Together

Food cost and labor cost are not two independent metrics: they are communicating vessels. The more you make in-house—house stocks, cuts from the whole primal, mother sauces instead of industrial bases—the lower your product cost and the more labor hours it takes to sustain it. Buying more prepared product does the opposite: product cost goes up and kitchen hours are freed. Looking only at food cost rewards the first decision and punishes the second without seeing what it costs in the other column; looking only at labor cost makes the mirror-image mistake. Prime cost is the sum of the two lines over net sales, and it is the only number that sees the combined effect of how the menu is produced.

It is also the number that exposes the case that fools people most: a food cost that looks impeccable on each plate's cost card while labor cost has run away and nobody has set the two side by side. A business can cost every recipe precisely and still lose margin because the schedule for the floor and the kitchen hasn't been reviewed in months. The dashboard in this pack is set up for a full-service business and puts raw-material cost over sales and labor cost on the same row, month by month: in the year it records, product cost comes in at 32.1%, labor cost at 31.3%, and the sum—prime cost—at 63.4%, with a margin after prime cost of $451,142, or 36.6% of sales left to pay rent, utilities and the rest of the overhead before you can talk about profit. Within the same year there is range: April closes at 62.7%, the best month, and August at 69.9%, a reading the sheet itself flags as "Above target." The yearly figure doesn't tell you which month went wrong; the monthly breakdown does.

### The Benchmark: 30% Food Cost and 30-35% Labor

The cost structure of a full-service restaurant is commonly cited as revolving around 30% for product and 30-35% for labor over net sales. Added together, those two lines draw the prime cost that this pack takes as its reference, which is why the full-service target is set at 65% in an editable cell on the "Inputs" sheet of prime-cost-dashboard.xlsx, and not buried inside the formula: every business can move it if its real structure departs from the reference, without touching the calculation that feeds it.

That 65% only works if the labor cost you compare against it has been calculated with the same yardstick. In this model, employer payroll taxes and benefits are set at 33% on top of gross pay (an input you replace with your own figure): in the year the dashboard records, gross wages add up to $277,600 and other labor costs to $16,450, and once the employer payroll taxes and benefits are added, labor cost comes to $385,658. Calculating labor cost on gross payroll alone, without employer payroll taxes and benefits, is measuring yourself against a yardstick that isn't yours: the result comes out lower than reality, and the prime cost that follows looks better than the business can support.

Keep in mind the widely quoted US rule of thumb: prime cost should stay at 60% at most, above which it becomes very hard to be profitable unless volume is very high (Toast—How to Calculate Prime Cost, 2026). That is a single round number for every format; the dashboard's 65% is a full-service target you can edit. The full picture of a restaurant's P&L adds to those two lines a commonly cited 5-10% for rent and 13-20% for overhead, with a healthy bottom line of 10-13%; below that floor, the reading is that the entire structure needs a review, not just the menu.

### Full Service or Counter: Two Different Targets

The pack also carries a prime cost target for counter service or self-service, at 55%, against the 65% for full service that is active in this dashboard. The difference isn't a template whim: in a counter or self-service format labor cost is structurally lower, because service dispenses with a good part of the dining room, so the same prime cost means very different things depending on the business model. Full-service labor is commonly cited at 30-35% of net sales, while partial-service counter or self-service sits at 15-25%, quite a bit lower. The US benchmark follows the same logic with a different cut: 60-65% for full service and 55-60% for quick service or QSR (Toast—How to Calculate Prime Cost, 2026). In both cases, what moves the bar is the service model, not the criterion you use to read it.

Reading prime cost this way is a diagnostic exercise: set it against the threshold for your business's format and tell apart when the product is failing and when labor is. When it's the second reading that fails—a labor cost that falls outside its range month after month—the work that follows is about schedules and hours, and that's what the Restaurant Staff Scheduling Kit Pro in this same catalog is for. This guide stays with the diagnosis; that kit is the one that steps in to fix it.

### Labor Cost Is Gross Pay Plus Employer Payroll Taxes and Benefits

Food cost and labor cost are not read separately: they are communicating vessels. When the kitchen takes on more in-house production—stocks, mother sauces, breaking down whole primals—product cost drops, because you pay for raw material and not for the margin of whoever already transformed it, but crew hours go up, because someone has to do that work. Buying prepared or semi-prepared product reverses the effect: food cost goes up and hours go down. Looking at only one of the two lines is seeing half of the decision. Prime cost—their sum over sales—is the only metric that sees them together, and the only one that doesn't reward shifting cost from one column to the other without the business actually getting better.

The commonly cited benchmark for a full-service restaurant puts product cost at around 30% of sales and labor between 30% and 35%. From that sum comes the target the dashboard carries for the Full service business type: 65% prime cost, a figure that lives in an editable cell on the "Inputs" sheet of prime-cost-dashboard.xlsx and not inside any formula, so you adjust it the day your service model or your staffing policy changes.

The same sheet carries two targets, not one:

- 65% for the full-service business, the one the dashboard has active.
- 55% for the business that works as a counter or self-service operation.

The second is not a more generous threshold: it reflects a different staffing structure. With less table service there are fewer dining-room hours per dollar sold, and the labor cost for that model is commonly cited at between 15% and 25% of net sales, against 30-35% for full service. The same 65% prime cost means very different things depending on which format you're talking about.

There is one nuance that decides whether the comparison makes sense: the labor cost that goes into the dashboard's prime cost includes employer payroll taxes and benefits, set at 33% on top of gross pay on the "Inputs" sheet (a model input: replace it with the real figure from your own payroll). The "Monthly" sheet separates the two lines for the year—$277,600 in gross wages and $16,450 in other labor costs—and adds them into a labor cost with employer payroll taxes and benefits of $385,658. If you calculate your labor cost on gross payroll and compare it against a target built for total labor cost, you're measuring yourself with a yardstick that isn't yours: the result comes out artificially low, and the diagnosis overly optimistic.

The reference that circulates most widely in the US puts the recommended prime cost at 60% at most, above which it is very hard to be profitable unless volume is very high, with a range of 60-65% for full service and 55-60% for quick service (Toast, a POS provider, is the most cited source, 2026). Treat it as a rule of thumb, not a law: your own staffing structure and payroll costs decide where your real line sits.

### Reading the Dashboard: The Good Month, the Bad Month and the Year

The "Monthly" sheet of prime-cost-dashboard.xlsx puts, month by month and on the same row, product cost over sales and labor cost, and from there calculates the prime cost for each month and for the year. It is the view that exposes the case that fools people most: an impeccable food cost living alongside a runaway labor cost, invisible if you only look at the product column. In the year the template carries, raw-material cost over sales closes at 32.1% and labor cost at 31.3%, with an annual prime cost of 63.4%, below the 65% target set for Full service. The margin left after covering those two lines is $451,142, or 36.6% of sales: what's available for rent, utilities and the rest of the overhead before you get to the bottom line.

The same sheet separates the best month from the worst. April closes with a prime cost of 62.7%, comfortably inside the target; August shoots it up to 69.9%, and the sheet itself flags it as "Above target." That gap of more than seven points is the reason to read the dashboard month by month and not just the annual total: a year on target can hide a single month where something went off the rails—a crew oversized for real occupancy, overtime badly planned, an extra shift that never found the sales to justify it—and that month is not fixed by looking only at December's figure.

August being above target doesn't mean the business loses money that month: it means less margin was left to pay rent, utilities and the rest of the fixed overhead than in a month like April. That is the reading that separates diagnosis from alarmism, and it is also the limit of this guide: prime cost tells you when labor cost has eaten margin that should have stayed free, but it doesn't rebuild schedules or redistribute hours. If you see your labor cost out of line month after month, that work lives in the Restaurant Staff Scheduling Kit Pro, built to work through schedules and hours in the detail this chapter doesn't cover. Here, the dashboard's job is to put the right number in front of you and tell you whether it's where it should be.

**Prime Cost Target by Business Type (prime-cost-dashboard.xlsx, "Inputs" Sheet)**

| Business Type | Prime Cost Target (%) |
|---|---|
| Full service | 65.0% |
| Counter / self-service | 55.0% |

*Both cells are editable: if your payroll costs, your mix or your format call for a different threshold, type it there and the twelve-month traffic light recalculates against yours.*

**Product and Labor in the Same Table, Month by Month (prime-cost-dashboard.xlsx, "Monthly" Sheet)**

| Month | Labor Cost with Payroll Taxes and Benefits ($) | Food Cost (%) | Labor Cost (%) | Prime Cost (%) | Target (%) | Margin After Prime Cost ($) |
|---|---|---|---|---|---|---|
| January | $29,988 | 31.7% | 33.5% | 65.2% | 65.0% | $31,212 |
| February | $29,918 | 32.5% | 35.6% | 68.0% | 65.0% | $26,882 |
| March | $30,919 | 31.8% | 32.5% | 64.3% | 65.0% | $33,981 |
| April | $31,255 | 31.6% | 31.1% | 62.7% | 65.0% | $37,445 |
| May | $32,256 | 31.7% | 29.9% | 61.6% | 65.0% | $41,444 |
| June | $33,656 | 34.7% | 30.4% | 65.1% | 65.0% | $38,644 |
| July | $34,657 | 32.4% | 29.8% | 62.3% | 65.0% | $43,843 |
| August | $34,517 | 35.2% | 34.7% | 69.9% | 65.0% | $29,983 |
| September | $31,920 | 30.1% | 30.3% | 60.4% | 65.0% | $41,780 |
| October | $31,255 | 31.3% | 30.4% | 61.7% | 65.0% | $39,345 |
| November | $30,919 | 30.6% | 31.6% | 62.2% | 65.0% | $36,981 |
| December | $34,398 | 31.4% | 28.1% | 59.5% | 65.0% | $49,602 |
| TOTAL / AVERAGE | $385,658 | 32.1% | 31.3% | 63.4% | 65.0% | $451,142 |


---
## 9. Four Ways to Price a Dish

### Method A: Cost Factor, and Where It Breaks

The first of the four methods starts from the plate cost on each dish's recipe cost card and multiplies it by a fixed factor, calculated so the result lands on the food cost % the business has set as its target. In the example menu, that target is the 30% that comes preloaded in the "By Dish" sheet of menu-pricing-calculator.xlsx, a cell that depends on each business's cost structure, not a rule that fits every menu. You will also hear this called food cost % markup or factor pricing. It is the best-known method in the trade, and it works reasonably well as long as the plate cost stays in a mid-range. The trouble starts when that cost climbs: the same factor that gives a sensible menu price on an inexpensive dish, applied to an expensive ingredient, pushes the number to a point where no guest will pay it. The example menu makes the case without any further argument: the bone-in ribeye, run through the factor method, comes out at a menu price of $49.33. That is no contrived anecdote. It is what happens every time this method is applied unfiltered to a high-cost product, and it is the reason no serious operator trusts a single method for the whole menu. The 30% target, by the way, is not an arbitrary figure: it matches the food cost benchmark commonly cited for restaurants, around 30% of sales with a healthy range of 25% to 35%. But an industry average helps you calibrate a starting point. It does not set the price of each dish one by one, least of all when the cost of the raw ingredient sits far above the rest of the menu.

### Method B: Target Contribution Margin in Dollars

The fix for that breaking point is not to change the percentage. It is to change the question. Instead of starting from cost and applying a factor, the target margin method starts from how much the business wants to earn per plate, a fixed dollar figure that does not move when the product cost moves, and lets the food cost % fall out as a consequence, even if the result looks ugly on paper. Applied to the same ribeye, this method returns a menu price of $25.30, far below what the factor produces, and it is the one finally chosen for that dish on the menu, as column Q of the "By Dish" sheet shows. You have to accept the consequence without flinching: the ribeye's final food cost lands at 58.5%, way above the 30% target for the menu as a whole, and the dish still leaves a healthy contribution margin in dollars, which is what actually pays the rent and the payroll, not the percentage that shows on the sheet. The chosen price also sits below the current menu price, $32.70, so the exercise leaves the operator with a decision: keep the current price or bring it down. This chapter does not make that call for you.

### Method C: Market Price in Your Area

Methods C and D are different in nature from the first two: they do not calculate a menu price, they import it from outside. Method C starts from what your direct local competition charges for an equivalent dish and sets your price there. Method D, which we will get to later in this chapter, does the same from a different outside reference. In both cases the sheet stops answering "how much do I have to charge?" and starts answering a different question: given that price, imposed from outside, what food cost am I left with, and can I afford it? That is a change in the direction of the calculation, not a third road to the same number, and it helps to be clear on that before you look at the table below.

The full example menu, 20 dishes with a calculated price, does not split the work between one winning method and three leftovers. It uses method A on 5 dishes, B on 6, C on 4 and D on 5, a nearly even split across the four. 11 dishes land within the target food cost and 9 above it, with a food cost of 36.7% for the whole menu at the chosen prices and an average contribution margin of $8.01 per dish. That is the right way to read the table that follows: do not look for which of the four methods "wins." Understand that each dish pulls on the method that best fits its own nature (cost, positioning or market) and that the whole menu is a portfolio of those four decisions, not a single rule applied dish after dish.

The croquettes are the example to look at separately, because they say something different from the ribeye. The factor method puts them at a menu price of $7.00. The current menu price is $8.60, which is $1.60 higher. Here the method does not ask you to cut anything: it confirms that the current price already sits above the floor the cost sets, so any correction, if there is one, goes in another direction. Not every dish on the menu needs to be touched. Some just need someone to check, recipe cost card in hand, that the price they already charge still makes sense.

### Method D: Perceived Value

The cost factor multiplies without asking what dish is in front of it, and that is its problem. Applied to the ribeye on the example menu, the price the pricing sheet returns is $49.33, a figure no guest pays for a portion of beef, however generous the cut. It is not a quirk of the math. It is the argument of this chapter. A fixed factor works well when the raw ingredient cost is moderate and behaves the same across the menu, but the moment an expensive product shows up, the same multiplier that balances the books on a pasta dish blows the ribeye's price up to a useless number.

The remedy is not to change the factor. It is to change the method. Target margin in dollars starts from the opposite question: instead of multiplying the cost, you fix how much you want to earn per plate and let the percentage come out of that, even if the result looks ugly on the sheet. With the ribeye, that route returns a menu price of $25.30, which is also the price chosen for the menu, and the food cost that results from accepting it rises to 58.5%, far above any reasonable target for the menu as a whole. Compare that with what the ribeye carries on the menu today, $32.70: neither the factor nor the dollar margin lands exactly on what you already charge, and that gap is precisely what you have to decide dish by dish, not something to force into balance.

Method D pushes the logic a step further. Methods C and D do not calculate the menu price: they impose it from outside, based on the competition, the positioning of the house or what the guest is willing to pay for the experience, and only afterward let the sheet say what food cost results from accepting that figure. The question stops being "how much do I charge for this dish?" and becomes "can I afford to charge this?", which is a different question and a rather more uncomfortable one to answer. With perceived value, the price does not come out of any cost or any desired margin. It comes out of what the dish means to the person ordering it, and the sheet simply hands back the food cost that price leaves you, so you can judge whether it is sustainable before you print it on the menu.

### Which Method Fits Which Dish

The example menu has 20 dishes with a calculated price, and the split across the four methods dismantles the idea that there is a winner: 5 dishes are settled by cost factor, 6 by target margin in dollars, 4 by market price and 5 by perceived value. There is no single formula for the whole menu. There is a portfolio of methods, and choosing which one to apply to each dish is as much a part of the craft as calculating the cost on the recipe cost card. Across the whole menu, 11 dishes land within the target food cost and 9 above it, with an overall menu food cost of 36.7% and an average contribution margin of $8.01 per dish. The numbers in the table do not call for one single criterion. They call for looking dish by dish, using the method that belongs to each.

The croquettes are the case to study slowly, because it runs against everything above. The cost factor returns a menu price of $7.00, but the current menu price is $8.60, which is $1.60 higher. Here the method is not correcting anything: it is confirming that the dish is already priced above its floor. A dish can be perfectly well priced without the method you use to review it spitting out a higher number. What the calculation does is mark the minimum you can defend, not dictate the final price. The table below shows the four methods applied to the entire menu, dish by dish, so the logic behind each choice is in plain view before you touch a single price.

**The Four Methods Applied to the Same Menu (menu-pricing-calculator.xlsx, "By Dish" Sheet)**

| Dish | Plate Cost ($) | Method Chosen | A · Cost Factor Menu Price ($) | B · Target Margin Menu Price ($) | Chosen Menu Price Pre-Tax ($) | Final Food Cost (%) | Status |
|---|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | A · Cost Factor | $7.00 | $8.60 | $7.00 | 30.0% | On target |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | A · Cost Factor | $12.00 | $10.10 | $12.00 | 30.0% | On target |
| Garlic shrimp | $6.90 | B · Target Margin | $23.00 | $13.40 | $13.40 | 51.5% | Above target |
| Broken eggs with fries and chistorra sausage | $2.40 | A · Cost Factor | $8.00 | $8.90 | $8.00 | 30.0% | On target |
| Local cheese board | $5.20 | A · Cost Factor | $17.33 | $11.70 | $17.33 | 30.0% | On target |
| Confit artichokes with ham | $3.10 | A · Cost Factor | $10.33 | $9.60 | $10.33 | 30.0% | On target |
| Roasted tomato soup with basil | $1.20 | D · Perceived Value | $4.00 | $7.70 | $7.56 | 15.9% | On target |
| Iberico pork tenderloin with sweet potato purée | $5.67 | C · Market Price | $18.90 | $16.17 | $18.68 | 30.4% | Above target |
| Confit cod with pil-pil sauce | $7.40 | B · Target Margin | $24.67 | $17.90 | $17.90 | 41.3% | Above target |
| Dry-aged beef burger with fries | $4.30 | C · Market Price | $14.33 | $14.80 | $12.92 | 33.3% | Above target |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | B · Target Margin | $20.67 | $16.70 | $16.70 | 37.1% | Above target |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | B · Target Margin | $49.33 | $25.30 | $25.30 | 58.5% | Above target |
| Salt-baked sea bass | $8.90 | B · Target Margin | $29.67 | $19.40 | $19.40 | 45.9% | Above target |
| Free-range roast chicken with potatoes | $3.70 | C · Market Price | $12.33 | $14.20 | $11.94 | 31.0% | Above target |
| Seasonal vegetable lasagna | $2.60 | C · Market Price | $8.67 | $13.10 | $10.49 | 24.8% | On target |
| Bluefin tuna tataki with sesame | $9.60 | B · Target Margin | $32.00 | $20.10 | $20.10 | 47.8% | Above target |
| Creamy cheesecake | $1.30 | D · Perceived Value | $4.33 | $5.50 | $6.61 | 19.7% | On target |
| Caramelized torrija (Spanish-style French toast) with ice cream | $1.10 | D · Perceived Value | $3.67 | $5.30 | $5.83 | 18.9% | On target |
| Chocolate lava cake | $1.60 | D · Perceived Value | $5.33 | $5.80 | $7.13 | 22.4% | On target |
| Prepared seasonal fruit | $1.40 | D · Perceived Value | $4.67 | $5.60 | $4.73 | 29.6% | On target |

*Columns A and B always calculate, even when the dish uses another method: they are there so you can see what price would have come out and decide with all four answers in front of you.*


---

## 10. Pricing Psychology: What Is Proven and What Is Myth

### The Decoy Effect: The Option You Don't Want to Sell

When a menu offers two dishes that are comparable in price and appeal, the guest hesitates. Add a third option that is clearly worse than one of the two on every count (pricier, with nothing going for it next to the one you want to sell) but is not worse than the other in any respect, and the choice tilts toward the option that dominates that decoy. This is asymmetric dominance applied to a menu: the decoy is not there to be sold, it is there to make its neighbor look like the sensible decision. Of all the pricing psychology that circulates in the industry, this is the mechanism with the most experimental support over time. The work that confirms it for menu choice was published in International Hospitality Review, from the publisher Emerald, and its conclusion is qualitative: the effect shows up consistently when the decoy is well built. Don't turn it into a percentage for your menu.

Putting it into practice does not require inventing a new dish. It requires looking at the menu you already have and asking yourself, dish by dish, whether any of them is acting as a decoy today without you having decided it. The goal is not to cut the weak dish. It is to place it deliberately next to the dish you want to win, so the comparison is settled before the guest finishes reading the page.

### Descriptive Names: The Study and Its Fine Print

The name you give a dish on the menu is not a style detail. It is a sales lever with a field study behind it. Wansink, Painter and van Ittersum (2001), in the Cornell Hotel and Restaurant Administration Quarterly, measured the effect of replacing a generic dish name with a descriptive one (same dish, same kitchen, only the label changed) and found a 27% increase in sales over the generic name, plus a better rating of the taste and a better attitude toward the dish and the restaurant, without the guest paying a cent more. Here comes the caveat, and it goes in the same paragraph because separating it would give the number more authority than it has: the lead author of that work was the subject of an investigation for statistical misconduct in later publications, and no independent replication of this particular study has been found. Treat the 27% as a sign that the name matters, not as a law you can promise anyone.

What you can do without depending on the number is apply the principle with judgment. A name that signals origin, technique or texture gives the guest a reason to pick that dish and not the one next to it, and that reason works whether or not the 27% is behind it.

### Price Format: What Was Measured and in Which Currency

Yang, Kimes and Sessarego (2009), in the Cornell Hospitality Report, studied something more specific than just dropping the dollar sign. They compared prices written as plain numbers with no sign at all against prices with the currency symbol or written out in words, and found an average of 8% additional spending, $5.55 more per diner, when the price appeared with no explicit reference to money. Precision matters here: the study was done in dollars, with American diners, and what was measured is not the dollar sign itself but the absence of any reminder that this number is money you are about to pay. There is no honest way to carry that figure over to another currency or another market, or to assume a diner in the UK, Canada or Australia reacts the same way to a menu with no symbols. The finding is presented as what it is, a measurement made in one place with one group of diners, and the decision about your own price format stays in your hands.

And it pays to be just as explicit about what has no such backing. Prices ending in nine, the habit of putting the dish you most want to sell in the upper right corner, and the rules about the path the eye takes when reading a menu get repeated in article after article across the industry, but no citable study has been found to support them. They are stated here with no number and no attribution, precisely because they have none.

Method D on the pricing sheet is, exactly, the application of all this: a price that does not come from adding cost plus margin, but is imposed from how the dish is perceived within the menu as a whole. In your pack, 5 dishes use that perceived value method. The sheet lets you see it plainly: if the whole menu were priced at perceived value, the total would rise to $307.04; with the menu prices you have actually chosen, the total for the menu stays at $266.90, and the food cost of the whole menu at those chosen prices comes to 36.7%. How far to push perception and where to stop is up to you, dish by dish, with that same sheet in front of you.

### What Circulates With No Study Behind It

The decoy effect is, of all the pricing psychology that circulates around the menu, the only one with peer-reviewed work behind it, published in International Hospitality Review, from the publisher Emerald: next to the two real options you want the guest to choose between, you place a third that is clearly worse than one of them (price included) but not worse than the other, there only to tilt the comparison. The guest, who was torn between two dishes or two prix fixe menus, sees that one of them clearly beats the decoy, and that relative win turns into a preference for the option that dominates. It is asymmetric dominance, and it explains why on a well-built menu a middle option is almost never wasted: each dish that sits next to two others usually serves a comparison function, not just a direct selling one.

One step down in strength is the study of descriptive dish names: Wansink, Painter and van Ittersum (2001), in the Cornell Hotel and Restaurant Administration Quarterly, found that replacing a dish's generic name with a descriptive one, evoking origin, texture or provenance, raised sales by 27% over the generic name. Their lead author was later the subject of an investigation for statistical misconduct, and no independent replication of this particular study has been found, so the figure is taken as a sign and not as a law. It was a six-week field trial with 140 real diners that also recorded a better attitude toward the dish and toward the restaurant, and a better sensory rating of the taste, 7.31 versus 6.83 out of 10, without the diner paying a cent more: the name did not change what left the kitchen, it changed what the diner said they had tasted.

With the price format study the caution is of a different kind: Yang, Kimes and Sessarego (2009), in the Cornell Hospitality Report, measured at St. Andrew's Café at the Culinary Institute of America in Hyde Park, New York, with the result later confirmed by the Cornell Chronicle, that showing the price as a plain number with no currency symbol, versus showing it with "$" or written in words, raised average spending per diner by 8%, $5.55 more per diner. The study was done in dollars and with American diners, and what they really measured was not the symbol but the absence of any explicit monetary reference when reading the price. So carrying the figure over to another currency, or assuming the same jump repeats on your menu, would be stretching the data further than the study itself allows.

And then there is everything that gets repeated with nothing citable behind it. Three claims show up in any menu engineering course with no study to point to and no author to credit:

- prices ending in nine sell more than the same price rounded;
- the dish you want to sell performs best in the upper right corner of the menu;
- the diner's eye travels the page following a fixed pattern that you can exploit.

None of the three has a citable experiment behind it, and that does not mean they don't work. It means that, unlike the three above, there is no study to point to if someone asks where the advice comes from, so here they stay with no number and no name attached.

### How This Applies to a Real Menu

All of this psychology stops being theory the moment you decide a dish's final price, and that is where method D of the pricing sheet comes in: a price imposed from the guest's perception, not from cost or from what the place next door charges, with the sheet itself handing back the food cost you are left with once you apply it. In the "By Dish" sheet of menu-pricing-calculator.xlsx several methods live side by side, and the split already says something on its own: 4 dishes use the market price method and 5 use perceived value, which is exactly where this psychology lives. If the whole menu were priced at perceived value, the combined price would rise to $307.04; with the prices you finally went with, the whole menu comes to $266.90, and the food cost of the whole menu at those chosen prices stands at 36.7%. Two dishes illustrate the range from one method to the other: the croquettes end up at a menu price of $7.00 pre-tax, and the ribeye at $25.30 pre-tax. In the last column of the table below, an illustrative 10% sales tax is added on top, the same for every dish, to show what the guest pays at the register. The table lays out, dish by dish, which method was applied and what margin is left at the end. Read it with this psychology in mind and you will see why neither the market price nor the perceived value is "the right one" in the abstract: each answers a different question, and method D only makes sense when the dish has something real behind it to hold up that perception.

**When the Price Comes From Outside: Market and Perceived Value (menu-pricing-calculator.xlsx, "By Dish" Sheet)**

| Dish | Plate Cost ($) | Local Market Price ($) | Perceived Value Price ($) | Chosen Menu Price Pre-Tax ($) | Chosen Menu Price With 10% Illustrative Sales Tax ($) |
|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $9.12 | $9.63 | $7.00 | $7.70 |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $11.21 | $12.63 | $12.00 | $13.20 |
| Garlic shrimp | $6.90 | $17.36 | $18.60 | $13.40 | $14.74 |
| Broken eggs with fries and chistorra sausage | $2.40 | $9.21 | $10.58 | $8.00 | $8.80 |
| Local cheese board | $5.20 | $15.64 | $16.59 | $17.33 | $19.07 |
| Confit artichokes with ham | $3.10 | $10.14 | $11.55 | $10.33 | $11.37 |
| Roasted tomato soup with basil | $1.20 | $6.48 | $7.56 | $7.56 | $8.32 |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $18.68 | $20.07 | $18.68 | $20.55 |
| Confit cod with pil-pil sauce | $7.40 | $21.39 | $22.92 | $17.90 | $19.69 |
| Dry-aged beef burger with fries | $4.30 | $12.92 | $14.42 | $12.92 | $14.21 |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $17.38 | $18.70 | $16.70 | $18.37 |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $39.24 | $40.88 | $25.30 | $27.83 |
| Salt-baked sea bass | $8.90 | $23.98 | $25.72 | $19.40 | $21.34 |
| Free-range roast chicken with potatoes | $3.70 | $11.94 | $13.59 | $11.94 | $13.13 |
| Seasonal vegetable lasagna | $2.60 | $10.49 | $11.97 | $10.49 | $11.54 |
| Bluefin tuna tataki with sesame | $9.60 | $25.76 | $27.33 | $20.10 | $22.11 |
| Creamy cheesecake | $1.30 | $6.25 | $6.61 | $6.61 | $7.27 |
| Caramelized torrija (Spanish-style French toast) with ice cream | $1.10 | $5.17 | $5.83 | $5.83 | $6.41 |
| Chocolate lava cake | $1.60 | $6.70 | $7.13 | $7.13 | $7.84 |
| Prepared seasonal fruit | $1.40 | $4.05 | $4.73 | $4.73 | $5.20 |

*In the US and Canada, the menu shows the pre-tax price, so that is the number the guest reads and where the effects in this chapter (price endings, anchoring, format) operate. The sales tax is added at the register, and it is the last column that shows what the guest actually pays. In the UK and Australia, the printed price already includes VAT or GST, so the effects operate on that tax-inclusive figure, not on the net amount you work with.*


---

## 11. Menu Engineering I: Kasavana & Smith Done Right

### What the Matrix Measures and What It Leaves Out

The matrix you are about to use in this chapter compares every dish on two axes: popularity (units sold against the rest of its category) and contribution margin (CM) in dollars, not food cost as a percentage. The model is credited to Kasavana and Smith (1982), "Menu Engineering: A Practical Guide to Menu Analysis," and their contribution was to cross those two axes in a single quadrant chart instead of looking at them one at a time. Every dish on your menu is measured against two benchmarks, and both come from its own category: the popularity threshold and the weighted average CM. Never the average of the whole menu.

That detail, comparing within the category and not against the whole, is what separates a useful matrix from one that misleads you. If you throw starters, mains and desserts into a single calculation, an expensive main and a cheap dessert never compete on margin on equal terms. On this menu, the weighted average CM is $10.80 for mains, $7.46 for starters and $4.48 for desserts, against $8.16 for the menu as a whole. A dessert that outperforms its own category would still land below that overall average without having done anything wrong. The problem wouldn't be the dish; it would be the yardstick.

The matrix also works with averages over one sales period, so a small change to the menu (dropping an item, adjusting a portion, moving a price) can push another dish into a different quadrant even though its recipe hasn't changed at all. It is not a label you stick on a dish forever. It is a snapshot of this sales cycle, and you should repeat it whenever the menu changes in a meaningful way.

### The Popularity Threshold: Why It Is 70% Divided Among the Category's Dishes

The threshold comes from simple arithmetic. If a category has N dishes and sales were spread perfectly evenly, each dish would get one N-th of the units that category sells. The threshold in this matrix is 70% of that even share (the classic 70% rule), not 100%: demanding the full share would knock out half of a healthy menu. That factor sits in a cell instead of being hard-coded into the calculation, so if you want to be stricter about what you call "popular," you can raise it without touching anything else on the sheet. With the 20 items on this menu and the 4,870 units a month they sell together, each category starts from its own even split, and the 70% is applied to that split, never to the menu total.

With both benchmarks set, every dish lands in one of the four classic quadrants. On this menu there are 6 Stars, which add up to 1,950 units (40.0% of everything sold) and $14,865 in total CM; 6 Plowhorses with $16,198 between them; 5 Puzzles with $6,357; and 3 Dogs with 350 units and $2,318. The table below breaks out each dish within its category, and the one after it shows how much each quadrant weighs against the total.

The order of intervention is not the same for all four, and getting it wrong is expensive. You touch a Star very little and very carefully: it is a proven seller, and a sharp price increase can wreck exactly what makes it popular. A Puzzle (high margin, low units) calls for a redesign before a price move: changing its position on the menu or the way you present it usually moves more units than raising the price all at once. Pulling a dish is the last lever, never the first, because even a Dog can be propping up other items on the check. The guest who orders it may be the same one who later orders the bottle of wine or the dessert that does earn a margin, a joint reading the matrix cannot see by design.

### By Category, Always: A Dessert Doesn't Compete With a Main

The Kasavana and Smith (1982) matrix, presented in "Menu Engineering: A Practical Guide to Menu Analysis," crosses two axes: each dish's popularity, measured in units sold, and its CM in dollars, which is what is left of a dish after you subtract what it costs to make. Each dish is compared with a unit threshold and with the weighted average CM, and that comparison only makes sense within the dish's own menu category: starters against starters, mains against mains, desserts against desserts. Mixing them in a single table is the mistake that ruins the method, along with comparing each dish's margin against the simple average of the whole menu instead of the weighted average of its own category.

The reference menu in this chapter has 20 dishes with sales and adds up to 4,870 units sold per month, with a weighted average CM of $8.16 for the menu as a whole. But that $8.16 hides three different worlds: starters sit around a weighted margin of $7.46, mains climb to $10.80 and desserts stay at $4.48. An expensive main and a cheap dessert will never compete on margin, and that has nothing to do with how well designed either one is. Measured against the average of the whole menu, the dessert always comes out misclassified, simply because it belongs to a category with a lower average margin.

The popularity threshold is just as simple to build: if a category has N dishes, splitting units evenly would give each one an N-th of that category's sales. The threshold is 70% of that even share, and the 70% sits in its own cell of the spreadsheet rather than being baked into the method. If you want to demand more from your dishes, you change that number and the classification recalculates on its own.

### The Four Quadrants and What They Really Mean

Crossing popularity and margin against the thresholds gives you four quadrants. We keep their original names (Stars, Plowhorses, Puzzles, Dogs) because those are the ones you will find in any material on the subject:

- Star: sells a lot and earns a lot of margin. On this menu that is 6 dishes totaling 1,950 units, 40.0% of everything sold, and they contribute $14,865 in CM.
- Plowhorse: sells a lot but earns little margin. That is 6 dishes that together contribute $16,198.
- Puzzle: earns a good margin but doesn't sell much. That is 5 dishes with $6,357 of combined contribution.
- Dog: neither sells nor earns margin. That is 3 dishes, 350 units between them, $2,318 in total CM.

The order of intervention goes by risk, not by the alphabet of the quadrants. On a Plowhorse you raise the price carefully, in small steps: it is the dish the most people order, and a sudden jump gets noticed. On a Puzzle you redesign before touching the price: you change its name on the menu, move it to a better spot on the page, or test it next to a dish that pulls more orders. Removing a dish is the last lever, not the first: a Dog may be propping up other items on the average check, rounding out a prix fixe menu, or closing a group table that would have gone elsewhere without that option. Cutting it without looking at that effect can take sales with it that will never show up on its own row of the matrix.

The matrix itself admits its limit: it works with averages, so a small change to the menu (a new dish, a price increase on another, a seasonal swap) can move a dish to a different quadrant without anything changing in its recipe. The chart below, with the menu classified dish by dish within its category, and the table below it, with the weight of each quadrant, are a snapshot of this moment, not a permanent label.

### What You Do With Each One, in Order of Risk

Kasavana and Smith (1982), in "Menu Engineering: A Practical Guide to Menu Analysis," set out the seminal model of menu engineering on two axes: each dish's popularity, in units sold, and its CM in dollars, selling price minus ingredient cost. Each dish is measured against two benchmarks: a popularity threshold and the weighted average CM of ITS category. The "Kasavana-Smith" sheet of `menu-engineering-matrix.xlsx` makes that comparison dish by dish, with the underlying breakdown on the "Data" sheet of the same workbook.

The threshold doesn't come from a historical average; it comes from an even split. If a category has N dishes, splitting sales evenly would give each one an N-th, and the threshold is set at 70% of that share (popularity threshold factor: 70%). That percentage lives in a cell on the "Data" sheet, so anyone who wants to demand more only has to raise it. With the 4,870 units sold per month across the menu's 20 dishes with sales, the cutoff is calculated category by category, never on the total.

Applying the matrix to the whole menu, mixing starters, mains and desserts in a single cloud of points, is the mistake that makes it useless. The weighted average CM of mains ($10.80) and of desserts ($4.48) are not in the same league, so a well-selling, well-designed dessert would always fall below the margin threshold just for sitting next to a main, which says nothing about its real profitability. That is why each category is read against its own average: starters against theirs ($7.46), mains against theirs ($10.80) and desserts against theirs ($4.48). The $8.16 average of the whole menu serves as a snapshot of the overall picture, never as the cutoff for a specific dish.

With the four labels in place (Star: high in popularity and in margin; Plowhorse: lots of sales, thin margin; Puzzle: good margin, few sales; and Dog: low on both metrics), you intervene from lowest risk to highest.

- Stars first, and carefully: these are the 6 dishes that already meet both conditions, move 1,950 units a month (40.0% of all the menu's sales) and contribute $14,865 in CM, the biggest block of the four quadrants. The work here is watchfulness: if you touch the price, raise it a little and measure the reaction before repeating.
- Plowhorses next: popular, but with margin below the threshold for their category. These are 6 dishes that already contribute $16,198. Here you raise the price, review the recipe cost card to trim cost without the guest noticing on the plate, or do both at once, making sure sales don't drop below the threshold that classified the dish here.
- Puzzles get redesigned, not tweaked: these are 5 dishes with a good margin ($6,357 between them) and short sales, so the job isn't about price. It is about the name, the photo, the placement on the page or a server's suggestion, to add the missing units without touching the margin.
- Dogs are the last intervention, and not the automatic one. Before you pull a dish, check whether it supports the average check of what gets ordered alongside it, or whether its presence still serves a purpose even though it sells little. The 3 Dogs in this example move 350 units among the three and contribute $2,318 in CM; the table below shows what each quadrant puts on the menu total.

Don't lose sight of the caveat the model's own authors put in writing: the matrix works with averages over one sales period, so a small change in the mix (a seasonal dish coming in or out, or a one-off promotion) can move a dish to a different quadrant from one month to the next. It is not a label you stick on once and forget. It is a snapshot you have to repeat.

**The Menu Classified Dish by Dish, Within Its Category (`menu-engineering-matrix.xlsx`, "Kasavana-Smith" Sheet)**

| Dish | Category | Units | Menu Mix in Category (MM%) | Threshold (%) | Popularity | Dish CM ($) | Category Avg CM ($) | Classification |
|---|---|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | Starters | 420 | 24.3% | 10.0% | High | $6.50 | $7.46 | Plowhorse |
| Heirloom tomato salad with tuna belly and scallions | Starters | 310 | 17.9% | 10.0% | High | $8.20 | $7.46 | Star |
| Garlic shrimp | Starters | 260 | 15.0% | 10.0% | High | $8.60 | $7.46 | Star |
| Broken eggs with potatoes and chistorra sausage | Starters | 380 | 22.0% | 10.0% | High | $7.40 | $7.46 | Plowhorse |
| Local cheese board | Starters | 90 | 5.2% | 10.0% | Low | $8.40 | $7.46 | Puzzle |
| Confit artichokes with ham | Starters | 120 | 6.9% | 10.0% | Low | $7.80 | $7.46 | Puzzle |
| Roasted tomato soup with basil | Starters | 150 | 8.7% | 10.0% | Low | $6.00 | $7.46 | Dog |
| Iberico pork tenderloin with sweet potato purée | Mains | 340 | 16.8% | 7.8% | High | $11.63 | $10.80 | Star |
| Confit cod in pil-pil sauce | Mains | 190 | 9.4% | 7.8% | High | $11.70 | $10.80 | Star |
| Dry-aged beef burger with fries | Mains | 460 | 22.8% | 7.8% | High | $9.30 | $10.80 | Plowhorse |
| Creamy rice with Iberico pork secreto and mushrooms | Mains | 270 | 13.4% | 7.8% | High | $10.20 | $10.80 | Plowhorse |
| Dry-aged bone-in ribeye (17.64 oz) | Mains | 110 | 5.4% | 7.8% | Low | $17.90 | $10.80 | Puzzle |
| Salt-baked sea bass | Mains | 80 | 4.0% | 7.8% | Low | $12.90 | $10.80 | Puzzle |
| Free-range roast chicken with potatoes | Mains | 300 | 14.9% | 7.8% | High | $9.00 | $10.80 | Plowhorse |
| Seasonal vegetable lasagna | Mains | 140 | 6.9% | 7.8% | Low | $8.80 | $10.80 | Dog |
| Seared bluefin tuna tataki with sesame | Mains | 130 | 6.4% | 7.8% | Low | $12.80 | $10.80 | Puzzle |
| Creamy cheesecake | Desserts | 520 | 46.4% | 17.5% | High | $4.60 | $4.48 | Star |
| Caramelized torrija with ice cream | Desserts | 210 | 18.8% | 17.5% | High | $4.40 | $4.48 | Plowhorse |
| Chocolate lava cake | Desserts | 330 | 29.5% | 17.5% | High | $4.60 | $4.48 | Star |
| Prepared seasonal fruit | Desserts | 60 | 5.4% | 17.5% | Low | $3.10 | $4.48 | Dog |

**How Much Each Quadrant Weighs (`menu-engineering-matrix.xlsx`, "Kasavana-Smith" Sheet)**

| Classification | Dishes | Units Sold | % of Menu Units | Total CM Contributed ($) |
|---|---|---|---|---|
| Star | 6 | 1,950 | 40.0% | $14,865 |
| Plowhorse | 6 | 2,040 | 41.9% | $16,198 |
| Puzzle | 5 | 530 | 10.9% | $6,357 |
| Dog | 3 | 350 | 7.2% | $2,318 |

*Look at the last column before you change anything: some quadrants with only a few dishes carry a big share of the month's margin.*


---

## 12. Menu Engineering II: What the Classic Matrix Can't See

### Miller: Popularity Against Food Cost Percentage

The classic matrix crosses two variables, popularity and contribution margin, and that is enough to read any menu at first glance. But there is a third variable that reading leaves out, food cost percentage, and no model measures all three at once: each one picks two of the three (popularity, food cost percentage and margin in dollars) and drops the one it doesn't need. That is why, applied to the same menu, the different models don't always crown the same dish as the winner. That discrepancy is not a calculation error. It is information, and reading it well is the thread that runs through this chapter.

Miller (1980) is the model for the operator who buys well. It crosses popularity with food cost percentage and rewards the dish that sells a lot at a low food cost, without looking at how many dollars each unit sold leaves behind. On the reference menu, the Winner group brings together 8 dishes that account for 2,940 units sold (60.4% of everything that leaves the kitchen) at a weighted average food cost of 26.9%, below the 32.7% of the full menu. The Loser group, with 5 dishes, climbs to 40.7%; the Marginal group sits in the middle, with 7 dishes. The risk of this reading is also its virtue: it can crown as a Winner a dish that is cheap to buy and sells a lot, even if the margin it leaves in dollars is slim. Miller doesn't see that, because it isn't the variable it measures.

### Pavesic: Food Cost Percentage Against Unit-Weighted Margin

Pavesic (1983) corrects that blind spot. Instead of looking only at the percentage, it weights each dish's CM by the units sold, so a high-margin dish almost nobody orders stops looking great once you multiply it by its real volume. On the same menu, the Prime group, 7 dishes, contributes a total weighted CM of $21,408; the Problem group, with 6 dishes, comes in at $7,830; between the two sit the Standard group, with 3 dishes, and the Sleeper group, with 4. The table below spreads those dollars out dish by dish.

Hayes and Huffman (1985), in "Menu Analysis: A Better Way," published in the Cornell Hotel and Restaurant Administration Quarterly, propose a way out that is no longer a quadrant matrix: Goal Value Analysis reduces food cost, selling price, popularity and variable costs to a single index per dish, and their criticism of the quadrant approach is precisely that it leans on averages of the whole menu instead of on the goal for each dish. With labor cost at 32% of sales and other variable costs at 10% (the two percentages that feed the index, which live in editable cells in the workbook), 9 dishes on the menu land above the goal for their own category and 11 below. The index has no units and is not expressed in dollars: it can only be read against the goal for its own category, never in absolute terms and never against dishes from another category.

LeBruto, Quain and Ashley (1995), in "Menu Engineering: A Model Including Labor," published in the FIU Hospitality Review, add labor cost to the Kasavana and Smith model and split its four quadrants into eight. Their key line is the one that organizes this whole chapter: operators bank dollars, not percentages.

### Goal Value: One Index per Dish Instead of Quadrants

Popularity, food cost percentage and margin in dollars are the three variables that decide whether a dish is worth having, and each model picks two and leaves the third out. That is why Miller, Pavesic and Goal Value can classify the same dish three different ways without any of them being wrong, and the discrepancy is information the classic matrix alone doesn't give you.

Miller (1980) set out the first matrix model that crosses food cost with sales mix, a forerunner of the Kasavana and Smith matrix: it rewards low food cost with volume, and it can crown a high-turnover dish a winner even if it leaves few dollars of margin. On your menu it flags 8 Winners (2,940 units sold, 60.4% of the total, weighted average food cost 26.9%), 7 Marginals and 5 Losers, the latter with a weighted average food cost of 40.7%.

Pavesic (1983) corrects that blind spot: it swaps the individual CM for the CM weighted by units sold, so a high-margin, low-volume dish stops looking great. On your menu it flags 7 Primes, with $21,408 of combined weighted margin; 3 Standards, 4 Sleepers and 6 Problems, the latter with $7,830 of combined weighted margin.

Goal Value is not a third matrix. It is the alternative from people who saw the problem in the quadrant format itself. Hayes and Huffman (1985), "Menu Analysis: A Better Way," in the Cornell Hotel and Restaurant Administration Quarterly, criticized the way Miller and Pavesic sort dishes against a menu average that shifts with every dish that comes in or out. Their alternative: a single index per dish that combines food cost, selling price, popularity and variable costs, with no quadrant and no average. On your menu it uses labor cost of 32% of sales and other variable costs of 10%, and compares each dish with the goal for its category: 9 dishes above and 11 below, on a weighted average menu food cost of 32.7%.

That index carries no units: not a dollar price and not an absolute percentage, so comparing it across categories, a stew against a fish dish, tells you nothing. It only counts when read against the goal for its own category, which is what the table below does, dish by dish.

### LeBruto: What Happens When Labor Cost Comes In

LeBruto, Quain and Ashley (1995), "Menu Engineering: A Model Including Labor," in the FIU Hospitality Review, added to the Kasavana and Smith matrix what neither Miller, Pavesic nor Goal Value had included: the labor cost of each dish. It isn't a new sheet but an added reading on the same matrix: each dish is also classified as high or low labor cost, and that layer splits the four classic quadrants into eight, the 8 quadrants of the extended matrix against the original 4.

Their line organizes the chapter: operators bank dollars, not percentages. A dish with a low food cost and a lot of kitchen work behind it can cost you in labor what you save on ingredients, and the classic matrix doesn't show that because it only looks at two variables at a time. It doesn't replace Goal Value or Pavesic's weighted margin: it asks you to add that question to any of the three, before you set the selling price or push a dish from the floor. It is what separates food cost percentage from the margin in dollars that actually lands in the till, and what turns Miller, Pavesic and Goal Value into three angles on the same problem, not competing answers.

### The Three Variables and Why No Method Measures Them All

Popularity, food cost percentage and CM in dollars are the three variables that define a dish's real profitability, and no model looks at all of them at once: each keeps two and leaves the third out. That is why, when two matrices applied to the same menu put the same dish in different groups, there is no calculation error behind it, just a different question. The discrepancy is not noise to be settled in favor of a single table. It is information, and reading it well takes knowing which variable each method left out.

Miller (1980) is the model for the operator who buys well. It crosses popularity and food cost percentage, and rewards with the Winner label the dish that pairs high demand with a low ingredient cost, leaving out precisely how many dollars of margin each unit served produces. It was the first matrix model to cross food cost and product mix, a direct forerunner of the classic Kasavana and Smith matrix. Applied to this menu, and as the table below shows, the eight Winners add up to 2,940 units sold (60.4% of everything that leaves the kitchen) at a weighted average food cost of 26.9%. That is where its blind spot lies: it buys cheap and sells a lot, but it can leave few dollars per guest if the selling price came up short. The five Losers carry a weighted average food cost of 40.7%, and the seven Marginals sit between the two.

Pavesic (1983) corrects that blind spot: it swaps the individual CM for the CM weighted by units sold, so a high-margin dish almost nobody orders stops looking great once you multiply it by its real volume. On this menu, the seven Primes contribute $21,408 of weighted margin between them, against the $7,830 the six Problems add up to: the distance between a dish that holds up the till and one that only looks good on the recipe cost card. Between the two sit three Standards and four Sleepers, a nuance Miller doesn't see because it never crosses volume and margin.

Hayes and Huffman (1985), in "Menu Analysis: A Better Way," published in the Cornell Hotel and Restaurant Administration Quarterly, proposed a way out that is not a matrix: Goal Value Analysis condenses food cost, selling price, popularity and variable costs into a single index per dish, and they criticize the quadrant approach for leaning on whole-menu averages that dilute what is happening to each item. Here the index is calculated with labor cost of 32% of sales and other variable costs of 10% of sales, both editable in the spreadsheet; with those, nine dishes land above the goal for their category and eleven below. Goal Value carries no dollars or percentage of its own: it is an index that only makes sense compared with the goal for its own category, never in absolute terms and never against another category's.

LeBruto, Quain and Ashley (1995), in "Menu Engineering: A Model Including Labor," published in the FIU Hospitality Review, don't propose another spreadsheet. They propose a different reading of the same matrix. They bring labor cost into the Kasavana and Smith model and split each of the four classic quadrants in two, depending on whether the dish carries a lot or a little labor cost, ending up with eight quadrants instead of the original four. Their line sums up the whole chapter: operators bank dollars, not percentages. It takes importance away from food cost percentage in isolation in favor of the margin a dish really leaves behind, and that is the idea that carries you from one table to the next: each method looks at a different part of the same menu, and none of them replaces the other three.

**Miller: How Much Each Group Weighs (`menu-engineering-matrix.xlsx`, "Miller" Sheet)**

| Classification | Dishes | Units Sold | % of Menu Units | Group Weighted Avg Food Cost (%) |
|---|---|---|---|---|
| Winner | 8 | 2,940 | 60.4% | 26.9% |
| Marginal | 7 | 1,460 | 30.0% | 32.0% |
| Loser | 5 | 470 | 9.7% | 40.7% |

**Pavesic: How Much Weighted Margin Each Group Contributes (`menu-engineering-matrix.xlsx`, "Pavesic" Sheet)**

| Classification | Dishes | Units Sold | % of Menu Units | Group Total Weighted CM ($) |
|---|---|---|---|---|
| Prime | 7 | 2,730 | 56.1% | $21,408 |
| Standard | 3 | 860 | 17.7% | $6,508 |
| Sleeper | 4 | 620 | 12.7% | $3,992 |
| Problem | 6 | 660 | 13.6% | $7,830 |

**Goal Value Dish by Dish, Against the Goal for Its Category (`menu-engineering-matrix.xlsx`, "Goal Value" Sheet)**

| Dish | Menu Price, Pre-Tax ($) | Food Cost (%) | Dish Goal Value | Category Goal Value Target | Reading |
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

*Goal Value is an INDEX, not a dollar amount: it only makes sense compared with the goal for its own category, which is the column right next to it.*


---
## 13. When the Methods Disagree: The Decision Protocol

### Agreement Is Not Confidence: What It Means When All Four Methods Match

Of the 20 dishes with sales on the menu, only 3 land in the best category on all four readings at once, with zero readings off: 15.0% of the menu. It is tempting to read those dishes as "the ones that are already fine" and stop looking at them. That is exactly the mistake this chapter exists to prevent, because agreement only tells you the models agree with each other. It does not tell you the dish is healthy. All four methods start from the same recipe cost card, the same menu price and the same sales history. If that input carries a bias (a portion that was weighed wrong, a one-off promotion that spiked units in a single month), the bias travels into all four results equally, and they will agree on the error just as cleanly as they would agree on the truth.

Here is a quick reminder of who is who, without repeating what we covered when each one was introduced. Kasavana and Smith built the matrix that crosses popularity and contribution margin into quadrants. Miller and Pavesic each reworked that idea in their own way. Hayes and Huffman's Goal Value drops the quadrant matrix and boils those same two variables down to a single numeric index per dish. None of the four is more "correct" than the others. They are four ways of projecting the same reality onto different axes, and the value of having them side by side is not in averaging them or picking the one you like best. The value is in treating the point where they split as a signal.

That shared starting point has a concrete reference on this menu: the weighted average contribution margin is $8.16. It is the yardstick each model uses to decide whether a dish "leaves" enough on the table, and even starting from the same number, each one combines it with popularity or with food cost in a different way. That is where disagreement begins: not in the data, but in how it is read afterward. There is also a fifth reading worth keeping in mind, even though it is not one of the four this chapter sorts: LeBruto, Quain and Ashley (1995) added labor cost to the Kasavana and Smith model and expanded the original 4-quadrant matrix to 8, classifying each dish by whether its labor cost is high or low. The authors sum it up in a line worth remembering whenever you read any of these results: "Operators bank dollars, not percentages." That is the same principle behind the next two patterns.

### The Most Common Disagreement Patterns

Of the 20 dishes, 12 have three or four readings outside their expected band: 4 of them have three readings off and 8 have all four. At the other end, 4 dishes have a single reading off and 1 has two readings off, which is 5.0% of the menu. On this menu, disagreement is not the exception. It is the majority, so you need to know how to read it rather than write it off as noise from the models.

Three patterns show up more often than any others:

- High margin with a poor food cost percentage: this is a dish built on expensive product that still leaves real dollars per guest served. The usual mistake is to look only at the percentage, see that it runs high, and sentence the dish as a problem. The decision is almost never to pull it. You review the menu price or the portion size, because the contribution margin has already shown that the guest is willing to pay it.
- Excellent food cost percentage with a low margin: it sells a lot and leaves little per unit. That dish earns its spot not on the P&L but on the check, in what it pulls in around it and in the volume it keeps the dining room running on. You decide whether to keep it as a commercial hook or to adjust the price so that favorable food cost starts turning into real contribution margin.
- Low popularity across every model: before you pull the dish, check whether the problem is the dish itself or its description and its place on the menu. A solid dish in the wrong spot, with a name that doesn't sell or sitting next to a cheaper direct competitor on the same page, can read like a failure without being one.

The rule that ties these three patterns together is simple to state and easy to skip: never touch more than two or three dishes at a time. Every price or portion change moves the sales mix of the whole menu and, with it, the thresholds for every other dish. What sits above the average margin today can fall below it as soon as what sells most changes. After each round you measure again with all four models. You don't assume the adjustment worked because your gut says so. The table below shows, dish by dish, where each reading agrees and where it splits.

### The Four Rs: Reformulate, Reprice, Redesign, Remove

When all four methods (the original Kasavana and Smith, Miller's reformulation, Pavesic's, and the Hayes and Huffman Goal Value) agree on a dish, do not read that agreement as validation. The four start from the same inputs: the same sales, the same cost from the recipe cost card and the same menu price. If that source data was loaded wrong, all four models inherit it equally, and four readings in agreement about a mistake are still a mistake. What really gives you information is the exact point where the methods stop agreeing, because that is where each one looks at a different variable of the same equation.

Of the 20 dishes with sales on the menu, 3 get the most favorable reading in all four methods at once, which is 15.0% of the menu and the same 3 with zero readings off. 4 dishes have a single reading off, 1 has two readings off (5.0% of the menu), and 12 have three or four readings off the best category: of those, 4 have three readings off and 8 have all four off. Those 12 are the ones that demand a dish-by-dish look at the table below, not a quick glance, because that is where the three patterns that repeat most often appear.

The first is high margin with a poor food cost percentage: a dish built on expensive product (fish, shellfish, a prime cut of beef) that leaves a solid contribution margin in dollars even though its cost percentage against the menu price runs high, because the base product is expensive too. You don't pull that dish. You rework the portion or raise the price, because the question isn't whether it's worth selling but how much you're charging to sell it.

The second pattern is the reverse: excellent food cost percentage with a low contribution margin. It sells a lot and leaves little per unit. That dish's job isn't on the P&L, it's on the check: it drives guest counts or pulls in sales of other dishes, and what you owe it is a deliberate decision about whether it stays as a hook on your menu. The labor-cost extension of the Kasavana and Smith model, published by LeBruto, Quain and Ashley (1995), expands the original 4-quadrant matrix to 8 precisely to separate these two cases, and its authors boil it down to a line worth keeping in mind when you read any percentage: "Operators bank dollars, not percentages."

The third pattern is low popularity across all four models at once. Before you pull the dish, check whether the problem is the dish or its description and its place on the menu. A name that says nothing, a spot lost in the middle of a long page or a missing photo are enough to sink the sales of something that, told another way, works. Redesigning (changing the copy, the position, the photo) comes before removing, and only when the redesign has been tested and sales still haven't moved does it make sense to take the dish off the menu.

### The Order of Intervention and How Many Dishes to Touch at Once

The four Rs are not a closed algorithm. They are an order of intervention, from the lightest change to the most drastic, and the person who decides where to stop is the one who knows the guest, not the matrix. Reformulating (touching the recipe or the portion) and repricing (touching the price) are the cheapest moves and the easiest to reverse if they don't work. Redesigning (touching how the dish is described and where it sits) takes more work but still takes nothing off the menu. Removing is the only move you can't undo without rewriting the recipe cost card and reshooting the photo, so it goes last, reserved for third-pattern dishes that have already been through a redesign without moving.

The operating rule behind this whole chapter is to never touch more than two or three dishes at a time. Every change in price, portion or position moves the sales mix of the entire menu, and that mix is the input all four methods depend on: the weighted average contribution margin of the menu, today at $8.16, gets recalculated with every intervention, and with it the popularity and food cost thresholds shift for the rest of the dishes, not just the one you touched. Changing half the menu at once invalidates the next reading before you've even taken it.

After each round of two or three dishes, run the four methods again and check, once more, where they disagree. The original popularity-and-contribution-margin matrix and Hayes and Huffman's Goal Value Analysis, which boils each dish down to a single numeric index instead of placing it in a quadrant matrix, do the same job here that they did in the first reading: confirming whether the change moved the dish to a new category or just pushed the problem somewhere else on the menu.

**The Four Readings of the Same Dish, Side by Side (menu-engineering-matrix.xlsx, "Comparison" sheet)**

| Dish | Category | Kasavana & Smith | Miller | Pavesic | Goal Value | Readings Off | Suggested Decision |
|---|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | Starters | Plowhorse | Winner | Prime | Above target | 1 | Reprice |
| Heirloom tomato salad with tuna belly and scallions | Starters | Star | Winner | Prime | Above target | 0 | Keep |
| Garlic shrimp | Starters | Star | Marginal | Standard | Below target | 3 | Review |
| Broken eggs with potatoes and chistorra sausage | Starters | Plowhorse | Winner | Prime | Above target | 1 | Reprice |
| Local cheese board | Starters | Puzzle | Loser | Problem | Below target | 4 | Redesign |
| Confit artichokes with ham | Starters | Puzzle | Marginal | Sleeper | Below target | 4 | Redesign |
| Roasted tomato soup with basil | Starters | Dog | Marginal | Sleeper | Below target | 4 | Review |
| Iberico pork tenderloin with sweet potato purée | Mains | Star | Winner | Prime | Above target | 0 | Keep |
| Confit cod in pil-pil sauce | Mains | Star | Marginal | Problem | Below target | 3 | Reformulate |
| Dry-aged beef burger with fries | Mains | Plowhorse | Winner | Prime | Above target | 1 | Reprice |
| Creamy rice with Iberico pork secreto and mushrooms | Mains | Plowhorse | Marginal | Standard | Above target | 3 | Reprice |
| Dry-aged bone-in ribeye (17.64 oz) | Mains | Puzzle | Loser | Problem | Below target | 4 | Redesign |
| Salt-baked sea bass | Mains | Puzzle | Loser | Problem | Below target | 4 | Redesign |
| Free-range roast chicken with potatoes | Mains | Plowhorse | Winner | Prime | Above target | 1 | Reprice |
| Seasonal vegetable lasagna | Mains | Dog | Marginal | Sleeper | Below target | 4 | Review |
| Seared bluefin tuna tataki with sesame | Mains | Puzzle | Loser | Problem | Below target | 4 | Redesign |
| Creamy cheesecake | Desserts | Star | Winner | Prime | Above target | 0 | Keep |
| Caramelized torrija with ice cream | Desserts | Plowhorse | Winner | Sleeper | Below target | 3 | Reprice |
| Chocolate lava cake | Desserts | Star | Marginal | Standard | Above target | 2 | Review |
| Prepared seasonal fruit | Desserts | Dog | Loser | Problem | Below target | 4 | Remove |

**How Many Dishes Disagree, and by How Much (menu-engineering-matrix.xlsx, "Comparison" sheet)**

| Readings Off the Best Category | Dishes | % of the Menu |
|---|---|---|
| 0 | 3 | 15.0% |
| 1 | 4 | 20.0% |
| 2 | 1 | 5.0% |
| 3 | 4 | 20.0% |
| 4 | 8 | 40.0% |

*The left-hand column isn't a footnote: it is the number of models that pull the dish out of its best category. The higher the number, the more all four agree that something needs a second look.*


---

## 14. Short Menus, Prix Fixe, Buffets and Banquets

### Menu Size: What You Gain by Pruning and What You Lose

Pruning your menu isn't an aesthetic question. It's kitchen logistics. Every dish you add drags along its own stock, its own trim loss and waste when it doesn't move the way you expected, and one more line the crew has to master at the pass. Fewer items means buying from fewer vendors, so the volume per line goes up and so does your negotiating power with each of them. Fewer dishes also means less open product in the walk-in and fewer portions going in the trash at close because nobody ordered them. The sample menu in this guide has 20 dishes, and that number isn't a recommendation. It's just the starting point for the examples that follow.

What you give up when you cut is coverage. Every dish that disappears leaves out the guest who only came for it, the allergy that only that option covered, or the party that needed a vegetarian or gluten-free alternative to close out the whole table. You also lose room to move with the seasons, because a short menu has less space to rotate seasonal product without pulling something permanent. There is no optimal number. You decide dish by dish, looking at what sales each item pulls in and what stock it takes to keep it alive, leaning on the data you already work with.

### Prix Fixe Menus: The Mix Decides the Margin

In a prix fixe menu the revenue is settled before the first guest sits down. The menu price is $13.18 pre-tax per prix fixe served; with an illustrative 10% sales tax, the guest pays $14.50 at the table (in the UK or Australia, a tax-inclusive price of $14.50 would work the same way and you would strip the tax out to get back to $13.18). That revenue doesn't move no matter how completely what people order changes, so your result for the month depends entirely on the mix. Managing a prix fixe menu is, in practice, managing that split.

The table below shows it with the same menu, the same price and the same service volume (100 prix fixe menus a month), changing only what people choose. With the base mix, the average menu cost is $5.63, with a food cost of 42.7% and a contribution margin of $7.55 per menu that, multiplied by the month's volume, leaves $754.93. If guests lean toward the expensive options in Scenario A, the average cost climbs to $5.93, food cost to 45.0% and the monthly margin drops to $725.18. If the mix tilts toward the cheaper options in Scenario B, the average cost falls to $5.35, food cost to 40.6% and the monthly margin rises to $782.93. Same menu, same price, same 100 guests, three different results: the whole difference is in what gets ordered, not in what gets charged.

The real lever isn't raising the menu price. If your most expensive dish is also your most ordered, you change its place on the specials board or the lunch menu, or you strengthen the appeal of the cheaper alternative to shift demand toward Scenario B. And there is one cost that many recipe costing sheets for a prix fixe lunch leave out: table bread, coffee and the included drink aren't part of any dish's price in the mix, and yet you serve them every time. On this sample menu that fixed cost per menu is $0.55, and against a $13.18 pre-tax price it weighs enough that you shouldn't treat it as a minor detail.

Outside the à la carte menu, the same principle changes shape. In a buffet, at a banquet and in a hotel, you don't cost per plated portion but per guest served, and the number that governs that calculation is measured consumption per head, which isn't in any book: you have to measure it in your own house, service by service. As an international point of contrast, typical food cost for hotel F&B and buffet runs between 28% and 40% of sales (Cucinovo, Food Cost % by Restaurant Type, 2026). In catering and events you don't see the mix after you serve: it is agreed in the proposal the client signs, so the menu engineering work has to happen before that signature, not after the service.

### The Two Mix Scenarios and What to Do With Them

In a prix fixe menu the revenue is already settled before the first guest sits down: $13.18 pre-tax, which becomes $14.50 at the table once the same illustrative 10% sales tax is added (a flat rate on everything served at the table, alcohol included). What isn't settled is the cost, because it depends on what people choose in each course. Managing a prix fixe menu is, in practice, managing that split: the mix.

The table below shows it with the same menu, the same price and the same service volume (100 menus a month) spread across three scenarios. With the base mix, the average cost is $5.63, food cost is 42.7% and the contribution margin is $7.55 per menu, or $754.93 a month. In Scenario A, with guests leaning toward the priciest options, cost rises to $5.93, food cost to 45.0% and the margin falls to $7.25, or $725.18 a month. In Scenario B, tilted toward the budget options, cost drops to $5.35, food cost to 40.6% and the margin rises to $7.83, or $782.93 a month. Price, tax and guest count are identical. Only what gets ordered changes, and that alone is enough to move the whole month.

That is the real lever. If the most expensive dish on the menu also turns out to be the most ordered, you don't touch the menu price: you change its place on the board or strengthen the alternative that competes with it, to bring the split closer to Scenario B. This menu's food cost target is 30%, right inside the 28-32% range commonly cited for traditional full-service restaurants, so a drift toward Scenario A (45.0%) hurts twice over. And there is a cost that many recipe costing sheets for a prix fixe lunch overlook: bread, coffee and the included drink add up to $0.55 of fixed cost per menu, before the guest has chosen anything. On a $13.18 pre-tax check, that up-front deduction weighs far more than on a high-check menu, and you should subtract it from the menu price before calculating each option's margin, not after.

### Buffet, Banquet and Hotel: The Same Problem at a Different Scale

In buffet, banquet and hotel F&B the problem is the same (revenue settled, result dependent on what gets consumed) but the unit of cost changes: you don't cost per plated portion, because there is no fixed portion, but per guest served. The number that governs that calculation is average consumption per head, and it doesn't come from any book or any template. You measure it in your own house, service by service, because every offer and every guest profile consumes differently. Cucinovo, in its Food Cost % by Restaurant Type report (2026), puts food cost for hotel F&B and buffet between 28% and 40% of sales. Treat it as a point of contrast and an order of magnitude, never as the number you have to hit in a specific house.

In catering and events the mix isn't managed during service: it is agreed in the proposal you sign with the client, with the menu, quantities and options locked weeks before a single plate hits the table. That is why the engineering work for this format happens before signing and not after serving: in the proposal you decide what goes into each option, at what cost and what margin it leaves. Once the quote is signed, you have no room left to correct the split with the board or any other gesture from the dining room.

### Catering and Events: The Mix Is Settled Beforehand

In catering and events the revenue isn't just settled the way it is in a prix fixe menu: it is signed weeks or months before a single plate is served. The guest doesn't choose at the table. If they choose at all, they choose on an options form that the client forwards to the organizer with as many days of notice as the contract sets. That moves all the engineering work to the moment you write the proposal. That is where you decide which options go on the event menu, how many main course alternatives you offer and what goes with each one. Once the client signs and confirms the headcount, there is no room left to correct the mix by moving a dish around the menu or improving the alternative competing with it inside the same menu, as you can in the day-to-day of a prix fixe menu. The correction here either happens before signing, or it doesn't happen.

That forces you to cost every event option with its own recipe cost card before you send the quote, not after it's accepted. It also means modeling at least two or three plausible mix splits in advance (a comfortable one, a realistic one and a demanding one) to check that the price per guest survives the worst of the three, not just the one that suits you best. A quote that has only been tested against the most favorable split is a quote that can lose margin the moment guests choose differently than expected.

It also pays to separate, in the calculation, what scales with each guest from what doesn't. The per-head cost covers the food and drink served. Front-of-house and kitchen staff, rental of smallwares, linens or a tent, and transport logistics don't grow in the same proportion as the guest count, and mixing everything into a single figure per guest hides which line is bleeding margin when the event is small.

In practice, this comes down to a few decisions you should always make at the same stage, before the event is accepted:

- Close the event options catalog, with its true cost already calculated, before the salesperson sits down to negotiate with the client.
- Set the deadline and the method for confirming the guest breakdown by option in the contract itself, because that breakdown is the real mix of the event.
- Require a minimum guaranteed guest count to be billed, so that a lower final headcount doesn't push the same fixed cost onto fewer heads.
- When the event closes, review the margin with the mix that was finally confirmed and not just the one you budgeted, so the next proposal starts from real data.

The logic is the same one that governs any prix fixe menu: the result depends on what people choose, not on the price you charge. In catering and events, though, all of that engineering has to be finished before the client signs, because after the signature there is no lever left to pull.

**The Menu Options and the Three Mix Splits (menu-engineering-matrix.xlsx, "Prix Fixe Menu" sheet)**

| Course | Option | Plate Cost ($) | Base Mix (%) | Scenario A Mix (%) | Scenario B Mix (%) |
|---|---|---|---|---|---|
| First courses | Garden salad | $1.10 | 40% | 25% | 35% |
| First courses | Pumpkin soup | $1.05 | 25% | 20% | 45% |
| First courses | Pasta with pesto | $1.60 | 35% | 55% | 20% |
| Main courses | Roast chicken with potatoes | $2.80 | 45% | 30% | 60% |
| Main courses | Battered hake | $3.90 | 30% | 45% | 15% |
| Main courses | Beef meatballs | $3.20 | 25% | 25% | 25% |
| Desserts | Homemade flan | $0.50 | 55% | 40% | 70% |
| Desserts | Seasonal fruit | $0.70 | 45% | 60% | 30% |

*Each of the three splits adds up to 100% within every course; the only thing that changes between scenarios is which option guests take.*

**The Average Cost of Each Course by Mix (menu-engineering-matrix.xlsx, "Prix Fixe Menu" sheet)**

| Course | Base Average Cost ($) | Scenario A Average Cost ($) | Scenario B Average Cost ($) |
|---|---|---|---|
| First courses | $1.26 | $1.37 | $1.18 |
| Main courses | $3.23 | $3.39 | $3.06 |
| Desserts | $0.59 | $0.62 | $0.56 |

**The Same Menu, the Same Price, Three Results (menu-engineering-matrix.xlsx, "Prix Fixe Menu" sheet)**

| Item | Base Mix | Scenario A | Scenario B |
|---|---|---|---|
| Average cost of first courses ($) | $1.26 | $1.37 | $1.18 |
| Average cost of main courses ($) | $3.23 | $3.39 | $3.06 |
| Average cost of desserts ($) | $0.59 | $0.62 | $0.56 |
| Fixed costs per menu ($) | $0.55 | $0.55 | $0.55 |
| Total average menu cost ($) | $5.63 | $5.93 | $5.35 |
| Menu food cost (%) | 42.7% | 45.0% | 40.6% |
| Contribution margin per menu ($) | $7.55 | $7.25 | $7.83 |
| Margin on prix fixe menus served per month ($) | $754.93 | $725.18 | $782.93 |


---
## 15. Multichannel: Dine-In, Takeout and Third-Party Delivery

### Three Channels, Three P&Ls

Your menu doesn't change from one channel to the next, but your P&L does. The app's commission isn't subtracted from your margin like a fixed cost per dish: it's charged on the selling price, so it grows with the price. The same dish at the same price runs a different effective food cost in dine-in, in takeout and in third-party delivery, and that's the number you need to watch, not the one on your dine-in menu.

The simulator sets the target food cost at 30% for dine-in and takeout and raises it to 40% for delivery, to absorb the app's commission, which is set at 30% of the selling price. The "Summary" sheet of multichannel-repricing-simulator.xlsx shows the average effective food cost across the menu: 31.4% in dine-in, 38.2% in takeout and 54.6% in delivery. Sixteen dishes are viable in dine-in, only twelve in delivery, and in delivery eight have to be dropped or reworked. Monthly margin goes from $43,635 in dine-in to $30,050 in delivery: $13,585 less, a gap you only see in the table at the end of this chapter.

The croquettes make the point: same dish, same price, a 24.4% food cost in dine-in against 46.5% in delivery. To get back to the 40% target, the sheet works out the pre-tax price the dish needs on the app, $10.00, and compares it with that dish's ceiling price there: $11.60. The app is a market of its own; a price above what the competition charges won't sell even when the numbers work, so the simulator doesn't hand you a price, it hands you a required price set against a ceiling. The gap between your dine-in price and the required app price is your app markup. If the required price sits below the ceiling, you take that markup and the problem is solved; if it sits above, the dish comes off that app's menu or gets reworked into a format that travels better and carries less packaging cost per portion. You don't keep raising the price of a dish that market won't pay for: you change the dish.

If you trade in the UK, Canada or Australia, the nine cells of the tax matrix and the commission cells are all editable: you don't have to live with the US defaults. In the US, third-party delivery mostly means DoorDash, Uber Eats and Grubhub; in the UK, Deliveroo and Just Eat. Terms vary from one contract to the next, so the cell gets the real figure from yours.

### Commission Isn't the Only Cost: Packaging and Dishes per Order

You don't pay for packaging per dish, you pay for it per order: its cost per dish is a division (packaging per order divided by the dishes in the average order), and that figure lives in a single cell on the "Inputs" sheet of multichannel-repricing-simulator.xlsx. In takeout and in delivery alike, packaging runs $1.75 per order, and the average order carries 2.5 dishes, so packaging per dish comes down to $0.70. Change the dishes per order (a family order spreads the packaging much better than a single-dish order) and you change that cell, and with it the effective food cost of your whole delivery menu, without touching a single price.

Treat the commission the simulator uses, 30% of the selling price, as an order of magnitude, not a fixed rate: whatever rate card an app shows you, what you actually pay depends on your market, the plan you sign up for and who makes the delivery. The working examples in this guide show how wide the spread can be. A zone-priced plan can run from 15% to 35% depending on area and demand (35% when the app does the delivery), with a monthly fee of around $39 and another 2-5% for marketing; tiered plans run from 15% to 30%; a marketplace listing can start at 13% and climb to 25-35% once the app delivers, plus $0.30 per order; and a 25-30% plan can come with a $50 monthly technology fee. The headline percentage isn't the whole cost, either: on top of it can come packaging at $1.35-$2.15 per order, promotional discounts of 20-30% to win visibility, and penalties of up to 2 more points of commission. Read all of these as example assumptions to stress-test the simulator, not as any app's published terms.

A third factor doesn't touch your food cost but does touch the price the guest sees: tax. In the US the menu price is before tax and the sales tax is added on the bill, so it doesn't move the channel math; just check whether your takeout and delivery rate matches your dine-in rate instead of assuming it, because some states and cities add a meals tax. Canada usually works the same way, with GST or HST added on top. The UK is where the rate itself changes with the channel: food and drink consumed on the premises and hot takeaway food pay the 20% standard rate, while most cold takeaway food is zero-rated, except soft drinks, confectionery and crisps. Australia folds its 10% GST into every printed price. Keep that in mind when you read an app's ceiling price in a UK kitchen: a cold sandwich and the can of cola that rides along with it don't carry the same rate.

### Tax Changes With the Channel and the Product

Tax doesn't land the same way in all three channels, and within a channel it doesn't land the same way on everything in the order. In the US and Canada, your menu and app prices are set before tax, the tax is added on the bill, and the simulator's nine tax cells stay at 0%: the gap between channels comes from commission and packaging, not from tax. In the UK, the line is drawn between eating in and taking away. On the premises, everything you serve pays the 20% standard rate, the glass of wine and the beer included, with no split between food and drink. Takeaway and delivery change the picture item by item: hot takeaway food stays at 20%, most cold takeaway food drops to zero, and soft drinks, confectionery and crisps never join that zero rate; the detail lives in VAT Notice 709/1 (catering and takeaway food) on gov.uk. So a single UK delivery order can carry two rates at once: apply them dish by dish and drink by drink, never as one rate for the whole order. In Australia, the 10% GST sits inside the printed price, so take out one eleventh before you read any percentage.

### The Ceiling Price: How High the App Lets You Go

The commission isn't a fixed cost you subtract from the margin: it's applied to the selling price and grows with it. The same dish at the same price runs a different effective food cost depending on the channel, and that's the number to keep an eye on, not the dine-in one: 31.4% in dine-in, right next to the 30% target; 38.2% in takeout, against the same target; and 54.6% in delivery, where the target relaxes to 40% to leave room for a commission that, in the template, is 30% of the order.

Look at packaging per dish, not per order. You pay for packaging by the order ($1.75 in takeout, another $1.75 in delivery), and its cost per dish depends on how many dishes the average order carries. At 2.5 dishes per delivery order, that $1.75 comes down to $0.70 per dish: a single dish carries the whole box, while an order for several people spreads it out.

With the commission scaling on the price and packaging spread per dish, you hit the real limit: the app is a market of its own, and a price above the competition won't sell even when the numbers work. The sheet doesn't give you a price: it gives you the price needed to hit the channel's target food cost and sets it against the ceiling price for that menu on that app. On the croquettes, food cost goes from 24.4% in dine-in to 46.5% in delivery at the same price; the target calls for a pre-tax price of $10.00, and the ceiling sits at $11.60. Of the 20 dishes on the menu, 16 are viable in dine-in and only 12 in delivery; the other 8 can't reach the target without breaking the ceiling, and the right call is to take them off that app or rework them so they travel better, not to force the price. The result: $43,635 of monthly margin in dine-in against $30,050 in delivery, $13,585 less.

Commissions are an order of magnitude, not a fixed price list: whatever an app publishes, your terms depend on the market, the plan and who makes the delivery. These are the kinds of terms a delivery contract can carry, with the figures this guide uses as working examples:

- A zone-priced plan: 15-35% depending on area and demand (35% when the app does the delivery), a monthly fee of about $39 and another 2-5% for marketing.
- A tiered plan: 30%, 25% or 15-20%, depending on the tier you sign up for.
- A marketplace listing: 13% if you deliver yourself, or 25-35% if the app delivers, plus $0.30 per order.
- A volume plan: 30% standard or 25% from 500 orders a month, plus a $50 monthly technology fee.

Beyond the headline percentage there are costs that sit outside it, and the guide's examples put them at $1.35-$2.15 of packaging per order, promotional discounts of 20-30% to win visibility, and up to 2 more points of commission as a performance penalty. Treat every figure in this list as an assumption to test in the simulator, never as a published rate.

If you trade in the UK, Canada or Australia, both the nine-cell tax matrix and the commissions are editable in the template; what changes are the apps you fill in, such as Deliveroo and Just Eat in the UK alongside the names US operators know best: DoorDash, Uber Eats and Grubhub.

### Which Dishes Shouldn't Be on Delivery

The app's commission isn't subtracted from the margin as if it were a fixed cost per dish: it's applied to the selling price, so it scales with it, and the same dish at the same menu price has a different effective food cost in each channel. That's the number to watch, not the dine-in one. That's why the target food cost is set per channel (30% in dine-in, 30% in takeout and 40% in delivery) and read against the effective food cost the full menu turns in today: 31.4%, 38.2% and 54.6%.

Packaging is the other piece that often gets miscalculated: takeout and delivery pay for packaging per ORDER, not per dish ($1.75 in both channels), so its cost per dish depends on how many dishes the average order carries. In delivery that's 2.5, which gives you the packaging per dish already worked out on the sheet: $0.70, in one cell, not an eyeball estimate.

With the commission on the price and the packaging spread per dish, the calculation gives you the price needed to reach the channel's target food cost and sets it against the ceiling price: what the app's own market will bear before the dish stops selling, even though the numbers work. The croquettes need $10.00 pre-tax to get under 40% in delivery (against 24.4% in dine-in), and the ceiling is $11.60: there's room to move. When the required price breaks the ceiling, you don't force the price up: you take the dish off that app or rework it into a format that travels better. Of the 20 dishes on the menu, 16 hold up in dine-in and only 12 in delivery; the other 8 have to be dropped or reworked, and the gap between $43,635 of monthly margin in dine-in and $30,050 in delivery is $13,585, with the same kitchen behind both.

Commissions aren't a closed price list. The guide's working examples run from a zone-priced plan at 15-35% depending on area and demand (up to 35% when the app handles delivery), with a monthly fee of about $39 and 2-5% extra for marketing, to tiered plans between 15% and 30%; a marketplace listing at 13%, or 25-35% with the app's own delivery, plus $0.30 per order; and a plan at 30% standard, 25% from 500 orders a month, plus a $50 monthly technology fee. They're ranges, not anyone's official rate: they depend on market, plan and who delivers, and there are costs outside the headline percentage ($1.35-$2.15 of packaging per order, visibility discounts of 20-30% and up to two points of performance penalty) that belong in the same test.

Drinks deserve a second look before they go on an app. The commission takes its share of a soda or a beer just as it does of a main course, and on a low-priced drink there isn't much left once it does: the can of cola that runs a 23.9% beverage cost at $2.30 in dine-in runs 34.2% at the same price once 30% comes off the top. In the UK there's a tax angle on top of that: soft drinks never join the zero rate that most cold takeaway food enjoys, so on a cold order they're the line still paying 20%. Alcohol is a licensing question before it's a pricing one: alcohol is licensed locally in every country, so whether you can sell it for delivery at all depends on your license, and that's worth checking with your licensing authority before you list a single bottle. Stack the commission on top of a cheap drink and you'll often find it's better left off the order.

### Selling Outside the US: Which Cells to Change

The tax matrix and the platform commissions aren't locked to the US case: they're editable cells, nine for tax plus the commission for each channel, designed so a reader trading in the UK, Canada or Australia can type in the local rate and their app's commission without touching a formula. The structure of the calculation doesn't change from one market to another; what changes is what goes in those cells. In the US and Canada, the nine tax cells stay at 0% and you type pre-tax prices; don't type your sales tax there, because the simulator reads every price as including the rate in its cell, and your menu is printed before tax. In the UK, you type 20%, and 0% where your cold takeaway food is zero-rated; in Australia, 10%.

As for which apps to fill in: in the US that usually means DoorDash, Uber Eats and Grubhub, and in the UK, Deliveroo and Just Eat. Each of them has its own commission terms, negotiated or published, and those are the numbers to enter before you trust any required price that comes out of the sheet.

**Channel Settings (multichannel-repricing-simulator.xlsx, "Inputs" sheet)**

| Channel | Packaging ($/order) | Dishes per order | Platform commission (%) | Target food cost (%) | Packaging per dish ($) |
|---|---|---|---|---|---|
| Dine-in | $0.00 | 1.0 | 0% | 30% | $0.00 |
| Takeout | $1.75 | 2.5 | 0% | 30% | $0.70 |
| Third-party delivery | $1.75 | 2.5 | 30% | 40% | $0.70 |

*Every setting in this table is yours to edit: it's the contract you signed, not an industry standard.*

**Delivery App Terms: An Order of Magnitude, Not a Rate Card (multichannel-repricing-simulator.xlsx, "Inputs" sheet)**

| Contract type | Reference commission and fees |
|---|---|
| Zone-priced plan | 15-35% depending on area and on whether the app delivers; monthly fee of about $39 |
| Tiered plan | 30% / 25% / 15-20% depending on the tier |
| Marketplace listing | 13% marketing only (you deliver) · 25-35% full service · $0.30 per order |
| Volume plan | 30% standard · 25% from 500 orders a month · technology fee of $50 a month |

*These ranges are the guide's working examples, and real terms change by market, by plan and by who makes the delivery. The number that goes in the cell is the one in your contract.*

**The Three Channels Compared (multichannel-repricing-simulator.xlsx, "Summary" sheet)**

| Channel | Viable dishes | Dishes to drop or rework | Average effective food cost (%) | Target food cost (%) | Average required price ($) | Total monthly margin ($) |
|---|---|---|---|---|---|---|
| Dine-in | 16 | 4 | 31.4% | 30.0% | $15.51 | $43,635 |
| Takeout | 12 | 8 | 38.2% | 30.0% | $17.85 | $49,597 |
| Third-party delivery | 12 | 8 | 54.6% | 40.0% | $19.12 | $30,050 |


---

## 16. Beverage Cost: The Bar as a P&L of Its Own

### Why Drinks Don't Get Measured With the Food Yardstick

The starting figure surprises anyone who runs the menu as a single line: a 2026 European industry study of restaurant costs and profits found product cost running at 34.5% of beverage revenue and only 28% of food revenue, on a revenue mix of 70% food and the remaining 30% from the bar. Read it as nuance, not as a general rule (it depends on each bar's mix), which is why this chapter treats each category separately instead of folding everything into one food cost. Market references don't settle on a single number either: getbackbar.com and purimax.com (2026) put beverage cost between 15% and 28% depending on the type of drink, 20% on average, and another industry source puts standard drinks between 15% and 25%, with one real case running 27.5% for the month. These are mid-reliability ranges, so each category's target sits in its own editable cell: 30% for wine, 22% for beer and soft drinks, 20% for spirits and cocktails. The month at the bar gets read against those three targets: $43,657 in sales, $11,503.96 in cost, a weighted beverage cost of 26.4% and a contribution margin of $32,153.04, with wine making up 41.6% of those sales and beer and soft drinks another 35.6%. There's also a border that food doesn't share: alcohol is licensed locally, and how it's taxed can depend on where and how it leaves your hands. In the US the menu price is pre-tax at the table, but alcohol can carry taxes of its own depending on your state, and whether you can sell a bottle to go at all depends on your license: check both. In the UK, everything consumed on the premises, the bottle of wine included, pays the 20% standard rate. The price-including-tax columns on the sheet handle both cases on their own, with the rates you set (0% by default, the US setting).

### Wine: The Glass Changes the Bottle's Math

Wine shows better than anything else how the unit of sale changes the result. Selling by the glass improves the percentage against the full bottle (the house red costs $0.78 a glass and leaves $2.22 of margin, with a beverage cost of 26.0% by the glass against 28.7% by the bottle), but that percentage only holds if the number of glasses per bottle holds: with 530 bottles and 2,540 glasses a month, that ratio is the figure to watch, because the moment it slips, beverage cost climbs without anyone noticing until the month closes, and the loss never shows up on any invoice. The sheet plans five glasses per bottle for every wine but the dessert wine: a 750 ml bottle poured five ways is 150 ml, or 5.07 fl oz, a glass, right at the 5 fl oz of wine in a US standard drink (in the UK, wine by the glass is sold in 125 ml or 175 ml, or multiples, so set that cell to 6 or 4.29). Wine as a whole closes at a weighted beverage cost of 30.2%, practically on its 30% target.

Draft beer plays a different game: you buy it by the liter or the gallon and sell it by the fluid ounce, and between the two sits the loss to foam at the tap and to line cleaning that no recipe cost card picks up on its own. With 6,360 beer and soft drink servings a month and a weighted beverage cost of 25.4% against a 22% target, that loss now has a name of its own on the summary. A cocktail is costed like a miniature recipe cost card, ingredient by ingredient, and the mix (ice that melts, fruit that gets thrown out, the extra splash at the pour) usually weighs more in the final cost than the bartender thinks while building the drink; spirits and highballs come in at 21.6%, just above the category's 20% target, and cocktails at 19.7%, just below it.

The overall reading is in the bottom row of the summary: each category has its own editable target on the "Inputs" sheet of beverage-cost-menu.xlsx, and the workbook calculates that $646.38 of margin would come back if each one hit its own. That number, not the weighted percentage of the whole bar, is what tells you where to start.

### Draft Beer and Soft Drinks: The Cost per Serving

It's worth opening with the figure that breaks the cliché. The same 2026 European industry study of the average restaurant's costs and profits, on a mix of 70% of revenue from food and 30% from beverage, puts cost at 28% of food sales against 34.5% of beverage sales: proportionally, the bar weighs more on its own revenue than the kitchen does on its own, the opposite of what most people take for granted. It isn't a universal rule; it's nuance that depends on your bar's mix and on how much you sell by the glass.

That's where glass versus bottle comes in. Selling by the glass improves the percentage: on the house red, the glass costs $0.78 and leaves $2.22 of margin, a beverage cost of 26.0% against 28.7% for the full bottle. What holds up that improvement is the number of glasses each bottle actually gives, and also what slips out of sight: with 530 bottles sold a month and 2,540 glasses, that ratio tells you whether the pour matches the plan. Pour a little heavy on every glass and the real beverage cost takes off without a single check giving it away.

The keg has its own trap: you buy it by the liter and sell it by the fluid ounce, and between those two units slip the foam from a badly balanced tap and the line cleaning, which use up product without ringing up a sale. A 30 L keg holds 7.93 gallons, and poured in 16.91 fl oz servings it gives 60 on paper, before foam and line cleaning take their share. That's why the beer and soft drink target is set separately, at 22%, with 6,360 servings sold a month holding a weighted beverage cost of 25.4% and a 35.6% share of beverage sales, inside the 20% to 26% range that the getbackbar.com and purimax.com (2026) industry aggregate gives for draft beer, a broad aggregate rather than a figure for your market.

Tax by channel enters this account too, in a different way in each country. In the US, and usually in Canada, the price on your menu is before tax whether the drink is poured at the bar or goes out the door, so tax never sits inside your beverage cost %. In the UK, everything consumed on the premises, alcohol included, pays the 20% standard rate, and soft drinks stay at that rate even when they go out with zero-rated cold food. In Australia, the 10% GST is already in the printed price. The price-including-tax columns on the sheet sort this out by channel on their own.

### Spirits and Cocktails: When the Cost Is in the Mix

A cocktail is costed just like any dish on the menu: it's a miniature recipe cost card, ingredient by ingredient, with its own loss and its own selling ratio. The mix usually weighs more than the team thinks, because a craft liqueur, an imported bitters or an elaborate garnish pushes the cost above what the base bottle suggests. Spirits and highballs run a weighted beverage cost of 21.6% and built cocktails 19.7%, on either side of the 20% target and inside the 15% to 22% range that the same getbackbar.com and purimax.com (2026) source gives for spirits and cocktails. Whatever you pour, the measure is what goes on the card: there's no federal pour size in the US, but the common standard pour is 1.5 fl oz, the spirit in one US standard drink; in the UK, gin, rum, vodka and whisky for drinking on the premises are sold only in 25 ml or 35 ml measures, or multiples of them.

The overall reading sits in the beverage summary. On total sales of $43,657 and a cost of $11,503.96, the weighted beverage cost of the whole bar comes to 26.4%, with a contribution margin of $32,153.04. Each category keeps its own target, editable on the sheet, and the margin you'd recover if wine, beer and soft drinks, and spirits and cocktails each reached theirs comes to $646.38. That number sets your priorities: with wine at 30.2% and spirits and cocktails at 20.9% already close to target, the category leaving the most margin on the table is beer and soft drinks, at 25.4% against the 22% set on the "Inputs" sheet, worth $525.32 of that $646.38 on its own. That's where to look first: the tap system, the line cleaning and the size of every pour.

### The Beverage Summary and the Margin You're Leaving on the Table

The first figure runs against what everyone takes for granted: drinks don't always leave a better margin than food. According to that 2026 European industry study of restaurant costs and profits, the average restaurant spends 28% of its food revenue on buying the food and 34.5% of its beverage revenue on buying the drinks, on a revenue mix of 70% food and 30% beverage: proportionally, the bar weighs more on itself than the kitchen does on itself. It's nuance, not a fixed rule: it depends on what makes up your wine and spirits list. That's why your bar needs its own dashboard, separate from your overall food cost.

The first decision that moves the needle is glass versus bottle. Selling by the glass improves the percentage, but the margin only holds if the real number of glasses per bottle matches the planned one. With 530 bottles of wine sold a month and 2,540 glasses over the same period, the house red leaves a cost per glass of $0.78 and a margin of $2.22, with a beverage cost of 28.7% by the bottle that drops to 26.0% by the glass. If the team pours heavy, that 26.0% creeps up without anyone noticing until the summary shows it.

The keg has its own trap: you buy it in liters or gallons and sell it in fluid ounces, with foam nobody pays for and lines that need cleaning in between. With 6,360 beer and soft drink servings sold a month, the category target is 22% and the real weighted figure lands at 25.4%; that gap is the loss the keg math has to absorb. As a market reference, not a target for your bar, the getbackbar.com and purimax.com (2026) industry aggregate puts target beverage cost at 20% to 26% for draft, 24% to 28% for bottles and cans, and 15% to 22% for spirits and cocktails, with an overall average of 20%. Another industry source gives a range of 15% to 25% for standard drinks, with one real case at 27.5% for the month; these are mid-reliability sources, to check yourself against, never a fixed target.

A cocktail is costed like a miniature recipe cost card: every spirit, syrup, piece of fruit and the ice go into the math, and the mix usually weighs more than it looks at first glance. The spirits and cocktails target is 20%; spirits and highballs come in at a weighted 21.6% and crafted cocktails at 19.7%, figures worth reading separately, because a simple highball and a signature cocktail don't behave the same way.

The beverage summary brings the three categories together: wine makes up 41.6% of sales, with a weighted 30.2% against a 30% target; beer and soft drinks make up 35.6%, with a weighted 25.4% against a 22% target; spirits and cocktails close at a weighted 20.9% against 20%. On sales of $43,657 and a cost of $11,503.96, the weighted beverage cost of the whole bar is 26.4% and total contribution margin reaches $32,153.04. The workbook calculates how much would come back if each category reached its own target: $646.38, your order of priorities for the next wine list and the next keg order.

That leaves tax, which also splits by channel at the bar, and on both sides of the ledger. On the sales side, the US and Canada price before tax, so your beverage cost % is always calculated on the pre-tax price; in the UK and Australia, take the 20% VAT (divide by 1.20) or the 10% GST (one eleventh) out of the printed price first. Whether a bottle can leave the building unopened at all is a licensing question, since alcohol is licensed locally. On the cost side, the rule from chapter 4 holds: in the US, any sales tax you actually pay on a purchase is part of its cost; in the UK, Canada and Australia, a registered business reclaims it, so the cost is the price before tax. The price-including-tax columns on the sheet already handle each situation: you just read the one for the channel the bottle goes out through.

**The Bar by Category, With Its Target Alongside (beverage-cost-menu.xlsx, "Beverage Summary" sheet)**

| Category | Monthly sales ($) | Monthly cost ($) | Weighted beverage cost (%) | Target (%) | Contribution margin ($) | Share of beverage sales (%) |
|---|---|---|---|---|---|---|
| Wine | $18,151 | $5,473.90 | 30.2% | 30.0% | $12,677.10 | 41.6% |
| Beer and soft drinks | $15,554 | $3,947.20 | 25.4% | 22.0% | $11,606.80 | 35.6% |
| Spirits and cocktails | $9,952 | $2,082.86 | 20.9% | 20.0% | $7,869.14 | 22.8% |
| BEVERAGE TOTAL | $43,657 | $11,503.96 | 26.4% |  | $32,153.04 | 100.0% |

*The category targets are editable cells seeded with industry references: they aren't a standard, they're a starting point for you to write your own.*

**Wine: The Same Bottle Sold by the Bottle and by the Glass (beverage-cost-menu.xlsx, "Wines" sheet)**

| Wine | Bottle purchase price pre-tax ($) | Glasses per bottle | Bottle menu price pre-tax ($) | Glass menu price pre-tax ($) | Cost per glass ($) | Beverage cost, bottle (%) | Beverage cost, glass (%) |
|---|---|---|---|---|---|---|---|
| House red (young Tempranillo) | $3.90 | 5.0 | $13.60 | $3.00 | $0.78 | 28.7% | 26.0% |
| Rioja Crianza | $6.10 | 5.0 | $19.10 | $4.10 | $1.22 | 31.9% | 29.8% |
| Ribera del Duero Roble | $7.40 | 5.0 | $21.80 | $4.50 | $1.48 | 33.9% | 32.9% |
| Rueda Verdejo | $4.20 | 5.0 | $14.50 | $3.20 | $0.84 | 29.0% | 26.2% |
| Rias Baixas Albariño | $7.90 | 5.0 | $22.70 | $4.80 | $1.58 | 34.8% | 32.9% |
| Cava Brut Nature | $5.60 | 5.0 | $18.20 | $3.90 | $1.12 | 30.8% | 28.7% |
| Navarra Rosé | $3.70 | 5.0 | $12.70 | $2.90 | $0.74 | 29.1% | 25.5% |
| Pedro Ximénez dessert wine | $11.50 | 8.0 | $27.30 | $4.00 | $1.44 | 42.1% | 35.9% |

**Beer and Soft Drinks: From Purchase Format to Serving (beverage-cost-menu.xlsx, "Beer & Soft Drinks" sheet)**

| Item | Purchase format | Purchase price pre-tax ($) | Servings per unit | Cost per serving ($) | Dine-in menu price pre-tax ($) | Beverage cost (%) |
|---|---|---|---|---|---|---|
| Draft beer, 30 L keg (8.45 fl oz pours) | keg | $78.00 | 120.0 | $0.65 | $2.30 | 28.3% |
| Draft beer, 30 L keg (16.91 fl oz pours) | keg | $78.00 | 60.0 | $1.30 | $4.10 | 31.7% |
| Bottled beer (330 ml, 11.16 fl oz) | bottle | $0.62 | 1.0 | $0.62 | $2.50 | 24.8% |
| Non-alcoholic beer (330 ml, 11.16 fl oz) | bottle | $0.58 | 1.0 | $0.58 | $2.40 | 24.2% |
| Cola (330 ml can, 11.16 fl oz) | can | $0.55 | 1.0 | $0.55 | $2.30 | 23.9% |
| Mineral water (500 ml, 16.91 fl oz) | bottle | $0.28 | 1.0 | $0.28 | $1.80 | 15.6% |
| Fresh-squeezed orange juice | lb of oranges | $0.64 | 1.81 | $0.35 | $3.20 | 10.9% |


---

## 17. Batch Costing for Commissary Kitchens and Pastry

### The Unit of Costing Is the Batch, Not the Piece

In a bakery you don't cost a single piece. You cost the bake, the proofing tub or the whole batch, and the cost of each piece comes from dividing that total by the GOOD units that actually come out, not by the number the formula promised on paper. It's the same principle as the butchery yield in chapter 5, moved from the knife to the oven: you weigh the dough that goes in, and you count the pieces that pass quality control coming out. Every batch has a yield of its own (pieces that break, deform, burn on the edge of the oven or over-proof), and that batch yield turns a formula cost into a real cost per sellable unit.

Loss isn't a single number. There is proofing loss, when the dough loses volume or over-proofs before it goes into the oven, and there is cooking loss, when the product loses weight and, once you count the rejects, whole units too. The yield workbook handles this by weighing before and after each stage, and it already comes with 5 cooking tests logged using that method. The weighted average yield across those five tests is 72.7%, with an average cooking loss of 27.3%. The word "weighted" matters, because not every product loses the same amount: the pan-seared pork tenderloin gives up 22.0%, the oven-roasted free-range chicken 28.0% (with the cooked pound already costing $3.40) and the roasted vegetables as much as 31.0%, as you can see in the table below. Those are kitchen tests, not bakery tests, but the method is exactly the one to apply to viennoiserie and pastry: scale before the tray goes in, scale when it comes out, and count the good pieces against the formula pieces. Without your own test for each product, any batch cost is an optimistic guess.

Once the product is sold packaged (box, film, a bag with an allergen label and a best-by date), packaging stops being an ordering expense and becomes a cost per piece. Every unit that leaves the batch carries its own container and its own label, inside the recipe cost card for that piece, never in a separate "supplies" line.

### Hourly Labor Inside the Batch Cost

In a piece of viennoiserie or pastry, the cost of hands usually weighs more than the flour, the butter or the filling. That's why a recipe cost that only looks at ingredients gives you a ruinous price: it's missing the most expensive part of the piece. The right calculation spreads the real time of the batch (mixing, shaping, supervised proofing, baking, cooling and packing) across the good pieces that come out of it, exactly as you already spread the raw material cost. The hourly cost of each position comes from your own business, with your actual wages and employer payroll taxes and benefits: there is no universal figure that works for every bakery. As a reference for how much payroll can weigh against sales, a 2026 European industry study puts labor cost at 30% to 35% of net sales in an integrated dine-in service, and at 15% to 25% in a partial self-service or counter operation. A bakery with counter sales usually sits closer to that second range, although every business has to measure its own.

Scaling the batch is where this cost becomes a lever. Doubling the formula doesn't double the mixing time or the time spent watching the proof, and it doesn't double the loss either, so the labor cost per piece falls as the batch size grows, until the capacity of the oven, the walk-in or the work table puts a ceiling on it. Finding that sweet spot means deciding how much staff and how much time you need for the volume you actually sell, not for the volume that fits in the oven.

To price a piece you've already costed, this format works better with the target margin method than with a simple multiplier on cost: you first set how much each piece has to leave you, and you calculate the menu price from there. Across the 6 dishes in the pack that already use this method, spread over the different menu formats, the average contribution margin is $8.01, with a combined food cost of 36.7%; the table below shows how you get to that figure. If you want the batch costing template already built, it's ready in the Food Cost Kit Pro. Here we stay with the method.

### Packaging and Labeling: The Cost That Isn't in the Recipe

In a bakery you don't cost the portion. You cost the whole batch, and the cost of each piece comes from dividing that total by the good pieces that reach the counter, never by the ones the formula promised on paper. It's the same principle as the butchery yield in chapter 5, moved from the knife to the oven and the proofing cabinet: first you weigh what goes in, then you count what you can actually sell, and only with that second number do you calculate the cost.

Here, labor also weighs on the recipe cost in a way it doesn't always weigh in a plated kitchen. A viennoiserie piece can carry more dollars of hands (mixing, rounding, laminating, shaping, decorating) than of flour, butter or filling, and a recipe cost that only looks at ingredients gives you a ruinous price. Across the whole business, labor cost as a share of net sales runs between 30-35% in integrated dine-in service and 15-25% in partial service (self-service or counter), according to a 2026 European industry study on restaurant costs and profits. In a bakery that weight doesn't get diluted into the average check of a dining room: it's concentrated piece by piece, which is why the timing of each formula has to appear on the card with the same rigor as the weight in grams.

Cooking loss and proofing loss are the other half of the batch yield, and they're measured the same way: by weighing before and after. The yield workbook captures that logic with five logged cooking tests, with a weighted average yield of 72.7% (an average loss of 27.3%) that runs from the 22.0% of the pan-seared tenderloin to the 31.0% of the roasted vegetables, passing through the 28.0% of the oven-roasted free-range chicken, with an already-cooked cost of $3.40 a pound. Those are kitchen tests, not bakery tests, and here they only illustrate the method: every formula, every oven and every bakery has its own yield, which you have to record with your own scale. Proofing loss is weighed the same way (the moisture lost in the first and second proof, and what's lost again inside the oven) and goes into the batch cost just like cooking loss.

And as soon as the piece leaves packaged (film, bag, individual box, with the allergen label and the best-by date), packaging stops being a purchase-order expense and becomes a cost of the piece. You buy it in big lots, spread it per unit, and add that unit to the card before you set the menu price, not after.

### Scaling a Formula Without Scaling the Error

Doubling a formula looks like simple arithmetic (twice the flour, twice the butter, twice the pieces), but the hands time doesn't double the same way. Mixing 2,000 g of dough doesn't take twice the minutes of mixing 1,000 g, and a bigger bake spreads the same oven, proofing and shaping time across more units. That's why the cost per piece falls as the batch grows, until a physical limit (oven capacity, walk-in space, the trays that fit on a rack) forces you to split into two bakes, and that's where the savings stop. That limit is set by your own oven and your own walk-in, never by a book's.

Loss doesn't scale in a straight line either. A large batch usually holds its temperature better and proofs more evenly than a small test, so the yield at real production scale won't match the one from the test you ran to build the recipe cost on paper. The first is the one you need to record, so the unit cost doesn't come in short of what the scale tells you every morning.

To price each piece, the method that fits this format is target margin. Instead of starting from cost and adding a percentage, you start from the contribution margin that piece needs to carry the batch and the business, and from there you work out the menu price. The guide applies that method to six dishes, with an average contribution margin of $8.01 per dish and a combined menu food cost of 36.7%. Those are dine-in dishes, not bakery pieces, but the table below illustrates the same mechanism you apply piece by piece in batch costing: you start from the margin the business needs, not from the habits of the trade.

If you want the batch costing template already built (with the batch scale, the timing and the packaging linked in a single card), it's in the Food Cost Kit Pro. What's left here is the method, which is what you need to adapt any template to your own bakery.

**What the Product Loses in the Oven and on the Griddle (yield-and-trim-loss.xlsx, "Cooking Loss Test" sheet)**

| Preparation | Technique | Raw Weight (lb) | Cooked Weight (lb) | Cooking Loss (%) | Cooking Factor | Cost per lb Raw ($) | Cost per lb Cooked ($) |
|---|---|---|---|---|---|---|---|
| Pan-seared Iberico pork tenderloin | Flat-top | 0.55 | 0.44 | 22.0% | 1.28 | $8.14 | $10.44 |
| Oven-roasted free-range chicken | Oven | 3.31 | 2.38 | 28.0% | 1.39 | $2.45 | $3.40 |
| Confit cod | Confit | 0.44 | 0.40 | 12.0% | 1.14 | $6.76 | $7.68 |
| Charcoal-grilled Iberico pork secreto | Charcoal | 0.66 | 0.49 | 26.0% | 1.35 | $7.48 | $10.12 |
| Roasted vegetables | Oven | 2.20 | 1.52 | 31.0% | 1.45 | $1.00 | $1.45 |

*The cooking factor is multiplied by the cost of the raw product: it's what turns the price on the delivery invoice into the cost of what comes out of the oven.*

**Pricing by Target Margin, the Bakery Method (menu-pricing-calculator.xlsx, "By Dish" sheet)**

| Dish | Plate Cost ($) | Target Margin ($) | B · Menu Price by Margin ($) | Resulting Food Cost with B (%) |
|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $6.50 | $8.60 | 24.4% |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $6.50 | $10.10 | 35.6% |
| Garlic shrimp | $6.90 | $6.50 | $13.40 | 51.5% |
| Broken eggs with potatoes and chistorra sausage | $2.40 | $6.50 | $8.90 | 27.0% |
| Local cheese board | $5.20 | $6.50 | $11.70 | 44.4% |
| Confit artichokes with ham | $3.10 | $6.50 | $9.60 | 32.3% |
| Roasted tomato soup with basil | $1.20 | $6.50 | $7.70 | 15.6% |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $10.50 | $16.17 | 35.1% |
| Confit cod in pil-pil sauce | $7.40 | $10.50 | $17.90 | 41.3% |
| Dry-aged beef burger with fries | $4.30 | $10.50 | $14.80 | 29.1% |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $10.50 | $16.70 | 37.1% |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $10.50 | $25.30 | 58.5% |
| Salt-baked sea bass | $8.90 | $10.50 | $19.40 | 45.9% |
| Free-range roast chicken with potatoes | $3.70 | $10.50 | $14.20 | 26.1% |
| Seasonal vegetable lasagna | $2.60 | $10.50 | $13.10 | 19.8% |
| Seared bluefin tuna tataki with sesame | $9.60 | $10.50 | $20.10 | 47.8% |
| Creamy cheesecake | $1.30 | $4.20 | $5.50 | 23.6% |
| Caramelized torrija with ice cream | $1.10 | $4.20 | $5.30 | 20.8% |
| Chocolate lava cake | $1.60 | $4.20 | $5.80 | 27.6% |
| Prepared seasonal fruit | $1.40 | $4.20 | $5.60 | 25.0% |


---

## 18. When Your Supplier Raises Prices: The Re-Costing Protocol

### The Four Triggers for a Re-Costing

A re-costing doesn't depend on anyone's memory. Four situations set it off, and it pays to have them written down somewhere visible in the kitchen.

- A supplier increase above the threshold you set yourself on the cost of that item; below that threshold, you let it pass and touch nothing.
- A change in the format or size of the product you buy, even if the price per purchase unit doesn't move: the real cost per portion does, and that's where the mismatch nobody sees on the invoice hides.
- A change of recipe, whether it comes from the kitchen or from a supplier adjusting the composition of the product.
- The calendar coming due, even if none of the above has happened: reviewing by date is the net that catches what the other three triggers don't see coming.

None of the four requires you to review the entire menu. Apply the 80/20 rule: review the items that weigh most in the month's consumption (the ones that move the most pounds or gallons, not the ones that appear most often in writing) and the dishes that sell best, because they amplify any cost error before anything else does. Of the 20 dishes with a calculated price in the pack's reference table, 11 land within target and 9 above it. The 80/20 rule says those 9 are the first place to look, and the other 11 can wait for the next review.

To know whether an increase crosses your threshold, there are two places to check before trusting the feeling a single invoice leaves you with. For how food prices are behaving in general, look at the published price indexes for food and non-alcoholic beverages that your country's statistics office or industry bodies release regularly: use them to tell whether what's rising is a market-wide movement or something specific to that supplier. For fresh produce, protein and seafood, compare against your supplier price lists from other vendors and against the wholesale market quotes that are published for your region: that's how you ask at which link of the chain the increase starts, and whether the price at origin already reflects it or the margin is being added further down. Neither of the two tells you how much to raise the menu; both tell you whether the increase is real and where in the chain it happened.

### The Calendar: What You Review Each Month and Each Quarter

The monthly review deals with what's urgent: the items that tripped the threshold that month, the dishes with the most flagged deviation in the target price table, and the follow-up on any supplier decisions in progress. The 90-day plan logs 2 supplier review decisions, with an estimated impact of $300, within a total estimated plan impact of $2,360 (the "Decisions" sheet of 90-day-action-plan.xlsx). Reviewing them each month means checking whether the supplier delivered on what was agreed, not reopening the whole negotiation every time.

The quarterly review is where you measure the entire menu against the target, dish by dish. The total gap against current menu prices (-$13.54) and the average change against the current menu price (-5.1%, negative because, taken as a whole, the menu already sits slightly above its target prices), both from the target price table, give you the complete picture of the 20 dishes, not just the ones you already knew were off.

How you pass the increase on: you don't raise the whole menu on the same day or by the same percentage. You raise where the market allows it (a starter takes a move that the menu's anchor dish doesn't take the same way) and you use a menu or seasonal change so the new price arrives inside "the new menu" and not as "the price increase." Start with the dishes whose increase is small in dollars even if it's big in percentage: they generate the least complaint in the dining room, so that's where it makes sense to act first. The pack's reference card, for example, needs a 9.3% increase to reach its target menu price, with a difference of barely $1.60 between target and current (the "Cost Card" sheet of recipe-cost-card.xlsx): in dollars it's a small adjustment, and it's exactly the kind of dish you raise first, without anyone noticing in the dining room. The croquettes, in the target price table, show up instead with a difference of -$1.60 against their current menu price: the opposite sign warns you that not every adjustment goes in the same direction, and it's the table that says so, never the cook's gut.

After you move any price, the menu profitability matrix stops being valid until you measure again: changing prices changes the sales mix, so drawing conclusions about which dish to drop or push using data from before the increase is measuring with a ruler that no longer applies. You wait for the next close, recalculate the entire matrix, and only then decide which dish stays, which one gets tweaked again and which one leaves the menu.

### Where to Look for Raw Material Prices

There are four moments that force a re-costing, and none of them depends on anyone's memory:

- a supplier increase above the threshold you yourself set as a red line;
- a change in the format or size of the goods you buy, even if the item looks like the same one;
- a change in the recipe, through an ingredient substitution or a portion adjustment;
- the review calendar coming due, even if apparently nothing has happened.

That last one is the one people skip most: if the supplier doesn't warn you, you assume everything is the same, and that's where the recipe cost drifts in silence.

When it's time to review, you don't open the whole menu: you apply the 80/20 rule, going first through the items that weigh most in the month's consumption (not the ones that appear most on the menu, but the ones that move the most pounds or gallons) and the best-selling dishes, because they drag the result even when their individual deviation is small. The table that follows this text, with the dishes whose price was recalculated in this cycle, is that cut: not the whole menu, but the part that concentrates the impact. There are 20 dishes; of them, 11 land within target and 9 above it, with a combined difference against current menu prices of -$13.54 and an average increase of -5.1% over the current menu price of the reviewed set: the picture of the full block, which helps you decide where to go in first.

Before you pick up the phone, there are two places to check whether the increase reflects the market or simply that your supplier can get away with it. The first is the published price index for food and non-alcoholic beverages in your market, which tracks how the food basket behaves month by month and helps you check whether one supplier's increase is in line with the sector or out of bounds. The second, for fresh goods, is the wholesale market quotes for your region, compared against your supplier price lists: they let you compare the price at origin with the price at wholesale and ask whether the margin at each link has widened. Neither is cited here for what it says today (that changes every week) but as the place to come back to when the next increase arrives.

### How to Raise a Price Without It Showing at the Register

Raising the whole menu at once, by the same percentage, is the fastest way for the guest to notice. You spread the increase: you raise where the market allows it (dishes with no clear price reference in the guest's head) and you use a menu or seasonal change to redesign the card or the side, so the new price doesn't read as a naked increase. The recipe cost card in this chapter is the example: the required increase works out to 9.3%, which in dollars is only $1.60 of difference between the target menu price and the current one. It's the kind of adjustment you should review first: small in dollars, so the guest barely notices; big in percentage, so it really corrects the margin. The same magnitude shows up from the other side in the by-dish table: the croquettes' difference from their current menu price is -$1.60, the exact mirror of the same adjustment.

Not every adjustment comes from raising the menu price. Part of the decisions in the 90-day action plan are about supplier review, not menu price: there are 2 decisions of this type logged, with an estimated impact of $300 out of a total impact of $2,360 for the whole plan. When to sit down to negotiate, and with what data in hand, is already covered in the Food Cost Kit Pro bonus that comes in the same pack; here it's enough to be clear that raising the menu price and negotiating the cost of the raw material are different levers, and it pays to look at both before deciding which one to touch first.

And one warning you can't skip: as soon as you touch a price, the sales mix moves. The dish that used to be ordered a lot because it looked cheap next to its neighbors on the page can lose weight, and another that was barely ordered can gain it. That's why, after applying any increase, you have to let time pass before you measure again (don't take any conclusion about a dish as good using data from before the change), because the matrix that decides what to promote and what to pull from the menu is built from real sales, and those take a while to settle after a new price.

**Which Dish to Touch and by How Much (menu-pricing-calculator.xlsx, "By Dish" sheet)**

| Dish | Plate Cost ($) | Current Menu Price Pre-Tax ($) | Chosen Menu Price Pre-Tax ($) | Difference ($) | Status vs. Target |
|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $8.60 | $7.00 | -$1.60 | On target |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $11.80 | $12.00 | $0.20 | On target |
| Garlic shrimp | $6.90 | $15.50 | $13.40 | -$2.10 | Above target |
| Broken eggs with potatoes and chistorra sausage | $2.40 | $9.80 | $8.00 | -$1.80 | On target |
| Local cheese board | $5.20 | $13.60 | $17.33 | $3.73 | On target |
| Confit artichokes with ham | $3.10 | $10.90 | $10.33 | -$0.57 | On target |
| Roasted tomato soup with basil | $1.20 | $7.20 | $7.56 | $0.36 | On target |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $17.30 | $18.68 | $1.38 | Above target |
| Confit cod in pil-pil sauce | $7.40 | $19.10 | $17.90 | -$1.20 | Above target |
| Dry-aged beef burger with fries | $4.30 | $13.60 | $12.92 | -$0.68 | Above target |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $16.40 | $16.70 | $0.30 | Above target |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $32.70 | $25.30 | -$7.40 | Above target |
| Salt-baked sea bass | $8.90 | $21.80 | $19.40 | -$2.40 | Above target |
| Free-range roast chicken with potatoes | $3.70 | $12.70 | $11.94 | -$0.76 | Above target |
| Seasonal vegetable lasagna | $2.60 | $11.40 | $10.49 | -$0.91 | On target |
| Seared bluefin tuna tataki with sesame | $9.60 | $22.40 | $20.10 | -$2.30 | Above target |
| Creamy cheesecake | $1.30 | $5.90 | $6.61 | $0.71 | On target |
| Caramelized torrija with ice cream | $1.10 | $5.50 | $5.83 | $0.33 | On target |
| Chocolate lava cake | $1.60 | $6.20 | $7.13 | $0.93 | On target |
| Prepared seasonal fruit | $1.40 | $4.50 | $4.73 | $0.23 | On target |

*The difference column is the one that sets the order of work: you start with the dishes where the correction is biggest in dollars and that sell a lot, not the ones with the ugliest percentage.*

**The Plan's Decisions, by Type (90-day-action-plan.xlsx, "Decisions" sheet)**

| Decision | Number of Decisions | Estimated Impact ($/month) | Achieved Impact ($/month) |
|---|---|---|---|
| Reformulate | 1 | $900.00 | $0.00 |
| Reprice | 1 | $210.00 | $0.00 |
| Redesign | 2 | $400.00 | $0.00 |
| Remove | 3 | $290.00 | $0.00 |
| Review | 2 | $300.00 | $0.00 |
| Negotiate | 1 | $260.00 | $0.00 |


---
## 19. The Full Case: One Entire Menu, Start to Finish

### The Starting Point: What Was on the Table

Before we get into the detail, let's be upfront: what follows is a modeled case, built entirely on the pack's templates so you can watch the whole flow chained together before you apply it to your own menu. It is not a real restaurant or an identifiable business; the figures from here on, and in the tables that go with this chapter, are simply what the exercise produces.

The starting menu had 20 dishes set up, with 4,870 units sold per month and net sales of $59,029 over that same period. The weighted average food cost of that menu was 32.7%, with a weighted average contribution margin of $8.16 per portion. To put that number in context: commonly cited reference ranges put a healthy food cost (product used as a share of sales) at 25-35% of sales, with a market average around 30%. The starting 32.7% therefore sat inside that range, but in its upper half, with room to improve without restructuring the menu.

That food cost doesn't live alone: it sits alongside labor, rent and overhead inside the P&L, and the commonly cited healthy EBITDA for that whole picture is 10-13% of sales. The case doesn't touch those other lines (they're outside the scope of this chapter), but keep them in mind, because they are the frame for reading any pricing decision.

With that starting point on the table, the walk through the pack's tools begins where it has to begin: with the recipe cost card for each dish.

### Step 1: Cost the Recipe and Measure Trim Loss

The first dish taken to the recipe cost card in `recipe-cost-card.xlsx` came out at a plate cost of $5.67. With that cost, the tool proposed a target menu price, pre-tax, of $18.90, calculated to sustain the contribution margin the menu needs. The decision at this step was not to accept the cost as it stood: it was to check, portion by portion, whether that cost captured the product's real trim loss or had stopped at the purchase weight.

That's where the second tool came in. The yield tests on the menu's raw ingredients, collected in `yield-and-trim-loss.xlsx`, gave a weighted average yield of 60.5%. In other words, a considerable share of every pound you buy gets lost to trimming, cutting waste and cooking loss before it ever reaches the plate. The decision taken with that number was to carry the measured yield into each product's card, instead of leaving the cost calculated on the gross weight on the supplier's invoice. That's the difference between a recipe cost that looks right on paper and one that is right in the kitchen, dish by dish. With yield built in, the plate cost stopped being an optimistic estimate and became the real number to work with in the next steps: classifying the menu and, after that, pricing it.

### Step 2: Classify the Menu With the Four Methods

With the real costs on the cards, the multi-method matrix crossed the 20 dishes on the menu through the four classic readings of menu engineering. The result, collected in `menu-engineering-matrix.xlsx`: only 3 dishes landed in the best category under all four readings at once, and 12 had three or four readings that disagreed with each other. In the Kasavana & Smith reading, the one most used as a quick reference, the menu came out with 6 Stars and 3 Dogs.

Those 12 disagreeing dishes are the whole reason for this step, because that's where trusting a single reading leads you astray. Some dishes one method calls a star for their sales volume, while another method demotes them to the weakest category as soon as you look at the margin they leave per portion. The decision in those cases was to keep them on the menu but review the price before touching anything else, because the volume is already won and what's failing is the margin. Others sit at the opposite extreme, with a high contribution margin but sales so thin that no method rewards them. There the decision was about visibility, not price: move them on the menu, work them into the dine-in pitch or the server's suggestion, so the margin they already have finds more guests. And there is a third group, the most uncomfortable one, where neither margin nor volume helps and all four readings point the same unfavorable way. With those there's no ambiguity, and they are the first candidates to leave the menu or to be redesigned from the recipe cost card, not from the price. The classification doesn't replace the decision; the decision still has to be made by whoever runs the menu, dish by dish, with all four readings in front of them and not just one.

### Step 3: Price Dish by Dish

Before we get into numbers, one necessary clarification: what follows is a modeled case, built on the pack's templates so you can see the full flow before applying it to your own menu. It is not a real client or an identifiable business.

The example menu has 20 dishes set up, moving 4,870 units a month and $59,029 in net sales, with a weighted average food cost of 32.7% and a weighted average contribution margin of $8.16 per dish. Before changing a single menu price, look at each dish with all four methods at once, not just one.

With the combined reading, 3 dishes land in the best category in all four classifications and stay exactly as they are: all four methods agree they are already where they should be. The interesting case is the other 12, with three or four readings outside their ideal category. There the decision doesn't come from averaging the four results, but from looking dish by dish at the contribution margin and the individual cost next to the real turnover. Where the problem is a high cost carried by good turnover, the decision was to review the recipe cost card (portion, supplier or technique) before touching the menu price. Where turnover is weak but the margin is fine, the decision was about placement: move the dish on the menu or rename it, don't change its cost. And where a high cost and weak turnover coincide, the dish was marked for removal or a complete redesign, because no price adjustment fixes that combination on its own. The separate Kasavana & Smith reading, the most classic of the four, places 6 dishes as Stars and 3 as Dogs, and already anticipates a good part of that split.

With the classification closed, it's time to set the target menu price. The example recipe cost card has a plate cost of $5.67 (with the weighted average yield from the tests applied, which across the products analyzed comes to 60.5%) and a target menu price, pre-tax, of $18.90. Repeated dish by dish, that leaves 11 of the 20 dishes on target after applying the new price. The food cost of the whole menu at those prices comes out at 36.7%, and the total difference against current menu prices is -$13.54: summed across the 20 dishes, the chosen prices sit $13.54 below the current ones.

### Step 4: Review Third-Party Delivery and Decide What to Exclude

The same menu, served through a delivery app, is not the same menu. The commission each platform keeps is added to product cost and packaging, so the effective food cost in that channel can't be compared directly with the dining room. Of the 20 dishes, 12 turn out to be viable on third-party delivery and 8 are left to exclude from the app or to reformulate. The criterion is to compare, dish by dish, the effective food cost against the ceiling price the channel allows before you stop making money on that order.

The dishes that come off the app are the ones that, with their current cost and the added weight of commission and packaging, don't reach that ceiling price no matter how much you raise the menu price. The ones that go up in price are the ones with room to move: their effective food cost falls into a manageable range as soon as you adjust the channel price, without touching the recipe or the recipe cost card. The aggregate result is an average effective food cost on delivery of 54.6%, against a total monthly dine-in margin of $43,635. The margin difference of delivery against dine-in is -$13,585: the channel brings volume and visibility, but with this menu it doesn't match dine-in on profitability.

### Step 5: Turn the Diagnosis Into Dated Decisions

Commonly cited reference ranges put a healthy restaurant food cost at 25-35% of sales, with a market average of 30%. The same reference ranges put the benchmark cost structure of a restaurant at about 30% for product, 30-35% for labor with service integrated, 5-10% for rent and 13-20% for overhead (ideally 17%), with a healthy EBITDA of 10-13%; below 10% calls for restructuring. The year's prime cost for the example menu is 63.4%, below the 65% target set in its dashboard: there is room to maneuver, but not so much that you can relax the tracking.

Everything above (classification, menu price and delivery) ends in 10 decisions recorded in the plan, each with an owner, an execution week and an estimated impact. That estimated impact adds up to $2,360 across the 10 decisions and $28,320 projected over twelve months: figures to read as an estimate calculated on the plan's date, not as a result already achieved. The plan sets who does what and by when; it doesn't certify the outcome.

The quarter's reading, with those ten decisions underway, moves food cost from 33.1% in month 0 to a target of 29.8% in month 3; prime cost, from 66.8% to 63.8%; and dishes on the menu, from 20 to 18. Read these three indicators for what they are in this book: an example target to teach how a plan is tracked quarter by quarter, not a promise of what will happen to you with your own menu. What you can replicate is the mechanism: a decision with a date, an owner and an estimated impact, and a tracking sheet that compares every month against the starting point.

### What Came Out of All This

Everything covered belongs to the modeled case built on the pack's templates: it is not a real restaurant or an identifiable business, but the same menu worked from start to finish with the eight tools, so you can see the whole picture before applying it to yours.

The starting menu has twenty dishes set up, with 4,870 units sold per month and net sales of $59,029; on that volume, the menu's weighted average food cost comes to 32.7% and the weighted average contribution margin to $8.16 per dish, inside the range commonly cited as healthy: an average food cost of about 30% of sales, with a healthy range of 25-35%. The recipe cost card that opens the case yields a plate cost of $5.67 and a target menu price, pre-tax, of $18.90, backed by a weighted average yield of 60.5% in that same product's yield test.

The multi-method classification is where judgment shows most, because disagreement between readings is the norm, not the exception: of the twenty dishes, only three land in the best category under all four readings at once, and twelve have three or four readings outside that agreement. With those twelve, the decision depended on each dish's turnover:

- Disagreement on a high-turnover dish: the menu price was kept and the volume watched, because losing sales to fix a single reading costs more than living with the disagreement between methods.
- Disagreement on a low-turnover dish: the recipe was reviewed or the dish was removed, because there is no volume there to make up for a food cost that's out of line.

The menu closed with six Stars and three Dogs under Kasavana & Smith, and those three Dogs concentrated a good part of the decisions in the next step. With the price set dish by dish, eleven of the twenty ended up on target; the whole menu at those chosen prices has a food cost of 36.7% and a total difference of -$13.54 against current menu prices, the gap between what you charge today and what the tool recommends charging.

On third-party delivery the menu splits differently: twelve dishes are viable on the app and eight are left to exclude or reformulate, with an average effective delivery food cost of 54.6%. The logic is always the same: every dish carries its effective food cost (the one that already includes the channel's commission and the packaging) set against its ceiling price; below the ceiling it goes up in price and stays on the app, and above the ceiling it comes off, because raising it would price it out of the channel. The total monthly dine-in margin is $43,635, and the margin difference of delivery against dine-in is -$13,585.

The bar, on its own, delivers a weighted beverage cost of 26.4% and a total contribution margin of $32,153.04. And the year, taken as a whole, closes with a prime cost of 63.4%, below the 65% target in force on the dashboard throughout the case. To read it inside the full P&L, the reference ranges put the cost structure of a restaurant at 30% product, 30-35% labor with service integrated, 5-10% rent and 13-20% overhead (with 17% as the ideal), which leaves a healthy EBITDA of 10-13%, with restructuring recommended below 10%.

All of that ends in the 90-day action plan: ten recorded decisions, each with its owner, its execution week and its estimated impact in the table below. Read it with that word up front, estimated: the total impact is $2,360 and, carried to twelve months, $28,320, and the achieved column of the same table stays at zero on purpose, because the work hasn't been carried out yet. It is the plan's reading on the date it closes, not a result already banked.

The quarter's indicators, in the table that follows, show the starting point and the target the case was built with: food cost goes from 33.1% in month zero to 29.8% in month three, prime cost from 66.8% to 63.8%, and the menu shrinks from twenty dishes to eighteen. Those month-three figures are the example target the modeled case closed with, not what will happen to you: yours will be told by your own menu, worked with the same eight tools.

**The Whole Example Menu, Dish by Dish (`menu-engineering-matrix.xlsx`, "Data" sheet)**

| Dish | Family | Units Sold | Plate Cost ($) | Menu Price Pre-Tax ($) | CM ($) | Food Cost (%) | Menu Price With 10% Illustrative Sales Tax ($) |
|---|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | Starters | 420 | $2.10 | $8.60 | $6.50 | 24.4% | $9.46 |
| Heirloom tomato salad with tuna belly and scallions | Starters | 310 | $3.60 | $11.80 | $8.20 | 30.5% | $12.98 |
| Garlic shrimp | Starters | 260 | $6.90 | $15.50 | $8.60 | 44.5% | $17.05 |
| Broken eggs with potatoes and chistorra sausage | Starters | 380 | $2.40 | $9.80 | $7.40 | 24.5% | $10.78 |
| Local cheese board | Starters | 90 | $5.20 | $13.60 | $8.40 | 38.2% | $14.96 |
| Confit artichokes with ham | Starters | 120 | $3.10 | $10.90 | $7.80 | 28.4% | $11.99 |
| Roasted tomato soup with basil | Starters | 150 | $1.20 | $7.20 | $6.00 | 16.7% | $7.92 |
| Iberico pork tenderloin with sweet potato purée | Mains | 340 | $5.67 | $17.30 | $11.63 | 32.8% | $19.03 |
| Confit cod in pil-pil sauce | Mains | 190 | $7.40 | $19.10 | $11.70 | 38.7% | $21.01 |
| Dry-aged beef burger with fries | Mains | 460 | $4.30 | $13.60 | $9.30 | 31.6% | $14.96 |
| Creamy rice with Iberico pork secreto and mushrooms | Mains | 270 | $6.20 | $16.40 | $10.20 | 37.8% | $18.04 |
| Dry-aged bone-in ribeye (17.64 oz) | Mains | 110 | $14.80 | $32.70 | $17.90 | 45.3% | $35.97 |
| Salt-baked sea bass | Mains | 80 | $8.90 | $21.80 | $12.90 | 40.8% | $23.98 |
| Free-range roast chicken with potatoes | Mains | 300 | $3.70 | $12.70 | $9.00 | 29.1% | $13.97 |
| Seasonal vegetable lasagna | Mains | 140 | $2.60 | $11.40 | $8.80 | 22.8% | $12.54 |
| Seared bluefin tuna tataki with sesame | Mains | 130 | $9.60 | $22.40 | $12.80 | 42.9% | $24.64 |
| Creamy cheesecake | Desserts | 520 | $1.30 | $5.90 | $4.60 | 22.0% | $6.49 |
| Caramelized torrija with ice cream | Desserts | 210 | $1.10 | $5.50 | $4.40 | 20.0% | $6.05 |
| Chocolate lava cake | Desserts | 330 | $1.60 | $6.20 | $4.60 | 25.8% | $6.82 |
| Prepared seasonal fruit | Desserts | 60 | $1.40 | $4.50 | $3.10 | 31.1% | $4.95 |

*This is the same menu that appears in the card, in the matrix, in the pricing sheet and in the multichannel simulator: everything you read in this guide comes from these lines. Printed prices in the US and Canada are the pre-tax column; in the UK and Australia the printed price already includes tax, so use the net figure for every percentage.*

**The Same Menu on Third-Party Delivery (`multichannel-repricing-simulator.xlsx`, "Menu" sheet)**

| Dish | Plate Cost ($) | Dine-In Menu Price Pre-Tax ($) | Delivery Food Cost (%) | Delivery Price Needed ($) | Ceiling Price ($) | Viable? |
|---|---|---|---|---|---|---|
| Iberico ham croquettes (6 pcs) | $2.10 | $8.60 | 46.5% | $10.00 | $11.60 | Yes |
| Heirloom tomato salad with tuna belly and scallions | $3.60 | $11.80 | 52.1% | $15.36 | $15.90 | Yes |
| Garlic shrimp | $6.90 | $15.50 | 70.0% | $27.14 | $20.90 | No: exclude or reformulate |
| Broken eggs with potatoes and chistorra sausage | $2.40 | $9.80 | 45.2% | $11.07 | $13.20 | Yes |
| Local cheese board | $5.20 | $13.60 | 62.0% | $21.07 | $18.40 | No: exclude or reformulate |
| Confit artichokes with ham | $3.10 | $10.90 | 49.8% | $13.57 | $14.70 | Yes |
| Roasted tomato soup with basil | $1.20 | $7.20 | 37.7% | $6.79 | $9.70 | Yes |
| Iberico pork tenderloin with sweet potato purée | $5.67 | $17.30 | 52.6% | $22.75 | $23.40 | Yes |
| Confit cod in pil-pil sauce | $7.40 | $19.10 | 60.6% | $28.93 | $25.80 | No: exclude or reformulate |
| Dry-aged beef burger with fries | $4.30 | $13.60 | 52.5% | $17.86 | $18.40 | Yes |
| Creamy rice with Iberico pork secreto and mushrooms | $6.20 | $16.40 | 60.1% | $24.64 | $22.10 | No: exclude or reformulate |
| Dry-aged bone-in ribeye (17.64 oz) | $14.80 | $32.70 | 67.7% | $55.36 | $44.10 | No: exclude or reformulate |
| Salt-baked sea bass | $8.90 | $21.80 | 62.9% | $34.29 | $29.40 | No: exclude or reformulate |
| Free-range roast chicken with potatoes | $3.70 | $12.70 | 49.5% | $15.71 | $17.10 | Yes |
| Seasonal vegetable lasagna | $2.60 | $11.40 | 41.4% | $11.79 | $15.40 | Yes |
| Seared bluefin tuna tataki with sesame | $9.60 | $22.40 | 65.7% | $36.79 | $30.20 | No: exclude or reformulate |
| Creamy cheesecake | $1.30 | $5.90 | 48.4% | $7.14 | $8.00 | Yes |
| Caramelized torrija with ice cream | $1.10 | $5.50 | 46.8% | $6.43 | $7.40 | Yes |
| Chocolate lava cake | $1.60 | $6.20 | 53.0% | $8.21 | $8.40 | Yes |
| Prepared seasonal fruit | $1.40 | $4.50 | 66.7% | $7.50 | $6.10 | No: exclude or reformulate |

**The Decisions, With Owner and Date (`90-day-action-plan.xlsx`, "Decisions" sheet)**

| Dish or Area | Source Tool | Decision | Week | Status | Estimated Impact ($/Month) |
|---|---|---|---|---|---|
| Garlic shrimp (S3) | Multi-method matrix | Review | 2 | Pending | $180.00 |
| Dry-aged bone-in ribeye (M5) | Multi-method matrix | Redesign | 1 | Pending | $260.00 |
| Local cheese board (S5) | Multi-method matrix | Redesign | 4 | Pending | $140.00 |
| Seasonal vegetable lasagna (M8) | Multi-method matrix | Review | 3 | Pending | $120.00 |
| Prepared seasonal fruit (D4) | Multi-method matrix | Remove | 3 | Pending | $60.00 |
| Salt-baked sea bass (M6) on delivery | Multichannel simulator | Remove | 2 | Pending | $90.00 |
| Ribeye (M5) on delivery | Multichannel simulator | Remove | 2 | Pending | $140.00 |
| Whole fish: switch to fillets | Yield test | Negotiate | 5 | Pending | $260.00 |
| Crianza by the glass: menu price | Beverage menu | Reprice | 2 | Pending | $210.00 |
| Dine-in staffing schedule in slow months | Prime cost dashboard | Reformulate | 6 | Pending | $900.00 |

**The Quarter's Indicators (`90-day-action-plan.xlsx`, "Tracking KPIs" sheet)**

| KPI | Month 0 | Month 3 | Change Month 3 vs. Month 0 | Reading |
|---|---|---|---|---|
| Food cost (%) | 33.1% | 29.8% | -3.3% | Improvement |
| Prime cost (%) | 66.8% | 63.8% | -3.0% | Improvement |
| Average check pre-tax ($) | 27.4 | 29.1 | 1.7 | Improvement |
| Contribution margin per cover ($) | 18.1 | 20.2 | 2.1 | Improvement |
| Dishes on the menu (no.) | 20.0 | 18.0 | -2.0 | Improvement |

*The month-3 figures are the target the book was seeded with so you can see how to read the table, not a forecast of results.*


---
## 20. When Your Spreadsheet Falls Short

### The Four Signs Your Spreadsheet Has Outgrown You

There comes a point when the spreadsheet stops being the tool and becomes the bottleneck. The first sign is opening a second location: every site brings its own vendors, its own menu and its own buying rhythm, and holding all of that in duplicated tabs of the same workbook multiplies the work without multiplying your control, until nobody knows which copy is the real one. The second is supplier prices that change daily: fish, shellfish and a good share of the produce come through your back door at a different price every morning, and updating every recipe cost card that uses those ingredients by hand is a job nobody keeps up for more than a few weeks. The third is inventory: once your storeroom no longer fits a visual count on a weekend, with several product families, several vendors and trim loss to log dish by dish, running it by hand stops being control and becomes guesswork. The fourth is more than one person touching the same sheet: with no record of who changed what and when, the sheet stops being reliable and turns into a file you have to audit before you believe it.

### What Software Gives You That a Spreadsheet Doesn't

Recipe-costing and menu-management software solves exactly that. First, price entry: the vendor sends the delivery invoice and the cost price updates itself, so every card reflects the cost on the day the dish was served, not the cost at your last manual review. Second, recalculation: change one vendor's price and the margin of every menu item that uses it recalculates without you opening a single document; the advantage over the spreadsheet is not that the math is more accurate, it is that it happens without anyone having to remember. Third, traceability: there is a record of who changed each price and when, so a margin that moves has an answer, not a suspect, between shifts.

And here is the line that settles the decision: this guide gives you the judgment, the software gives you the automation. Software like this runs somewhere around $1,100 a year per location, before sales tax, so the jump makes sense when the time it saves is worth more than that figure, not before.

Staying in the spreadsheet isn't free to maintain either. The 90-day plan in this pack sets 26 milestones on its calendar, each with an owner and a date; right now, fresh out of the box, all 26 are still pending and progress reads 0%, because people move it, not the template. The same plan logs 10 decisions with a 90-day completion target of 80%: their estimated impact is $2,360, with a twelve-month projection, as the plan itself shows it, of $28,320. Of those, 5 come from the multi-method matrix ($760 of impact) and 2 from the multichannel simulator; the table below splits the rest by tool, and the table above splits the work by block.

### What an AI Agent Gives You

An AI agent will not calculate your margin for you; that is what the recipe cost card is for and, if your volume justifies it, the software. What it does is speed up the work around your menu. It drafts a dish's card from its ingredients and method in the time it would take you to dictate it. It proposes reformulations when an ingredient goes up in price or becomes unavailable, using the same substitution logic you already apply yourself, only in seconds and across the whole menu: on a sample menu with 20 dishes loaded, going through them one by one to decide what to swap stops taking an afternoon and gets settled in a single query. And it reads your menu in plain language: you describe what you have set up and it tells you where there is a pricing imbalance, a name that doesn't sell or a dish nobody has touched in months.

What it doesn't do is replace the judgment in this guide. It applies it faster. Which dish to raise, which to pull and what price to anchor the menu on are decisions you already know from earlier chapters; the agent runs that logic so you don't have to repeat it by hand every time.

That is where AI Chef Pro comes in, the platform behind this guide: AI agents built for people who run a restaurant and need to write up, reformulate and read their menu without opening a new spreadsheet every time. It is not required to get value from this guide (the pack works fully with a pencil, a calculator and the templates you already have), and it is not a promise of results. It is one more tool, for whoever decides it suits them.

### The Math: What Each Step Up Costs

There are four signs your spreadsheet has fallen short, and they almost always arrive together. The first is having more than one location: every new opening duplicates the file, and with two or three locations nobody is sure which version is the good one. The second is supplier prices that change daily (fish, shellfish, seasonal produce), because a recipe cost card you must update by hand every morning stops getting updated the first week things get busy. The third is an inventory you can no longer run by hand: when the number of items passes what one person can count and value in an afternoon, the data stops being reliable the same day it is written down. And the fourth is having more than one person touching the same sheet at once, which is exactly where two different versions of the same dish show up with two different costs and nobody knows which one won in the end.

Recipe-costing and menu-management software solves three things a spreadsheet doesn't solve well, no matter who runs it: prices come in on their own from the delivery invoice, with nobody typing them or copying them from one document to another; the recipe cost recalculates the instant an ingredient's cost changes, without anyone opening or touching a file; and there is a trail of who changed each figure and when, something a sheet passed around by email never gives you. None of the three is magic: they are automations that replace mechanical tasks, not decisions.

An AI agent adds a different layer. It drafts a dish's recipe card from the data you give it, proposes reformulations when an ingredient spikes in price and reads the whole menu in plain language to point out which dishes to review first. None of that replaces the judgment this book brings: it applies it faster, across more dishes, without you rereading card by card.

This guide gives you the judgment; the software gives you the automation. Recipe-costing and menu-management software runs somewhere around $1,100 a year per location, before sales tax, so you make the jump when the time it saves is worth more than that figure, and each business does that math with its own numbers, not a book.

### The Right Order: Judgment First, Automation Second

Staying in Excel has a cost too, even if no invoice shows up each month. The 90-day action plan in this pack logs 26 milestones on its calendar, with all 26 still open, a 0% progress reading the moment you open the file, as the "90-Day Calendar" sheet of 90-day-action-plan.xlsx shows, because the calendar starts blank on day one. Every milestone has an owner and a date; if nobody closes them, neither the sheet nor the software you buy later will be worth anything, because the tool doesn't make the decision for you: it just records it.

The "Decisions" sheet of 90-day-action-plan.xlsx holds 10 decisions already logged, with a 90-day completion target of 80% and a total estimated impact of $2,360, which the workbook itself projects to $28,320 over twelve months. Of those ten decisions, 5 come from the multi-method matrix, with an estimated impact of $760, and another 2 come from the multichannel simulator: two different origins for the same discipline, because you first test the decision with a method (the matrix, the simulator) and only then carry it out. The sample menu that comes with the matrix, on the "Data" sheet of menu-engineering-matrix.xlsx, has 20 dishes loaded: just enough to see the pattern without the volume drowning out the judgment.

That order, method first and then the tool that automates it, is what holds up everything before it. No platform decides for you what to reformulate or what menu price to set: the matrix, the simulator and the judgment you have already worked through in the earlier pages decide that. AI Chef Pro is a platform of AI agents built for people who run restaurants and want to apply that same judgment with less manual work (drafting cards, proposing reformulations, reading the full menu), but it does not promise results on its own and you don't need it to get value from this guide: the 90-day plan works the same with or without it. You close the final math yourself: if the time you spend maintaining the sheet weighs more than what it costs to automate it, that is the moment to make the jump, not before and not after.

**Plan Progress by Work Block (90-day-action-plan.xlsx, "90-Day Calendar" Sheet)**

| Block | Milestones | Done | Progress (%) |
|---|---|---|---|
| Measure | 4 | 0 | 0% |
| Cost and Classify | 4 | 0 | 0% |
| Apply Decisions | 8 | 0 | 0% |
| Measure the Effect | 8 | 0 | 0% |
| Review | 2 | 0 | 0% |

*The workbook ships with everything at zero: progress is written by whoever does the work, and that is exactly what no software does for you.*

**Which Tool Each Decision Comes From (90-day-action-plan.xlsx, "Decisions" Sheet)**

| Source Tool | Decisions | Estimated Impact ($/Month) | Achieved Impact ($/Month) |
|---|---|---|---|
| Recipe Cost Card | 0 | $0.00 | $0.00 |
| Yield Test | 1 | $260.00 | $0.00 |
| Target Price | 0 | $0.00 | $0.00 |
| Multi-Method Matrix | 5 | $760.00 | $0.00 |
| Multichannel Simulator | 2 | $230.00 | $0.00 |
| Beverage Menu | 1 | $210.00 | $0.00 |
| Prime Cost Dashboard | 1 | $900.00 | $0.00 |


---


---

## About the Author and Terms of Use

John Guerrero is CEO of AI Chef Pro and founder of ChefBusiness Group. He has worked in kitchens since he was 17 and has been a hospitality consultant since 2010, advising on the opening of more than 200 venues, including MICHELIN-starred restaurants in Spain and across Europe. More about his work at johnguerrero.es.

**Version 1.0 · October 2026 · aichef.pro/en/digital-products/food-cost-menu-engineering-guide · info@aichef.pro**

*This guide is a professional working document, not tax, legal or accounting advice. The tax rates it mentions are illustrative and sit in editable cells of the spreadsheets precisely because they change: if the rate changes, you change the cell and the whole workbook recalculates. The costs, menu prices, margins and percentages are example values taken from the eight Excel templates that come with this pack, and they are there for you to replace with your own: none of them is a forecast of your results or a pricing recommendation. How a specific transaction is classified for tax purposes, such as what counts as a restaurant service versus a sale of goods, or which rate applies to a given product, depends on the facts of that transaction. Before you change your menu, the price of a dish or the tax rate you charge, check with your accountant or tax advisor.*
