# OpenAI Debaters


[![SF City Hall](docs/city_hall.jpeg)](https://youtu.be/I2j70VwPGug "Measure A")

Are you trying to be an informed voter? Do you hate listening to talking heads attack each other and never talk about the actual issues? Do you just want to know what the measures are and then hear intelligent debate around them? 

Well this repo is for you! We feed the [official city election guide](https://voterguide.sfelections.org/local-ballot-measures) from San Francisco for the upcoming 2024 city ballot measures to the [OpenAI Assistants API](https://platform.openai.com/docs/api-reference/assistants), then create an informed debate on each measure. We then turn the text into audio using [OpenAI's TTS model](https://platform.openai.com/docs/models/tts). 

The result? High quality, informed debate on all measures on the San Francisco ballot this year.
Each debater opens and closes their debate, and the number of rounds is configurable.  Worried about me trying to sway you to either side? This repo open sources the instructions given to each agent, so you can examine exactly what they are asked to do. 

You can click the image above of city hall to go directly to an audio clip of the results on Measure A!

Enjoy!


## Results
| Measure      | Text | Audio |
| ----------- | ----------- | ----------- |
|Measure A: Affordable Housing Bonds | [text](docs/debate_a.txt) | [audio](docs/issue_a.mp3) |
|Measure B: Police Office Staffing Levels | [text](docs/debate_b.txt)| [audio](docs/issue_b.mp3) |
|Measure C: Real Estate Transfer Tax Exemption | [text](docs/debate_c.txt)| [audio](docs/issue_c.mp3) |
|Measure D: Changes to Local Ethics Laws | [text](docs/debate_d.txt)| [audio](docs/issue_d.mp3) |
|Measure E: Police Department Policies and Procedures | [text](docs/debate_e.txt)| [audio](docs/issue_e.mp3) |
Measure F: Illegal Substance Dependence Screening and Treatment for Recipients of City Public Assistance | [text](docs/debate_f.txt)| [audio](docs/issue_f.mp3) |
|Measure G: Offering Algebra 1 to Eighth Graders | [text](docs/debate_g.txt)|  [audio](docs/issue_g.mp3) |


## Installation
1. Generate an OpenAI key: https://platform.openai.com/api-keys. 
2. Export it to your local environment using `export OPENAI_API_KEY=<your key here>`
3. Install necessary libraries with `pip install -r requirements.txt`
4. Launch the included jupyter notebook and run the cells. 
5. Output will be placed in `<location of repo>/outputs`

# Design
![Block Diagram](docs/openai_sf_debaters.png)

- Each measure gets a custom assistant, which has access to a downloaded copy of the measure summary from sf.gov.
- Each debate takes place in a persistent thread, and the user acts as a moderator by inserting messages into the thread.
- The AI Assistant debates itself. To do so a run is created which points to the past history of messages and the assistant that should respond.

## Notes
- At first I created two agents to debate each other, but then realized I could include [additional instructions](https://platform.openai.com/docs/api-reference/runs/createRun) per run that would tell the assistant to flip sides. 
- The assistant is initially created with explicit instructions on how a debate is structured. 
- After some prompt engineering, I found that it was necessary to:
    - Explicitly ask the assistant to respond to the other debater
    - Have the assistant preface its answers with the debater title so it was easier to tell who was who
    - Ask the assistant to introduce novel arguments so it wasn't just repeating what was in the downloaded summary.

## So, does it work? 
The audio sounds smooth and the text is coherent. The agents respond to each other, and in the case of most measures, come up with novel arguments. 
<br><br> 
For example, in Measure A, a supporter of the measure brings up the economic benefits of creating this housing:

>Introducing new arguments, I would also point to the broader economic benefits that come with investing in affordable housing. Research has demonstrated that every dollar spent on building affordable housing contributes to local economies by supporting jobs in construction and related industries, increasing disposable income, and promoting further economic activity.

An opponent brings up that government involvement in housing can create market distortions: 
>Continuing on novel arguments, it is important to consider the potential market distortions that can arise from government intervention in the housing market. The creation of affordable housing through bond measures may inadvertently affect the housing market by disincentivizing private sector investment and development. There's a delicate balance between providing affordable housing and allowing the market to respond to demand, and heavy-handed approaches can lead to unintended consequences.

Neither of these points was mentioned in the Measure A summary provided by SF.gov, and are valid concerns!
<br><br>
Downsides - the agents are still quite verbose, and one could make the argument that you could still get higher information density by just reading the ballot measure. Additionally, they don't cite their sources, and tend to repeat themselves. But, the debaters do bring new insights and considerations into the mix. Plus, it's nice to be able to listen to a summary of the issues while commuting or washing dishes :)


