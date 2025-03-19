# AI Blog Generator 📝

A Streamlit web application that leverages AI to generate customized blog posts with different writing styles and real-time news integration.

## Features

- **AI-Powered Content Creation**: Uses Meta's LLaMA 3.3 70B model via Groq's inference platform to generate high-quality blog content with ultra-low latency.
- **Multiple Writing Styles**: Choose from various preset styles:
  - Conversational
  - Technical
  - Shakespearean
  - Elon Musk-style
  - Custom style option
- **Real-time News Integration**: Automatically incorporates recent relevant news into your blog content
- **Adjustable Length**: Control the word count from 100 to 2000 words
- **Markdown Formatting**: Generated blogs include proper headers, bullet points, bold text, and italics
- **Export Functionality**: Download your generated blogs as Markdown files

## Prerequisites

- Python 3.x
- Groq API key
- News API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tapan2003/AI-Blog-Generator.git
cd ai-blog-generator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory with your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

## Dependencies

The application requires the following Python packages:
- groq
- streamlit
- requests
- langchain
- langchain-core
- langchain-groq
- python-dotenv

## Usage

1. Launch the application:
```bash
streamlit run app.py
```

2. In your web browser:
   - Enter your desired blog topic
   - Adjust the word count using the slider
   - Select a writing style or create a custom one
   - Click "Generate Blog"
   - Download your blog post as a Markdown file using the provided button

## How It Works

1. The application takes your blog topic, desired length, and writing style
2. If a News API key is provided, it fetches recent news related to your topic
3. It then uses the LLaMA 3.3 70B model via Groq to generate a well-structured blog post
4. The generated content incorporates proper Markdown formatting and recent news if available

## Getting API Keys

- **Groq API Key**: Sign up at [Groq](https://console.groq.com/login) to get your API key
- **News API Key**: Register at [News API](https://newsapi.org/register) for a free API key