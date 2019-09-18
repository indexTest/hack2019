/* Radar mode app module */
window.app = window.app || {};
window.app.radar = (function() {
    var exports = {};

    var match = false;

    var ownHeading = null;
    var ownCoord = null;

    var groupID = null;
    var tgtCoord = null;
    var tgtId = null;

    var gMap = null;
    var relativeAngle = 0;

    function render() {
        if (match) {
            //calculateAngle();
            // $('#debug_focus_self').text('heading: ' + ownHeading + '; coord: ' + JSON.stringify({ lon: ownCoord.longitude, lat: ownCoord.latitude }));
            // $('#debug_focus_tgtf').text('groupID: ' + groupID + '; coord: ' + JSON.stringify({ lon: tgtCoord.longitude, lat: tgtCoord.latitude }) + '; id: ' + tgtId);
            // $('#debug_focus_angle').text('Calculated angle: ' + relativeAngle);
        } else {
            //view.
        }
    }

    function makeGoogleMapCallback(dom, ownCoord, tgtCoords) {
        var markerCoord = {
            lat: ownCoord.latitude,
            lng: ownCoord.longitude
        };

        return function() {
            gMap = new google.maps.Map(dom, {
                zoom: 17,
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
        markerCoords.forEach(function(e) { new google.maps.Marker({position: e, map: gMap}); });
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
        if (data.matches) {
            groupID = data.group;
            tgtId = data.matches[0].pid;
            tgtCoord = {
                longitude: data.matches[0].lon,
                latitude: data.matches[0].lat
            }
            addGoogleMapMarker([tgtCoord]);
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
            longitude: ownCoord + 0.01,
            latitude: ownCoord + 0.01
        };

        addGoogleMapMarker([newCoord]);
    }

    exports.isSingle = false;

    return exports;
})()
