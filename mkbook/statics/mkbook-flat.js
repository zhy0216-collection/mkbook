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

    function markCurTocTree() {
        var curTocTree = null;
        console.log("curTocTree: " + curTocTree)

        function _markCurTocTree(target) {
            if (curTocTree != null) {
                curTocTree.removeClass("current");
            }
            curTocTree = target;
            curTocTree.addClass("current");
        }
        return _markCurTocTree;
    }

    markCurTocTreeOne = new markCurTocTree();
    markCurTocTreeTwo = new markCurTocTree();


    $(".toctree-l1-a").on("click", function(e) {

        var $this = $(this);
        if (!$this.hasClass("ajax")) {
            e.preventDefault();
        }

        var curTocTreeOne = $this.closest(".toctree-l1");
        var tocTreeTwo = curTocTreeOne.find(".toctree-l2 a").first();

        if (tocTreeTwo.length > 0) {
            window.location.hash = tocTreeTwo.attr("href");
            markCurTocTreeTwo(tocTreeTwo.closest(".toctree-l2"));
        }
        markCurTocTreeOne(curTocTreeOne);

    })

    $(".toctree-l2 a").on("click", function() {
        markCurTocTreeTwo($(this).closest(".toctree-l2"));
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