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
        self.params = {"limit": 20}
        self.url = "https://oauth.reddit.com/r/{subreddit_name}/new"
        self.posts_title = {}

    def set_requests_config(self):
        requests.get("https://oauth.reddit.com/api/v1/me", headers=self.headers)

    def get_posts_subreddit(self):
        with open(self.subreddit_csv_location, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for rows in reader:
                subreddit_url = self.url.format(subreddit_name=rows["subreddit_name"])
                res = requests.get(subreddit_url, headers=self.headers, params=self.params).json()
                full_name = ""
                self.posts_title[rows["subreddit_name"]] = []
                for post in res["data"]["children"]:
                    fullname = post["kind"] + "_" + post["data"]["id"]
                    self.posts_title[rows["subreddit_name"]].append(post["data"]["title"])
            return self.posts_title


def main():
    # Argument 1 is the token
    read_subreddit = Read_subreddit(sys.argv[1])
    read_subreddit.set_requests_config()
    print(read_subreddit.get_posts_subreddit())


if __name__ == "__main__":
    main()
