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
    function mypajx(url) {
        $.get(url)
            .done(function(data) {
                $("#doc-content").html(marked(data));
            })
    }

    // if hash is #!/something, load /something
    (function() {
        var hash = window.location.hash;
        if (hash[1] == "!") {
            var url = window.location.hash.substr(2);
            mypajx(url);
        }
    })();

    var curTocTreeOne = null;
    $(".toctree-l1-a").on("click", function(e) {

        var $this = $(this);
        if (!$this.hasClass("ajax")) {
            e.preventDefault();
        } else {

        }
        if (curTocTreeOne != null) {
            curTocTreeOne.removeClass("current");
        }
        curTocTreeOne = $this.closest(".toctree-l1");
        curTocTreeOne.addClass("current");
    })



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
    /*
    $("a.ajax").on("click", function(e) {
        e.preventDefault();
        var url = $(this).attr("href");
        $.get(url)
            .done(function(data) {
                $("#doc-content").html(marked(data));
            })

    })
*/



    $(window).on('hashchange', function() {
        var hash = window.location.hash;
        if (hash[1] == "!") {
            var url = window.location.hash.substr(2);
            mypajx(url);
        }
    });


});