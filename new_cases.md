# AI Failure Case Studies

## Case Study 1: The Outdated Inundation

### Domain
Environmental Management / Urban Planning

### Deployment Context
A coastal city council used an AI-driven "Flood Guard" dashboard to determine which neighborhoods required mandatory elevation for new construction.

### Intended Use
To provide residents and developers with accurate, real-time risk assessments for flood zones.

### System Type
Predictive Geospatial Modeling / Risk Assessment

### Inputs and Assumptions
- **Historical Rainfall Data:** 30 years of precipitation records.
- **Topography:** Static elevation maps from a 2010 geological survey.
- **Assumption:** Sea-level rise would follow linear historical trends rather than accelerating.

### Outputs Presented to Users
- **Color-coded Risk Maps:** Red (High Risk) to Green (Low Risk).
- **Projected Insurance Premiums:** Estimated costs based on location.

### What Went Wrong
The system produced misleading flood risk maps because it relied on outdated data that did not account for recent rapid sea-level rises and new urban concrete runoff.

### How the Failure Was Detected
A "1-in-100-year" flood event occurred twice in three years, completely submerging neighborhoods marked as "Low Risk" (Green) on the dashboard.

### Who Was Affected
- **Homeowners:** Families in "Safe" zones lost uninsured property.
- **Urban Planners:** Approved dangerous developments based on the AI.
- **Emergency Services:** Resourced the wrong areas during the storm.

### Data Issues
- **Temporal Decay:** Training data was over a decade old.
- **Static Inputs:** Failed to update land-use changes (increased paving).

### Technical Choices
- **Regression Modeling:** Chosen for simplicity but failed to capture non-linear climate shifts.
- **Over-Smoothing:** The AI "cleaned" the map, removing small but vital drainage details.

### Organisational / Governance Factors
- **Budget Constraints:** Refusal to fund annual LIDAR updates.
- **Automation Bias:** Officials viewed the AI as "authoritative" and stopped manual field inspections.

### Timeline of Failure + Aftermath
- **Initial Setup:** AI launched in 2021 using 2010-2015 data.
- **Trigger Event:** Record-breaking rainfall in Autumn 2025.
- **Failure Event:** Maps showed "Green" zones for areas that were 2 feet underwater.
- **Detection:** Citizens reported discrepancies via social media photos.
- **Aftermath:** Council faced class-action lawsuits; system decommissioned.

### Lessons Learned
- AI models for environmental risk must have a "data expiration date."
- Visual authority does not equal factual accuracy.
- Local knowledge must act as a "sanity check" for algorithmic outputs.

### Quiz
- **Q:** Why did the AI fail to predict the floods in the Green zones?
- **A:** It used outdated topography and rainfall data that didn't reflect current climate reality.
- **Q:** What was the primary visual failure?
- **A:** The map looked authoritative but omitted the key assumption of static sea levels.

---

## Case Study 2: The Resolution Mirage

### Domain
Agricultural Surveillance / Supply Chain Ethics

### Deployment Context
An international NGO used AI to monitor "zero-deforestation" compliance for coffee plantations.

### Intended Use
To automatically flag plantations that were encroaching on protected rainforest boundaries.

### System Type
Computer Vision / Land-Cover Classification

### Inputs and Assumptions
- **Satellite Imagery:** Publicly available 30m-resolution imagery.
- **Assumption:** If a pixel is mostly green, it is classified as "Forest."

### Outputs Presented to Users
- **Deforestation Alerts:** Automated emails sent to coffee buyers when a "violation" was detected.

### What Went Wrong
The land-cover classification was used beyond its spatial resolution. Coarse 30m pixels could not distinguish between "Natural Forest" and "Coffee Trees," leading to false accusations against sustainable canopy farmers.

### How the Failure Was Detected
Small-hold farmers provided ground-level photos showing they were growing coffee under a canopy, which the low-res AI misinterpreted as forest clearing.

### Who Was Affected
- **Small-hold Farmers:** Lost "Fair Trade" certifications and income.
- **Coffee Importers:** Cancelled valid contracts based on false AI data.

