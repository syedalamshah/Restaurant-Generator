# Restaurant Generator

A Streamlit web app that generates a restaurant name and menu items for a chosen cuisine using LangChain and Google Gemini.

## What this project does

- Lets the user choose a cuisine from a Streamlit dropdown
- Sends the cuisine to Gemini through LangChain prompts
- Generates a restaurant name
- Generates matching menu items
- Displays the results in a styled Streamlit interface

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini via `langchain-google-genai`
- `python-dotenv` for environment variable loading

## Project Structure

- `main.py` - Streamlit UI and app entry point
- `langchain_helper.py` - LangChain and Gemini prompt logic
- `.env` - Local environment file containing your API key
- `.env.example` - Example environment file for setup
- `.gitignore` - Ignores secrets and local Python build artifacts

## Prerequisites

- Python 3.10 or later
- A valid Google API key for Gemini

## Installation

1. Clone the repository.

```powershell
git clone https://github.com/syedalamshah/Restaurant-Generator.git
cd Restaurant-Generator
```

2. Create and activate a virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install the required packages.

```powershell
pip install streamlit langchain langchain-core langchain-google-genai python-dotenv
```

4. Create your local `.env` file.

```powershell
Copy-Item .env.example .env
```

5. Open `.env` and replace the placeholder with your real API key.

```text
GOOGLE_API_KEY=your_actual_api_key_here
```

## Run the App

```powershell
streamlit run main.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## How It Works

1. The user selects a cuisine type.
2. `langchain_helper.py` creates two prompt chains.
3. Gemini generates a restaurant name for the chosen cuisine.
4. Gemini generates menu items for that restaurant name.
5. Streamlit displays the final result in a clean UI.

## Notes

- Do not commit your `.env` file to version control.
- The repository includes `.env.example` so other users can set up their own key safely.
- If the app fails with an API key error, verify that your Google API key is valid and saved in `.env`.

## License

No license has been added yet.