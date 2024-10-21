# LinkedIn Ice Breaker

LinkedIn Ice Breaker is a Python application that helps you quickly gather and summarize information about a person from their LinkedIn profile. It's designed to prepare you for meetings, interviews, or networking events by providing a concise summary and interesting facts about your contact. 

This project is part of the exercises for the LangChain- Develop LLM powered applications with LangChain course by Eden Marco, and is available via Udemy [here](https://www.udemy.com/course/langchain/learn/). Marco's original project is available [here](https://github.com/emarco177/ice_breaker). Note that Marco's version uses Flask instead of Streamlit for the web interface, and uses Tavily instead of SerpApi for the LinkedIn profile URL lookup. I forked Marco's repo and modified it to use Streamlit and SerpApi, and added some additional exercises as well. For anyone looking to learn LangChain, I highly recommend the course!


## Features

- Automatic LinkedIn profile URL lookup based on a person's name
- LinkedIn profile scraping
- AI-powered summary generation, including:
  - A short summary of the person's professional background
  - Two interesting facts about the person
- Profile picture URL retrieval

## Technologies Used

- Python 3.x
- LangChain
- OpenAI's GPT models
- Custom LinkedIn scraping module
- Streamlit for the web interface
- SerpApi for the LinkedIn profile URL lookup


## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PROXYCURL_API_KEY=your_proxycurl_api_key
   SERP_API_KEY=your_serp_api_key

   ```
3. Run the application:
   ```
   streamlit run app.py
   ```

Then, follow the instructions in the web interface to input a person's name and generate their LinkedIn profile summary.

## License

This project is licensed under the Apache License, Version 2.0 (APL 2.0). See the [LICENSE](LICENSE) file for details.