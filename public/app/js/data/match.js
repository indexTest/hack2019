/* Calls the user match api */
window.data = window.data || {};
window.data.getMatch = function(single, cb) {
    lib.location.get(function(pos) {
        $.get('https://ixplus.club/api/v1/userconnect', {
            lon: pos.longitude,
            lat: pos.latitude,
            mode: single ? 'single' : 'multi',
            limit: single ? 1 : 10,
            threshold: 10
        }, cb);
    });
};

window.data.mockGetMatch = function() {
    window.data.getMatch = function(single, cb) {
        cb({
            group: '123456',
            matches: [{
                pid: 'abcdef',
                lat: 12.34,
                lon: 56.78,
                seg: ["sample"]
            }]
        })
    }
}
