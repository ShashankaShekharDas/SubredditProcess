import sys
import csv


class Read_subreddit:
    def __init__(self, token):
        self.reddit_token = token
        # Creating the header
        self.headers = {'User-Agent': 'MyBot/0.0.1'}
        self.headers = {**self.headers, **{'Authorization': f"bearer {self.reddit_token}"}}

    def read_csv(self):
        with open('/home/airflow_exec/airflow-medium/data/subreddit.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)


def main():
    # Argument 1 is the token
    print(sys.argv[1])
    read_subreddit = Read_subreddit(sys.argv[1])
    read_subreddit.read_csv()


if __name__ == "__main__":
    main()
