/* App engine */
window.app = window.app || {};
window.app.engine = (function() {
    var exports = {};
    var started = false;

    function cleanup() {
        hooks.heading.off();
        hooks.location.off();
    }

    // Start a new app process, possibly terminating the old one
    exports.start = function (module, done) {
        if (started) { cleanup(); }
        
        exports.loadedModule = module;
        module.init(function () {
            data.getMatch(module.isSingle, function (data) {
                module.updateData(data);
            });
            hooks.location.on(module.updateLocation);
            started = true;

            done && done();
        });
    }
    
    exports.loadedModule = null;

    return exports;
})()
