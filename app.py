import streamlit as st
import pandas as pd

# Load CSV file
data = pd.read_csv('Anuprayaas.csv')  # Replace with your actual CSV file name

# Title
st.title("Video Search Interface")

# Search bar
query = st.text_input("Search for a word:").lower()

# Display results
if query:
    results = data[data['word'].str.contains(query, case=False, na=False)]
    if not results.empty:
        st.write("Results:")
        for _, row in results.iterrows():
            link = row['URL']
            # Convert Google Drive link to embeddable format if needed
            if "drive.google.com" in link and "/view" in link:
                link = link.replace("/view", "/preview")
            st.markdown(f"**{row['File_Name']}**")
            # Embed the iframe directly for Google Drive videos
            if "drive.google.com" in link:
                st.markdown(
                    f'<iframe src="{link}" width="640" height="480" frameborder="0" allowfullscreen></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                st.video(link)
    else:
        st.write("No results found.")
else:
    st.write("Enter a word to search for related videos.")
