from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from ga import recommend_products

app = Flask(__name__)
app.secret_key = "secret123"  # 🔐 مهم لتفعيل session

# =========================
# تحميل البيانات
# =========================
users = pd.read_excel("data/users_clean.xlsx", engine="openpyxl")
products = pd.read_excel("data/products_clean.xlsx", engine="openpyxl")
ratings = pd.read_excel("data/ratings_clean.xlsx", engine="openpyxl")
behavior = pd.read_excel("data/behavior_clean.xlsx", engine="openpyxl")


# =========================
# دالة إضافة الصور حسب الفئة
# =========================
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


# =========================
# تسجيل الدخول
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["user_id"]

        # تخزين في session
        session["user_id"] = user_id

        # تحويل مع إظهار user_id في الرابط
        return redirect(url_for("home", user_id=user_id))

    return render_template("login.html")


# =========================
# الصفحة الرئيسية
# =========================
@app.route("/home")
def home():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    recommendations = recommend_products(
        int(user_id), users, products, ratings, behavior
    )

    # إضافة الصور
    recommendations = add_images(recommendations)

    return render_template(
        "home.html",
        recommendations=recommendations,
        user_id=user_id
    )


# =========================
# المنتجات
# =========================
@app.route("/products")
def products_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("products.html", user_id=user_id)


# =========================
# الفئات
# =========================
@app.route("/categories")
def categories_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("categories.html", user_id=user_id)


# =========================
# التواصل
# =========================
@app.route("/contact")
def contact_page():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = request.args.get("user_id") or session["user_id"]
    session["user_id"] = user_id

    return render_template("contact.html", user_id=user_id)


# =========================
# Refresh (تحديث التوصيات)
# =========================
@app.route("/refresh", methods=["POST"])
def refresh():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]

    recommendations = recommend_products(
        int(user_id), users, products, ratings, behavior
    )

    # إضافة الصور
    recommendations = add_images(recommendations)

    return render_template(
        "home.html",
        recommendations=recommendations,
        user_id=user_id
    )


# =========================
# تسجيل الخروج
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# =========================
# تشغيل التطبيق
# =========================
if __name__ == "__main__":
    app.run(debug=True)