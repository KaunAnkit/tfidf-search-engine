from bs4 import BeautifulSoup


def file_parser(data):
    soup = BeautifulSoup(data, "html.parser")
    
    parsed_data = {"Title" : "","Links" : [],"Text": ""}
    data_links = [] 
    
    text = soup.get_text()

    parsed_data["Text"] = text

    title = soup.find('title')
    
    if title != None:
        parsed_data["Title"] = title.text
    else:
        parsed_data["Title"] = ""

    for a in soup.find_all('a',href ='True'):
        data_links.append(a['href'])

    parsed_data["Links"] = data_links
    
    return parsed_data

        