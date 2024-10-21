import os
from dotenv import load_dotenv

load_dotenv()

from tools.tools import get_profile_url_tavily, get_profile_url_duckduckgo, get_profile_url_serapi

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool 
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

def lookup(name: str) -> str:
    """ Return the linkedin URL for Person whose name is given as input """

    llm_openai = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    llm_perplexity = ChatPerplexity(temperature=0, 
                                    model='llama-3.1-sonar-large-128k-chat')
    llm_mistral = ChatOllama(model="mistral") #pretty bad. 


    template = """
        Search for the linkedin profiles of {name_of_person}, filtering for those with exact name match. From the search results, extract and return the linkedin URL. The URL should have the following format: https://www.linkedin.com/<profile-id>. If multiple URLs are found, return the best match.
        Remember to return just the URL, remove any extra words or characters surrounding the URL. 
        """

    promt_template = PromptTemplate(input_variables=["name_of_person"], template=template)

    tools_for_agent = [
        Tool(
            name = "Crawl Google for linkedin profile page",
            func=get_profile_url_serapi,
            description="useful for when you need to get Linkedin page URL for a person"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm_openai, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

    result = agent_executor.invoke(input={"input" : promt_template.format(name_of_person=name)})
    
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__=="__main__":
    linkedin_url = lookup(name="Prakash Narayana Moorthy")
    print(linkedin_url)