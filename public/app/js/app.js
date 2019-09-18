$(document).foundation()

if (Cookies.get('testmode') === 'true') {
    lib.location.useMock();
    resources.heading.mock(Math.random()*200-100);
    data.mockGetMatch();
}

// Switch to app landing if pid already exists
if (Cookies.get('pid')) {
    view.screen.switchScreen(view.SCREENS.app.landing);
}

function setTestMode() {
    Cookies.set('testmode', true);
}

function setPid(val) {
    Cookies.set('pid', val);
}

function reset() {
    Cookies.remove('pid');
}

console.log('Commands:\n\tsetPid(val); - set specific pid\n\treset(); - clear app state');
