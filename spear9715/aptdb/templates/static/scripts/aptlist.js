// Function to redirect to a URL
function redirectTo(url) {
  // This function redirects the user to the specified URL by setting the window location
  window.location.href = url;
}

function getCity(address) {
  // This function extracts the city name from the given address using a regular expression
  // Define a regular expression to match the city between the first and second commas
  const cityRegex = /,\s*(.*?),/;
  // Return the located City
  return address.match(cityRegex)[1];
}

function getState(address) {
  // This function extracts the state abbreviation from the given address using a regular expression
  // Define a regular expression to match the state abbreviation
  const stateRegex = /\b(?:AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)\b/gi;
  // Return the located State
  return address.match(stateRegex)[0];
}

function getZip(address) {
  // This function extracts the zip code from the given address using a regular expression
  // Regular expression to match zip code pattern
  var zipRegex = /\b\d{5}(?:-\d{4})?\b/;
  // Return the located ZipCode
  return address.match(zipRegex)[0];
}

function generateTile(img_src, name, min_price, max_price, city_name, state_name, zip_code, link, phone_number) {
  // This function generates a tile object with the provided data
  return {
    imageSrc: img_src, // URL of the image
    title: name, // Name/title of the room
    min: min_price, // Minimum price
    max: max_price, // Maximum price
    city: city_name + "," + state_name + " " + zip_code, // City, state, and zip code combined
    url: link, // URL for more information
    phone_number: phone_number, // The phone number for the apartment
  }
}

// Function to generate room HTML
function generateRoomHTML(room) {
  // This function generates HTML markup for a room tile based on the provided room object
  return `
    <div class="room-tile">
      <img src="${room.imageSrc}" alt="${room.title}" class="room-image"> <!-- Image -->
      <div class="room-info">
        <h3>${room.title}</h3> <!-- Title -->
        <h6 class="room-price">Price Range: $${room.min} - $${room.max}</h6> <!-- Price Range -->
        <p>City:</p>
        <p><u>${room.city}</u></p> <!-- City, state, and zip code -->
        <br>
        <p>Phone Number:</p>
        <p><u>${room.phone_number}</u></p> <!-- Phone number -->
        <button class="info-button" onclick="redirectTo('${room.url}')">Get More Info</button> <!-- Button to get more information -->
      </div>
    </div>
  `;
}

// CSS styles for responsiveness (to be included in your CSS file or <style> section)
const styles = `
  #aptContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start; /* Align items to the left */
  }
  .room-tile {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 600px;
    margin: 10px; /* Add margin to space out the tiles */
    padding: 15px;
    box-sizing: border-box;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 10px;
    overflow: hidden;
  }
  .room-image {
    width: 100%;
    height: auto;
    border-radius: 10px 10px 0 0;
  }
  .room-info {
    width: 100%;
    padding: 15px;
    text-align: center;
  }
  .room-price {
    font-weight: bold;
    margin: 10px 0;
  }
  .info-button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
  }
  .info-button:hover {
    background-color: #0056b3;
  }
`;

// Inject the styles into the document
const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

function generateTiles() {
  // This function generates room tiles based on the provided data arrays
  var apts = [];
  for (var i = 0; i < names.length; i++) {
    // Generate a tile object for each room and push it to the 'apts' array
    var tile = generateTile(imgs[i], names[i], mins[i], maxs[i], getCity(addresses[i]), getState(addresses[i]), getZip(addresses[i]), links[i], numbers[i]);
    apts.push(tile);
  }
  return apts; // Return the array of room tiles
}

// Generate room tiles and append to container
var apts = generateTiles(); // Generate room tiles
const container = document.getElementById('aptContainer'); // Get container element
apts.forEach(apt => {
  const aptHTML = generateRoomHTML(apt); // Generate HTML markup for each room
  container.innerHTML += aptHTML; // Append HTML markup to container
});
