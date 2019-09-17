/* Anything involving showing something in the UI */
window.view = window.view || {};

view.SCREENS = {
    app: {
        landing: "screen_app_landing",
        focus: "screen_app_focus",
        radar: "screen_app_radar"
    }
}

// Transist to a different screen on the app
// which:
//    - screen_signup
//    - screen_information
//    - screen_app_landing
view.switchScreen = function(which) {
    $('section.active').removeClass('active');
    $(`#${which}`).addClass('active');
}

// HTML5 Location API is not usable for whatever reason 
view.showNoLocationSupport = function() {
    alert('Location support unavailable or disabled');
}

// Render coordinates
view.showCoordArrow = function (angle) {
    $('#debug_arrow_angle').text(angle);
}
