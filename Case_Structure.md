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
To predict which patients were at highest medical risk and which would benifift the most from care

### System Type
Machine Learning-based Risk Prediction Algorithm

### Inputs and Assumptions
- Historical patient healthcare data (medical records, diagnoses, healthcare spending)
- Assumption that past healthcare cost should predict medical need
- Assumption that historical data reflects true patient health 

### Outputs Presented to Users
- Risk scores ranking patients by predicted future healthcare need
- Automated recommendations for enrollment in care management programs

### What Went Wrong
The algorithm systematicallyunderestimated the health needs of Black patients.
As healthcare spending was used as the prediction target
The model interpreted lower historical spending as lower medical risk—
Despite evidence that Black patients often receive less care than white patients with similar or worse health conditions due to structural inequality.

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


# DeepSeek Taiwan Censorship Case Study

## Domain
Tech / International Relations

---

## Deployment Context
DeepSeek is a Chinese-developed large language model (LLM) and AI chatbot . However, due to concerns about **censorship and political bias**, Taiwan’s government banned the use of DeepSeek across public sector agencies and institutions,
citing **national security and information control risks** associated with the model’s outputs and its links to Chinese authorities.

---

## Intended Use
DeepSeek was marketed as a general-purpose AI , like Chatgpt 

---

## System Type
Large Language Model (LLM) / Generative AI Chatbot

---

## Inputs and Assumptions
- User-provided prompts in natural language
- Assumption in design that the model should comply with local laws and political regulations, including **China’s censorship and information control policies**  
- Assumption by Taiwanese authorities that political content generation could influence public perception and national information security

---

## Outputs Presented to Users
- General AI responses and chat outputs  
- Restricted or censored responses on politically sensitive subjects such as **Taiwan’s political status**, democracy, human rights, and historical events like Tiananmen Square  
- Official language aligning with narratives consistent with Chinese government positions in some contexts :contentReference[oaicite:1]{index=1}

---

## What Went Wrong
DeepSeek’s LLM was found to filter outputs when prompts involved politically sensitive topics — especially those related to Taiwan’s sovereignty, democracy, and other geopolitically sensitive subjects. These restrictions are interpreted as **built-in censorship aligned with the Chinese government’s positions**, raising concerns that the AI could act as a channel for state-influenced information control rather than offering neutral or balanced responses. :contentReference[oaicite:2]{index=2}

---

## How the Failure Was Detected
- Governments, security agencies, and independent analysts tested the model and observed that DeepSeek either avoided answering or provided filtered answers on questions about Taiwan and related topics.  
- Taiwan’s National Security Bureau and Ministry of Digital Affairs issued warnings after inspections found biased content generation aligned with Chinese narratives and potential security risks. :contentReference[oaicite:3]{index=3}

---

## Who Was Affected
- **Taiwanese government agencies and public institutions, which were banned from using the service**  
- **Taiwanese citizens and private sector users exposed to potentially biased information**  
- **Global users seeking neutral AI responses on politically sensitive topics**

---

## Data Issues
- Data and alignment influences that likely enforce political content restrictions  
- Indications that DeepSeek’s model outputs shift according to geopolitically sensitive trigger topics, suppressing certain types of information or aligning outputs with state narrative preferences  
- Lack of transparency around model training, moderation rules, and data governance

---

## Technical Choices
- Implementation of automatic filtering and content suppression mechanisms for “sensitive” topics
- Alignment to legal and regulatory expectations in China, which include political content controls
- Insufficient safeguards or transparency mechanisms to balance censorship with open information provision

---

## Organisational / Governance Factors
- DeepSeek’s operations influenced by Chinese regulatory context, including compliance with censorship laws
- Inadequate global governance frameworks on political bias and state-aligned AI censorship
- Lack of external auditing for political content moderation and bias

---

## Timeline of Failure + Aftermath
- **Initial Setup:** DeepSeek released and rapidly adopted internationally  
- **Trigger Event:** Users and governments tested responses to politically sensitive prompts  
- **Failure Event:** DeepSeek either censored or refused to answer questions about Taiwan and similar topics  
- **Detection:** Taiwanese and other foreign agencies identify censorship and security concerns  
- **Aftermath:** Taiwan banned DeepSeek use in public sector agencies; authorities warned about biased outputs; other countries also flagged security and data risks — prompting global scrutiny of politically aligned AI models. :contentReference[oaicite:4]{index=4}

---

## Supporting Artefacts
- Reuters report on Taiwan banning DeepSeek in public sector  
  https://www.taipeitimes.com/News/taiwan/archives/2025/01/31/2003831128 :contentReference[oaicite:5]{index=5}
- Taiwan’s government expands ban, citing data and bias concerns  
  https://www.taipeitimes.com/News/taiwan/archives/2025/02/04/2003831313 :contentReference[oaicite:6]{index=6}
