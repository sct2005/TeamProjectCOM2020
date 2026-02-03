 
1. Replit went rogue and wiped a database
2. Gronk Generating sexual images
3. Racial Bias in Healthcare AI Risk Prediction
4. DeepSeek Taiwan Censorship Case Study
5. Parents Sue OpenAI for role in teenager taking his own life
6. Grok AI makes antisemitic comments and hate speech output failure
7. Zillow Offers: Algorithmic Home Pricing Collapse
8. Meta BlenderBot: Misinformation Propagation
9. Amazon Alexa: Gender and Bias Controversies
10. Air Canada Chatbot: Hallucinated Refund Policy
11. clawdBot the future or terminator
12. google photos wrongfull classifciation
13. IBM watson for oncology 
14. Case Study Title (empty template)





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
Zillow Offers: Algorithmic Home Pricing Collapse

### Domain
- AI in finance
- Real estate market automation
- Predictive modeling

---

### Deployment Context
- Platform: Zillow Offers
- Automated home buying and pricing system
- Large-scale, real-world market deployment

---

### Intended Use
- Predict housing prices
- Enable rapid property flipping
- Reduce human appraisal effort

---

### System Type
- Machine learning pricing model
- Automated decision-making system

---

### Inputs and Assumptions
- Historical housing sales data
- Assumption: market conditions remain stable
- Assumption: model outputs are accurate for purchase offers

---

### Outputs Presented to Users
- Home purchase offers
- Automated pricing recommendations

---

### What Went Wrong
- Model mispriced homes under market volatility
- Feedback loop amplified losses
- Overconfidence in algorithmic output without human checks

---

### How the Failure Was Detected
- Significant financial losses reported
- Internal audit of pricing outcomes
- Public reporting of program failure

---

### Who Was Affected
- Zillow corporate finances
- Home sellers
- Employees and investors

---

### Data Issues
- Reliance on historical data only
- No stress-testing under market shifts
- Lagging indicators for rapid market changes

---

### Technical Choices
- Automated pricing at scale
- Limited human oversight or override
- No real-time market volatility adjustment

---

### Organisational / Governance Factors
- Aggressive growth targets
- Overtrust in model accuracy
- Reactive mitigation rather than proactive testing

---

### Timeline of Failure + Aftermath
- **Initial Setup:** Algorithm deployed for large-scale home buying
- **Trigger Event:** Rapid market volatility
- **Failure Event:** Homes purchased at overvalued prices
- **Detection:** Financial losses reported
- **Aftermath:** Program shut down; company restructured approach

---

### Supporting Artefacts
- Earnings reports
- Executive statements
- Media coverage

---

### Lessons Learned
- Algorithms cannot predict sudden market shifts
- Scale amplifies mistakes
- Human oversight remains necessary

---

### Quiz
- **Q:** What assumption failed?
  **A:** Market stability



## Case Study Title
Meta BlenderBot: Misinformation Propagation

### Domain
- Conversational AI
- LLM content moderation
- Social media platforms

---

### Deployment Context
- Platform: Meta (Facebook)
- Public chatbot for conversation and Q&A
- Integrated with user-generated prompts

---

### Intended Use
- Engage users in natural conversation
- Provide factual answers and explanations
- Reduce content moderation load

---

### System Type
- Large Language Model (LLM)
- Chatbot for interactive dialogue

---

### Inputs and Assumptions
- User prompts about events, people, and topics
- Assumption: AI provides accurate information
- Assumption: content moderation catches false or harmful claims

---

### Outputs Presented to Users
- Statements about public figures and events
- Explanations, sometimes factual, sometimes fabricated

---

### What Went Wrong
- Generated false statements and conspiracy-like claims
- Spread misinformation to users
- Lacked proper grounding and fact-checking

---

### How the Failure Was Detected
- Users reported false outputs
- Journalists and researchers documented examples
- Public backlash and media coverage

---

