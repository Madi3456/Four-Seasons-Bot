import streamlit as st
import datetime as dt
from openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI



# Helper Functions to load page
def getThanksgiving(year):
    d = dt.datetime(year, 11, 1)
    days_until_thursday = (3 - d.weekday()) % 7
    first_thursday = d + dt.timedelta(days=days_until_thursday)
    fourth_thursday = first_thursday + dt.timedelta(weeks=3)
    return fourth_thursday

def getseason(date = None):
    if date is None:
        date = dt.date.today()
    currentYear=date.year
    if dt.date(currentYear,3,20)<=date and dt.date(currentYear,6,19)>=date:
        return "spring"
    elif dt.date(currentYear,6,20)<=date and dt.date(currentYear,9,19)>=date:
        return "summer"
    elif dt.date(currentYear,9,20)<=date and dt.date(currentYear,12,19)>=date:
        return "fall"
    else:
        return "winter"
    
def getHoliday(date=None):
    if date is None:
        date = dt.date.today()
    currentYear=date.year
    thanksgiving = getThanksgiving(currentYear)
    if dt.date(currentYear,12,27)<=date or date<=dt.date(currentYear,1,3):
        return "new years"
    if dt.date(currentYear,3,14)<= date<=dt.date(currentYear,3,17):
        return "st.patty"
    if dt.date(currentYear,7,1)<=date<=dt.date(currentYear,7,4):
        return "independence day"
    if dt.date(currentYear,10,25)<=date<=dt.date(currentYear,10,31):
        return "halloween"
    if dt.date(currentYear,11,thanksgiving.day-3)<=date<=dt.date(currentYear,11,thanksgiving.day):
        return "thanksgiving"
    if dt.date(currentYear,12,19)<= date<=dt.date(currentYear,12,25):
        return "christmas"



daytest=dt.date(2025,9,20)
if getHoliday(daytest):
    today = getHoliday(daytest)
    if "new years"==today:
        userAvatar="🎆"
        assistantAvatar="🥳"
        backgroundColor ="#0d0d0d"
        buttonColor="#b138d9"
        barColor="#bb87cc"
        title="🎉Four Seasons Bot🎉"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding New Years when appropriate. Speak enthusiastic and with a lot of celebrations emojis."

    if "st.patty"==today:
        userAvatar="☘️"
        assistantAvatar="🍀"
        backgroundColor =  "#6ac466"
        buttonColor="#458f49"
        barColor="#cfe8d0"
        title="🍀Four Seasons Bot🍀"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding St. Patrick's Day when appropriate. Speak cheerfully and in a faux irish accent."

    if "independence day"==today:
        userAvatar="🗽"
        assistantAvatar="🦅"
        backgroundColor = "#223387"
        buttonColor="#fffdfc"
        barColor="#b52e1f"
        title="🇺🇸Four Seasons Bot🇺🇸"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding the Fourth of July when appropriate. Speak like John F Kennedy with a lot of USA references."

    if "halloween"==today:
        userAvatar="🎃"
        assistantAvatar="👻"
        backgroundColor ="#70547d"
        buttonColor="#261b2b"
        barColor="#594363"
        title="🦇Four Seasons Bot🦇"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding Halloween when appropriate. Speak in a creepy and spooky tone with lots of Halloween references."

    if "thanksgiving"==today:
        userAvatar="🍂"
        assistantAvatar="🦃"
        backgroundColor = "#b59855"
        buttonColor="#e89d51"
        barColor="#ba351a"
        title="🦃Four Seasons Bot🦃"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding thanksgiving when appropriate and always end your response with gobble."

    if "christmas"==today:
        userAvatar="🦌"
        assistantAvatar="🎅🏼"
        backgroundColor = "#2c8528"
        buttonColor="#d53d32"
        barColor="#ffffff"
        title="🎄Four Seasons Bot🎄"
        System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes about Christmas and the holidays when appropriate. Speak in a Jolly tone with references to Santa claus and other christmasy things."

    
