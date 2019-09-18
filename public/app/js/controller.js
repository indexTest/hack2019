/* Anything involving input coming from the UI */
var controller = {};

controller.signup = function() {
    var pid = lib.uuid.make();
    console.log(`Your pid: ${pid}`)
    Cookies.set('pid', pid);

    view.screen.switchScreen(view.SCREENS.onboarding);
}

controller.startFocusMode = function () {
    view.screen.switchScreen(view.SCREENS.app.focus);
    app.engine.start(app.focus);
}

controller.startRadarMode = function () {
    view.screen.switchScreen(view.SCREENS.app.radar);
    app.engine.start(app.radar);
}

controller.addMockMatch = function () {
    app.engine.loadedModule.addMockMatch();
}
