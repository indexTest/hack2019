/* HTML5 location API */
window.lib = window.lib || {};
window.lib.location = (function() {
    var exports = {};
    var watchId;

    exports.available = !!navigator.geolocation;
    exports.get = function (cb) {
        navigator.geolocation.getCurrentPosition(function(pos) {
            cb(pos.coords, null);
        }, function (err) {
            cb(null, err);
        }, {
            enableHighAccuracy: true
        });
    }

    exports.watch = function (cb) {
        watchId = navigator.geolocation.watchPosition(function(pos) {
            cb(pos.coords, null);
        }, function (err) {
            cb(null, err);
        }, {
            enableHighAccuracy: true
        });
    }

    exports.stop = function () {
        navigator.geolocation.clearWatch(watchId);
    }

    // Constructor
    if (!exports.available) {
        view.showNoLocationSupport();
    }

    exports.useMock = function () {
        mockCoord = function() {
            return {
                longitude: Math.random()*200-100,
                latitude: Math.random()*200-100
            }
        };

        exports.available = true;
        exports.get = function (cb) { cb(mockCoord(), null); }
        exports.watch = function (cb) { watchId = setInterval(function () { cb(mockCoord(), null); }, 3000); }
        exports.stop = function () { clearInterval(watchId); }
    }

    return exports;
})()