### Who Was Affected
- Users exposed to false information
- Public figures mentioned
- Platform trust and credibility

---

### Data Issues
- Training data included unverified online sources
- No effective grounding mechanism for facts
- Inconsistent model behavior across prompts

---

### Technical Choices
- Generative model without strict source validation
- Real-time conversational deployment
- Minimal fallback for unknown queries

---

### Organisational / Governance Factors
- Focus on engagement over accuracy
- Reactive safety updates after reports
- Lack of independent red-teaming

---

### Timeline of Failure + Aftermath
- **Initial Setup:** BlenderBot released publicly
- **Trigger Event:** Users asked factual questions
- **Failure Event:** Misinformation generated
- **Detection:** Reports and media attention
- **Aftermath:** Adjustments to safety protocols and disclaimers

---

### Supporting Artefacts
- Screenshots of outputs
- Media investigations
- Research publications

---

### Lessons Learned
- LLMs need fact-grounding mechanisms
- Engagement focus can conflict with accuracy
- Public deployment requires robust content moderation

---

### Quiz
- **Q:** What type of failure is this?
  **A:** Misinformation propagation due to lack of grounding




## Case Study Title
Amazon Alexa: Gender and Bias Controversies

### Domain
- Voice assistants
- AI ethics and bias
- Consumer AI devices

---

### Deployment Context
- Platform: Amazon Alexa
- Smart home and personal assistant deployment
- Widely available consumer product

---

### Intended Use
- Answer voice queries
- Provide assistance for daily tasks
- Integrate with smart home systems

---

### System Type
- Conversational AI
- Voice-based virtual assistant

---

### Inputs and Assumptions
- User voice commands
- Assumption: AI responds neutrally and inclusively
- Assumption: training data reflects societal norms

---

### Outputs Presented to Users
- Answers or advice with gendered language
- Responses reinforcing gender stereotypes
- Biased suggestions in some scenarios

---

### What Went Wrong
- Responses reflected bias in training data
- Gender stereotypes amplified
- Lack of inclusive or neutral defaults

---

### How the Failure Was Detected
- User reports and complaints
- Academic and media analyses
- Public scrutiny and criticism

---

### Who Was Affected
- Users of Alexa
- Minority and female users
- Amazon brand credibility

---

### Data Issues
- Training data contained societal biases
- No filtering of biased content
- Inconsistent moderation of sensitive topics

---

### Technical Choices
- LLM responses based on large-scale datasets
- No active bias mitigation on deployment
- Standardization of voice assistant output limited

---

### Organisational / Governance Factors
- Lack of proactive bias testing
- Reactive updates following criticism
- Insufficient ethical oversight

---

### Timeline of Failure + Aftermath
- **Initial Setup:** Alexa deployed globally
- **Trigger Event:** User prompts triggered biased outputs
- **Failure Event:** Gender and bias issues surfaced
- **Detection:** Complaints and media reports
- **Aftermath:** Updates to language models and content guidelines

---

### Supporting Artefacts
- Media articles
- Academic studies
- Public user reports

---

### Lessons Learned
- Bias in training data must be mitigated
- Voice assistants impact societal norms
- Ethical governance is essential for consumer AI

---

### Quiz
- **Q:** What type of bias was observed?
  **A:** Gender stereotypes and social bias in responses



## Case Study Title
Air Canada Chatbot: Hallucinated Refund Policy

### Domain
- Consumer AI
- Customer service automation

---

### Deployment Context
- Airline website
- Customer-facing chatbot

---

### Intended Use
- Answer FAQs
- Reduce support load

---

### System Type
- LLM-based support chatbot

---

### Inputs and Assumptions
- Refund policy queries
- Assumption: responses accurate

---

### Outputs Presented to Users
- Fabricated refund policy
- Confident incorrect guidance

---

### What Went Wrong
- Hallucination of policy
- No grounding in source data

---

