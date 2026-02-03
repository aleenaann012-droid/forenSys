def init_state(st):
    defaults = {
        "email_body": "",
        "url": "",
        "analysis": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v