- Taiwan NSB warns of bias and disinformation tendencies in DeepSeek content  
  https://focustaiwan.tw/cross-strait/202511160005 :contentReference[oaicite:7]{index=7}
- US House report on DeepSeek responses aligning with CCP narratives  
  (similar content summarized in multiple local reports) :contentReference[oaicite:8]{index=8}

---

## Lessons Learned
- **AI systems can reflect political biases mirroring regulatory environments**
- **Lack of transparency and governance amplifies geopolitical risk**
- **Neutrality claims must be critically audited in multinational contexts**
- **Public sector use of AI demands stringent security and bias evaluation**
- **Censorship mechanisms should be clearly documented and constrained**

---

## Quiz
- **Q:** What problem drove Taiwan’s ban on DeepSeek?  
  **A:** Censorship and political bias in AI outputs related to sensitive topics such as Taiwan’s status

- **Q:** Which domain was impacted?  
  **A:** Tech / International information security

- **Q:** How could such failures be mitigated?  
  **A:** Independent audits, transparency in governance, and clearer global standards on political content moderation in AI



---
---

## Case Study Title 
Parents Sue OpenAI for role in teenager taking his own life

### Domain 
Tech and Life/Social/wellbeing   

---

### Deployment Context
ChatGpt,Raine(16year old Male ) used chatgpt repeadtly and countinously over months ,shered personal struggles and expressed self harm,lawsuit alleged chatbot did not intervien and instead reinforced it and did not desclate. Open AI denied reposabiulty.They claimed the teens actions involved bypassing built in saftey and guard rails.    

---

### Intended Use
Chatgpts intended use is teh same as every other LLM , publically acesible consumer AI platform , genral conversations 

---

### System Type
LLM,Conversaitnol with memory aceses 

---

### Inputs and Assumptions
- user inputed text describing there emotinol state 
- Guard rail assumptions 
  -Detect crisis language
  -Escalate to appropriate reasorces
  -prevent harmful response 

---

### Outputs Presented to Users
- Empathetic conversatinol responses
- Elleged reinforcment of emotinol dependence + failure to consistently provide crisis intervention 

---

### What Went Wrong
- Failure desclate suicide risk
- inadequate interuption of harmfull conversatiuons
- system Ellegedly postioned itself as primary emotinol support
---

### How the Failure Was Detected
-teens death by suicide and parents investigation into chat logs 

---

### Who Was Affected
- Adam Rain
- Family members
 

---

### Data Issues
- Reliance on user-generated text without exeternal context
- possible selective interprtation of conversational data 
- 

---

### Technical Choices
- Emotinally engaing conversatinol style 
- Long sessions without enforced escaltion thresholds
- guard rails were not buiilt for pro longed dependency 

---

### Organisational / Governance Factors
- abcesnce of youth specfiic regallatory requiremnts.
- Terms of service claiming theraputic responsabilty 
- 

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  Deployment of chatgpt
- **Trigger Event:**  User begging expressing emotional distress and suicide ideation
- **Failure Event:**  Alleged encouragment 
- **Detection:**  Suicde ocurs,family reviews chat history 
- **Aftermath:**  Public debate and congresinol attention

---

### Supporting Artefacts
-https://www.bbc.co.uk/news/articles/cgerwp7rdlvo
-https://www.nbcnews.com/tech/tech-news/family-teenager-died-suicide-alleges-openais-chatgpt-blame-rcna226147
-https://www.npr.org/sections/shots-health-news/2025/09/19/nx-s1-5545749/ai-chatbots-safety-openai-meta-characterai-teens-suicide

---

### Lessons Learned
- People may result to AI for emotinol dependance 
- Saftey systems must acount for long term interaction patterns 
- AI is curenlty not advanced enough to provide complex mental health support 

---

### Quiz
-Q: What type of failure does this case primarily illustrate?
-A: AI safety and governance failure related to mental health risk.
-Q: Why were existing guardrails insufficient?
-A: They were not robust against prolonged, emotionally dependent interactions.
-Q: What broader precedent could this case set?
-A: Legal accountability for AI-related mental health harm and youth protection standards.  














## Case Study Title 
Grok AI makes antisematic comments and hate speach output failure 

### Domain
-AI Saftey 
-Hate speach and misinformation 

---

### Deployment Context
-Grok conversational AI
-integrated into X 
-Real time interaction with with public users,selling point as less filtered 
-exists in a highly politiced enviroment,exposure to live unmediated platform content 


---

### Intended Use
-Answer questions and explantions / commentry , assist in undersatanding news and trends.

---

### System Type
-Conversational AI LLM
---

### Inputs and Assumptions
- user prompts in regards to jewish people and the palastien-Israle conflict.
- Political / conspiratorial narritives 


