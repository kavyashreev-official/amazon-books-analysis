# 📚 Amazon Books Analysis with Visualizations

## 🧠 Overview
This project analyzes Amazon's bestselling books dataset to uncover insights such as:
- Which authors appear most frequently on the bestseller list  
- Average ratings by genre  
- Price distribution across books  
- Rating trends over the years  

The analysis uses **Python**, **Pandas**, **Matplotlib**, and **Seaborn** for data processing and visualization.

---

## 📂 Dataset
The dataset used is **`bestsellers.csv`**, which contains the following columns:

| Column Name     | Description |
|-----------------|--------------|
| Name            | Title of the book |
| Author          | Author of the book |
| User Rating     | Average user rating (0–5) |
| Reviews         | Number of user reviews |
| Price           | Price of the book (in USD) |
| Year            | Publication year |
| Genre           | Type of book (Fiction / Non-Fiction) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/amazon-books-analysis.git
cd amazon-books-analysis
````

### 2️⃣ Install dependencies

Make sure you have Python 3 installed, then install required libraries:

```bash
pip install pandas matplotlib seaborn
```

### 3️⃣ Add the dataset

Place your **`bestsellers.csv`** file in the project folder.

---

## 🚀 How to Run

Run the Python script:

```bash
python amazon_books_analysis.py
```

Or, if using VS Code:

1. Open the folder in VS Code
2. Open the integrated terminal
3. Run:

   ```bash
   python amazon_books_analysis.py
   ```

---

## 📊 Visualizations

The script generates several insightful charts:

1. **Top 10 Bestselling Authors**
   Bar chart showing authors with the highest number of bestselling books.

2. **Average Rating by Genre**
   Comparison of mean user ratings for Fiction vs Non-Fiction books.

3. **Price Distribution**
   Histogram showing how book prices are distributed.

4. **Ratings Over Years**
   Boxplot showing how ratings vary by publication year.

---

## 🧾 Output Files

The analysis also exports summary CSV files:

* `top_authors.csv` → Top 10 bestselling authors
* `avg_rating_by_genre.csv` → Average rating per genre

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** Pandas, Matplotlib, Seaborn
* **Environment:** VS Code / Jupyter Notebook

---

## 📈 Sample Insights

* Non-Fiction books tend to have slightly higher ratings.
* A few authors dominate the bestseller charts.
* Most books are moderately priced between $10–$20.

---

## 👩‍💻 Author

**Kavya Shree**
📧 Feel free to connect or give feedback via GitHub!
⭐ If you like this project, consider starring the repository!

---

## 🪪 License

This project is open source and available under the [MIT License](LICENSE).

```
