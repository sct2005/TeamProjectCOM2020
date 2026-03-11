# AI Failure Case Studies

## Case Study 1: The Outdated Inundation

### Domain
Environmental Management / Urban Planning

### Deployment Context
A coastal city council decided to use a AI-driven "Flood Guard" dashboard to determine which neighborhoods they shoul look to raies up.
### Intended Use
to provide real time risk assesemnts for areasof flood risk

### System Type
Predictive Modeling / Risk Assessment

### Inputs and Assumptions
- **Historical Rainfall Data:** 30 years of rainfall records.
- **Topography:**  elevation maps from a 2010 geological survey.
- **Assumption:** Sea-level rise would follow linear historical trends rather than accelerating.

### Outputs Presented to Users
- **Color-coded Risk Maps:**  High Risk to Low Risk.
- **Projected Insurance Premiums:** Estimated costs based on location.

### What Went Wrong
The system produced misleading flood risk maps because it used on outdated data that did not account for recent  sea-level rises .

### How the Failure Was Detected
A unexpected enormous flood event occurred twice in three years, submerging neighborhoods marked as "Low Risk" on the dashboard.

### Who Was Affected
- **Homeowners:** Families in "Safe" zones lost uninsured property.
- **Urban Planners:** Approved dangerous developments based on the AI.
- **Emergency Services:** Resourced the wrong areas during the storm.

### Data Issues
- **Temporal Decay:** Training data was to old.
- **Static Inputs:** Failed to update land-use changes.

### Technical Choices
- **Regression Modeling:** Chosen for simplicity but failed to capture non-linear climate shifts.
- **Over-Smoothing:** The AI "cleaned" the map, removing small but vital drainage details.

### Organisational / Governance Factors
- **Budget Constraints:** Refusal to fund annual LIDAR updates.
- **Automation Bias:** Officials stopped manual field inspections.

### Timeline of Failure + Aftermath
- **Initial Setup:** the system was launched in 2021 using outdated data.
- **Trigger Event:** record breaking rain fall 
- **Failure Event:** Maps showed "safe" zones for areas that were 2 feet underwater.
- **Detection:** citizens reported the failure on social media 
- **Aftermath:** Council was faced  with class action lawsuits and thesystem decommissioned.

### Lessons Learned
- AI models for environmental risk must have a "data expiration date."
- Visual authority does not equal factual accuracy.
- Local knowledge must act as a "sanity check" for algorithmic outputs.

### Quiz
- **Q:** Why did the AI system fail to predict the floods in the safe zones?
- **A:** It used outdated topography and rainfall data that didn't reflect current climate reality.
- **Q:** What was the primary visual failure?
- **A:** The map looked authoritative but omitted the key assumption of static sea levels.

---

## Case Study 2: The Resolution Mirage

### Domain
Agricultural Surveillance

### Deployment Context
AI was used to monitor deforestation in coffee plantations 

### Intended Use
to flag plantations if they were getting to close to protected areas 

### System Type
Computer Vision and classifiction 

### Inputs and Assumptions
- **Satellite Imagery:** Publicly available imagery.
- **Assumption:** If a pixel is majority green, then its classified as "Forest."

### Outputs Presented to Users
- **Deforestation Alerts:** Automatic emails sent to plantaitions when the encoach on the forest.

### What Went Wrong
it struggled to distinguisg between rainforest and coffe trees in the pkantation leeding to wrongfull classifications 

### How the Failure Was Detected
farmers spoke to the desingers after reciveing emails saying they were encroaching on rianforest but in reality they were growing cofee beans under the canopy 

### Who Was Affected
- **Small-hold Farmers:** Lost "Fair Trade" certifications and income.
- **Coffee Importers:** Cancelled valid contracts based on false AI data.

### Data Issues
- **Resolution Mismatch:** inadequet precision + failure to encorperaet the fact that it could be grown under the canaopy 
- **Class Ambiguity:** failure to distinguish between cofee plantions and rainforest 

### Technical Choices
- **Cost-Saving:** Chose free, low-res satellite images.

### Organisational / Governance Factors
- **Lack of Appeals Process:** data was published saying teh coffe comapnys wernt follwoing ethicall practices resulting in back lash and  order cancellation.

### Timeline of Failure + Aftermath
- **Initial Setup:** System deployed 
- **Trigger Event:** Farmers cross croping to  improve soil health.
- **Failure Event:** AI flagged corss cropping as deforestation
- **Detection:** Audit by geographer lead to discovery resolution error.
- **Aftermath:** the company  issued a public apology and helped the reinsation of there credentials 

