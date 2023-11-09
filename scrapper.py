
from bs4 import BeautifulSoup
import requests
import fitz  # PyMuPDF

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



    def add_pdf_content_to_file(): #assuming that the file will be saved as my_file.pdf name 
        text = ""
        try:
            with fitz.open("pdf_files/my_file.pdf") as pdf_document:
                num_pages = pdf_document.page_count
                for page_num in range(num_pages):
                    page = pdf_document[page_num]
                    text += page.get_text()
            with open("data.txt", "w") as f:
                f.write(text)
        except Exception as e:
            print(f"Error: {e}")
            
            