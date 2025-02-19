import streamlit as st
import requests
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Fetching News API key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_recent_news(query, api_key):

    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])[:5]  # Get top 5 articles
        news_context = "\n".join(
            [
                f"**{article['title']}**: {article['description']}"
                for article in articles if article.get("description")
            ]
        )
        return news_context
    else:
        return ""


def generate_blog(input_text, no_words, selected_style, news_context):

    base_prompt = ("""
        "Write a blog post in {style} style about {text}.
        The post should include an introduction, detailed main content with headers and bullet points,
        and a concise conclusion—all within approximately {number} words.
        The blog must distinctly reflect the {style} style throughout its language, tone, and structure.
        Emphasize the unique characteristics of {style} writing.
        Ensure that all terms used are clear, standard English words relevant to the topic and style, avoiding foreign or invented words.
        If relevant, seamlessly integrate the following recent news highlights into the narrative: {news_context}.
        Use proper Markdown formatting with headers, bullet points, **bold text**, and _italics_ as needed."""
                   )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful blog writing assistant. Your task is to write well-structured blogs using Markdown formatting wherever necessary."
            ),
            ("human", base_prompt)
        ]
    )

    chain = prompt | llm
    params = {
        "style": selected_style,
        "text": input_text,
        "number": no_words,
        "news_context": news_context
    }
    response = chain.invoke(params)
    return response.content


# Streamlit UI Configuration
st.set_page_config(
    page_title="Blog Generator",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Blog Generator 📝")

blog_topic = st.text_input("Enter the Blog Topic:")
no_words = st.slider("Select word count:", min_value=100,
                     max_value=2000, step=50)

writing_styles = [
    "Conversational", "Technical", "Literary", "Shakespearean",
    "J.K. Rowling-style", "Elon Musk-style", "Humorous", "Inspirational"
]
selected_style = st.selectbox(
    "Choose a writing style:", writing_styles + ["Custom"])

custom_style = ""
if selected_style == "Custom":
    custom_style = st.text_input("Enter your custom style:")
final_style = custom_style if selected_style == "Custom" and custom_style.strip(
) else selected_style

if st.button("Generate Blog"):
    if not blog_topic.strip():
        st.warning("Please enter a blog topic.")
    else:
        news_context = ""
        if NEWS_API_KEY:
            news_context = fetch_recent_news(blog_topic, NEWS_API_KEY)
        try:
            with st.spinner("Generating your blog..."):
                blog_content = generate_blog(
                    blog_topic, no_words, final_style, news_context)
                st.markdown(blog_content)
                st.success("Blog generated successfully!")

                # Export the blog as a Markdown file
                st.download_button(
                    label="Download Blog as Markdown",
                    data=blog_content,
                    file_name="blog_post.md",
                    mime="text/markdown"
                )
        except Exception as e:
            st.error("An error occurred while generating your blog.")
            st.error(f"Debug Info: {e}")
