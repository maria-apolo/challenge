*Instructions: Click on the raw button in the upper right hand corner of this box.  Copy and paste the template into the README.md document on your github.  Fill in the titles, information and links where prompted! Feel free to stray a bit to suit your project but try to stick to the format as closely as possible for consistency across DSWG projects.*

# LATAM challenge - María José Apolo

## Instructions

### Part I.

In order to operationalize the model, transcribe the `.ipynb` file into the `model.py` file:

- If you find something wrong (i.e. bug), fix it and/or change it, argue why.
- Choose the best model at your discretion, argue why.
- Apply all the good programming practices that you consider necessary in this item.
- The model should pass the tests by running `make model-test`.

Note:
- **You cannot** remove or change the name or arguments of provided methods.
- **You can** change/complete the implementation of the provided methods.
- **You can** create the extra classes and methods you seem necessary.

### Part II.

Deploy the model in an `API` with `FastAPI` (use the `api.py` file).

- The `API` should pass the tests by running `make api-test`.
- You should modify the tests in `tests/integration/test_api.py` to match the previous question.

Note: 
- **You can** use other framework but you should:
  - Argue why.
  - Implement your own tests (the `API` **MUST** be tested).

### Part III.

Deploy your `API` to you favorite cloud provider (we recomend to use GCP, you will need to put a credit card but no charge will be issue [[info]](https://cloud.google.com/free/docs/free-cloud-features#billing_verification)) where we going to run a series of test and run performance benchmark.

We are looking for seeing a proper `CI/CD` implementation for this development. We recommend using GitHub Actions but this is not a constraint, feel free to use whatever you wish (we will check the implementation).

Put your url in the `Makefile` (`line 26`). Then we will test the perfomance with the comand `make stress-test`. Make sure to go in `tests/stress/api-stress.py` and add the necesary inputs so the test run in the endpoint.

**It is important that the API is deployed until we review the tests. If your API needs any authentication method, you must indicate which one and ensure that we can access it.**


## Implementation

### Part 1 
#### Fixes

Before operationalized the model, It was necessary to implement fixes in the following files:

* utils.py - 
* model.py - 

### Partner
* [Name of Partner organization/Government department etc..]
* Website for partner
* Partner contact: [Name of Contact], [slack handle of contact if any]
* If you do not have a partner leave this section out

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* R 
* Python
* D3
* PostGres, MySql
* Pandas, jupyter
* HTML
* JavaScript
* etc. 

## Project Description
(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Data

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!