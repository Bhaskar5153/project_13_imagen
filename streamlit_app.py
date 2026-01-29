import streamlit as st
import requests

st.set_page_config(page_title="Imagen 4 Chatbot", page_icon="🖼️")
st.title("🖼️ Imagen 4 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
        if "image_path" in msg:
            st.image(msg["image_path"], caption=msg["content"])

if prompt := st.chat_input("Enter your image prompt..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # FIXED: use port 8001 instead of 8000
        response = requests.post("http://127.0.0.1:8001/generate-image/", data={"prompt": prompt})
        if response.status_code == 200:
            file_path = response.json()["file_path"]
            st.session_state["messages"].append({"role": "assistant", "content": "Here’s your image:", "image_path": file_path})
            st.chat_message("assistant").write("Here’s your image:")
            st.image(file_path, caption=prompt)
        else:
            st.session_state["messages"].append({"role": "assistant", "content": f"Failed to generate image. Status: {response.status_code}"})
            st.chat_message("assistant").write(f"Failed to generate image. Status: {response.status_code}")
    except Exception as e:
        st.session_state["messages"].append({"role": "assistant", "content": f"Error: {e}"})
        st.chat_message("assistant").write(f"Error: {e}")