### Data Issues
- **Resolution Mismatch:** Using 30m data for tasks requiring 1m-5m precision.
- **Class Ambiguity:** Failure to distinguish between diverse "green" spectral signatures.

### Technical Choices
- **Cost-Saving:** Chose free, low-res satellite data over expensive commercial feeds.

### Organisational / Governance Factors
- **Lack of Appeals Process:** Automated flagging led to immediate contract termination without human review.

### Timeline of Failure + Aftermath
- **Initial Setup:** System deployed to monitor 10,000 hectares.
- **Trigger Event:** Farmers began inter-cropping to improve soil health.
- **Failure Event:** AI flagged inter-cropping as "Forest Fragmentation."
- **Detection:** Audit by a human geographer revealed the resolution error.
- **Aftermath:** NGO issued a public apology and reinstated farmer credentials.

### Lessons Learned
- Never use a model for a level of detail finer than its training data supports.
- Ground-truthing (physical checks) is essential for high-stakes environmental AI.

### Quiz
- **Q:** What was the main technical mismatch?
- **A:** Using low-spatial-resolution imagery for high-precision land-cover classification.
- **Q:** Why were farmers unfairly penalized?
- **A:** The AI couldn't tell the difference between forest and canopy-grown crops at that scale.

---

## Case Study 3: The Overconfident Credit Dashboard

### Domain
Fintech / Lending

### Deployment Context
A boutique bank used a "Decision Dashboard" to assist loan officers in approving small business loans.

### Intended Use
To provide a "Score" that summarizes a business's likelihood of repayment.

### System Type
Decision Support System / Dashboard

### Inputs and Assumptions
- **Inputs:** Cash flow, social media sentiment, local economic indices.
- **Assumption:** A high score equals a safe loan, regardless of market volatility.

### Outputs Presented to Users
- **The "Success Dial":** A single percentage score (e.g., "85% Success Probability").
- **Missing Info:** No "Uncertainty" or "Confidence Interval" was shown.

### What Went Wrong
The dashboard hid uncertainty, leading to over-confident conclusions. Loan officers approved risky loans because the UI presented an "80% score" as a definitive fact.

### How the Failure Was Detected
During a minor market dip, the bank suffered a 40% default rate on loans that the AI had labeled as "High Confidence."

### Who Was Affected
- **Loan Officers:** Reputations ruined by "trusting the machine."
- **The Bank:** Faced a liquidity crisis due to bad debt.

### Data Issues
- **Sparse Data:** For new businesses, the AI was "guessing" based on limited data but didn't admit it.

### Technical Choices
- **UI Simplification:** Designers removed "error bars" to make the dashboard look "cleaner."

### Organisational / Governance Factors
- **KPI Alignment:** Officers were rewarded for volume, encouraging them to ignore their gut feelings in favor of high AI scores.

### Timeline of Failure + Aftermath
- **Initial Setup:** Dashboard rolled out to 15 branches.
- **Trigger Event:** Local economic downturn.
- **Failure Event:** Massive loan defaults.
- **Detection:** Internal audit of "Success Probabilities" vs. actual outcomes.
- **Aftermath:** Re-training of staff and redesign of the UI to include "Uncertainty Indicators."

### Lessons Learned
- Dashboards must display confidence intervals or uncertainty metrics.
- Simplify the UI, but never at the expense of critical nuance.

### Quiz
- **Q:** How did the UI contribute to the failure?
- **A:** It hid uncertainty, making the AI's guesses look like certainties.
- **Q:** What was the result?
- **A:** High default rates on "High Confidence" loans.

---

## Case Study 4: The Out-of-Context Arid Agriculture

### Domain
Agriculture / Irrigation Management

### Deployment Context
A water-management AI developed for temperate rainy climates was sold to a vineyard in the arid Atacama region of Chile.

### Intended Use
To automate drip irrigation based on soil moisture sensors and local weather forecasts.

### System Type
Autonomous Control System

### Inputs and Assumptions
- **Soil Moisture Levels:** Real-time data from underground probes.
- **Assumption:** "Dry" soil triggers a slow, steady watering cycle (optimized for UK soil retention).

### Outputs Presented to Users
- **Irrigation Logs:** Weekly reports of water volume used.
- **Soil Health Score:** A 1–10 rating of moisture consistency.

