
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from serpapi import search as GoogleSearch

from dotenv import load_dotenv
import os

def get_profile_url_tavily(search_string: str):
    """Carries out a google search for search string using Tavily. For example if you want to 
    search for a linkedin profile of a person, defined search string as [search for linkedin
    profile of <person name>]"""
    search = TavilySearchResults(max_results=5)
    res = search.run(f"{search_string}")
    return res

def get_profile_url_duckduckgo(search_string : str):
    """Carries out a google search for search string using DuckDuckGo. For example if you want to 
    search for a linkedin profile of a person, defined search string as [search for linkedin
    profile of <person name>]"""

    search = DuckDuckGoSearchAPIWrapper()
    results = search.results(f"{search_string}", max_results=50)
    formatted_results = [
        {"title": result["title"],
         "url": result["link"],
         "content": result["snippet"]
         } for result in results if "linkedin.com" in result["link"].lower()
    ]

    return formatted_results


def get_profile_url_serapi(search_string : str):
    params = {
        "api_key": f"{os.environ.get("SERP_API_KEY")}",
        "engine": "google",
        "q": f"{search_string}",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.data
    formatted_results = [
        {"title": result["title"],
         "url": result["link"],
         "content": result["snippet"]
         } for result in results["organic_results"] if "linkedin.com" in result["link"].lower()
    ]

    return formatted_results
        



if __name__=="__main__":
    load_dotenv()
    print(get_profile_url_serapi("Prakash Narayana Moorthy linkedin profile"))
