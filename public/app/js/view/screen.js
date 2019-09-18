/* Anything involving showing something in the UI */
window.view = window.view || {};
window.view.screen = {};

view.SCREENS = {
    signup: 'screen_signup',
    onboarding: 'screen_onboarding',
    app: {
        landing: 'screen_app_landing',
        focus: 'screen_app_focus',
        radar: 'screen_app_radar'
    }
}

// Transist to a different screen on the app
view.screen.switchScreen = function(which) {
    $('section.active').removeClass('active');
    $(`#${which}`).addClass('active');
}

// HTML5 Location API is not usable for whatever reason 
view.screen.showNoLocationSupport = function() {
    alert('Location support unavailable or disabled');
}

// Render coordinates
view.screen.showCoordArrow = function (angle) {
    $('#debug_arrow_angle').text(angle);
}
