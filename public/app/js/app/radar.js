/* Radar mode app module */
window.app = window.app || {};
window.app.radar = (function() {
    var exports = {};

    var match = false;
    var ownCoord = null;
    var groupID = null;
    var tgtId = null;
    var tgtCoords = [];
    var tgtPins = [];

    var gMap = null;
    var relativeAngle = 0;

    function render() {
        if (match) {
            view.radar.showMap();
        } else {
            view.radar.showNoData();
        }
    }

    function makeGoogleMapCallback(dom, ownCoord, tgtCoords) {
        var markerCoord = {
            lat: ownCoord.latitude,
            lng: ownCoord.longitude
        };

        return function() {
            gMap = new google.maps.Map(dom, {
                zoom: 15,
                center: markerCoord,
                disableDefaultUI: true
            });

            new google.maps.Marker({
                position: markerCoord,
                map: gMap,
                icon: {
                    url: "img/you.png"
                }
            });
        }
    }

    function addGoogleMapMarker(tgtCoords) {
        var markerCoords = tgtCoords.map(function(e) { return { lat: e.latitude, lng: e.longitude }; });
        return markerCoords.map(function(e) { return new google.maps.Marker({position: e, map: gMap}); });
    }

    exports.init = function (done) {
        lib.location.get(function (coord) {
            ownCoord = coord;

            // Create a callback with randomized name
            var callbackName = lib.uuid.make().replace(/\-/g, '');
            window[callbackName] = makeGoogleMapCallback(document.getElementById('radar_map'), coord);

            // Load the google map library
            var apiKey = 'AIzaSyBJ-FEAhLyZhxmJSe7R70qKKCbZBmuPAzg';
            var googleMapsUrl = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=${callbackName}`;
            $.ajaxSetup({ cache: true });
            $.getScript(googleMapsUrl, function () {
                done();
            })
        });
    }

    exports.updateData = function (data) {
        if (data.uuid) {
            // The api is only capable of returning one entry, as a not-array
            groupID = data.uuid;
            tgtId = data.pid;
            tgtCoords.push({
                longitude: data.lon,
                latitude: data.lat
            })
            tgtPins = tgtPins.concat(addGoogleMapMarker(tgtCoords));
            match = true;
        } else {
            match = false;
        }
        render();
    }

    exports.updateLocation = function (coord) {
        ownCoord = coord;
        render();
    }

    exports.addMockMatch = function () {
        match = true;
        newCoord = {
            longitude: ownCoord.longitude + (Math.random() * 0.02 - 0.01),
            latitude: ownCoord.latitude + (Math.random() * 0.02 - 0.01)
        };

        tgtCoords.push(newCoord);
        tgtPins = tgtPins.concat(addGoogleMapMarker([newCoord]));
        render();
    }

    exports.generateJitter = function () {
        setInterval(function () {
            for (var c=0 ; c<tgtPins.length ; c++) {
                tgtCoords[c] = {
                    longitude: tgtCoords[c].longitude + (Math.random() * 0.0002 - 0.0001),
                    latitude: tgtCoords[c].latitude + (Math.random() * 0.0002 - 0.0001)
                }
                tgtPins[c].setMap(null);
            }
            tgtPins = addGoogleMapMarker(tgtCoords);
        }, 1000);
    }

    exports.isSingle = false;

    return exports;
})()
