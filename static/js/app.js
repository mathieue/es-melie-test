console.log('hello there !');

function showSearchResult(content) {
    document.getElementById("content-search").innerHTML = content;
}

function doSearch(q, searchSelect) {
    axios.get('/search', {
        params: {
            q: q,
            searchid: searchSelect
        }
    }).then(function (response) {
        showSearchResult(response.data);
    }).catch(function (error) {
        console.log(error);
        document.getElementById("content-search").innerHTML(error);
    });
}

function getSearchInputs() {
    var val = document.getElementById("search-input").value;
    var e = document.getElementById("searchSelect");
    var searchSelect = e.options[e.selectedIndex].value;

    console.log('you typed: ' + val + ' search number ' + searchSelect);
    doSearch(val, searchSelect);
}

$(document).ready(function () {
    $("#search-input").on("input", function () {
        getSearchInputs();
    });

    $("#searchSelect").change(function () {
        getSearchInputs();
    });

});