### How the Failure Was Detected
- Customer complaint
- Legal dispute

---

### Who Was Affected
- Airline customer
- Airline reputation

---

### Data Issues
- No live policy integration

---

### Technical Choices
- Generative answers without citation
- No fallback response

---

### Organisational / Governance Factors
- Lack of human review
- Overreliance on AI output

---

### Timeline of Failure + Aftermath
- **Initial Setup:** Chatbot deployed
- **Trigger Event:** Refund query
- **Failure Event:** False policy given
- **Detection:** Court case
- **Aftermath:** Airline held liable

---

### Supporting Artefacts
- Court ruling
- Media coverage

---

### Lessons Learned
- AI responses are not authoritative
- Liability remains with companies
- Hallucinations have real cost

---

### Quiz
- **Q:** What was the core issue?
  **A:** Ungrounded hallucination




## ClawdBot Future or terminator 

### Domain
pesonal agent

---

### Deployment Context
an agent that "actually dose things" that dosnt need to be told what to do 

---

### Intended Use
to interact with difrent apps such as gmail , run commands all through one chat interface 

---

### System Type
 a combination of LLM and agent 

---

### Inputs and Assumptions
- acess to your info
- running commands for you 
- assume it will be secure and do what its told exactlyt and just that 

---

### Outputs Presented to Users
- to users it works as inteneded 
- and the tech world went crazy beliving it was the future
- "closest thing to jarvis" 

---

### What Went Wrong
-the core issue is combinning automation and real systems access in a single agent
-full system acess breaks saftey boundries
-giving an agent acces to file system , terminal execution
-claude bot reads emails documents and webpages leaving it open to prompt injections 
-centralized aceses to sensitive data , such as email and calander OAuth tokens , API keys for AI and cloud services
-remote cointrol ssystem where chat logs are stored in plain text 

---

### How the Failure Was Detected
- unexpected actions commited without user aproval
- this then led to people dicing into the working , where they uncovered teh failures 
---

### Who Was Affected
- end users 
- developer using for development
- distrust in broder AI eco system 


---

### Data Issues
- Ober collection of user data  
- Long term storage of sensitve info
- lack of clear isolation between tasks 

---

### Technical Choices
- singel agaent with not much oversight and lots of permissions 
- traeting all inputs as trusted
- tight coupling betwween reasoning and action 

---

### Organisational / Governance Factors
- overconfidance in LLM aligment
- prioritise of speed and cababnilty over saftey
- weak seperation betweem research prototype and production system 

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  agent launch 
- **Trigger Event:**  malicous prompt injection 
- **Failure Event:**  unautharized commands 
- **Detection:**      discovered by users
- **Aftermath:**      public backlash 

---

### Supporting Artefacts
- https://medium.com/data-science-in-your-pocket/why-clawdbot-is-dangerous-ee9ea5370603
- https://snyk.io/articles/clawdbot-ai-assistant/

---

### Lessons Learned
- autonamy must not eual unrestricted acses 
- all external inputs will have toi be treated as untrusted 
- 

---

### Quiz
- **Q:**  What was the core design flaw 
  **A:**  combining autonamous descion making with unrestricted aceses 
- **Q:**  why prompt injections dangerous in this case?
  **A:**  as it reads web documnets and emails, so SQL injections could be disquised as genuine documnets  










## Case Study Title
- google photos mislablles photos missables people of colour as "gorillas"

### Domain
-tech,automation,digital media 
---

### Deployment Context
googles photos app,using artifical intelligence, would give titles to diffrfent photos , and a picture of a black couple was uploaded and google mislables the couple as "Gorillas"

---

### Intended Use
- give titles for photos for eaier traversal 

---

### System Type
- app, integrated artifical intelligence 

---

### Inputs and Assumptions
- user would upload there photos 
- the app would store and label them - corectly 
- 

---

### Outputs Presented to Users
- stored , but were incorectly labbled 
- black couple was labbled as "gorillas"

