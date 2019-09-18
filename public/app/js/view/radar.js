/* Radar app UI */
window.view = window.view || {};
window.view.radar = {};

// HTML5 Location API is not usable for whatever reason 
view.radar.showNoData = function() {
    $('#radar_no_data').show();
    $('#radar_map').hide();
}

// Render coordinates
view.radar.showMap = function (angle) {
    $('#radar_no_data').hide();
    $('#radar_map').show();
}