### Lessons Learned
- dont try use a model on images with a higer resalution images that it was trained on 


### Quiz
- **Q:** What was mismatch led to the issue ?
- **A:** using the model on higher qualkity images than it was trained on
- **Q:** Why were farmers unfairly penalized?
- **A:** Tthe model couldnt tell the diffrence between the crops and rainforest
---

## Case Study 3: The Overconfident Credit Dashboard

### Domain
Fintech 

### Deployment Context
a bank used a modle to help bankers approve loans for small busineses 

### Intended Use
to provide an proabilty of re payment 

### System Type
Decision Support System 

### Inputs and Assumptions
- **Inputs:** Cash flow from past years , current market , debts 
- **Assumption:** an high probabilty of re payemnt means they will re pay there loan 

### Outputs Presented to Users
- **The "Success Dial":** A single percentage score ).
- **Missing Info:** no way to show how certain the model was of their prediction .

### What Went Wrong
The didnt show unccertantiy , leading to over-confident conclusions. led to teh approval of risky loans. 

### How the Failure Was Detected
During a minor market dip, the bank suffered alosses on loans that were labeld as high confidence.

### Who Was Affected
- **Loan Officers:** Reputations ruined by trusting the modle 
- **The Bank:** Faced a liquidity crisis due to bad debt.

### Data Issues
- **Sparse Data:** For new businesses, the AI was "guessing" based on limited data 

### Technical Choices
- **UI Simplification:** Designers removed error bars to make the dashboard less clustered

### Organisational / Governance Factors
- **KPI Alignment:** Officers were rewarded for volume encouraging them to not carry out additinol research

### Timeline of Failure + Aftermath
- **Initial Setup:** Dashboard rolled out 
- **Trigger Event:** Local economic downturn
- **Failure Event:** Massive loan defaults
- **Detection:** Internal audit of Success Probabilities vs. actual outcomes
- **Aftermath:** Re-training of staff and redesign of the UI 

### Lessons Learned
- Dashboards must display confidence intervals or uncertainty metrics.
- 

### Quiz
- **Q:** How did the User Interface contribute to failure?
- **A:** It hid uncertainty, making the AI's guesses look like certainties.
- **Q:** What was the result?
- **A:** approval of loans that shouldnt of been 

---



## Case Study 4: The Out-of-Context Arid Agriculture

### Domain
Agriculture 

### Deployment Context
an ai rainfall prediction system thta was modeled for rainy climates was sold to an vinyard on a arid climate

### Intended Use
so they could fidn out how much water to use for their drip irragtion system 

### System Type
Autonomous Control System

### Inputs and Assumptions
- **Soil Moisture Levels:** from under groud oprobes 
- **Assumption:** dry soil increases irragation system 

### Outputs Presented to Users
- **Irrigation Logs:** reports of water volume used.
- **Soil Health Score:** A  of moisture consistency.

### What Went Wrong
the climaet the syetme was deployed on varied from the climate where the system was created 

### How the Failure Was Detected
Visual inspection found t he soil in the vinyard was dry and patchy 

### Who Was Affected
- **Vineyard Owners:** Lost an entire season's high-value export crop
- **Local Workers:** layoffs due to the harvest failure

### Data Issues
- **Contextual Bias:** Training data lacked  arid environmental parameters.
- **Sensor Misinterpretation:** Sensors were calibrated for peat did not read correctly in sandy soil.

### Technical Choices
- **Hard-Coded Thresholds:** The AI used "wet/dry" definitions that wernt geographically transferable.

### Timeline of Failure + Aftermath
- **Initial Setup:** System installed 
- **Trigger Event:** major summer heatwave.
- **Failure Event:** model maintained wrong  drip rates for the heat wave.
- **Detection:** Detected 3 weeks later when vines turned brown.
- **Aftermath:** The vineyard sued the tech provider for the system not being fit for purpose

### Lessons Learned
.
- Universal AI dosnt work in  biological contexts.

### Quiz
- **Q:** Why did the AI fail to keep the plants alive?
- **A:** It applied irrigation logic designed for a temperate climate to a desert.
- **Q:** What was the primary error?
- **A:** High evaporation rates were not accounted for in the original training data.

---


## Case Study 5: The Authoritative Air Quality Omission

### Domain
Public Health 

### Deployment Contextan app that notifies citizens when its safe to exersise outside

