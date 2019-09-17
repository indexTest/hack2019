/* Anything involving input coming from the UI */
var controller = {};

controller.signup = function() {
    // Generate UUID
    view.switchScreen('screen_information');
}

controller.startFocusMode = function () {
    view.switchScreen(view.SCREENS.app.focus);
    app.engine.start(app.focus);
}

controller.startRadarMode = function () {
    view.switchScreen(view.SCREENS.app.radar);
    app.engine.start(app.radar);
}
