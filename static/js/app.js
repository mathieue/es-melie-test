console.log('hello there !');

$(document).ready(function () {
    $("#search-input").on("input", function () {
        var val = $(this).val();
        console.log('you typed: ' + val);
    });
});