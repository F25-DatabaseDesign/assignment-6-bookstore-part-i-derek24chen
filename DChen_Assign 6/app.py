
from flask import Flask, render_template

app = Flask(__name__)

# -----------------------
# Data: Categories & Books
# -----------------------

categories = [
    {"id": 1, "name": "Biographies"},
    {"id": 2, "name": "Music Theory"},
    {"id": 3, "name": "Sports"},
    {"id": 4, "name": "Food Recipes"}
]

books = [
    # Biographies
    {"title": "Becoming", "author": "Michelle Obama", "ISBN": "13-9781524763138", "price": 11.99, "categoryId": 1},
    {"title": "Steve Jobs", "author": "Walter Isaacson", "ISBN": "13-9781451648539", "price": 12.49, "categoryId": 1},
    {"title": "Elon Musk: Tesla, SpaceX", "author": "Ashlee Vance", "ISBN": "13-9780062301253", "price": 13.99, "categoryId": 1},
    {"title": "Alexander Hamilton", "author": "Ron Chernow", "ISBN": "13-9780143034759", "price": 14.95, "categoryId": 1},

    # Music Theory
    {"title": "Music Theory for Dummies", "author": "Michael Pilhofer", "ISBN": "13-9781118991322", "price": 19.99, "categoryId": 2},
    {"title": "The Study of Orchestration", "author": "Samuel Adler", "ISBN": "13-9780393935556", "price": 36.99, "categoryId": 2},
    {"title": "Harmony and Voice Leading", "author": "Edward Aldwell", "ISBN": "13-9780020130869", "price": 29.99, "categoryId": 2},
    {"title": "Jazz Theory Book", "author": "Mark Levine", "ISBN": "13-9781883217117", "price": 23.50, "categoryId": 2},

    # Sports
    {"title": "The Mamba Mentality", "author": "Kobe Bryant", "ISBN": "13-9780374201234", "price": 17.99, "categoryId": 3},
    {"title": "Open: An Autobiography", "author": "Andre Agassi", "ISBN": "13-9780307388408", "price": 16.50, "categoryId": 3},
    {"title": "Relentless", "author": "Tim Grover", "ISBN": "13-9781476714202", "price": 15.95, "categoryId": 3},
    {"title": "Moneyball", "author": "Michael Lewis", "ISBN": "13-9780393057654", "price": 14.99, "categoryId": 3},

    # Food Recipes
    {"title": "Salt, Fat, Acid, Heat", "author": "Samin Nosrat", "ISBN": "13-9781476753836", "price": 24.99, "categoryId": 4},
    {"title": "The Joy of Cooking", "author": "Irma Rombauer", "ISBN": "13-9780743246264", "price": 22.95, "categoryId": 4},
    {"title": "Cravings", "author": "Chrissy Teigen", "ISBN": "13-9781101903919", "price": 19.95, "categoryId": 4},
    {"title": "The Food Lab", "author": "J. Kenji López-Alt", "ISBN": "13-9780393081086", "price": 29.99, "categoryId": 4},
]


# -----------------------
# Routes
# -----------------------

@app.route("/")
def home():
    # Home page shows description + list of categories
    return render_template("index.html", categories=categories)


@app.route("/category/<int:category_id>")
def category_page(category_id):
    # Find selected category
    selected = next((c for c in categories if c["id"] == category_id), None)
    if selected is None:
        # Unknown category, show error page
        return render_template("error.html", message="Category not found."), 404

    # Filter books for this category
    filtered_books = [b for b in books if b["categoryId"] == category_id]

    return render_template(
        "category.html",
        categories=categories,
        books=filtered_books,
        selected_category_id=category_id,
        selected_category_name=selected["name"],
    )


if __name__ == "__main__":
    # Debug=True is fine for EdStem / development
    app.run(debug=True)
