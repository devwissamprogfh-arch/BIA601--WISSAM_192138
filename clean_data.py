import pandas as pd

# 1. Read data---------------
users = pd.read_excel("data/users.xlsx")  
products = pd.read_excel("data/products.xlsx")  
ratings = pd.read_excel("data/ratings.xlsx")  
behavior = pd.read_excel("data/behavior.xlsx")

#*************************************************
# 2. Clean users data--------------
users = users.drop_duplicates()  # Remove duplicate rows in users data
users = users.dropna()  # Remove rows with missing values

# Ensure age is within a logical range between 10 and 100
if "age" in users.columns:
    users = users[(users["age"] >= 10) & (users["age"] <= 100)]  

#**************************************************
# 3. Clean products data--------------------------
products = products.drop_duplicates() 
products = products.dropna()

# Remove products with invalid price <0
if "price" in products.columns:
    products = products[products["price"] > 0]

#*************************************************
# 4. Clean ratings data
ratings = ratings.drop_duplicates()
ratings = ratings.dropna()

# Ensure rating is between 1 and 5 only
if "rating" in ratings.columns: 
    ratings = ratings[(ratings["rating"] >= 1) & (ratings["rating"] <= 5)]

#*************************************************
# 5. Clean user behavior data
behavior = behavior.drop_duplicates()
behavior = behavior.dropna()

# Convert values to binary (0 or 1)
for col in ["viewed", "clicked", "purchased"]:
    if col in behavior.columns: 
        behavior[col] = behavior[col].apply(lambda x: 1 if x > 0 else 0)

#*************************************************
# 6. Save cleaned data
users.to_excel("data/users_clean.xlsx", index=False)  
products.to_excel("data/products_clean.xlsx", index=False) 
ratings.to_excel("data/ratings_clean.xlsx", index=False)
behavior.to_excel("data/behavior_clean.xlsx", index=False)

print("Data Cleaning Completed Successfully!")