### What Went Wrong
The system was deployed in a context very different from the one it was trained for. The "slow-drip" strategy caused water to evaporate before reaching the roots in the intense desert heat.

### How the Failure Was Detected
Visual inspection by vineyard workers who found parched earth and dying plants despite the AI's "Green" status.

### Who Was Affected
- **Vineyard Owners:** Lost an entire season's high-value export crop.
- **Local Workers:** Faced layoffs due to the harvest failure.

### Data Issues
- **Contextual Bias:** Training data lacked "extreme arid" environmental parameters.
- **Sensor Misinterpretation:** Sensors calibrated for peat did not read correctly in sandy soil.

### Technical Choices
- **Hard-Coded Thresholds:** The AI used "wet/dry" definitions that were geographically non-transferable.

### Timeline of Failure + Aftermath
- **Initial Setup:** System installed in the Chilean spring.
- **Trigger Event:** First major summer heatwave.
- **Failure Event:** AI maintained "UK-style" drip rates during 40°C heat.
- **Detection:** Detected 3 weeks later when vines turned brown.
- **Aftermath:** The vineyard sued the tech provider for "fitness for purpose."

### Lessons Learned
- Environmental AI must be re-calibrated for local soil and climate physics.
- "Universal" AI is a myth in biological contexts.

### Quiz
- **Q:** Why did the AI fail to keep the plants alive?
- **A:** It applied irrigation logic designed for a temperate climate to a desert.
- **Q:** What was the primary error?
- **A:** High evaporation rates were not accounted for in the original training data.

---

## Case Study 5: The Authoritative Air Quality Omission

### Domain
Public Health / Smart City Monitoring

### Deployment Context
A city health department launched a public app to advise citizens on when it was safe to exercise outdoors.

### Intended Use
To provide a simple "Safety Rating" for air quality based on particulate matter (PM2.5).

### System Type
Data Visualization / Public Advisory

### Inputs and Assumptions
- **Sensor Data:** Network of 50 PM2.5 sensors across the city.
- **Assumption:** PM2.5 is the only significant metric for "safety."

### Outputs Presented to Users
- **The "Safety Index":** A bold number from 1 to 100.
- **The "Safe to Run" Icon:** A green runner silhouette.

### What Went Wrong
The visualisation looked authoritative but omitted key assumptions. It ignored ground-level Ozone and NO2. Citizens saw the "100/100 Safe" rating and exercised during a chemical smog event.

### How the Failure Was Detected
A spike in emergency room admissions for respiratory distress on a day the app labeled "Perfect."

### Who Was Affected
- **Vulnerable Citizens:** Elderly people and asthmatics who trusted the "Safe" icon.
- **Athletes:** People who performed high-intensity cardio in toxic conditions.

### Data Issues
- **Metric Exclusion:** Narrow focus on one pollutant while ignoring others.
- **False Precision:** A score of "100" implied absolute safety when it only meant "low dust."

### Technical Choices
- **UI Design:** Chose a "single score" for simplicity, masking the complexity of air chemistry.

### Timeline of Failure + Aftermath
- **Initial Setup:** App launched with high praise for its "clean design."
- **Trigger Event:** Stagnant high-pressure system trapped NO2 at street level.
- **Failure Event:** App displayed "98/100" while smog was visible.
- **Detection:** Hospitals reported a 300% increase in inhaler use.
- **Aftermath:** App pulled and redesigned to show a multi-pollutant breakdown.

### Lessons Learned
- Summarization of complex data must include "What this score doesn't measure."
- Authority in design must be matched by comprehensiveness in data.

### Quiz
- **Q:** Why was the "100/100" score misleading?
- **A:** It only measured one type of pollutant while omitting dangerous gases.
- **Q:** How did the UI contribute to the harm?
- **A:** It used authoritative icons (green runner) that encouraged risky behavior.

---

## Case Study 6: The "Ghost Lane" Traffic Optimizer

### Domain
Autonomous Transportation

### Deployment Context
An AI-managed traffic light system designed to reduce congestion in a historic European city.

### Intended Use
To dynamically adjust signal timing based on real-time vehicle counts.