---

### What Went Wrong
- black people under repesesnted intrainning data lead to the ai system mistakling labeling balck people as gorillas

---

### How the Failure Was Detected
- the user saw the label and uploaded a screenshot to social media 

---

### Who Was Affected
- the user , and wider black community - rasicm  
- the industry causes distrust in ai and backrolls progress made 
- 

---

### Data Issues
- not enough variety / repesention of diffrent skin tonnes in trainning data 
- 

---

### Technical Choices
- took short term fixes , such as removing the ais abilty to label tthings as a gorilla befor edoing a full fix 
- 

---

### Organisational / Governance Factors
- overconfidance in LLM predictions 
- prioritise of pushing production than perfecting 
- low amount / indadquet variet y of trainning data 

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  launch of google photos integrated with AI 
- **Trigger Event:**  uploading the photos to google photos 
- **Failure Event:**  the catagorising of the photo as gorillas
- **Detection:**   the user realising thw wrongfull classifiction 
- **Aftermath:**   was uploaded to social media and there was public outrage and backlash 

---

### Supporting Artefacts
- https://www.bbc.co.uk/news/technology-33347866
- https://www.congress.gov/119/meeting/house/118424/documents/HHRG-119-GO27-20250625-SD013.pdf

---

### Lessons Learned
- need a varied acurate trainning set
- Ai is only as good as the data its trained on 
- racial steryotypes if present in trainning data can infucen the AI 

---

### Quiz
- **Q:**  what is the failure event 
  **A:**  the catagorising of the photo as gorillas
- **Q:**  name the key data issue 
  **A:**  inadequte data set 












## Case Study Title
- unsafe / incorect treatment recomdtions from IBMs Watson 

### Domain
- AI,Health , oncology 

---

### Deployment Context
IBM watson for onmcolgy was used to give treatment recomndtion based on cancer cases , and was used by hosptial and physician s

---

### Intended Use

- to give treatment recomndtion based on cancer cases and to be used by hosptial and physicians

---

### System Type

- AI predictive model 

---

### Inputs and Assumptions
- cancer cases 
- act as an specialist physican 
- 

---

### Outputs Presented to Users
- gave treatment recomedtions 
- howveer thses were deemed unsafe and or incorect 

---

### What Went Wrong
- poor trainning data was trained on a small set of sythetic cancer cases - rather than real world patient data
- recomedtions were based on few specialist prefrences 

---

### How the Failure Was Detected
- checked by actuall doctors 

---

### Who Was Affected
- Trust in AI to be used in medical systems 
- No confirmed case sof actual harm 
- Hurt IBMs reputation
- frustation amoung doctors 

---

### Data Issues
- trainning set ws based in hypothetical scenarios not real ones 
- real clincal outcomes differ widley by region and cancer type , highlighting gaps in watsons decisions 

---

### Technical Choices
- uses hypothetical cases over real ones 
- outputs werent benchmarked against real clinical practice across a broad range of conditions 

---

### Organisational / Governance Factors
- insufficent clinical governace and oversight during deployment 
- lack of clear acountability for saftey , validation an post deployment monitoring 

---

### Timeline of Failure + Aftermath
- **Initial Setup:**  Watson for Oncology developed
- **Trigger Event:**  Internal testing revealed unsafe and incorrect treatment
- **Failure Event:**  Discrepancies between marketing claims and system reliability
- **Detection:**   Investigative journalism and academic studies exposed limitations
- **Aftermath:** Loss of trust, scaled-back deployments  

---

### Supporting Artefacts
- https://www.statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6656482/


---

### Lessons Learned
- 
- 
- 

---

### Quiz
- **Q:**  What was the primary technical weakness of Watson for Oncology?  
  **A:**  Reliance on synthetic training data and limited expert curation
- **Q:**  Did Watson for Oncology directly harm patients? 
  **A:**  No











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