### Intended Use
to provide a saftey raitting based on air quality

### System Type
Public Advisory

### Inputs and Assumptions
- **Sensor Data:** Network of  sensors across the city.
- **Assumption:** PM.5 is only usabel metric

### Outputs Presented to Users
- **The "Safety Index":** A number from 1 to 100.


### What Went Wrong
The visualisation looked authoritative but omitted key assumptions. It ignored ground-level Ozone and NO2.
### How the Failure Was Detected
peopel admitted for respiratory distress on a day the app labeled "Perfect."

### Who Was Affected
- **Vulnerable Citizens:** Elderly people and asthmatics who trusted the "Safe" raitting .
- **Athletes:** peopel who exercised in toxic conditions 

### Data Issues
- **Metric Exclusion:** too foucused on one pollutent and not others
- **False Precision:** A score of 100 implied absolute safety when it only meant low if the polutent monitored 

### Technical Choices
- **UI Design:** a score that based of one metric hides the whole story 

### Timeline of Failure + Aftermath
- **Initial Setup:** App launched 
- **Trigger Event:** Stagnant high-pressure system trapped NO2 at street level
- **Failure Event:** App displayed 98/100 while smog was visible.
- **Detection:** Hospitals reported a 300% increase in respitory cases 
- **Aftermath:** people were exposed yo harmful levels of pollutent based of them using the app as a guid line 

### Lessons Learned
- Summarization of complex data must include "What this score doesn't measure."
  

### Quiz
- **Q:** Why was the 100/100 score misleading?
- **A:** as it only measured one type of pollutant while omitting dangerous gases.
- **Q:** How did the UI contribute to the harm?
- **A:** didnt show what the score didnt take into acount 

---

## Case Study 6: The "Ghost Lane" Traffic Optimizer

### Domain
Autonomous Transportation

### Deployment ContextAi used to controll a traffic light systemn , with the idea of removing congestion 

### Intended Use
Tdynamicallay adjust the lighst that the system controll based of traffic volume , speed and position

### System Type
 Control System

### Inputs and Assumptions
- **Video Feeds:** Cameras at  intersections.
- **Assumption:** Large objects moving above 10km/h are vehicles and stationary objects are ignored after 5 minutes.

### What Went Wrong
The system was deployed in a  different city from its training (modern US cities). In narrow European streets, the AI misclassified outdoor cafe umbrellas as stationary delivery trucks, keeping lights red indefinitely.

### Timeline of Failure + Aftermath
- **Initial Setup:** System activated 
- **Trigger Event:** A sunny Friday when cafes opened umbrellas.
- **Failure Event:** A gridlock that lasted >6 hours.
- **Detection:** Police officers had to physically cover the sensors
- **Aftermath:** The city reverted to fixed timers. 

### Lessons Learned
- Visual object detection is highly sensitive 
- Systems need a manual override.

### Quiz
- **Q:** What environmental difference caused the failure?
- **A:** The AI was trained on modern US cities but deployed in a historic European city 
- **Q:** What specific object did the AI misclassify?
- **A:** Outdoor cafe umbrellas, which it mistook for delivery trucks.

---

## Case Study 7: The Confidence-Blind Wildlife Tracker

### Domain
Conservation Biology

### Deployment Context
ai model to track the population of an nearly extinct clouded leopard

### Intended Use
counting animals from remote camera trap images.

### What Went Wrong
The decision dashboard hid uncertainty. it would often makr blurry shaped as leopords with non 100% uncertantiy , but as the uncrtanty wasnt shown , it was unclear that the model  wasn uncertain it was an leopard.

### How the Failure Was Detected
manual checking of images that were marked as leopard  revealling 60% were false positives

### Timeline of Failure + Aftermath
- **Initial Setup:** system implemented
- **Failure Event:** the system overestimated the population 
- **Aftermath:** oversetimated population led to loss of funding for conservation problems 

### Lessons Learned
consercatuion decisions could never be fully autiomated withouthuman approval 
### Quiz
- **Q:** What did the dashboard hide that led to poor decisions?
- **A:** Uncertainty
- **Q:** What was the tragic consequence of the overestimation?
- **A:** Conservation funding was withdrawn
---

## Case Study 8: The Resolution-Blurred Property Line

### Domain
Legal Tech

### Deployment Context
AI was used to check incroachments on property boundries

### What Went Wrong
the system used 1 pixel as 2 meters o if there was a blurry pixel on teh boudrie the system would classify it as an encroachment 