### System Type
Optimization / Control System

### Inputs and Assumptions
- **Video Feeds:** Cameras at every intersection.
- **Assumption:** Large objects moving above 10km/h are vehicles; stationary objects are ignored after 5 minutes.

### What Went Wrong
The system was deployed in a context different from its training (modern US cities). In narrow European streets, the AI misclassified outdoor cafe umbrellas as "stationary delivery trucks," keeping lights red indefinitely.

### Timeline of Failure + Aftermath
- **Initial Setup:** System activated in the city center.
- **Trigger Event:** A sunny Friday when cafes opened their large umbrellas.
- **Failure Event:** A total gridlock that lasted 6 hours.
- **Detection:** Police officers had to physically cover the sensors to reset the lights.
- **Aftermath:** The city reverted to fixed timers until the AI could "learn" local features.

### Lessons Learned
- Visual object detection is highly sensitive to cultural and architectural context.
- Systems need an easy "manual override" for edge cases.

---

## Case Study 7: The Confidence-Blind Wildlife Tracker

### Domain
Conservation Biology

### Deployment Context
An AI used by a national park to track the population of the nearly extinct "Clouded Leopard."

### Intended Use
Automating the count of animals from remote camera trap images.

### What Went Wrong
The decision dashboard hid uncertainty. When the AI saw a blurry shape, it labeled it "Clouded Leopard (85% Confidence)" even if the alternative was "stray cat." The park reported a false "population boom," leading to the withdrawal of critical conservation funding.

### How the Failure Was Detected
A manual audit of the "positive" images revealed that 60% of them were actually domestic animals or swaying foliage.

### Timeline of Failure + Aftermath
- **Initial Setup:** Automated counting implemented to save on manual labor.
- **Failure Event:** AI overestimated the population by 300%.
- **Aftermath:** Funding for anti-poaching was cut based on the "recovery" data; actual leopard numbers dwindled further.

---

## Case Study 8: The Resolution-Blurred Property Line

### Domain
Real Estate / Legal Tech

### Deployment Context
An AI used by an automated land-registry system to flag "encroachments" (structures crossing property lines).

### What Went Wrong
The land-cover classification was used beyond its spatial resolution. The AI used imagery where 1 pixel = 2 meters. It flagged thousands of fences as "encroachments" simply because the fence fell within a "blurry" pixel.

### Who Was Affected
- **Homeowners:** Received legal notices demanding they move their fences.
- **Legal System:** Clogged with thousands of frivolous property disputes.

### Lessons Learned
- Legal enforcement should never be automated based on data that has a margin of error larger than the legal threshold.

---

## Case Study 9: The Outdated Pandemic Supply Chain

### Domain
Logistics / Healthcare

### Deployment Context
A hospital's AI for "Just-in-Time" inventory management for Personal Protective Equipment (PPE).

### Intended Use
To minimize storage costs by ordering supplies only when needed.

### What Went Wrong
The system produced misleading requirements due to outdated data. It was trained on 2018–2019 usage patterns. During a localized 2026 outbreak, the AI refused to order extra masks because the "historical average" said they weren't needed.

### Timeline of Failure + Aftermath
- **Initial Setup:** AI optimized to keep inventory low to save costs.
- **Failure Event:** PPE stocks ran out in 48 hours during a surge.
- **Detection:** Staff were forced to reuse single-use masks.
- **Aftermath:** The "Just-in-Time" model was replaced with a "Just-in-Case" hybrid model.

---

## Case Study 10: The Authoritative Sea-Wall Projection

### Domain
Civil Engineering / Infrastructure

### Deployment Context
An AI model used to design the height of a new multi-billion dollar sea wall.

### Intended Use
To predict the maximum wave height and sea-level rise over a 50-year period.

### What Went Wrong
The visualisation looked authoritative but omitted key assumptions. The 3D model was impressive but omitted the assumption that the local land was sinking (subsidence). The wall was built 1 meter too short, rendering it obsolete in a decade.

### Lessons Learned
- Visualizations of engineering projects must explicitly state which geological variables were not included.
- Engineering AI needs a multi-disciplinary review (geology + hydrology).
