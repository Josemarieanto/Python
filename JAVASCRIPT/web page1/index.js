import breakfastRecipes from "./mock-data/breakfast.js";
import lunchRecipes from "./mock-data/lunch.js";
import dinnerRecipes from "./mock-data/dinner.js";
const doc = document;

function CardItem(data) {
    const { type,title, description, image,price,rating } = data;
    return `<section class="card-item">
              <img class="image" src="${image}" width="100%" alt="img">
              <article class="content">
                <p class="title">${type}</p>
                  <p>${title}</p>
                  <p class="description">${description}</p>
                  <article class="details">
                          <p class="price">Price - ${price}</p>
                          <p class="rating">Rating - ${rating}</p>
                  </article>
              </article>
          </section>`;
        }

const breakfastlists = doc.querySelector(".breakfast");
const lunchlists = doc.querySelector(".lunch");
const dinnerlists = doc.querySelector(".dinner");

breakfastlists.innerHTML = breakfastRecipes.map(CardItem).join("");
lunchlists.innerHTML = lunchRecipes.map(CardItem).join("");
dinnerlists.innerHTML = dinnerRecipes.map(CardItem).join("");