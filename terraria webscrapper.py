from bs4 import BeautifulSoup
import pip._vendor.requests as requests

def scrapTerrariaWiki(query):
    
        # Get the page content
        page_to_scrape = requests.get("https://terraria.fandom.com/wiki/"+query)
        page_to_scrape.raise_for_status()  # Check for request errors
        
        
        # Parse the HTML content
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        for p in soup.select('p'):
                print(p.get_text(strip=True, separator='\n'))
                print('-' * 80)


        
# Call the 
search=input(print("PLease enter a topic to search on Terraria Wikipedia:"))
scrapTerrariaWiki(search)
