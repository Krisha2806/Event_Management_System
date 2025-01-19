import pandas as pd
import streamlit as st

from member.database import view_event_db


def view_event(srn):
    result = view_event_db(srn)
    # st.success("Success")
    df = pd.DataFrame(result, columns=['Event Name','Event Price', 'Event Venue','Event Date' ])
    st.dataframe(df)

