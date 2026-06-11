from bs4 import BeautifulSoup
import warnings

# Suppress XML parsing warnings
warnings.filterwarnings("ignore", category=UserWarning)

def file_parser(data):
    try:
        # Try parsing as HTML first
        soup = BeautifulSoup(data, "html.parser")
    except Exception as e:
        # If HTML parsing fails, try with lxml if available, otherwise use html.parser with error handling
        try:
            soup = BeautifulSoup(data, "lxml-xml")
        except:
            try:
                soup = BeautifulSoup(data, "lxml")
            except:
                # If all else fails, return empty data
                return {"Title": "", "Links": [], "Text": ""}
    
    parsed_data = {"Title" : "","Links" : [],"Text": ""}
    data_links = [] 
    
    try:
        text = soup.get_text()
        parsed_data["Text"] = text

        title = soup.find('title')
        
        if title != None:
            parsed_data["Title"] = title.text
        else:
            parsed_data["Title"] = ""

        for a in soup.find_all('a', href=True):
            data_links.append(a['href'])

        parsed_data["Links"] = data_links
    except:
        # If parsing fails, return empty parsed data
        pass
    
    return parsed_data

        