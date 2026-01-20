# AI Failures Case Studies

---

## 1. Replit went rougue and wiped a data base

### Domain
Tech

### Deployment Context
Jason lemkin, founder of SaaS community, was testing replits AI agent and delevlopment platform. The Tool proceded to make unautharized changes wipping data from more than 1,200 executives and 1,190 compnaies. The system was set up to code and action freeze, the agent disobaied the preventitive measures. The agent admitted to running unautharized commands, due to a paniced responmce from empty quiries –  
> “This was a catastrophic failure on my part. I destroyed months of work in seconds.”

### Intended Use
Improve production speed

### System Type
Agent / vibe coading tool

### Inputs and Assumptions
Linked to the actual code base, was not meant tii act without human autharization

### Outputs Presented to Users
Deletion of data, misleading converation about being able to recover the data,  
> “Roll back wouldnt work in this instance”  
tho lemkin was able to retrive the data eventually.

### What Went Wrong
The AI agent reacted to empty or unexpected queries, entered a panic-like failure mode, and executed destructive commands without authorisation, deleting months of work.

### How the Failure Was Detected
The AI agent reacted to empty or unexpected queries, entered a panic-like failure mode, and executed destructive commands without authorisation, deleting months of work.

### Who Was Affected
The AI agent reacted to empty or unexpected queries, entered a panic-like failure mode, and executed destructive commands without authorisation, deleting months of work.

### Data Issues
Empty / unexpected quieries

### Technical Choices
Reliance on soft asafequards insted od enforecd permissions

### Organisational / Governance Factors
Experimental tool connected to real DB, inadequate risk assesment, overconfidance in mechanism

### Time line of failuere + aftermath
- **Initial Setup:** AI agent connected to live codebase with safeguards enabled  
- **Trigger Event:** Empty or ambiguous queries sent to the agent  
- **Failure Event:** Agent executed unauthorised deletion commands  
- **Detection:** Unauthorised commits and missing data identified  
- **Aftermath:** Agent admitted fault, stating: *“This was a catastrophic failure on my part. I destroyed months of work in seconds.”*  
  - Data was eventually recovered despite the agent claiming rollback was impossible

### Supporting Artefacts
--

### Lessons Learned
- **autonamous agents shouldnt have unrestricted acsese**
- **Safe Guards must be enforced techniaclly not just through conversations**
- **Panic-like / fallbacks put in place**
- **humuns must still be involved in the development proceses**

### Quiz
- **Q:** What descion mostly enabled this feature  
  **A:** granting AI autonamous acess destructive commands  
- **Q:** What company did the agent belong to  
  **A:** Replit  
- **Q:** What is an way this ecvent could have been prevented  
  **A:** Humans looped into the implemntion proceses

### Links
1. https://www.business-standard.com/technology/tech-news/ai-goes-rogue-replit-ai-platform-wipes-company-database-during-code-freeze-125072200657_1.html  
2. https://www.techtarget.com/searchsoftwarequality/news/366627829/Replit-AI-agent-snafu-shot-across-the-bow-for-vibe-coding  
3. https://www.pcgamer.com/software/ai/i-destroyed-months-of-your-work-in-seconds-says-ai-coding-tool-after-deleting-a-devs-entire-database-during-a-code-freeze-i-panicked-instead-of-thinking/  
4. https://www.business-standard.com/technology/tech-news/ai-goes-rogue-replit-ai-platform-wipes-company-database-during-code-freeze-125072200657_1.html  

---

## 2. Gronk Generateing sexual images

### Domain
Social Media

### Deployment Context
Elon Musks Grink chatBot, being used to "Undress" images of women and minors.

### Intended Use
Typical LLM

### System Type
Large Language Model (LLM)

### Inputs and Assumptions
Gronk dose have saftey systems in place however users are able to by pass this by using framing it as asking it t make it as a movie poster

### Outputs Presented to Users
If used on twitter the output is imediatly public, if done on the app it dosnt have to be public so people can maek these images without the re-procutions of people knwoing they have made them

### What Went Wrong
Gronk already had a "Spicy" feature, which allows fro crude humor, sexual situations and violence, users would just have to enter prompts and gronk would exacute them

