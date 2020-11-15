from bs4 import BeautifulSoup

def scrape_landing():
    html_doc = open('./html/landing.html', 'r')
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title.string)

    # find the search box
    search_input = soup.find_all(placeholder="Search for a dataset or explore an app...")
    print(search_input)


scrape_landing()