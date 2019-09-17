/* Device heading resource */
window.hooks = window.hooks || {};
window.hooks.heading = (function() {
    var exports = {};
    var handler;

    exports.on = function (cb) {
        handler = window.addEventListener('deviceorientation', function (event) {
            // IOS
            if (event.webkitCompassHeading) {
                cb(event.webkitCompassHeading);
            } else {
                var alpha = event.alpha;
                if(!window.chrome) {
                    // Assume stock Android browser
                    alpha -= 270;
                }
                cb(alpha);
            }
        }, true);
    }

    exports.off = function () {
        window.removeEventListener('deviceorientation', handler);
    }

    exports.mock = function (cb) {
        cb(Math.random()*200-100);
    }

    return exports;
})()
