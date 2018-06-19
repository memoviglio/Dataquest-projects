import read
df = read.load_data()
#finding the count of every domain
print(df["url"].value_counts()[0:100])


