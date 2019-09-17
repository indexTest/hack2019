/* Device heading resource */
window.resources = window.resources || {};
window.resources.heading = (function() {
    var exports = {};
    var enabled = false;
    var handler;

    exports.value = 0;

    exports.enable = function () {
        if (enabled) { return; }
        handler = window.addEventListener('deviceorientation', function (event) {
            // IOS
            if (event.webkitCompassHeading) {
                exports.value = event.webkitCompassHeading;
            } else {
                exports.value = event.alpha;
                if(!window.chrome) {
                    // Assume stock Android browser
                    exports.value = exports.value-270;
                }
            }
        }, true);
    }

    exports.disable = function () {
        if (!enabled) { return; }
        window.removeEventListener('deviceorientation', handler);
    }

    exports.mock = function (mock) {
        exports.value = mock;
    }

    return exports;
})()
