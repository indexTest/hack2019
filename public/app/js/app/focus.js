/* Focus mode app module */
window.app = window.app || {};
window.app.focus = (function() {
    var exports = {};

    var match = false;

    var ownHeading = null;
    var ownCoord = null;

    var groupID = null;
    var tgtCoord = null;
    var tgtId = null;

    var relativeAngle = 0;

    function calculateAngle() {
        if (match) {
            var abs = Math.atan((ownCoord.longitude - tgtCoord.longitude) / (ownCoord.latitude - tgtCoord.latitude));
            relativeAngle = abs - ownHeading;
        } else {
            relativeAngle = 0;
        }
    }

    function render() {
        if (match) {
            calculateAngle();
            $('#debug_focus_self').text('heading: ' + ownHeading + '; coord: ' + JSON.stringify(ownCoord));
            $('#debug_focus_tgtf').text('groupID: ' + groupID + '; coord: ' + JSON.stringify(tgtCoord) + '; id: ' + tgtId);
            $('#debug_focus_angle').text('Calculated angle: ' + relativeAngle);
        } else {
            $('#debug_focus_orientation').text('No match');
        }
    }

    exports.init = function (done) {
        ownHeading = resources.heading.value;
        lib.location.get(function (coord) {
            ownCoord = coord;
            done();
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

    exports.updateHeading = function (heading) {
        ownHeading = heading;
        render();
    }

    exports.isSingle = true;

    return exports;
})()
