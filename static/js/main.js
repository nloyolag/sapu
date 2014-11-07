$( document ).ready(function() {

    $('.project-table').DataTable( {
        paging: false,
        searching: false,
        infoCallback: function(){}
    } );

    $("#institution-info").click(function() {
        $("#institution-collapse").slideToggle('slow');
    });

    var modalDeleteSummon = $(".modal-delete-summon");

    modalDeleteSummon.click(function() {
        var _href = $(this).attr("href");
        _href = _href.substr(1);
        var targetModal = document.getElementById(_href);
        var modal_href = $(targetModal).children("a").attr("href");
        $(targetModal).children("a").attr("href", modal_href + $(this).attr("id"));
    });

    $(".modal-summon").fancybox({

    });

    modalDeleteSummon.fancybox({

    });




});