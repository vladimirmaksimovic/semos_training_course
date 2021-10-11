import Car from "./Car.js";

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
