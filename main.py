import streamlit as st
import json
import pandas as pd


@st.cache
def load_data():
    return json.load(open("./name_store.json"))



def filter_data(data):

    # result = []
    # for x in data:
    #     # name = x["Name"]
    #     if "Pronunciation" not in x:
    #         continue
    #     pron_segs = [s.lower() for s in x["Pronunciation"].split("-")]
    #     #
    #     # if not (
    #     #         "zee" in pron_segs or
    #     #         "cee" in pron_segs or
    #     #         "siy" in pron_segs or
    #     #         "see" in pron_segs or
    #     #         name.endswith("cy")
    #     # ):
    #     #     continue
    #     #
    #     if len(pron_segs) == 2:
    #         result.append(x)
    #
    # return result
    return data[:10]

#
data = load_data()
cleaned_data = filter_data(data)



for name_item in cleaned_data:
    st.markdown(f"""
    ### [{name_item["Rank"]}.{name_item["Name"]}](https://nametrends.net/name.php?name={name_item["Name"]})
    > **Meaning**: *{name_item["Meaning"]}*

    > **Origin**: *{name_item["Origin"]}*

    > **Pronunciation**: *{name_item["Pronunciation"] if "Pronunciation" in name_item else ""}*

    > {name_item["More"]}

    """)
    if "Dist" in name_item:
        df = pd.DataFrame({
            'year': [x["year"] for x in name_item["Dist"]],
            'per 1000': [x["ratio"] for x in name_item["Dist"]]
        })

        df = df.set_index('year')

        st.area_chart(df)
    st.markdown("---")