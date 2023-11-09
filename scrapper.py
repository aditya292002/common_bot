
from bs4 import BeautifulSoup
import requests

class read_content:    
    def scrape_website(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove header and nav tags
        for tag in soup(['header', 'nav', 'footer']):
            tag.decompose()

        # Find all heading, paragraph, table, and list tags
        tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'table', 'ul', 'ol'])

        # Extract the text from each tag and remove leading/trailing whitespace
        content = [tag.get_text().strip() for tag in tags]

        # Write the content to data.txt, skipping empty lines
        with open('data.txt', 'w') as f:
            for item in content:
                if item:  # skip empty lines
                    f.write("%s\n" % item)

        return content

    def 
url = 'https://takeuforward.org/computer-network/layers-of-osi-model/'  # replace with your URL
content = scrape_website(url)