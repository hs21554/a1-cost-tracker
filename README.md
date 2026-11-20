# AI Token & Cost Tracker

A Python-based Command Line application that integrates "Google Gemini" and "Groq" API's to Generate AI Responses, Track Token Usage, Estimate Input-Output Tokens Cost and save Results in "Results.json" File.

## Overview

AI Token & Cost Tracker helps you monitor how many input and output tokens are used for different AI Models and estimate the associated API Cost.

> The current version supports: - Google Gemini API - Groq API

When the script runs, it asks for three prompts for Gemini and then three prompts for Groq. It displays each model's response, token usage, and estimated cost. Results from both providers are stored together in "Results.json".

> **Note:** The current script asks for prompts separately for each provider. The prompts are not automatically shared between Gemini and Groq.

## Features

Generate responses using the Google Gemini API.
Generate responses using the Groq API.
Enter prompts interactively in the terminal.
Track input and output token counts.
Calculate estimated input, output, and total token costs.
Store results from both models in one JSON file.
Clear previous results at the beginning of a new script run in "Results.json" file.
Save each response to "Results.json" as it is generated.

## Technologies

1. **Python** --- application logic
2. **Google Gen AI SDK** --- Gemini API integration
3. **Groq Python SDK** --- Groq API integration
4. **python-dotenv** --- load API keys and model names from environment variables
5. **JSON** --- store generated results
6. **uv** --- Python project, dependency and package management

## Project Structure

The following is the structure based on the current script.

a1-cost-tracker/
|___src/
│   └── a1_cost_tracker/
│       └── tracker.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
├── Results.json
└── README.md

"Results.json" is updated by the application when the script runs. It does not need to contain committed personal or API data.

## Prerequisites

1. Python version supported by the dependencies in "pyproject.toml".
2. uv installed using command "winget install --id = astral-sh .uv -e.
3. Check uv --version.
4. A Google Gemini API key (Get from Google AI API Studio)
5. A Groq API key (Get from Groq Cloud)

## Installation

Clone the repository and move into the project directory:

```Bash 
git clone YOUR_GITHUB_REPOSITORY_URL
cd a1-cost-tracker
```
Install the project dependencies:

```bash
uv sync" 
```

If you are setting up the dependencies manually, the script uses these packages:

``` bash
winget install --id = astral-sh .uv -e
uv --version
source src/Scripts/activate
uv init
uv add google-genai groq python-dotenv
uv run src/a1-cost-tracker/tracker.py
```

## Environment Configuration

Create a `.env` file in the project root (the same directory from which you run the command).

Add your model names and API keys:

``` env
Genai_MODEL=your_gemini_model_name
Genai_API_Key=your_gemini_api_key

Groq_MODEL=your_groq_model_name
Groq_Key=your_groq_api_key
```
Replace the example values with your actual model names and API keys.

If you maintain a `.env.example` file, include only placeholder values:

``` env
Genai_MODEL=
Genai_API_Key=

Groq_MODEL=
Groq_Key=
```

**Security:** Never commit your real `.env` file or expose API keys insource code or GitHub. Add `.env` to `.gitignore`.

## Run the Application

From the project root, run:

``` bash
uv run src/a1_cost_tracker/tracker.py
```

The application will:

1.  Clear the previous contents of `Results.json` at the start of the run.
2.  Ask for three prompts for Gemini, one at a time.
3.  Generate and display each Gemini response.
4.  Display input tokens, output tokens, and estimated cost for each response.
5.  Then Ask for three prompts for Groq, one at a time.
6.  Generate and display each Groq response.
7.  Display input tokens, output tokens, and estimated cost for each response.
8.  Save each model response to the same `Results.json` file.

At the end of a successful run, the JSON file should contain up to six records: three Gemini results and three Groq results.

## Cost Calculation

The script estimates cost using the following formula:

``` text
Input Cost  = (Input Tokens  × Input Rate)  / 1,000,000
Output Cost = (Output Tokens × Output Rate) / 1,000,000
Total Cost  = Input Cost + Output Cost
```

The rates currently configured in the script are:

Provider: Gemini 
Input Token Per 1 Million: $0.30
Output Token Per 1 Million: $2.50

Provider: Groq
Input Token Per 1 Million: $0.10
Output Token Per 1 Million: $0.60
  
**Pricing warning:** These are the values currently hardcoded in this
project. API prices vary by model and can change. Verify the official pricing for the exact model
you use, then update the rates in `tracker.py`.

## Results File

The application writes results to `Results.json`. Each record includes the model name, prompt number, prompt text, generated response, input token count, output token count, and estimated total cost.

## Example 

``` json
{
    "Model": "your_model_name",
    "Prompt_No": 1,
    "Prompt": "What is Python?",
    "Response": "Python is a programming language.",
    "Input_Tokens": 5,
    "Output_Tokens": 10,
    "Total_Cost": 0.0000265
}
```

The actual response, token counts, and cost will depend on the prompt and selected model.

## Current Limitations

> The application currently supports Gemini and Groq only.
> It collects three prompts separately for each provider.
> It is a command-line application; there is no web dashboard yet.
> Cost rates are currently configured directly in the Python script.
> If an API request fails, the current basic script may stop before completing all prompts.

## Future Improvements

> Add OpenAI API integration.
> Add Anthropic Claude integration.
> Build a dashboard for model, token, and cost comparisons.
> Add error handling and logging.

## Suggestion

Suggestions and improvements are welcome. For significant changes, consider opening an issue first to discuss what you would like to change.
