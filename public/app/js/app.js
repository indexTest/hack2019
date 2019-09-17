$(document).foundation()

if (Cookies.get('testmode') === 'true') {
    // lib.location.useMock();
    // resources.heading.mock(Math.random()*200-100);
    data.mockGetMatch();
}
