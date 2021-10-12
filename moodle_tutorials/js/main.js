// imports
import Car from "./Car.js";

/**
 * create navigation
 */

// array with link names
const navLinks = ["Home", "Send", "Recive", "CSS position", "CSS flex"];

// create navigation elements with template literals

/* const nav = `
  <ul>
  <li><a href="#">${navLinks[0]}</a></li>
  <li>/</li>
  <li><a href="./pages/01-send.html">${navLinks[1]}</a></li>
  <li>/</li>
  <li><a href="./pages/02-receive.html">${navLinks[2]}</a></li>
  <li>/</li>
  <li><a href="./pages/03-css_poistion.html">${navLinks[3]}</a></li>
  <li>/</li>
  <li><a href="./pages/04-css_flex.html">${navLinks[4]}</a></li>
  </ul>
`; */

// create navigation with createElement() method

const headerSection = document.querySelector("#header-section");
const navContainer = document.createElement("nav");
const ulNav = document.createElement("ul");

headerSection.append(navContainer);
navContainer.append(ulNav);

/* const navContainer = document.querySelector("#main-nav");
console.log("Nav container => ", navContainer); */
//navContainer.innerHTML = nav;

/* navLinks.forEach((link) => {
  const li = document.createElement("li");
  const a = document.createElement("a");

  a.innerText = link;
  li.append(a);
  ulNav.append(li);
}); */

// create navigation from object

const navObj = {
  "index.html": "Home",
  "01-send.html": "Send",
  "02-receive.html": "Receive",
  "03-css_poistion.html": "CSS position",
  "04-css_flex.html": "CSS flex",
};

for (const key in navObj) {
  const li = document.createElement("li");
  const a = document.createElement("a");

  a.setAttribute(
    "href",
    key === "index.html" ? "index.html" : "./pages/" + key
  );
  a.innerText = navObj[key];
  li.append(a);
  ulNav.append(li);
}

// play with objectss

/* const punto = new Car("Fiat", "Punto", 2001, 5, true, true, "automatic");
const bravo = new Car("Fiat", "Bravo", 2001, 3, true, false, "manual");
const grandePunto = new Car(
  "Fiat",
  "Grande Punto",
  2009,
  5,
  true,
  false,
  "automatic"
);
const evo = new Car("Fiat", "EVO", 2011, 5, true, true, "automatic"); */
//const punto = new Car("Fiat", "Punto", 2001, 5, true, false, "automatic");

const cars = [
  new Car("Fiat", "Punto", 2001, 5, true, true, "automatic"),
  new Car("Fiat", "Bravo", 2001, 3, true, false, "manual"),
  new Car("Fiat", "Grande Punto", 2009, 5, true, false, "automatic"),
  new Car("Fiat", "EVO", 2011, 5, true, true, "automatic"),
];

/**
 * AJAX
 *
 * Create XMLHttpRequest
 * Open new connection, using GET request on the URL endpoint
 * Access JSON data
 * Send request
 *
 * API root endpoint:  https://swapi.dev/api/
 */

// get root element
const root = document.querySelector("#root");

const request = new XMLHttpRequest();

request.open("GET", "https://swapi.dev/api/starships/", true);

request.onload = function () {
  const data = JSON.parse(this.response);
  ///console.log("response data => ", data); // object, not array of objects

  if (request.status >= 200 && request.status < 400) {
    //console.log("Array of results in data object => ", data.results); // array of objects
    // results are divided in pages, 10 per page

    const starships = data.results;
    //console.log("Starships array => ", starships);

    // loop through array
    starships.forEach((starship) => {
      console.log(starship.model);

      // card
      const card = document.createElement("div");
      card.className = "card-container";

      // card header
      const cardHeader = document.createElement("h3");
      cardHeader.className = "card-header";
      cardHeader.textContent = starship.name;

      // card body
      const cardBody = document.createElement("div");
      cardBody.className = "card-body";

      const ul = document.createElement("ul");

      // loop throug object
      for (const prop in starship) {
        const li = document.createElement("li");
        li.innerHTML = `${prop}: ${starship[prop]}`;
        ul.appendChild(li);
      }

      root.appendChild(card);
      card.appendChild(cardHeader);
      card.appendChild(cardBody);
      cardBody.appendChild(ul);
    });
  }
};

request.send();
