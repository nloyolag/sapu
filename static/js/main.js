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
    var mainContent = $(".main-content");

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


    /*$(".submit-delete").click(function() {
        event.preventDefault();
        var _href = $(this).attr("href");
        $(".delete-modal").load(_href);
    });*/

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

    // Target the action button to send data by ajax
    $(document).on(
        'click',
        '.modal-footer a.success-button[href="#"]',
        function(event) {
            event.preventDefault();
            var $modal, $button, $form, button_text;
            $modal = $(this).parents(".fancybox-inner");
            $button = $(this);
            button_text = $button.html();
            $form = $(this).parents('form');
            $modal.find('.form-error').slideUp().remove();
            $modal.find('.messages').slideUp().remove();
            $button.html('<i class="fa fa-refresh fa-spin"></i>');
            $button.css('pointer-events', 'None');
            console.log($form.attr('action'));
            var action = $.post(
                $form.attr('action'),
                $form.serialize()
            )
            .done(function(data){
                var $messages, $warnings, $errors;
                $messages = $(data).find('.success');
                $warnings = $(data).find('.warning');
                $errors = $(data).find('.error');

                if ($errors.length > 0 || $warnings.length > 0) {
                    // Show error messages and reload form
                    $errors = $(data).find('.form-error');
                    $errors.hide().prependTo('sapu-modal');
                    $errors.slideDown();
                    $modal.find('.modal-form').remove();
                    var $modal_forms = $(data).find('.modal-form');
                    $modal.find('.modal-main').append($modal_forms);
                } else {
                    var url = document.getElementById("url-holder");
                    var _href = $(url).attr("href");
                    mainContent.load(
                        _href,
                        function() {
                            mainContent.data('url', _href)
                    });
                    mainContent.prepend($messages);
                    // close_parent_modal($button);
                }
            })
            .fail(function(data){
                var $alert = $('<div class="error message"/>')
                    .text("No se puede contactar el servidor. " +
                        "Intente de nuevo más tarde.");
                $alert.hide().prependTo('.sapu-modal');
                $alert.slideDown();
            })
            .always(function(){
                $button.find('.fa').fadeOut();
                $button.html(button_text);
                $button.css('pointer-events', '');
            });

        });

});