### Who Was Affected
- **Homeowners:** Received told to move their fences based of false classifications
- **Legal System:** backlog due to cases with false reports

### Lessons Learned
 should not automnate task that will lead to lega reprocusions 
### Quiz
- **Q:** What was the resolution problem?
- **A:** Each pixel represented 2 meters leading to a marginal erro 
- **Q:** Why is this particularly problematic for legal applications?
- **A:** laws rewuire precision , cant make cases  without convincing evidence 

---



## Case Study 9: The Outdated Pandemic Supply Chain

### Domain
Logistics 
### Deployment Context
an automated invatory tracker 

### Intended Use
to try top minimise storage costs it would only order when it was gonna be needed

### What Went Wrong
trained on data from 2018 , there was an outbreak in 2026 due to increse usage led to the hospital riunning out of supplies 

### Timeline of Failure + Aftermath
- **Initial Setup:** deployment 
- **Failure Event:** PPE stocks ran out 
- **Detection:** re use of single used PPE.
- **Aftermath:** modle was replaced with an modle that oreders just in case

### Lessons Learned
models must acount for un for seen circumstanecs were situstions ore non linear or prone to variabilty 

### Quiz
- **Q:** What time period was the AI trained on?
- **A:** 2018–2019 
- **Q:** What replacement model did the hospital adopt?
- **A:** A "Just-in-Case"

---

## Case Study 10: The Authoritative Sea-Wall Projection

### Domain
Civil Engineering 

### Deployment Context
AAI modle to desing the height of an sea wall

### Intended Use
predict sea level rise 

### What Went Wrong
didi not take into account that the land could sink not that sea level woudl rise 

### Lessons Learned
AI model mustr state what modles are not included 

### Quiz
- **Q:** What critical geological factor did the AI omit?
- **A:** land sinking 


---

## Case Study 11: The Subsurface Blind Spot

### Domain
Civil Engineering

### Deployment Context
predicting sinholes based of road levels based of traffic vibrations 

### Intended Use
identify where areas have sinking soil before the sink hole itself apears

### System Type
Predictive Maintenance

### Inputs and Assumptions
- **Seismic Sensors:** sensors placedunder the road
- **Assumption:** Surface vibrations are an acurate measurment to predict road erasure 

### Outputs Presented to Users
- **Risk Map:** A digital twin of the city with compromised or safe
- **Maintenance Priority List:** rank streets based on urgancy 

### What Went Wrong
didnt acount for damge by other means e.g dampness
diffrent surfaces could mask the level of vibnbrations 

### How the Failure Was Detected
an acident was caused sue to a sink whole in an area that was deemed safe 

### Who Was Affected
- **Commuters:** Public safety compromised.
- **City Maintenance:** Budgets used for roads that were demed needing fixing but were not in reality 

### Lessons Learned
- Surface vibrations alone was  insufficant 

### Quiz
- **Q:** What physical phenomenon did the AI fail to account for?
- **A:** The dampening effect 


---

## Case Study 12: The Arctic Drift Bias

### Domain
Climate Research

### Deployment Context

an autonmous navigation system for ice breakers sailling in the northen sea 

### Intended Use
to find th optimal pathfor fuel efficency.

### System Type
Autonomous Navigation and optimal path finding 

### Inputs and Assumptions
- **Historical Ice Thickness:** Data from 2000–2015.
- **Assumption:**  Ice movemnt patterns are predictable not random and canm be predicted based of data from the 20th century. 

### What Went Wrong

system prodiced misleading routes due to being trained on old ice movment but due to global warming current ice moves faster and is more unpredicable, system lead a vessel into a clear path that want clear.

### Timeline of Failure + Aftermath
- **Initial Setup:** Deployment of system.
- **Trigger Event:** An unpredicted shift in wind direction.
- **Failure Event:** Three vessels became ice-locked in a route that was deemed clear.
- **Aftermath:** Expensive rescue operations, system was scrapped due 

### Lessons Learned
- Climate change creates new unpredicatablre enviromental conditions that are hard/impossible to predict with historical data 
- Navigation systems need real time adabtibilty 

### Quiz
- **Q:** What was the key difference between "Old Ice" and "New Ice"?
- **A:** New Ice moves and breaks 40% faster than the Old Ice the AI was trained on.
- **Q:** Why couldn't the AI adapt to the changing conditions?
- **A:** It relied on historical patterns from 2000–2015 and lacked real-time adaptability to respond to rapid ice movements.

