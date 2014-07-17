require.config({
    baseUrl: 'bower_components',
    paths: {
        jquery: 'jquery/dist/jquery',
        pjax: 'jquery-pjax/jquery.pjax',
        swig: 'civswig/swig'
    },
    "shim": {
        "pjax": ["jquery"]
    }
});

require(["jquery", "swig", "pjax"], function($, swig) {
    console.log($);
    console.log($.fn.pjax);
    console.log(swig);
});