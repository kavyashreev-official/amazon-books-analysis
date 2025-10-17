# 📚 Amazon Books Analysis with Visualizations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('bestsellers.csv')

# View basic information
print("🔹 First 5 rows:")
print(df.head(), "\n")

print("🔹 Shape of dataset:", df.shape)
print("\n🔹 Columns:", df.columns.tolist())
print("\n🔹 Summary statistics:")
print(df.describe(), "\n")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Rename columns for readability
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Convert data types
df["Price"] = df["Price"].astype(float)

# Author popularity (number of books)
author_counts = df['Author'].value_counts()
print("🔹 Top Authors:")
print(author_counts.head(10), "\n")

# Average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print("🔹 Average Rating by Genre:")
print(avg_rating_by_genre, "\n")

# Export results
author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

# -----------------------------
# 📊 VISUALIZATIONS
# -----------------------------

# 🎨 Seaborn style
sns.set(style="whitegrid", palette="pastel")

# ---------------------------------
# 📊 TOP 10 AUTHORS (Bar Chart)
# ---------------------------------

import matplotlib.pyplot as plt

# Get top 10 authors
plt.figure(figsize=(10,5))
author_counts.head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Bestselling Authors on Amazon")
plt.xlabel("Author")
plt.ylabel("Number of Books")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# 2️⃣ Average Rating by Genre
plt.figure(figsize=(6,4))
sns.barplot(x=avg_rating_by_genre.index, y=avg_rating_by_genre.values, palette="viridis")
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# 3️⃣ Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=20, kde=True, color='coral')
plt.title("Distribution of Book Prices")
plt.xlabel("Price ($)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 4️⃣ Ratings Over Years
plt.figure(figsize=(10,5))
sns.boxplot(x="Publication Year", y="Rating", data=df, palette="mako")
plt.title("Ratings Distribution Over Years")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
