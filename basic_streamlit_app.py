import streamlit as st
st.title('Chat with the Alex')

##sick
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Display or clear chat messages


prompt = st.chat_input()

if prompt:
    st.write("Thanks for asking")
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)



def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.session_state.generated = []
    st.session_state.past = []


# with st.sidebar:
#     st.header("Upload your CSV data file")
#     data_file = st.file_uploader("Upload CSV", type=["csv"])



# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    pass
    # captured_output = capturer.get_output()


