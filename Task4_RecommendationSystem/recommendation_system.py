import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
books = pd.read_csv("books.csv")

# Convert genres into vectors
cv = CountVectorizer()
vectors = cv.fit_transform(books["Genre"])

# Calculate similarity
similarity = cosine_similarity(vectors)

def recommend(book_name):
    if book_name not in books["Book"].values:
        print("Book not found!")
        return

    index = books[books["Book"] == book_name].index[0]

    distances = list(enumerate(similarity[index]))
    recommendations = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:4]

    print("\nRecommended Books:\n")

    for book in recommendations:
        print(
            books.iloc[book[0]]["Book"],
            "-",
            books.iloc[book[0]]["Genre"]
        )

# Display books with genres
print("\nAvailable Books:")
print(books[["Book", "Genre"]].to_string(index=False))

user_book = input("\nEnter a book you like: ")

recommend(user_book)