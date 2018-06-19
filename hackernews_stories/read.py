import pandas as pd

# writing a function to return a dataframe with column names
def load_data():
    d = pd.read_csv("hn_stories.csv", names = ["submission_time","upvotes","url","headline"])
    #print(d.head())
    return d
# calling function from command line
if __name__ == "__main__":
    load_data()
    
    
    