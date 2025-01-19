import pandas as pd
import streamlit as st

from member.database import view_team_db


def view_team(srn):
    result = view_team_db(srn)
    df = pd.DataFrame(result, columns=['Member Name', 'Phone Number', 'SRN', 'DOB'])
    st.dataframe(df)
