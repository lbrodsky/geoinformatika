'use strict';

/*** General Leaflet Code ***/
// Create map and center in Prague
var map = L.map('map', {
  center: [14.4, 50.0],
  zoom: 13
});

// Add Open Street Map as base map
var osm = L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a>'
}).addTo(map);

/*** Code for adding GeoJSON ***/
// UK Sites GeoJSON file
// 
var geoJsonUrl = 'https://github.com/lbrodsky/geoinformatika/blob/main/geodata/geojson/uk_adresy.geojson'
// Change to this url to test error function
//var geoJsonUrl = 'todo';

// Placeholder for layer. Required to test if layer is added to map or not.
var ukDist;

// HTML element to display error message
var errMsgSpan = $('#errorMsg');

/*** Add layer using jQuery $.getJSON() method
See https://api.jquery.com/jquery.getjson/
1. Check to make sure layer is not already added to map.
2. Call $.getJSON method, passing in url for geoJSON data
3. Call function that creates Leaflet geoJSON layer and adds it to map
4. A function for the fail event is created to handle errors with the request
*******************************************************************************/

function addDataJQuery() {
  if (!mapHasLayer()) {
    var getLayerJQuery = $.getJSON(geoJsonUrl, function(data) {
      // create a GeoJSON layer
      createukDistGeoJson(data);
    }); // end getLayerJQuery()

    // If there is an error making the request, write the error out in the <span id="#errorMsg"> element
    getLayerJQuery.fail(function(jqxhr, textStatus, error) {
      var err = textStatus + ', ' + error + ' (' + jqxhr.status + ')';
      errMsgSpan.text('Request Failed: ' + err);
      errMsgSpan.show();
    }); // end getLayerJQuery().fail()
  } // end if (!mapHasLayer())
} // end addDataJQuery()

/*** Add layer using Vanilla JS to make an XML HTTP Request
See https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
1. Check to make sure layer is not already added to map.
2. Create a XMLHttpRequest
3. Open the request using GET method
4. Send the request
5. Request will cycle through states. See https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState
6. Once the request is complete (4), if the request was successful (200), parse the request from string to JSON
See https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
7. Call function that creates Leaflet geoJSON layer and adds it to map
8. If the response status is not 200, then an error message is generated
***********************************************************************************************************************/
// Add layer using vanilla AJAX request
function addDataVanillaJS() {
  if (!mapHasLayer()) {
    var getLayerVanillaJS = new XMLHttpRequest();
    getLayerVanillaJS.open('GET', geoJsonUrl);
    getLayerVanillaJS.send();

    getLayerVanillaJS.onreadystatechange = function(data) {
        if (getLayerVanillaJS.readyState === 4 && getLayerVanillaJS.status === 200) {          
            var geoJsonData = JSON.parse(getLayerVanillaJS.responseText);
            // create a GeoJSON layer
            createukDistGeoJson(geoJsonData);
          } else if (getLayerVanillaJS.readyState === 4 && getLayerVanillaJS.status !== 200) {
            // add error message to span         
            var err = getLayerVanillaJS.statusText + ' (' + getLayerVanillaJS.status + ')';
            errMsgSpan.text('Request Failed: ' + err);
            errMsgSpan.show();          
        } // end if (getLayerVanillaJS.readyState === 4)
      } // end getLayerVanillaJS.onreadystatechange()
  } // if (!mapHasLayer())  
} // end addDataVanillaJS()

/*** Helper Functions ***/
// create GeoJSON layer, style, add popup, and add to map
function createukDistGeoJson(data) {
  // see http://leafletjs.com/reference.html#geojson
  ukDist = L.geoJson(data, {
    // symbolize features
    style: function(feature) {
      return {
        color: '#000',
        weight: 3,
        opacity: 1,
        fillColor: '#EBE34D',
        fillOpacity: 0.5
      }
    },
    onEachFeature: function(feature, layer) {
      var name = feature.properties.NAME;
      var popupContent = L.Util.template('<h2 class="map-popup">{NAME}</h2>', feature.properties);
      // add a popup to each feature
      layer.bindPopup(popupContent, {
        closeOnClick: true
      });
    }
  }).addTo(map); // add layer to map
}

// Test if map has layer
function mapHasLayer() {
  if (map.hasLayer(ukDist)) {
    return true;
  } else {
    return false;
  }
}

// Remove layer from map
function removeLayerFromMap() {
  // if layer is on map, remove the layer
  if (mapHasLayer()) {
    map.removeLayer(ukDist);
  }
}

/*** Event Handlers ***/
// Add layer with $.getJSON()
// tied to <a id="addJQ">
$('#addJQ').click(function() {
  addDataJQuery();
});

// Add layer with XMLHttpRequest()
// tied to <a id="addVanillaJS">
var addVanillaJS = document.getElementById('addVanillaJS');
addVanillaJS.addEventListener('click', addDataVanillaJS);

// Remove layer from map
// tied to <a id="removeLayer">
$('#removeLayer').click(function() {
  removeLayerFromMap();
  errMsgSpan.hide();
});