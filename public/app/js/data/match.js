/* Calls the user match api */
window.data = window.data || {};
window.data.getMatch = function(single, cb) {
    lib.location.get(function(pos) {
        $.get('http://35.203.62.254:8080/api/getMatcher', {
            lon: pos.longitude,
            lat: pos.latitude,
            // Endpoint only support single
            mode: 'single',
            //mode: single ? 'single' : 'multi',
            limit: single ? 1 : 10,
            threshold: 10,
            pid: Cookies.get('pid')
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
