import pandas as pd

# Rest of the file go here...
df = pd.read_csv('bestsellers.csv')
# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

#Drop duplicates
df.drop_duplicates(inplace=True)

#Renaming columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Converting Data Types
df["Price"] = df["Price"].astype(float)

# Analyzing Author Popularity
author_counts = df['Author'].value_counts()
print(author_counts)

# Average Rating by Genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
