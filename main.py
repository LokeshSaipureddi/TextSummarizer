import streamlit as st
from transformers import pipeline

def main():
    st.title("Text Summarizer App")
    # Text input
    text_input = st.text_area("Enter your text here:")

    # Summary button
    if st.button("Generate Summary"):
        if text_input:
            # Summarize the input text
            summary = summarize_text(text_input)

            # Display the summary
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter text to summarize.")


def summarize_text(text):
    # Use BERT Extractive Summarizer
    summarizer = pipeline('summarization', model = 'facebook/bart-large-xsum')
    summary = summarizer(text)

    return summary[0]["summary_text"]


if __name__ == "__main__":
    main()