---

## Case Study 13: The High-Altitude Diagnostic

### Domain
Healthcare 

### Deployment Context

AI to identify respitory issues via a pulse Oxygen level 

### Intended Use
Flag patients with low oxygen levels 

### What Went Wrong


used sensors on a watch, diffrent skintones cuase diffrent readings as it cant penatrate darker tones as easily. leading to pateints being miss diagnosed.

### Data Issues
- **Contextual Blindness:** Failed to get acurate reaadings on diffrent skin tones 
- **Population Bias:** Training data lacked representation for diffrent skintones 

### Lessons Learned
- Medical AI must be trained on populations that reflect the deployment context's environmental conditions.
- take into acount all users.

### Quiz
- **Q:** What was the main  factor in the incorect predictions?
- **A:** the system didnt take into acount diffrent skin tones.
- **Q:** What happened when the AI was deployed?
- **A:** gave incorrect readings on pateints 

---

## Case Study 14: The Solar Microgrid Blackout

### Domain
Energy 

### Deployment Context
An AI-managed solar microgrid for an remoote island.

### Intended Use
To balance battery discharge and solar intake for power maximisation.

### What Went Wrong
their was no uncertantiy raitting on the dashboard , so when the system predicted 90% of enough storage on a day when their was heavy fog,their wasnmt enough power conserved and led to a power outaeg for the island.

### Who Was Affected
- **Local Hospital:** Lost refrigeration and internet connection
  
- **Small Businesses:** Experienced data loss and equipment damage.

### Lessons Learned
- Energy systems must display uncertainty ranges especially if they dont include all weather metric s such as perceotiation.

### Quiz
- **Q:** What did the dashboard hide from users?
- **A:** The wide confidence interval caused by a malfunctioning sensor—it only showed the 90% prediction without the uncertainty.
- **Q:** What critical consequence occurred at 2 AM?
- **A:** The grid collapsed, causing the hospital to lose vaccine refrigeration and businesses to suffer data loss.

---

## Case Study 15: The Precision-Mismatched Firebreak

### Domain
Emergency Services 

### Deployment Context
AI system that wuld predict the nest place to conduct controll burns to stop wildfires

### What Went Wrong
A land-cover classification was used beyond its spatial resolution. The AI used 50-meter satellite pixels to determine "burnable fuel." It missed a 10-meter wide dry drainage ditch (invisible at that resolution), which acted as a fuse, carrying the fire directly into a residential area the AI labeled as "Protected by Firebreak."

a classifiction model was used to see land cover , but the incorrect spatial resoultionswere used , teh ai used a 50 meter satilite pixels and predicted it as burnable fuel , howver it missed a 10 meter dry drainage ditch, which was invisable to the resalution, drainage ditch acted as a fuse an lead to the fire going directly towards an residential area causing property damage. 

### Lessons Learned
- for modles making predictions with very high consequences they should be precise ass possibel 50meters is not precise enough 
### Quiz

- **Q:** What spatial resolution did the AI use?
- **A:** 50-meter pixels, which were too coarse to detect a 10-meter wide drainage ditch.
- **Q:** How did this resolution mismatch lead to disaster?
- **A:** The AI missed the dry ditch, which acted as a fuse and carried fire into a residential area.

---

## Case Study 16: AI data centers enviromental impacts
### Domain
enviromental 

### Deployment Context
Data centers , are massive warehouses which have 1000s of computers to host AI modelds and have massive enrgy consuption.
" Data centres and data transmission networks account for around 1% of global energy-related greenhouse gas emissions."[1]
they produce pressure on the electricty grids in plavces there built , this can lead to higher electricty prices effecting local residents.

### Lessons Learned
- Data centers shoulkd build power facilties to support their data centers
- tehy should be built in places where minimal people wil  be effected. 

### Quiz
- **Q:** how much of global energy assumption do data centers consume?
- **A:** 1%
- **Q:** who are the first peopel effected?
- **A:** The residents.


### Citations 
- [1] https://www.iea.org/energy-system/electricity/data-centres-and-data-transmission-networks?
---

## Case Study 17: Water scarcity and Mismangment
### Domain
Enviromental 

