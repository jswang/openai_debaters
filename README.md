# OpenAI Debaters

![SF City Hall](docs/city_hall.jpeg)

Are you trying to be an informed voter? Do you hate listening to talking heads attack each other and never talk about the actual issues? Do you just want to know what the measures are and then hear intelligent debate around them? 

Well this repo is for you! We feed the [official city election guide](https://voterguide.sfelections.org/local-ballot-measures) from San Francisco for the upcoming 2024 city ballot measures to the [OpenAI Assistants API](https://platform.openai.com/docs/api-reference/assistants), then create an informed debate on each measure. We then turn the text into audio using [OpenAI's TTS model](https://platform.openai.com/docs/models/tts). 

The result? High quality, informed debate on all 7 measures up for election this year.
Each debater will open and close their debate, and the number of rounds in between is configurable.  Worried about me trying to sway you to either side? This repo open sources the instructions given to each agent, so you can examine exactly what they are asked to do. 

Enjoy!

## Results
|Measure A: Affordable Housing Bonds | [text](docs/debate_a.txt) |
|Measure B: Police Office Staffing Levels | [text](docs/debate_b.txt)|
|Measure C: Real Estate Transfer Tax Exemption | [text](docs/debate_c.txt)|
|Measure D: Changes to Local Ethics Laws | [text](docs/debate_d.txt)|
|Measure E: Police Department Policies and Procedures | [text](docs/debate_e.txt)|
Measure F: Illegal Substance Dependence Screening and Treatment for Recipients of City Public Assistance | [text](docs/debate_f.txt)|
|Measure G: Offering Algebra 1 to Eighth Graders | [text](docs/debate_g.txt)| 


## Installation
1. Generate an OpenAI key: https://platform.openai.com/api-keys. 
2. Export it to your local environment using `export OPENAI_API_KEY=<your key here>`
3. Install necessary libraries with `pip install -r requirements.txt`
4. Launch the included jupyter notebook and run the cells. 
5. Output will be place in `<location of repo>/outputs`
