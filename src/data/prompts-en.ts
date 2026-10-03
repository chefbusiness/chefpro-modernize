// English edition of src/data/prompts.ts for the EN dashboard of
// /en/digital-products/ai-prompts-for-restaurants.
// Keep in sync with the Spanish file (same ids, categories, order and placeholder counts).

export interface Prompt {
  id: number;
  title: string;
  compatible: string[];
  text: string;
}

export interface Category {
  id: string;
  title: string;
  promptCount: number;
  prompts: Prompt[];
}

export const categories: Category[] = [
  {
    id: "cocina",
    title: "Creative Cooking and Recipes",
    promptCount: 10,
    prompts: [
      {
        id: 1,
        title: "Signature recipe built around a main ingredient",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Act as an executive chef with experience in contemporary signature cuisine. Create a fine-dining recipe that makes [MAIN INGREDIENT] the absolute star. The dish must have:\n- A creative, evocative name\n- The story of the dish (2-3 sentences)\n- Ingredients for 4 servings with exact quantities\n- Step-by-step method (professional techniques)\n- Plating and presentation\n- Recommended pairing\n- Difficulty level: [BASIC/INTERMEDIATE/ADVANCED]\nCuisine style: [MEDITERRANEAN/NORDIC/ASIAN/FUSION]"
      },
      {
        id: 2,
        title: "7-course tasting menu",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design a 7-course tasting menu for a [TYPE OF CUISINE] restaurant. The menu must:\n- Follow a coherent culinary narrative from start to finish\n- Include: welcome bite, 2 starters, fish, meat, pre-dessert and dessert\n- Respect the progression of flavors (from light to intense)\n- Give each dish a name, a description and its main technique\n- Restrictions to avoid: [ALLERGENS/PREFERENCES]\n- Target price per guest: [PRICE RANGE]\n- Season: [SPRING/SUMMER/FALL/WINTER]"
      },
      {
        id: 3,
        title: "Reinterpret a classic with modern techniques",
        compatible: ["AI Chef Pro", "ChatGPT", "Perplexity"],
        text: "Take the classic dish [DISH NAME] from [COUNTRY/REGION] cuisine and reinterpret it with contemporary cooking techniques. Keep the essence and recognizable flavors of the original but transform:\n- The texture of at least 2 components\n- The plated presentation\n- Include at least one modern technique (gelification, spherification, dehydration, emulsion, etc.)\nExplain what you keep from the original and what you transform. Include the complete recipe."
      },
      {
        id: 4,
        title: "Seasonal recipe with local products",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "I'm the chef of a restaurant in [CITY/REGION] and I want to create a dish that highlights the seasonal products of [MONTH/SEASON]. Give me a recipe that:\n- Uses at least 3 seasonal, locally sourced products from that region\n- Can be executed during restaurant service (no more than 15 min of mise en place per pass)\n- Has a food cost below [X]% of the menu price\n- Target menu price: [PRICE]\n- Estimated number of guests per service: [N]"
      },
      {
        id: 5,
        title: "Fine-dining plant-based recipe",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design a restaurant-quality plant-based (100% vegan) recipe that can compete on the menu with animal-protein dishes. The dish must:\n- Have a flavor complexity comparable to a meat or fish dish\n- Use techniques that build umami (fermentation, Maillard, reduction, etc.)\n- Be visually striking on the plate\n- Star plant ingredient: [INGREDIENT]\n- Without: [ADDITIONAL RESTRICTIONS]\nInclude the complete recipe, techniques and a pairing suggestion."
      },
      {
        id: 6,
        title: "Zero-waste utilization recipe",
        compatible: ["AI Chef Pro", "ChatGPT", "DeepSeek"],
        text: "I have these by-products and trim in my kitchen that normally get thrown away: [LIST OF BY-PRODUCTS]. Create one or more recipes that use them in full in menu dishes or small plates. For each recipe give me:\n- Dish name\n- By-product used and how it is transformed\n- Technique applied\n- Value added to the menu (sustainability story)\n- Suggested menu price"
      },
      {
        id: 7,
        title: "Creative fermentation recipe",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Act as an expert in culinary fermentation. I want to ferment [INGREDIENT] to use in [TYPE OF DISH/CONTEXT]. Give me:\n- The most suitable fermentation technique (koji, lacto-fermentation, garum, kombucha, miso, shoyu...)\n- A detailed step-by-step process with times and temperatures in °F (°C)\n- Expected result in flavor, texture and aroma\n- Culinary applications of the finished ferment (3 ideas)\n- Common mistakes to avoid\n- Total time until it is ready to use"
      },
      {
        id: 8,
        title: "Menu-ready dish description",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Write the description of the dish [DISH NAME] for the menu of a [TYPE] restaurant. The main ingredients are: [LIST]. The description must:\n- Be between 18 and 28 words (concise but evocative)\n- Appeal to the senses without being cheesy\n- Mention the main technique if it adds value\n- Tone: [ELEGANT/CASUAL/MODERN/TRADITIONAL]\nGive me 3 alternative versions to choose from."
      },
      {
        id: 9,
        title: "Scaling a recipe for high-volume service",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "I have this recipe designed for [ORIGINAL NUMBER OF SERVINGS]: [PASTE RECIPE]. I need to scale it to [TARGET NUMBER OF SERVINGS]. Please:\n- Scale all quantities precisely\n- Warn me about ingredients that do NOT scale linearly (yeast, salt, spices, gelatin)\n- Adjust cooking times if needed\n- Tell me whether any process changes when producing at that volume\n- Suggest adaptations for production in a commissary kitchen if the volume is above 50 servings"
      },
      {
        id: 10,
        title: "Fusion recipe between two cuisines",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create a fusion recipe between [CUISINE 1] cuisine and [CUISINE 2] cuisine that feels coherent and not forced. The dish must respect the essence of both culinary traditions. Tell me:\n- What elements you take from each cuisine (techniques, ingredients, philosophy)\n- Why this combination makes culinary sense\n- The complete recipe with ingredients and method\n- A dish name that reflects the fusion\n- Possible points of cultural friction to keep in mind"
      }
    ]
  },
  {
    id: "gestion",
    title: "Management, Costs and Waste",
    promptCount: 8,
    prompts: [
      {
        id: 11,
        title: "Food cost calculation for a recipe",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Calculate the food cost of this recipe for [N] servings. I'm giving you the ingredients and costs:\n[LIST: ingredient - quantity - price per lb/kg/unit]\nPlease calculate:\n- Total raw-material cost\n- Cost per serving\n- Food cost % if the menu price is [PRICE]\n- Recommended food cost % for this type of establishment: [TYPE]\n- If the food cost is high, suggest 2-3 optimizations that don't sacrifice quality"
      },
      {
        id: 12,
        title: "Waste and yield analysis by ingredient",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Act as an expert in restaurant cost control. For the following ingredients, give me the standard yield loss percentage by type of processing and the usable net weight:\n[LIST OF INGREDIENTS]\nFor each one, indicate:\n- % loss from raw trimming\n- % loss after cooking (if applicable)\n- Final net yield per unit of gross weight (lb or kg)\n- Real price per net lb/kg (if the gross costs [PRICE PER LB/KG])\n- Tips to reduce waste in the kitchen"
      },
      {
        id: 13,
        title: "Menu engineering: profitability by dish",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Analyze the profitability of these dishes on my menu using the menu engineering matrix (Boston Matrix):\n[TABLE: dish - menu price - food cost - units sold/week]\nClassify each dish as: Star (high profitability, high demand), Puzzle (high profitability, low demand), Plowhorse (low profitability, high demand), Dog (low profitability, low demand).\nRecommend what to do with each one: keep, redesign, remove or relaunch."
      },
      {
        id: 14,
        title: "Complete professional recipe costing",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Build the complete recipe costing (cost card) for the dish [DISH NAME]. Ingredients and quantities: [LIST]. Target menu price: [PRICE]. Include:\n- Costing table with cost per ingredient\n- Total raw-material cost\n- Estimated labor cost (prep time: [MINUTES] × hourly cost: [HOURLY COST])\n- Estimated indirect costs (energy, consumables): [%]\n- Gross and net margin\n- Minimum menu price to reach the target margin: [%]\n- Menu price recommendation"
      },
      {
        id: 15,
        title: "Weekly purchasing optimization",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Help me optimize my restaurant's weekly order. Data:\n- Menu for the week: [DESCRIPTION OR LIST OF DISHES]\n- Estimated number of services per day: [N]\n- Active days of the week: [DAYS]\n- Ingredients I already have in stock: [LIST]\nGenerate an optimized shopping list with exact quantities, factor in standard yield loss, and group by supplier where possible (butcher, fishmonger, produce, dry goods)."
      },
      {
        id: 16,
        title: "Dish redesign to improve profitability",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "This dish has a food cost that is too high: [DISH DESCRIPTION] with a current food cost of [%]. My goal is to bring it down to [%] without the guest perceiving any loss of value. Propose:\n- Substitution or reduction of high-cost ingredients\n- Techniques that add perceived value without increasing cost\n- A plating redesign that justifies the price\n- A new menu price proposal if perceived value improves"
      },
      {
        id: 17,
        title: "Inventory control and rotation",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "I have the following ingredients in my walk-in with these expiration / best-by dates: [LIST WITH DATES]. I need:\n- Order of use priority by urgency\n- Suggestions for daily specials that use them up\n- Preservation techniques to extend the shelf life of the most critical items\n- An alert on what will be lost if I don't act within 24/48 hours\n- A mise en place proposal that minimizes losses this week"
      },
      {
        id: 18,
        title: "Market-based menu pricing",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Help me set the menu price for [DISH NAME]. The raw-material cost is [PRICE] per serving. My restaurant is a [TYPE] in [CITY], with a current average check of [PRICE]. Consider:\n- Benchmark against market prices for that type of establishment\n- Price elasticity for that guest profile\n- Pricing strategy: price leader, premium price, fair price\n- The price that maximizes margin without sacrificing sales volume\n- Whether it is better to present it as a round price or with cents (price psychology)"
      }
    ]
  },
  {
    id: "catering",
    title: "Catering and Events",
    promptCount: 8,
    prompts: [
      {
        id: 19,
        title: "Wedding menu proposal",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design a menu proposal for a wedding with [N] guests:\n- Profile of the couple/guests: [DESCRIPTION]\n- Budget per person: [PRICE]\n- Confirmed dietary restrictions: [LIST]\n- Time of year: [MONTH]\n- Venue: [INDOOR/OUTDOOR/ESTATE/HOTEL]\n- Format: [PLATED SERVICE/BUFFET/STATIONS/COCKTAIL RECEPTION]\nInclude: welcome cocktail hour, a complete menu with options, a suggested beverage list and an estimate of the staff required."
      },
      {
        id: 20,
        title: "Corporate catering quote",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Prepare a detailed quote for a corporate event:\n- Number of people: [N]\n- Format: [COFFEE BREAK/LUNCH/GALA DINNER/COCKTAIL]\n- Duration: [HOURS]\n- Location: [OUR OWN VENUE/CLIENT SITE/EXTERNAL VENUE]\n- Maximum budget: [PRICE]\nBreak down: food cost, beverages, staff, logistics, equipment rental and profit margin. Include payment terms and cancellation policy."
      },
      {
        id: 21,
        title: "Operational production plan for an event",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create the operational production plan for this event: [DESCRIPTION]. Date: [DATE]. Menu: [DESCRIPTION]. Available staff: [N people]. Organize:\n- Production timeline (from 3 days before through service)\n- Task assignment per person\n- Mise en place list by day\n- Loading/transport checklist if applicable\n- Plan B for the most critical preparations"
      },
      {
        id: 22,
        title: "Event menu with multiple restrictions",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design a menu for an event of [N] people where these dietary restrictions coexist: [DETAILED LIST: X vegan, Y celiac, Z lactose-free, etc.]. The challenge: no segregated special menus. Propose a single unified menu that works for everyone without anyone feeling they got an inferior version."
      },
      {
        id: 23,
        title: "Food stations for a cocktail reception",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design [N] themed food stations for a cocktail reception of [N] people lasting [HOURS]. Each station must have:\n- A name and thematic concept\n- 4-6 preparations (cold/hot mix)\n- 1 spectacular or interactive element to draw in the guests\n- Setup time and staffing needs per station\nOverall event theme: [THEME]. Total budget: [PRICE]"
      },
      {
        id: 24,
        title: "Sales proposal email for a client",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write a sales proposal email for a prospective catering client. Event: [TYPE]. The email must:\n- Be professional but warm, not robotic\n- Summarize our differentiating value proposition\n- Briefly mention the suggested menu: [DESCRIPTION]\n- Price per person: [PRICE]\n- Include a clear call to action to schedule a meeting or tasting\n- Length: 200 words maximum\nSigned by: [NAME/TITLE]"
      },
      {
        id: 25,
        title: "Buffet quantity calculation",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Calculate the exact food quantities for a buffet of [N] people lasting [HOURS]. Profile: [CORPORATE/FAMILY/GALA/CASUAL]. Buffet menu: [DESCRIPTION]. Take into account:\n- Standard per-person ratios by category\n- Consumption factor based on guest profile and time of day\n- Recommended safety surplus\n- Order of placement on the buffet line to optimize consumption"
      },
      {
        id: 26,
        title: "Seasonal menu for premium catering",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design a premium catering menu for the [SEASON/MONTHS] season that highlights hyperlocal products and top quality. Level: gourmet/high-end. The menu must be a culinary statement, not just a food service. Include storytelling for the main ingredients and suggest how to communicate it to clients."
      }
    ]
  },
  {
    id: "marketing",
    title: "Business Marketing",
    promptCount: 8,
    prompts: [
      {
        id: 27,
        title: "Instagram post for a menu dish",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Write an Instagram post to introduce the dish [NAME] at the restaurant [NAME]. Main ingredients: [LIST]. The post must:\n- Start with a powerful hook in the first line\n- Tell the story or concept behind the dish\n- Include a natural call to action\n- End with 15-20 relevant hashtags\n- Tone: [ELEGANT/FRIENDLY/PASSIONATE/INFORMATIVE]\n- Length: 150-200 words of text + hashtags"
      },
      {
        id: 28,
        title: "Local SEO content for a restaurant blog",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write an SEO-optimized blog article for the restaurant [NAME] in [CITY]. Target keyword: [DISH/TYPE OF CUISINE] in [CITY]. Include:\n- H1 optimized with the keyword\n- Introduction with the keyword used naturally in the first 100 words\n- A description of the experience with genuinely valuable content\n- A \"why visit us\" section with differentiators\n- Practical information (hours, address, reservations)\n- A 155-character meta description\nLength: 600-800 words. Natural tone, not over-optimized."
      },
      {
        id: 29,
        title: "Professional response to a negative review",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "A guest left this negative review: [PASTE REVIEW]. Write a public response that:\n- Thanks them for the feedback without being condescending\n- Acknowledges the problem if it is legitimate\n- Briefly explains what will be done about it\n- Invites the guest to give us a second chance\n- Is neither defensive nor aggressive\nMaximum 100-120 words. Signed by: [NAME/TITLE]"
      },
      {
        id: 30,
        title: "Monthly social media content plan",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Create a social media content plan for the month of [MONTH] for the restaurant [NAME/TYPE]. Frequency: [N posts/week]. Platforms: [Instagram/Facebook/TikTok]. For each post include:\n- Day and time of publication\n- Format (photo/reel/story/carousel)\n- Topic and content concept\n- Summarized copy or main idea\n- Suggested hashtags\nRecommended ratio: 70% value, 20% community, 10% sales."
      },
      {
        id: 31,
        title: "Email marketing for your customer list",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write a marketing email for our customer list. Goal: [ANNOUNCE NEW MENU/EVENT/OFFER/REOPENING]. The email must have:\n- An irresistible subject line (50 characters max)\n- A complementary preheader\n- A warm, personal body (not corporate)\n- A single clear CTA\n- No spammy language\n- A P.S. with a human touch\nTone: as if the chef/owner were writing it personally. Maximum 200 words."
      },
      {
        id: 32,
        title: "Script for a food Reel or TikTok",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Create the complete script for a Reel/TikTok of [DURATION: 30/45/60 seconds] showing [DISH/TECHNIQUE/RECIPE/BEHIND THE SCENES]. The script includes:\n- A visual hook for the first 2 seconds\n- Scene structure with visual description\n- On-screen text (captions/overlays)\n- Recommended music (type/mood)\n- Final CTA\nThe goal is to [GO VIRAL/EDUCATE/SELL/BUILD BRAND]."
      },
      {
        id: 33,
        title: "Chef storytelling for a professional bio",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write the professional bio of [NAME] for the website, press and social media. Details: [CAREER PATH, TRAINING, RESTAURANTS, PHILOSOPHY, ACHIEVEMENTS]. Give me:\n- Long version (300 words) for web and press\n- Short version (80 words) for social media\n- Ultra-short version (1 high-impact sentence) for presentations\n- Tone: [ELEGANT/FRIENDLY/EPIC]\nIt should convey authenticity, not a cold resume."
      },
      {
        id: 34,
        title: "Collaboration pitch to an influencer",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write a collaboration message to a food influencer with [N] followers on [PLATFORM]. Our restaurant: [NAME AND BRIEF DESCRIPTION]. The proposal: [DESCRIPTION]. The message must:\n- Be personalized (mention something specific from their profile)\n- Be direct about what we are proposing\n- Explain the mutual benefit\n- Not sound generic\n- Include a concrete CTA\nMaximum 120 words."
      }
    ]
  },
  {
    id: "pasteleria",
    title: "Pastry, Bakery and Chocolate",
    promptCount: 7,
    prompts: [
      {
        id: 35,
        title: "Contemporary restaurant dessert",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design a fine-dining restaurant dessert that is visually striking and technically executable during service. It must include at least 3 components with different textures (crunchy, creamy, gelled). Star ingredient or concept: [INGREDIENT/CONCEPT]. Restrictions: [ALLERGENS TO AVOID]. Include: dessert name, the story of the dish, complete recipe, specific techniques and a plating description."
      },
      {
        id: 36,
        title: "Chocolate ganache formulation",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Formulate a chocolate ganache with the following characteristics:\n- Type of chocolate: [DARK XX%/MILK/WHITE/BLOND]\n- Application: [BONBON FILLING/TRUFFLE/GLAZE/CAKE/ICE CREAM]\n- Desired final texture: [FIRM/SOFT/FLUID/MOLDABLE]\n- Additional ingredients to incorporate: [LIST]\nGive me: chocolate-to-cream ratio, working temperature in °F (°C), detailed process, crystallization time and storage tips."
      },
      {
        id: 37,
        title: "Artisan sourdough bread",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Create an artisan sourdough bread recipe with these specifications:\n- Type of flour: [TYPE AND STRENGTH]\n- Desired hydration: [%]\n- Mix-ins: [SEEDS/NUTS/OLIVES/SPICES/NONE]\n- Final shape: [BOULE/BATARD/ROLLS/CIABATTA]\n- Baked in: [HOME OVEN/BAKERY OVEN/DUTCH OVEN]\nInclude: sourdough starter formula, complete process with fermentation times, baking temperature in °F (°C) and tricks for a perfect crust."
      },
      {
        id: 38,
        title: "Artisan ice cream formulation",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Formulate an artisan ice cream with the following characteristics:\n- Main flavor: [FLAVOR]\n- Type: [CREAMY/SORBET/SEMIFREDDO/GRANITA]\n- Restrictions: [LACTOSE-FREE/VEGAN/SUGAR-FREE/CONVENTIONAL]\n- Use: [RESTAURANT/GELATO SHOP/RETAIL SALE]\nProvide: complete formula with percentages, sweetness and freezing-point indexes, production process, serving temperature in °F (°C) and a pairing or presentation suggestion."
      },
      {
        id: 39,
        title: "Celebration cake: design and recipe",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Design a celebration cake for [OCCASION] for [N] people. Visual style: [ELEGANT/MODERN/RUSTIC/THEMED]. Desired flavors: [LIST]. Restrictions: [ALLERGENS]. Provide:\n- A detailed visual concept (layers, colors, decoration)\n- Complete recipe for the sponge, filling and frosting\n- Layer structure and assembly\n- Decorating techniques\n- Production timeline (what to do each day)"
      },
      {
        id: 40,
        title: "Chocolate tempering temperature chart",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "I need the complete chocolate tempering guide for professional work. For each type of chocolate (dark, milk, white, blond/caramel) give me:\n- Melting temperature in °F (°C)\n- Cooling temperature (1st drop)\n- Working temperature (final rise)\n- Visual cues to tell whether it is well tempered\n- Common mistakes and how to fix them\n- Alternative tempering methods: seeding and tabling\nFormat: comparison table + process notes."
      },
      {
        id: 41,
        title: "Petit fours collection for a restaurant",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design a collection of 6 petit fours for the end of the meal at a [TYPE/STYLE] restaurant. The collection must:\n- Have visual and conceptual coherence across the 6 pieces\n- Combine techniques: gelification, chocolate, crunchy, creamy\n- Be executable in daily production for [N] services\n- Season: [SEASON]\n- Without: [ALLERGENS]\nFor each piece: name, description, summarized recipe and main technique."
      }
    ]
  },
  {
    id: "food-pairing",
    title: "Food Pairing",
    promptCount: 8,
    prompts: [
      {
        id: 42,
        title: "Molecular pairing between two ingredients",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Analyze the molecular compatibility between [INGREDIENT 1] and [INGREDIENT 2] based on their shared aroma compounds. Tell me:\n- The aroma compounds they share\n- Compatibility level (high/medium/low) and why\n- How to enhance that combination in the kitchen (recommended techniques)\n- 3 concrete dish or preparation ideas that take advantage of this pairing\n- A bridge ingredient that can unite both if the compatibility is low"
      },
      {
        id: 43,
        title: "The perfect ingredient substitute",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "I need a substitute for [ORIGINAL INGREDIENT] in this recipe: [BRIEF DESCRIPTION]. The reason is: [ALLERGY/UNAVAILABLE/PRICE/SEASON]. The substitute must:\n- Keep the flavor profile as similar as possible\n- Work with the same cooking technique\n- Be available in [REGION/SEASON]\nGive me the 3 best options ranked by similarity, with quantity adjustments and any necessary changes to the technique."
      },
      {
        id: 44,
        title: "Wine and dish pairing",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Recommend the ideal wine pairing for this dish: [DISH DESCRIPTION]. Consider:\n- Intensity of the dish and wine/food balance\n- Preferred wine region if applicable: [REGION OR \"any\"]\n- Budget per bottle: [PRICE]\n- Setting: [RESTAURANT/DINNER AT HOME/EVENT]\nGive me: 3 options (a safe one, an interesting one, a surprising one), with grape variety, appellation or region, and an explanation of why the pairing works."
      },
      {
        id: 45,
        title: "Unexpected combinations with a scientific basis",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Propose 5 unexpected or counterintuitive ingredient combinations that are justified by scientific food pairing. For each combination:\n- The two (or more) ingredients\n- Why it works (shared compounds or balanced contrast)\n- One concrete culinary application\n- Surprise level for the guest (from 1 to 5)\nReference ingredient or cuisine profile: [INGREDIENT OR STYLE]"
      },
      {
        id: 46,
        title: "Sensory profile of a dish",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Analyze the complete sensory profile of this dish: [DESCRIPTION]. Evaluate:\n- Dominant and secondary flavors (sweet, salty, sour, bitter, umami, spicy)\n- Textures present and their contrast\n- Main aromas and how they evolve\n- Temperature and thermal contrast\n- Overall balance: what stands out? what is missing?\n- Recommendations to improve the sensory balance\nFormat: detailed analysis + summary table."
      },
      {
        id: 47,
        title: "Single-ingredient menu",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design a 5-course tasting menu where the absolute star of every dish is [INGREDIENT]. The challenge: each dish must show a completely different facet of the same ingredient (raw, cooked, fermented, dehydrated, in a sauce, etc.). Include: the name of each dish, the technique applied to the star ingredient and how the experience evolves from start to finish."
      },
      {
        id: 48,
        title: "Adapting a recipe to a dietary restriction",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Adapt this recipe: [PASTE RECIPE] so that it is suitable for [VEGAN/CELIAC/LACTOSE-FREE/NUT-FREE/DIABETIC]. The adaptation must:\n- Keep the spirit and flavors of the original dish\n- Indicate each substitution with its exact equivalent\n- Warn me if any change significantly affects texture or flavor\n- Verify that the final result fully complies with the restriction\n- If there is a loss of quality, propose compensations"
      },
      {
        id: 49,
        title: "Texture contrast in a dish",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "I want to add texture contrast to this dish, which is currently too uniform: [DISH DESCRIPTION]. Propose:\n- 3 crunchy elements that fit the flavor profile\n- 2 creamy or gelled elements as a counterpoint\n- 1 element that adds contrasting temperature if appropriate\nFor each proposal: ingredient, preparation technique and how to work it into the plating without breaking the coherence of the dish."
      }
    ]
  },
  {
    id: "alergenos",
    title: "Allergens and Food Safety",
    promptCount: 6,
    prompts: [
      {
        id: 50,
        title: "Allergen analysis of a recipe",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Analyze the allergens present in this recipe: [PASTE COMPLETE RECIPE WITH INGREDIENTS]. Identify:\n- Allergens that must be declared by law (use the allergen rules that apply to me: US: the FDA's 9 major allergens · UK/EU: the 14 regulated allergens)\n- Ingredients that may contain hidden allergens or traces\n- Cross-contact risk based on the techniques used\n- Possible substitutes to eliminate each allergen identified\n- How to communicate it correctly on the menu"
      },
      {
        id: 51,
        title: "Protocol for serving a guest with an allergy",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create a service protocol for when a guest reports a food allergy or intolerance in the dining room. The protocol must cover:\n- How to receive the guest's information (key questions to ask)\n- Communication process between front of house and kitchen\n- Verification before serving the dish\n- What to do if there is doubt about cross-contact\n- How to document the incident\nFormat: a step-by-step checklist that can be printed and posted in the kitchen and front of house."
      },
      {
        id: 52,
        title: "Spec sheet with allergen declaration",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Create the complete spec sheet for the dish [NAME] with an allergen declaration for internal use and/or the menu. Ingredients: [COMPLETE LIST]. Include:\n- Allergen table (use the allergen rules that apply to me: US: the FDA's 9 major allergens · UK/EU: the 14 regulated allergens) marked as confirmed present / possible traces / absent\n- Preparation instructions to minimize cross-contact\n- A print-ready format to post in the kitchen\n- A short version to include on the menu or ordering app"
      },
      {
        id: 53,
        title: "Complete celiac-safe menu",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design a complete menu of [NUMBER OF DISHES] that is 100% safe for celiacs (gluten-free ingredients and no cross-contact). The menu is for a [TYPE OF ESTABLISHMENT]. It must:\n- Be culinarily appealing, not a scaled-down version\n- Specify which alternative flours to use in each preparation\n- Indicate the kitchen protocol to avoid cross-contact\n- Include gluten-free desserts that don't feel like a compromise"
      },
      {
        id: 54,
        title: "Labeling an artisan product for sale",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "I need the correct labeling to sell this artisan product: [PRODUCT DESCRIPTION]. It will be sold through [OWN SHOP/MARKET/ONLINE/THIRD PARTIES]. The applicable rules are the local food labeling regulations that apply to me. Provide:\n- Ingredient list in descending order by weight\n- Allergens in bold or highlighted\n- Nutrition information per 100 g and per serving\n- Recommended shelf life and storage conditions\n- Producer information that must appear\n- Mandatory warnings if applicable"
      },
      {
        id: 55,
        title: "HACCP training plan for your team",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create a basic HACCP (Hazard Analysis and Critical Control Points) training plan for the team of a [TYPE OF ESTABLISHMENT] with [N] people. Follow the local regulations that apply to me. The plan must include:\n- Fundamental food safety concepts (executive summary)\n- The most relevant critical control points for that type of business\n- Table of safe temperatures in °F (°C) for storage and cooking\n- Daily hygiene and temperature control checklist\n- A 45-minute training session format for the team"
      }
    ]
  },
  {
    id: "negocio",
    title: "Business Management",
    promptCount: 7,
    prompts: [
      {
        id: 56,
        title: "Restaurant business plan",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Help me structure the business plan for [TYPE OF RESTAURANT/CONCEPT] in [CITY]. Project details: [BRIEF DESCRIPTION]. The plan must cover:\n- Market and local competition analysis\n- Differentiating value proposition\n- Business model and revenue streams\n- Fixed and variable cost structure\n- 12-month revenue projection (with conservative and optimistic scenarios)\n- Estimated initial investment and break-even point\n- Launch marketing strategy"
      },
      {
        id: 57,
        title: "Concept description for a franchise",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Write the concept description to present [RESTAURANT/CHAIN NAME] as a potential franchise. The document must include:\n- Brand history and philosophy (origin and evolution)\n- Value proposition for the franchisee\n- Description of the replicable operating model\n- Competitive advantages of the concept\n- Ideal franchisee profile\n- Summary of investment and estimated return\nTone: a professional executive document of 2 pages."
      },
      {
        id: 58,
        title: "Basic operations manual",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create the table of contents and the first sections of the operations manual for [TYPE OF FOOD BUSINESS]. The manual must cover:\n- Service standards and guest service protocol\n- Opening and closing procedures\n- Reservation management and incident handling\n- Hygiene and food safety standards\n- New-staff training protocol\nFormat: a structured document that can be handed to staff on their first day."
      },
      {
        id: 59,
        title: "SWOT analysis of the business",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Run a complete SWOT analysis for [TYPE OF FOOD BUSINESS] in [CITY/CONTEXT]. Business details: [DESCRIPTION]. Include:\n- Internal weaknesses to work on\n- External threats to monitor\n- Strengths to emphasize in communication\n- Market opportunities to seize\nFor each category: at least 4 items with a description and impact level (high/medium/low). Add the 3 most urgent actions that come out of the analysis."
      },
      {
        id: 60,
        title: "Job description for a key position",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write the job description for [POSITION NAME: executive chef/front-of-house manager/pastry chef/bartender/general manager] at a [TYPE OF ESTABLISHMENT]. Include:\n- Mission of the role within the team\n- Main responsibilities (8-10 points)\n- Experience and training requirements\n- Key competencies (technical and personal)\n- Working conditions (schedule, type of employment if applicable)\n- A description of the team culture to attract the right profile"
      },
      {
        id: 61,
        title: "Pricing strategy for a new menu",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Help me define the pricing strategy for the new menu of a [TYPE OF RESTAURANT]. Business data: current average check [PRICE], monthly fixed costs [PRICE], covers per service [N], services per week [N]. Propose:\n- Price range per category (starters, mains, desserts, beverages)\n- Psychological pricing strategy (charm pricing, anchoring)\n- Target margin structure per category\n- How to communicate a price increase if one is needed"
      },
      {
        id: 62,
        title: "Culinary consulting proposal",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Write a culinary consulting proposal for the client [TYPE OF BUSINESS]. The client has this problem or need: [DESCRIPTION]. The proposal must include:\n- Initial diagnosis of the problem\n- Proposed work methodology\n- Project phases with deliverables per phase\n- Team and consultant profile\n- Investment and payment terms\n- Expected results and success metrics\nTone: professional and results-oriented, not academic."
      }
    ]
  },
  {
    id: "liderazgo",
    title: "Leadership, Teams and Wellbeing",
    promptCount: 6,
    prompts: [
      {
        id: 63,
        title: "Managing stress during high-pressure service",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Act as a wellbeing coach specialized in restaurant industry professionals. I have this stress problem in my team/in myself: [DESCRIPTION OF THE SITUATION]. I need:\n- Stress management techniques that can be applied DURING service (not just afterward)\n- A 5-minute pre-service routine to center the team\n- Early warning signs of burnout in the kitchen\n- How to tell the team there is a problem without creating more tension\n- 3 changes in work dynamics that can reduce chronic pressure"
      },
      {
        id: 64,
        title: "Constructive feedback for the team",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "I need to give feedback about a performance or attitude problem to a [PROFILE: cook/chef de partie / line cook/server/pastry cook]. The situation is: [OBJECTIVE DESCRIPTION OF THE PROBLEM]. The employee has been on the team for [TIME]. Help me:\n- Structure the conversation (SBI model: Situation-Behavior-Impact)\n- The exact phrases to open the conversation without triggering defensiveness\n- How to actively listen to their perspective\n- How to agree on a concrete, measurable improvement plan\n- What to say if the conversation gets tense"
      },
      {
        id: 65,
        title: "Pre-service mindfulness routine",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Design an 8-10 minute mindfulness routine specifically for the kitchen team before an intense service. The routine must:\n- Be practical, not esoteric (adapted for skeptical professionals)\n- Be done in the workspace itself, without changing clothes or location\n- Include breathing techniques, mental focus and gentle physical activation\n- End with a team ritual that builds cohesion\n- Have a script the head chef can read aloud"
      },
      {
        id: 66,
        title: "Effective post-service meeting",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create the outline of a 15-minute post-service meeting for the team of a [TYPE OF ESTABLISHMENT]. Today's service had: [DESCRIPTION: incidents, positive moments, etc.]. The meeting must:\n- Start with what went well (positive reinforcement)\n- Address problems with a focus on solutions, not blame\n- Generate 1-2 concrete actions for the next service\n- Close with something that leaves the team with positive energy\n- Last 15 minutes maximum (script with timings)"
      },
      {
        id: 67,
        title: "Professional development plan for an employee",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Create a 6-month professional development plan for [EMPLOYEE PROFILE: cook with X years of experience, specialty in Y]. The employee wants to grow toward: [CAREER GOAL]. The plan must include:\n- Assessment of current competencies vs. those required for the goal\n- Specific recommended training (courses, workshops, stages)\n- Progressive responsibilities within the team\n- Evaluation milestones every 2 months\n- How to involve the employee in the process so they feel ownership of it"
      },
      {
        id: 68,
        title: "Conflict resolution in the kitchen brigade",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "I have a conflict between two members of my team: [OBJECTIVE DESCRIPTION OF THE SITUATION, no names]. The conflict is affecting: [HOW IT AFFECTS SERVICE/ATMOSPHERE]. As head chef or manager, help me:\n- Understand the possible root causes of the conflict\n- How to approach the conversation separately with each party\n- How to facilitate a joint conversation if necessary\n- What team boundaries and rules to set to prevent recurrence\n- When it is time to escalate the issue to HR"
      }
    ]
  },
  {
    id: "deep-research",
    title: "Deep Research — In-Depth Analysis",
    promptCount: 8,
    prompts: [
      {
        id: 69,
        title: "In-depth analysis of food trends",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "Run an in-depth analysis of emerging food trends for [YEAR/SEASON] in [REGION/COUNTRY]. Research:\n- The 10 trends with the most traction on social media, trade publications and international trade shows\n- Which chefs or restaurants are leading each trend\n- Emerging ingredients and rising techniques\n- Impact on consumer behavior\n- Concrete opportunities for a [TYPE OF ESTABLISHMENT]\n- Predictions for the next 12-18 months\nFormat: executive report with sources and verifiable data."
      },
      {
        id: 70,
        title: "Market study for a new food concept",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "I want to open a [TYPE OF BUSINESS: restaurant/ghost kitchen/food truck/catering] in [CITY/AREA]. Run an in-depth market study that includes:\n- Demographic analysis of the area (potential customer profile)\n- Mapping of direct and indirect competition (at least 10 competitors)\n- Analysis of average prices in the area for similar concepts\n- Market gaps and uncovered opportunities\n- Estimated average check and market volume\n- Barriers to entry and critical success factors\n- Positioning and differentiation recommendation\nFormat: professional report with comparison tables."
      },
      {
        id: 71,
        title: "Ingredient and supplier research",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "I need to research the ingredient [INGREDIENT NAME] in depth to add it to my menu. Analyze:\n- Origin, seasonality and main varieties\n- Nutritional properties and associated allergens\n- Optimal culinary techniques (temperature in °F (°C), time, combinations)\n- Classic and avant-garde pairings\n- Reference suppliers in [COUNTRY/REGION]\n- Market price and seasonal fluctuations\n- Applications in fine dining, casual dining and pastry\n- Search trends and popularity among consumers"
      },
      {
        id: 72,
        title: "Competitive benchmarking of restaurants",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "Run an in-depth benchmarking of my restaurant [NAME/TYPE] against the [3-5] main competitors in [AREA/CITY]. For each one, analyze:\n- Value proposition and positioning\n- Menu: structure, pricing, signature dishes\n- Digital presence: website, social media, reviews (Google, TripAdvisor)\n- Average rating and review sentiment analysis\n- Visible marketing strategy (promotions, events, collaborations)\n- Strengths and weaknesses detected\n- Differentiation opportunities for my business\nFormat: comparison table + report with actionable recommendations."
      },
      {
        id: 73,
        title: "Profitability analysis by dish",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Analyze the profitability of my entire menu using the menu engineering methodology. The data is:\n[LIST OF DISHES with: name, food cost, menu price, units sold/month]\n\nClassify each dish in the culinary BCG matrix:\n- Stars (high popularity + high profitability)\n- Plowhorses (high popularity + low profitability)\n- Puzzles (low popularity + high profitability)\n- Dogs (low popularity + low profitability)\n\nFor each category, recommend specific actions: keep, reposition, reformulate or remove. Include calculations of the impact on total margin."
      },
      {
        id: 74,
        title: "Research on avant-garde techniques",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "Research in depth the avant-garde culinary technique [TECHNIQUE: fermentation/sous vide/spherification/nixtamalization/cold smoking/etc.]. I want a complete report covering:\n- History and origin of the technique\n- Scientific principles (chemistry and physics involved)\n- Equipment needed (basic and professional)\n- Detailed step-by-step to master it\n- 5 creative applications for a [TYPE OF RESTAURANT]\n- Common mistakes and how to avoid them\n- Reference chefs who master it\n- Estimated implementation cost"
      },
      {
        id: 75,
        title: "Feasibility analysis of a new service",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "I want to add a new service to my business: [DESCRIPTION: brunch/delivery/corporate catering/cooking classes/meal prep/pop-up]. My current establishment is [TYPE AND CAPACITY]. Run a feasibility analysis that includes:\n- Estimated initial investment (equipment, staff, marketing)\n- Additional monthly operating costs\n- Revenue projection (pessimistic, realistic, optimistic scenario)\n- Break-even point\n- Human resources needed\n- Impact on current operations\n- Implementation timeline (90 days)\n- Main risks and how to mitigate them"
      },
      {
        id: 76,
        title: "Guest experience audit",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT", "Perplexity"],
        text: "Design a complete guest experience audit for my [TYPE OF ESTABLISHMENT]. I need to evaluate every touchpoint of the customer journey:\n- Discovery (how they find us: SEO, social media, word of mouth)\n- Reservation (process, friction, confirmation)\n- Arrival (first impression, welcome, wait)\n- Service (timing, attention, team knowledge)\n- Food (presentation, temperature, flavor, consistency)\n- Payment (process, options, tip)\n- Post-visit (follow-up, loyalty, reviews)\n\nFor each touchpoint: what to measure, how to measure it, industry benchmark and improvement actions prioritized by impact."
      }
    ]
  }
];
