from bs4 import BeautifulSoup
import pip._vendor.requests as requests

def scrap_terraria_wiki(queries):
    base_url = "https://terraria.fandom.com/wiki/"
    
    for query in queries:
        print(f"Searching for: {query}")
        print("=" * 80)
        
        try:
            # Get the page content
            response = requests.get(base_url + query)
            response.raise_for_status()
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Get page title
            title = soup.find("span", class_="mw-page-title-main")
            print(f"Title: {title.text if title else 'No title found'}")
            print("-" * 80)
            
            # Get paragraphs and links
            for p in soup.select("p"):
                print(f"Paragraph: {p.get_text(strip=True, separator=' ')}")
                links = p.find_all("a", href=True)
                if links:
                    print("Links:")
                    for link in links:
                        print(f"- {link.get_text(strip=True)}: {link['href']}")
                print("-" * 80)
        except Exception as e:
            print(f"Error fetching data for {query}: {e}")
        print("\n" + "=" * 80 + "\n")

# Input: List of topics to search
search_queries = input("Enter topics to search, separated by commas: ").split(",")
scrap_terraria_wiki([query.strip() for query in search_queries])
