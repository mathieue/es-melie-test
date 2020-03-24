console.log('hello there !');


function doSearch(q) {
    axios.get('/ping', {
        params: {
            q: q
        }
    }).then(function (response) {
        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}


$(document).ready(function () {
    $("#search-input").on("input", function () {
        var val = $(this).val();
        console.log('you typed: ' + val);
        doSearch(val);
    });
});