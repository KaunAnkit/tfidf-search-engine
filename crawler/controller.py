from crawler.cleaner import parsed_data_text_cleaner
from crawler.featcher import url_data_featcher
from crawler.parser import file_parser


def url_input(base_url):


    try:
        data = url_data_featcher(base_url)
    except:
        return None
    
    data_1 = file_parser(data)

    data_2 = parsed_data_text_cleaner(data_1["Text"])

    data_1["Text"] = data_2
    data_1["url"] = base_url



    return data_1

