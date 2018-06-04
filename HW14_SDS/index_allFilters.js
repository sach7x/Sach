// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateInput = document.querySelector("#datetime");
var $countryInput = document.querySelector("#country");
var $stateInput = document.querySelector("#state");
var $cityInput = document.querySelector("#city");
var $shapeInput = document.querySelector("#shape");
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
    var filterDate = $dateInput.value;
    var filterState = $stateInput.value.trim().toLowerCase();
    var filterCity = $cityInput.value.trim().toLowerCase();
    var filterCountry = $countryInput.value.trim().toLowerCase();
    var filterShape = $shapeInput.value.trim().toLowerCase();

  if (filterDate != "")
  {
    filteredTable = dataSet.filter(function(UFO) 
    {
      var UFODate = UFO.datetime; 
    return UFODate === filterDate;
    });
  }
  else {filteredTable};

  if(filterState != "")
  {
    filteredTable = filteredTable.filter(function(UFO)
    {
      var UFOState = UFO.state;
      return UFOState === filterState;
    });
  }
  else{filteredTable};

  if(filterCity != "")
  {
    filteredTable = filteredTable.filter(function(UFO)
    {
      var UFOCity = UFO.city;
      return UFOCity === filterCity;
    });
  }

  else{filteredTable};

  if(filterCountry != "")
  {
    filteredTable = filteredTable.filter(function(UFO)
    {
      var UFOCountry = UFO.country;
      return UFOCountry === filterCountry;
    });
  }

  else{filteredTable};

  if(filterShape != "")
  {
    filteredTable = filteredTable.filter(function(UFO)
    {
      var UFOShape = UFO.shape;
      return UFOShape === filterShape;
    });
  }
  else{filteredTable};      
    
    renderTable();
  }
  


  // Render the table for the first time on page load
  renderTable();