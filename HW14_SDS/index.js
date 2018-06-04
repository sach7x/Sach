// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
//var $dateInput = document.querySelector("#datetime");
//var $countryInput = document.querySelector("#country");
var $stateInput = document.querySelector("#state");
//var $cityInput = document.querySelector("#city");
//var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredUFO to data initially
var filteredUFO = dataSet;
 //console.log(data)

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
    $tbody.innerHTML = "";
    for (var i = 0; i < filteredUFO.length; i++) {
      // Get get the current address object and its fields
      var UFO = filteredUFO[i];
      var fields = Object.keys(UFO);
      // Create a new row in the tbody, set the index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = UFO[field];
      }
    }
  }
  
  function handleSearchButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterState = $stateInput.value.trim().toLowerCase();
  
    // Set filteredUFO to an array whose "state" matches the filter
    filteredUFO = dataSet.filter(function(UFO) {
      var UFOstate = UFO.state.toLowerCase();
  
      // If true, add to filteredUFO, otherwise don't add it to filteredUFO
      return UFOstate === filterState;

    
    });
    renderTable();
  }
  


  // Render the table for the first time on page load
  renderTable();