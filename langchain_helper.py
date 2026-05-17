from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

def generate_restaurant_name_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name."
    )
    name_chain = prompt_template_name | llm

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest menu items for {restaurant_name}. Return as comma separated string."
    )
    items_chain = prompt_template_items | llm

    # Chain the operations
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).content.strip()
    menu_items = items_chain.invoke({"restaurant_name": restaurant_name}).content.strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }