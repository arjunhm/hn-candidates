import requests
from bs4 import BeautifulSoup as bs 
#from dotenv import load_dotenv
import logging

logger = logging.getLogger()

#load_dotenv()

class Scraper:

    def __init__(self, url):
        # general
        self.URL = url
        self.PROFILE_LINK = "https://news.ycombinator.com/user?id="
        
        # database
        self.table_name = None

        # scraped data
        self.scraped_data = None
        self.misc_data = None
        self.data = {}
        self.count = 0

    def dump(self, data, filename):
        with open(filename, 'w') as fp:
            fp.write(data)

    def load(self, filename):
        with open(filename) as fp:
            self.scraped_data = fp.read()

    def scrape_site(self):
        response = requests.get(self.URL)
        if response.status_code == 200:
            self.scraped_data = response.text
            self.dump(self.scraped_data, "hn.txt")
        else:
            logger.error(f"Failed to scrape url={url}")
    
    def extract_table_name(self, soup):
        href = self.URL.split("/")[-1]
        table_name = soup.find("a", href=href).text
        table_name = table_name.split("(")[-1]
        table_name = table_name.split(")")[0]
        table_name = "_".join(table_name.split())
        table_name = table_name.lower()
        return table_name

    def extract_remote(self, data):
        pass

    def extract_relocation(self, data):
        pass

    def extract_technologies(self, data):
        pass

    def extract_resume(self, data):
        pass

    def extract_email(self, data):
        pass

    def extract_linkedin(self, data):
        pass

    


    def extract(self):
        content = self.scraped_data
        soup = bs(content, "html.parser")
        table_name = self.extract_table_name(soup)
        self.table_name = table_name

        posts = soup.find_all("tr", class_="athing comtr")
        self.count = len(posts)

        for i in range(10):
            post = posts[i]
            print(f"\n---------------------\n\n")
            try:
                post_id = post["id"]
                post_link = f"https://news.ycombinator.com/item?id={post_id}"
            except Exception as e:
                logger.error(f"Error fetching post_id: {e}")
                continue
            print(f"{post_id=}")

            try:
                comment_div = post.select_one("div.commtext")
                links = [a["href"] for a in comment.find_all("a", href=True)]
                print(f"{links=}")

            except Exception as e:
                logger.error(f"content: {e}")
                continue

            comment = comment.find_all('p')
            if len(comment) > 0:
                comment_text = comment[0].text

            # author
            try:
                author_div = post.find("a", class_="hnuser")
                author_name = author_div.text
                author = {"name": author_name, "link": self.PROFILE_LINK + author_name}
            except Exception as e:
                logger.error(f"author: {e}")
                continue

            remote = self.extract_remote(comment)
            relocate
            
            self.data[post_id] = {
                "author": author,
                "text": comment_text,
                "remote": None,
                "relocate": None,
                "technologies": None,
                "resume": None,
                "email": None,
                "linkedin": None,
                "about": None,
                "links": links,
            }
            self.count += 1

            print(self.data[author_name])

            

    def run(self):
        #self.scrape_site()
        self.load("hn.txt")
        self.extract()


def main():
    url = "https://news.ycombinator.com/item?id=41709299"
    s = Scraper(url)
    s.run()

if __name__ == "__main__":
    main()
