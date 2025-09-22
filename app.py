import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool


# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# ------------------ API CALL FUNCTIONS ------------------

def get_train_info(train_no: str):
    """Fetch info about a specific train"""
    url = f"https://indian-railway-api.cyclic.app/trains/getTrain/?trainNo={train_no}"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {"error": "Unable to fetch train info"}

def get_trains_between(from_stn: str, to_stn: str):
    """Fetch trains between two stations"""
    url = f"https://indian-railway-api.cyclic.app/trains/betweenStations/?from={from_stn}&to={to_stn}"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {"error": "Unable to fetch trains between stations"}

def get_trains_on_date(from_stn: str, to_stn: str, date: str):
    """Fetch trains between two stations on a specific date (dd-mm-yyyy)"""
    url = f"https://indian-railway-api.cyclic.app/trains/gettrainon?from={from_stn}&to={to_stn}&date={date}"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {"error": "Unable to fetch trains on date"}

def get_route(train_no: str):
    """Fetch route of a specific train"""
    url = f"https://indian-railway-api.cyclic.app/trains/getRoute?trainNo={train_no}"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {"error": "Unable to fetch route"}

# ------------------ LANGCHAIN TOOLS ------------------

tools = [
    Tool(
        name="Train Info",
        func=lambda q: str(get_train_info(q)),
        description="Use this to get train info by train number. Input: train number."
    ),
    Tool(
        name="Trains Between Stations",
        func=lambda q: str(get_trains_between(q.split(',')[0], q.split(',')[1])),
        description="Use this to get trains between two stations. Input: from_station_code,to_station_code"
    ),
    Tool(
        name="Trains On Date",
        func=lambda q: str(get_trains_on_date(q.split(',')[0], q.split(',')[1], q.split(',')[2])),
        description="Use this to get trains between two stations on a specific date. Input: from_station_code,to_station_code,date(dd-mm-yyyy)"
    ),
    Tool(
        name="Train Route",
        func=lambda q: str(get_route(q)),
        description="Use this to get full route of a train by train number. Input: train number."
    )
]

# ------------------ LLM + AGENT ------------------

llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# ------------------ STREAMLIT UI ------------------

st.set_page_config(page_title="🚉 AI Train Crossing Assistant", layout="wide")
st.title("🚉 AI Train Crossing Assistant")

st.markdown("Ask me about trains, routes, timings, or if it’s safe to cross!")

user_query = st.text_input("Your Question:", placeholder="E.g. When will train 22137 cross Nagpur?")

if st.button("Ask"):
    if user_query:
        try:
            response = agent.run(user_query)
            st.success(response)
        except Exception as e:
            st.error(f"Error: {e}")
