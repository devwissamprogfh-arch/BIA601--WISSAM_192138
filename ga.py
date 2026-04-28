import random

# عدد المنتجات في التوصية
N = 8


# ==================================================
# 1. Baseline Recommendation
# ==================================================
def basic_recommend(user_id, products, ratings, behavior):

    user_behavior = behavior[behavior["user_id"] == user_id]

    # مستخدم جديد
    if user_behavior.empty:
        top_products = (
            ratings.groupby("product_id")["rating"]
            .mean()
            .nlargest(N)
            .index
            .tolist()
        )

        return products[
            products["product_id"].isin(top_products)
        ].to_dict(orient="records")

    # الفئة المفضلة
    purchased = user_behavior[user_behavior["purchased"] == 1]

    if not purchased.empty:
        merged = purchased.merge(products, on="product_id")
        favorite_category = merged["category"].mode()[0]
    else:
        clicked = user_behavior[user_behavior["clicked"] == 1]

        if not clicked.empty:
            merged = clicked.merge(products, on="product_id")
            favorite_category = merged["category"].mode()[0]
        else:
            favorite_category = products["category"].mode()[0]

    # اختيار منتجات من نفس الفئة
    category_products = products[
        products["category"] == favorite_category
    ]

    avg_ratings = (
        ratings.groupby("product_id")["rating"]
        .mean()
        .reset_index()
    )

    final = category_products.merge(avg_ratings, on="product_id")

    final = final.sort_values(
        by="rating",
        ascending=False
    ).head(N)

    return final.to_dict(orient="records")


# ==================================================
# 2. Fitness Function (متطورة)
# ==================================================
def fitness(solution, user_id, products, ratings, behavior):

    score = 0

    user_behavior = behavior[behavior["user_id"] == user_id]

    # الفئة المفضلة
    if not user_behavior.empty:
        merged = user_behavior.merge(products, on="product_id")
        if not merged.empty:
            favorite_category = merged["category"].mode()[0]
        else:
            favorite_category = None
    else:
        favorite_category = None

    for product_id in solution:

        # التقييم
        r = ratings[
            ratings["product_id"] == product_id
        ]["rating"].mean()

        if not str(r) == "nan":
            score += r * 2

        # المشتريات
        purchases = behavior[
            (behavior["product_id"] == product_id) &
            (behavior["purchased"] == 1)
        ].shape[0]

        score += purchases * 3

        # الفئة
        product_category = products[
            products["product_id"] == product_id
        ]["category"].values[0]

        if favorite_category and product_category == favorite_category:
            score += 5

        # سلوك المستخدم
        user_interaction = user_behavior[
            user_behavior["product_id"] == product_id
        ]

        if not user_interaction.empty:
            score += 2
            if user_interaction["clicked"].values[0] == 1:
                score += 3
            if user_interaction["purchased"].values[0] == 1:
                score += 5

    return score


# ==================================================
# 3. Genetic Algorithm (Hybrid)
# ==================================================
def recommend_products(user_id, users, products, ratings, behavior):

    product_ids = products["product_id"].tolist()

    # =========================
    # الحل الأولي (Baseline)
    # =========================
    base_solution = basic_recommend(user_id, products, ratings, behavior)
    base_ids = [item["product_id"] for item in base_solution]

    while len(base_ids) < N:
        base_ids.append(random.choice(product_ids))

    base_ids = base_ids[:N]

    # =========================
    # إنشاء Population
    # =========================
    population = [base_ids]

    for _ in range(9):
        new_solution = base_ids.copy()
        idx = random.randint(0, N - 1)
        new_solution[idx] = random.choice(product_ids)
        population.append(new_solution)

    # =========================
    # التطور
    # =========================
    for _ in range(20):

        population = sorted(
            population,
            key=lambda x: fitness(x, user_id, products, ratings, behavior),
            reverse=True
        )

        new_population = population[:2]

        while len(new_population) < 10:
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])

            cut = random.randint(1, N - 1)
            child = parent1[:cut] + parent2[cut:]

            if random.random() < 0.2:
                child[random.randint(0, N - 1)] = random.choice(product_ids)

            new_population.append(child)

        population = new_population

    best = population[0]

    return products[
        products["product_id"].isin(best)
    ].to_dict(orient="records")