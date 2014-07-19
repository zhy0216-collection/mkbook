require.config({
    baseUrl: 'bower_components',
    paths: {
        jquery: 'jquery/dist/jquery',
        swig: 'civswig/swig',
        marked: "marked/lib/marked"
    },
    "shim": {
        "pjax": ["jquery"]
    }
});

require(["jquery", "swig", "marked"], function($, swig, marked) {
    marked.setOptions({
        renderer: new marked.Renderer(),
        gfm: true,
        tables: true,
        breaks: false,
        pedantic: false,
        sanitize: true,
        smartLists: true,
        smartypants: false
    });

    $("a.ajax").on("click", function(e) {
        e.preventDefault();
        var url = $(this).attr("href");
        $.get(url)
            .done(function(data) {
                $("#doc-content").html(marked(data));
            })

    })




});