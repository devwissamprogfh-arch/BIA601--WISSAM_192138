// =======================
// Categories Data
// =======================
const categories = [
    {name:"Clothes", image:"images/clothes.jpg"},
    {name:"Electronics", image:"images/electronics.jpg"},
    {name:"Sports", image:"images/sports.jpg"},
    {name:"Home", image:"images/home.png"},
    {name:"Perfumes", image:"images/per.png"},
    {name:"Toys", image:"images/toys.png"},
    {name:"Books", image:"images/book.png"}
];

// =======================
// Render Categories
// =======================
const container = document.getElementById("categories-container");

categories.forEach(cat => {
    container.innerHTML += `
        <div class="cat-card" onclick="goToCategory('${cat.name}')">
            <img src="${cat.image}">
            <h3>${cat.name}</h3>
        </div>
    `;
});

// =======================
// Click Function (optional)
// =======================
function goToCategory(category){
    alert("Selected Category: " + category);
    // لاحقًا يمكن ربطها بصفحة المنتجات
    // window.location.href = "products.html?category=" + category;
}