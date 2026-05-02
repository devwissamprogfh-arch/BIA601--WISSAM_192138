from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from ga import recommend_products

app = Flask(__name__)
app.secret_key = "secret123"  # Required to enable session handling

#*************************************************
# Load datasets
users = pd.read_excel("data/users_clean.xlsx", engine="openpyxl")
products = pd.read_excel("data/products_clean.xlsx", engine="openpyxl")
ratings = pd.read_excel("data/ratings_clean.xlsx", engine="openpyxl")
behavior = pd.read_excel("data/behavior_clean.xlsx", engine="openpyxl")


#*************************************************
# Function to assign images based on category
def add_images(recommendations):
    category_images = {
        "Clothes": "images/clothes.jpg",
        "Electronics": "images/electronics.jpg",
        "Sports": "images/sports.jpg",
        "Home": "images/home.png",
        "Perfumes": "images/per.png",
        "Toys": "images/toys.png",
        "Books": "images/book.png"
    }

    for item in recommendations:
        item["image"] = category_images.get(item["category"], "images/store.jpg")

    return recommendations


#*************************************************
# Login route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["user_id"]

        # Store user_id in session
        session["user_id"] = user_id

        # Redirect to home page with user_id in URL
        return redirect(url_for("home", user_id=user_id))

    return render_template("login.html")


#*************************************************
# Home page
@app.route("/home")
def home():

    # Check if user is logged in
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    # Generate recommendations
    recommendations = recommend_products(
        int(user_id), users, products, ratings, behavior
    )

    # Add images to recommendations
    recommendations = add_images(recommendations)

    return render_template(
        "home.html",
        recommendations=recommendations,
        user_id=user_id
    )


#*************************************************
# Products page
@app.route("/products")
def products_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("products.html", user_id=user_id)


#*************************************************
# Categories page
@app.route("/categories")
def categories_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("categories.html", user_id=user_id)


#*************************************************
# Contact page
@app.route("/contact")
def contact_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("contact.html", user_id=user_id)


#*************************************************
# Refresh recommendations
@app.route("/refresh", methods=["POST"])
def refresh():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    # Generate new recommendations
    recommendations = recommend_products(
        int(user_id), users, products, ratings, behavior
    )

    # Add images
    recommendations = add_images(recommendations)

    return render_template(
        "home.html",
        recommendations=recommendations,
        user_id=user_id
    )


#*************************************************
# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


#*************************************************
# Run the application
if __name__ == "__main__":
    app.run(debug=True)