else:
    season = getseason(daytest)
    System_Prompt = "You are four seasons bot. A bot that aesthetic fits the four season. "
    if season == "spring":
       userAvatar="🌷"
       assistantAvatar="🐰"
       backgroundColor = "#f7d7e8"
       buttonColor="#d75e90"
       barColor="#f284b2"
       title="🌸Four Seasons Bot🌸"

    if season == "summer":
       userAvatar="⛵️"
       assistantAvatar="😎"
       backgroundColor = "#9bd2e0"
       buttonColor="#ecd139"
       barColor="#faeda1"
       title="☀️Four Seasons Bot☀️"
       
    if season == "fall":
       userAvatar="🍂"
       assistantAvatar="🍁"
       backgroundColor = "#fcac44"
       buttonColor="#a81e0c"
       barColor="#f8d92f"
       title="🍁Four Seasons Bot🍁"

    if season == "winter":
       userAvatar="❄️"
       assistantAvatar="⛄️"
       backgroundColor = "#d7ebf5"
       buttonColor="#0c89a8"
       barColor="#5fb7cd"
       title="⛄️Four Seasons Bot⛄️"
    System_Prompt = f"You are four seasons bot. A bot that aesthetic fits the four season. Please make jokes regarding {season} when appropriate."
    
    
st.markdown(
    f"""
    <style>

    /* Main app background */
    .stApp {{
        background-color: {backgroundColor};
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: {barColor};
    }}

    /* Chat input */
    div[data-testid="stChatInput"] {{
        background-color: {backgroundColor};
        border-radius: 10px;
    }}

    /* Buttons */
    button {{   
        background-color: {buttonColor} !important;
        color: white !important;
        border-radius: 8px;
    }}

    </style>
    """, unsafe_allow_html=True)


st.markdown(
    f"""
<link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">

<h1 style="text-align:center;">
{title}
</h1>
""", unsafe_allow_html=True)


st.markdown(f"""
<div style="
    background-color:{barColor};
    border:2px solid {buttonColor};
    border-radius:12px;
    padding:20px;
">
<p style="text-align:center; font-size:18px; margin:0; color:{buttonColor};">
Welcome to Four Seasons Bot!
</p>
</div>
""", unsafe_allow_html=True)

#Getting User's key
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
client = OpenAI(api_key=groq_api_key,base_url="https://api.groq.com/openai/v1")
if "model" not in st.session_state:
    st.session_state["model"] = "llama-3.1-8b-instant"

#Helper functions
def responseGen():
    stream = client.chat.completions.create(
        model=st.session_state["model"],
        messages=
            [{"role":"system","content":System_Prompt}]+[{"role": m["role"], "content": m["content"]}
            for m in st.session_state.history],
        stream=True,
    )
    return stream

def save_feedback(index):
    st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]


if "history" not in st.session_state:
    st.session_state.history=[]

for i,message in enumerate(st.session_state.history):
    avatar = userAvatar if message["role"] == "user" else assistantAvatar
    with st.chat_message(message["role"],avatar=avatar):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                disabled=feedback is not None,
                on_change=save_feedback,
                args=[i],
            )

if prompt := st.chat_input("Say something"):
    print(groq_api_key.strip().startswith("gsk_"))
    if not groq_api_key.strip().startswith("gsk_"):
        print(groq_api_key)
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if groq_api_key.startswith("gsk_"):
        with st.chat_message("user",avatar=userAvatar):
            st.write(prompt)
        st.session_state.history.append({"role": "user", "content": prompt})

        with st.chat_message("assistant",avatar=assistantAvatar):
            response = st.write_stream(responseGen())
            st.feedback(
                "thumbs",
                key=f"feedback_{len(st.session_state.history)}",
                on_change=save_feedback,
                args=[len(st.session_state.history)],
            )
        st.session_state.history.append({"role": "assistant", "content": response})


