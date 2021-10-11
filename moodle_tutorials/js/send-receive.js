// get display element
const dataContainer = document.querySelector("#data");

// fetch and store data results from URL
const urlSearchResults = new URLSearchParams(window.location.search);

// loop through results
urlSearchResults.forEach((value, name) => {
  // append received data in display element
  dataContainer.append(`${name}: ${value}`);
  // create br element for visual separation
  dataContainer.append(document.createElement("br"));
});
