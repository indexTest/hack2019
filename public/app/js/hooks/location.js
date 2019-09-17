/* Location updates */
window.hooks = window.hooks || {};
window.hooks.location = (function() {
    var exports = {};
    var watchId;

    exports.available = !!navigator.geolocation;
    exports.on = function (cb) {
        watchId = navigator.geolocation.watchPosition(function(pos) {
            cb(pos.coords, null);
        }, function (err) {
            cb(null, err);
        }, {
            enableHighAccuracy: true
        });
    }

    exports.off = function () {
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
        exports.on = function (cb) { watchId = setInterval(function () { cb(null, mockCoord()); }, 3000); }
        exports.off = function () { clearInterval(watchId); }
    }

    return exports;
})()
