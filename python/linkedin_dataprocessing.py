from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatPerplexity


from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_loopup_agent
from output_parsers import summary_parser

import os

def ice_beak_with(name: str) -> str:
    linkedin_url= linkedin_loopup_agent(name = name)
    print(linkedin_url)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)


    summary_template = """
        given the Linkedin information {information} about a persion, I want you to create :
        1. A short summary
        2. two interesting facts about them. Please only use the linkedin information provided to create both the summary and the two interesting facts.

    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
                                             partial_variables={"format_instructions" : summary_parser.get_format_instructions()})
                                            # note that unlike input variables, partial variable is full defined here
                                            # this is becuase the variable in text is static, and independent of the specific invocation of the chain. The term partial variables could have
                                            # been instead named as static variables, and input variable as run time variables.


    llm_perplexity = ChatPerplexity(temperature=0, 
                                    model='llama-3.1-sonar-large-128k-chat') # good for this task
    llm_openai = ChatOpenAI(temperature=0, model="gpt-4o-mini")  # very good for this task
    
    chain = summary_prompt_template | llm_perplexity | summary_parser 
    
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
    
if __name__=='__main__':
    load_dotenv()
    print('Ice Breaker Enter!')
    ice_beak_with(name = "Sundar Pichai")
       