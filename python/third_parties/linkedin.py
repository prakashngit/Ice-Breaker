import os
import requests 
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """
    Scrape information from Linkedin profiles, Manually scrape the information from the LinkedIn profile
    """

    if mock:
        linkedin_profile_url =  'https://gist.githubusercontent.com/prakashngit/540614a7dd8677490ab43200a07258d6/raw/340259de2641d69aff55538d9320f8675893aeac/Prakash.json'

        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint='https://nubela.co/proxycurl/api/v2/linkedin'
        header = {'Authorization': 'Bearer {}'.format(os.environ.get('PROXYCURL_API_KEY'))}
        response = requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=header, timeout=10)
    
    data = response.json()

    data = {
        k: v 
        for k, v in data.items() 
        if v not in ([], "", None) and k not in {"people_also_viewed", "certifications"} 
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url = 'https://www.linkedin.com/in/prakash-narayana-moorthy-522021b3/'
        )
    )