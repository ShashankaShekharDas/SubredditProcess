import sys
import csv

import requests


class Read_subreddit:
    def __init__(self, token):
        self.reddit_token = token
        self.subreddit_csv_location = "/home/airflow_exec/airflow-medium/data/subreddit.csv"
        # Creating the header
        self.headers = {'User-Agent': 'MyBot/0.0.1'}
        self.headers = {**self.headers, **{'Authorization': f"bearer {self.reddit_token}"}}
        # Parameters for getting posts
        self.params = {"limit": -1}
        self.url = "https://oauth.reddit.com/r/{subreddit_name}/new"
        self.posts_contents = {}

    def set_requests_config(self):
        requests.get("https://oauth.reddit.com/api/v1/me", headers=self.headers)

    def get_posts_subreddit(self):
        with open(self.subreddit_csv_location, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for rows in reader:
                subreddit_url = self.url.format(subreddit_name=rows["subreddit_name"])
                if rows["start_post"] == "none":
                    # If none, get all historical posts
                    res = requests.get(subreddit_url, headers=self.headers,params=self.params).json()
                    full_name = ""
                    self.posts_contents[rows["subreddit_name"]] = {}
                    print(len(res["data"]["children"]))
                    for post in res["data"]["children"]:
                        fullname = post["kind"] + "_" + post["data"]["id"]
                        self.posts_contents[rows["subreddit_name"]]["title"] = post["data"]["title"]
                        self.posts_contents[rows["subreddit_name"]]["author_fullname"] = post["data"]["author_fullname"]
                        self.posts_contents[rows["subreddit_name"]]["selftext"] = post["data"]["selftext"]
            return len(self.posts_contents["cscareerquestionsEU"]["title"])


def main():
    # Argument 1 is the token
    read_subreddit = Read_subreddit(sys.argv[1])
    read_subreddit.set_requests_config()
    print(read_subreddit.get_posts_subreddit())


if __name__ == "__main__":
    main()