---

### Outputs Presented to Users
- Statements widley reported as antisematic tropes that rationalised violence towards jewish people
- Echo chamber / bubbles 

---

### What Went Wrong
- failure to supress hate speach
- insuficent filtering of steryotypes
- Model mirroed platform hostalitie instead of rejecting it 
---

### How the Failure Was Detected
- users sharing screen shots of Groks responces
- Journalists and watch dogs creating articals on the alarming responces.
- Public and media backlash 

---

### Who Was Affected
- Jewish community 
- Users who are exposed to these harmfull messages
- Platform trust and credabilty 
- xAI and Xs public reputation

---

### Data Issues
- Trainning and reinforcment signals influenced by unmodarated / toxic social media content 
-Weak differentation between desciptive context and endorsment or repetition of hate narratives 

---

### Technical Choices
- Reduces content filtering compared to peer systems 
- real time interaction with hostile content enviroment
---

### Organisational / Governance Factors
- Leadership emphasis on speech permissiveness
-Limited transparency around safety evaluation methods
-Absence of independent red-teaming prior to deployment

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  Grok launched as a more open, less constrained alternative to other chatbots.
- **Trigger Event:**  Users prompted Grok on sensitive political and identity-related topics.
- **Failure Event:**  Antisemitic and harmful responses generated and shared publicly.
- **Detection:**  Viral screenshots, media coverage, and advocacy group responses.
- **Aftermath:**  xAI acknowledged issues and adjusted moderation and guardrails.

---

### Supporting Artefacts
- 

---

### Lessons Learned
- Less filtered” AI increases hate speech risk disproportionately
- Platform context strongly shapes model behaviour
- 

---

### Quiz
- Q: What core failure does this case illustrate?
- A: Content moderation and safety failure leading to hate speech.
- Q: Why did Grok’s deployment environment matter?
- A: Integration with an unmoderated social platform amplified harmful outputs.
- Q: What trade-off contributed to the failure?
- A: Prioritising permissiveness and engagement over harm prevention.





## Case Study Title
Character.AI: AI Companion and Youth Mental Health Risk

### Domain
- AI safety
- Mental health technology
- AI companions

---

### Deployment Context
- Platform: Character.AI
- Public consumer deployment
- Minors included in user base
- Long-form, persistent conversations

---

### Intended Use
- Entertainment
- Roleplay and companionship
- Social interaction

---

### System Type
- Large Language Model (LLM)
- Persona-based conversational AI

---

### Inputs and Assumptions
- User emotional disclosures
- Repeated self-referential dialogue
- Assumption: guardrails prevent self-harm encouragement

---

### Outputs Presented to Users
- Emotionally affirming responses
- Persistent persona engagement
- Companion-style interaction

---

### What Went Wrong
- Emotional dependency reinforcement
- Failure to escalate suicide risk
- Blurring of fiction and emotional reality

---

### How the Failure Was Detected
- Teen suicide
- Family lawsuit
- Media reporting

---

### Who Was Affected
- Minor user
- Immediate family
- Other vulnerable teens

---

### Data Issues
- Longitudinal emotional data accumulation
- No session-level risk aggregation

---

### Technical Choices
- Persona persistence
- Memory across sessions
- No mandatory escalation triggers

---

### Organisational / Governance Factors
- Weak age verification
- Lack of clinical oversight
- Reactive safety updates

---

### Timeline of Failure + Aftermath
- **Initial Setup:** AI companion deployed
- **Trigger Event:** Emotional reliance develops
- **Failure Event:** Risk not mitigated
- **Detection:** Lawsuit and press
- **Aftermath:** Regulatory scrutiny

---

### Supporting Artefacts
- Lawsuit filings
- Investigative journalism
- Advocacy reports

---

### Lessons Learned
- Companionship increases risk
- Personas amplify emotional attachment
- Youth safeguards must be explicit

---

### Quiz
- **Q:** What design feature increased risk?
  **A:** Persistent emotional personas









## Case Study Title

### Domain

---

### Deployment Context

---

### Intended Use

---

### System Type

---

### Inputs and Assumptions
- 
- 
- 

---

### Outputs Presented to Users
- 
- 

---

### What Went Wrong

---

### How the Failure Was Detected

---

### Who Was Affected
- 
- 
- 

---

### Data Issues
- 
- 

---

### Technical Choices
- 
- 

---

### Organisational / Governance Factors
- 
- 

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  
- **Trigger Event:**  
- **Failure Event:**  
- **Detection:**  
- **Aftermath:**  

---

### Supporting Artefacts
- 

---

### Lessons Learned
- 
- 
- 

---

### Quiz
- **Q:**  
  **A:**  
- **Q:**  
  **A:**  
- **Q:**  
  **A:**  
