// =======================
// Category Images
// =======================
const categoryImages = {
    Clothes: "/static/images/clothes.jpg",
    Electronics: "/static/images/electronics.jpg",
    Sports: "/static/images/sports.jpg",
    Home: "/static/images/home.png",
    Perfumes: "/static/images/per.png",
    Toys: "/static/images/toys.png",
    Books: "/static/images/book.png"
};

// =======================
// Dummy Products Data (30)
// =======================
const products = [
{product_id:101, name:"T-Shirt", category:"Clothes", price:29.99, rating:4.5},
{product_id:102, name:"Smartphone", category:"Electronics", price:199.99, rating:4.7},
{product_id:103, name:"Football", category:"Sports", price:59.99, rating:4.3},
{product_id:104, name:"Sofa", category:"Home", price:299.99, rating:4.6},
{product_id:105, name:"Perfume X", category:"Perfumes", price:49.99, rating:4.4},
{product_id:106, name:"Novel Book", category:"Books", price:19.99, rating:4.8},
{product_id:107, name:"Toy Car", category:"Toys", price:24.99, rating:4.2},

{product_id:108, name:"Jacket", category:"Clothes", price:39.99, rating:4.1},
{product_id:109, name:"Laptop", category:"Electronics", price:899.99, rating:4.9},
{product_id:110, name:"Basketball", category:"Sports", price:29.99, rating:4.3},

{product_id:111, name:"Table", category:"Home", price:120.99, rating:4.5},
{product_id:112, name:"Perfume Y", category:"Perfumes", price:59.99, rating:4.6},
{product_id:113, name:"Kids Toy", category:"Toys", price:19.99, rating:4.2},
{product_id:114, name:"Science Book", category:"Books", price:25.99, rating:4.7},

{product_id:115, name:"Jeans", category:"Clothes", price:49.99, rating:4.4},
{product_id:116, name:"Headphones", category:"Electronics", price:79.99, rating:4.6},
{product_id:117, name:"Tennis Racket", category:"Sports", price:89.99, rating:4.3},
{product_id:118, name:"Lamp", category:"Home", price:35.99, rating:4.2},

{product_id:119, name:"Perfume Z", category:"Perfumes", price:44.99, rating:4.5},
{product_id:120, name:"Story Book", category:"Books", price:18.99, rating:4.6},
{product_id:121, name:"Toy Robot", category:"Toys", price:29.99, rating:4.3},

{product_id:122, name:"Shirt", category:"Clothes", price:27.99, rating:4.2},
{product_id:123, name:"Tablet", category:"Electronics", price:299.99, rating:4.7},
{product_id:124, name:"Gym Equipment", category:"Sports", price:149.99, rating:4.4},
{product_id:125, name:"Chair", category:"Home", price:65.99, rating:4.3},

{product_id:126, name:"Luxury Perfume", category:"Perfumes", price:89.99, rating:4.8},
{product_id:127, name:"Children Book", category:"Books", price:15.99, rating:4.5},
{product_id:128, name:"Puzzle Toy", category:"Toys", price:14.99, rating:4.1},

{product_id:129, name:"Hoodie", category:"Clothes", price:54.99, rating:4.6},
{product_id:130, name:"Camera", category:"Electronics", price:499.99, rating:4.9}
];

// =======================
// Render Function
document.addEventListener("DOMContentLoaded", function () {

    const container = document.getElementById("products-container");

    products.forEach(item => {

        const image = categoryImages[item.category];

        container.innerHTML += `
            <div class="card">
                <img src="${image}">
                <div class="card-body">
                    <h3>${item.name}</h3>
                    <p>Category: ${item.category}</p>
                    <p>ID: ${item.product_id}</p>
                    <p class="price">$${item.price}</p>
                    <p>⭐ ${item.rating}</p>
                    <button class="btn small">Add to Cart</button>
                </div>
            </div>
        `;
    });

});