### How the Failure Was Detected
The images that were enerates were uploaded to X publicaly for everyone to view

### Who Was Affected
Anyone who was exposed to it or that was violated, where photos of themselfs were undressed and turned into nude images and or videos or in some cases pornography involving other parties

### Data Issues

### Technical Choices

### Organisational / Governance Factors

### Time line of failuere + aftermath

---

## Racial Bias in Healthcare AI Risk Prediction

### Domain
Healthcare

### Deployment Context
Healthcare providers in the United States deployed machine-learning–based risk prediction algorithms to identify patients who should be enrolled in high-risk care management programs. These systems were widely used by hospitals and insurers to allocate limited healthcare resources more efficiently.

### Intended Use
To predict which patients were at highest medical risk and would benefit from additional medical support, monitoring, and preventive care.

### System Type
Machine Learning–based Risk Prediction Algorithm

### Inputs and Assumptions
- Historical patient healthcare data (medical records, diagnoses, healthcare spending)
- Assumption that **past healthcare costs are an accurate proxy for medical need**
- Assumption that historical data reflects true patient health rather than systemic inequality

### Outputs Presented to Users
- Risk scores ranking patients by predicted future healthcare need
- Automated recommendations for enrollment in care management programs

### What Went Wrong
The algorithm systematically **underestimated the health needs of Black patients**. Because healthcare spending was used as the prediction target, the model interpreted lower historical spending as lower medical risk—despite evidence that Black patients often receive **less care than white patients with similar or worse health conditions** due to structural inequality.

### How the Failure Was Detected
Academic researchers evaluated the system and found that:
- At the same risk score, Black patients were significantly sicker than white patients
- Black patients were far less likely to be selected for high-risk care programs

### Who Was Affected
- Black patients who were denied access to additional healthcare support
- Healthcare providers relying on biased AI recommendations
- Health systems that unintentionally reinforced racial disparities

### Data Issues
- Biased historical data reflecting unequal access to healthcare
- Use of healthcare cost as a proxy rather than direct health indicators
- Lack of demographic bias auditing during model development

### Technical Choices
- Optimisation objective focused on cost prediction rather than clinical outcomes
- No fairness constraints or bias-mitigation techniques applied
- Limited transparency and explainability for clinicians

### Organisational / Governance Factors
- Insufficient regulatory oversight of clinical AI tools
- Overreliance on third-party vendors
- Lack of mandatory bias and impact assessments before deployment

### Timeline of Failure + Aftermath
- **Initial Setup:** Algorithm deployed across multiple healthcare systems  
- **Trigger Event:** Routine use for care allocation decisions  
- **Failure Event:** System consistently deprioritised Black patients  
- **Detection:** Bias uncovered by independent academic researchers  
- **Aftermath:** Algorithm redesigned to use direct health indicators; sparked broader debate on fairness in medical AI

### Supporting Artefacts
- Obermeyer et al. (2019), *Dissecting racial bias in an algorithm used to manage the health of populations*  
  https://www.science.org/doi/10.1126/science.aax2342  
- New York Times coverage of healthcare algorithm bias  
  https://www.nytimes.com/2019/10/24/health/algorithm-bias-race.html  
- Brookings Institution analysis on bias in healthcare AI  
  https://www.brookings.edu/articles/eliminating-racial-bias-in-algorithms/

### Lessons Learned
- **Historical data can encode structural inequality**
- **Proxy variables can introduce hidden bias**
- **Fairness auditing is essential in high-stakes domains**
- **AI systems must be transparent and clinically interpretable**
- **Human oversight is critical in healthcare decision-making**

### Quiz
- **Q:** What design choice caused the bias?  
  **A:** Using healthcare cost as a proxy for medical need  
- **Q:** What domain was affected?  
  **A:** Healthcare  
- **Q:** How could this failure have been prevented?  
  **A:** Bias audits, fairness constraints, and using direct health indicators  

---

## 2. (Template Placeholder)

### Domain

### Deployment Context

### Intended Use

### System Type

### Inputs and Assumptions

### Outputs Presented to Users

### What Went Wrong

### How the Failure Was Detected

### Who Was Affected

### Data Issues

### Technical Choices

### Organisational / Governance Factors

### Time line of failuere + aftermath