### Deployment Context
Data centers require cooling to prevent overheating which need maassive volumes of water, "gloabl AI demand could require 4.2 - 6.6 billioncubic meters pf water by 2027"[2], this leads to demand on local , physical and ecological impacts , most importantly in regions that already face drought as it will create a water shortage for local communities. "The extra water consumption by data centres is a big problem for some in Querétaro which last year endured the worst drought of a century" ,""Private industries are being prioritised in these arid zones," she says. "We hear that there's going to be 32 data centres but water is what's needed for the people, not for these industries."[3] an area that is already classified as high water scarcity[4].


### What Went Wrong
Building of AI data centers in areas that alrady have high  water scaricty leaves little to no water for the residents putting  proffits over people.

### Lessons Learned
- Data centers should be built in places where there large demands wont have significant imapcts oon local people or the enviroment.

### Quiz
- **Q:** What could the demand of water from AI be in by 2027?
- **A:** 4.2 - 6.6 billion cubic meters.
- **Q:** what country that faces high water scarcity are there plans for data centers to be built?
- **A:** Querétaro
[2] https://chatgpt.com/c/69b159ae-8544-8331-9a46-41251ff24a86
[3]https://www.bbc.co.uk/news/articles/cx2ngz7ep1eo#:~:text=In%20addition%2C%20data%20centres%20also,is%20needed%20to%20produce%20electricity.&text=The%20extra%20water%20consumption%20by,water%20supplies%20to%20some%20communities.
[4] https://www.thinkhazard.org/en/report/2049-mexico-queretaro/DG#:~:text=In%20the%20area%20you%20have,on%20average%20every%205%20years.
---

## Case Study 18: The Forest Carbon Credit Mirage

### Domain
Finance / Sustainability

### Deployment Context
An AI used by an exchange to verify carbon offsets by measuring forest density.

### What Went Wrong
The land-cover classification was used beyond its spatial resolution. The AI counted "green pixels" as carbon-sequestering trees. However, the resolution was so low it couldn't distinguish between a 50-year-old oak tree and a dense patch of invasive, fast-growing vines covering a dead stump. The "Carbon Credits" sold were essentially backed by weeds.

### Lessons Learned
- Carbon credit verification requires ground-truthing and species-level identification, not just "greenness" detection.
- Financial instruments based on environmental data must use verification methods appropriate to the economic value at stake.

### Quiz
- **Q:** Why did this case fail commercially?
- **A:** It used low-resolution land-cover data that couldn't distinguish between high-value trees and low-value invasive weeds.
- **Q:** What were the carbon credits actually backed by?
- **A:** Often just invasive vines and weeds covering dead stumps, not legitimate carbon-sequestering forests.

---

## Case Study 19: The Arid-Logic Flood Barrier

### Domain
Water Management

### Deployment Context
An autonomous sluice-gate system in a region that recently shifted from arid to monsoon-heavy due to climate change.

### What Went Wrong
The system was deployed in a context very different from its training. Trained on data from 1990–2010 when the region was a desert, the AI was programmed to "Save Every Drop." When the first major monsoon hit, the AI kept the gates closed to "save" the water, causing the reservoir to overflow and flood the town.

### Lessons Learned
- Water management AI must be continuously updated as climate patterns shift.
- Systems optimized for scarcity can become dangerous when abundance suddenly occurs.

### Quiz
- **Q:** What climate shift did the AI fail to account for?
- **A:** The region shifted from arid desert conditions to monsoon-heavy rainfall due to climate change.
- **Q:** Why did the AI cause a flood?
- **A:** It was programmed to "save every drop" based on 1990–2010 desert data, so it kept gates closed during the monsoon, causing the reservoir to overflow.

---

## Case Study 20: The Confidence-Blind Dam Sensor

### Domain
Public Infrastructure

### Deployment Context
An AI dashboard used by dam engineers to monitor structural "seepage" levels.

### What Went Wrong
The decision dashboard hid uncertainty. The AI detected a 5% increase in seepage but gave a "95% Stability Rating" because its sensors were vibrating. The dashboard didn't show that the sensors were fluctuating wildly (high uncertainty). Engineers saw the 95% and went home for the weekend; the dam suffered a partial breach the next morning.

### Lessons Learned
- Infrastructure monitoring systems must prominently display sensor reliability and data quality metrics.
- High confidence scores are meaningless when based on unreliable sensor data.

### Quiz
- **Q:** What did the dashboard hide that led to the dam breach?
- **A:** The fact that sensors were fluctuating wildly, creating high uncertainty that contradicted the "95% Stability Rating."
- **Q:** What decision did engineers make based on the misleading dashboard?
- **A:** They went home for the weekend thinking the dam was safe, when in fact it was in critical condition.
