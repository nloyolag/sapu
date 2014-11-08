$( document ).ready(function() {

    // Data Table creation on projects view
    $('.project-table').DataTable( {
        paging: false,
        searching: false,
        infoCallback: function(){}
    } );

    $("#institution-info").click(function() {
        $("#institution-collapse").slideToggle('slow');
    });

    var modalDeleteSummon = $(".modal-delete-summon");

    // Changes delete button URL on click
    modalDeleteSummon.click(function() {
        var _href = $(this).attr("href");
        _href = _href.substr(1);
        var targetModal = document.getElementById(_href);
        var modal_href = $(targetModal).children("a").attr("href");
        $(targetModal).children("a").attr("href", modal_href + $(this).attr("id"));
    });

    $(".modal-summon").fancybox({
        type: 'ajax'
    });

    // Return delete button URL back to default
    modalDeleteSummon.fancybox({
       'afterClose' : function() {
            var _href = $(this).attr("href");
            _href = _href.substr(1);
            var targetModal = document.getElementById(_href);
            var modal_href = $(targetModal).children("a").attr("href");
            while(modal_href.charAt(modal_href.length - 1) != '/')
                modal_href = modal_href.substr(0, modal_href.length - 1);
            $(targetModal).children("a").attr("href", modal_href);
        }
    });

    // Target the cancel button to close the modal
    $(document).on(
        'click',
        'form.modalform a.cancel-button[href="#"]',
        function(event){
            console.log("hola")
            event.preventDefault();
            close_parent_modal($(this));
        }
    )

    function close_parent_modal($element) {
        $modal = $($element).parents('.reveal-modal');
        $modal.foundation('reveal', 'close');
    }

});