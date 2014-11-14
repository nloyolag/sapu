$( document ).ready(function() {

    // Selectors reutilized throughout the script
    var modalDeleteSummon = $(".modal-delete-summon");
    var mainContent = $(".main-content");
    var listContent = $("#list-content");

    // Data Table creation on projects view
    $('.project-table').DataTable( {
        paging: false,
        searching: false,
        infoCallback: function(){}
    } );

    // Changes delete button URL on click
    $(document).on("click", ".modal-delete-summon", function() {
        var _href = $(this).attr("href");
        _href = _href.substr(1);
        var targetModal = document.getElementById(_href);
        var modal_href = $(targetModal).children("a").attr("href");
        $(targetModal).children("a").attr("href", modal_href + $(this).attr("id"));
        console.log(modal_href + $(this).attr("id"));
    });

    // Return delete button URL back to default, add fancybox
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

    // Makes AJAX deletion
    $(document).on("click", ".submit-delete", function() {
        event.preventDefault();
        var $button = $(this);
        $button.html('<i class="fa fa-refresh fa-spin"></i>');
        var _href = $(this).attr("href");

        $(this).load(_href, function(data) {
            var url = document.URL;
            var $messages = $(data).find('.success');
            mainContent.empty();
            mainContent.load(
            url + " #main-content > *",
            function() {
                mainContent.prepend($messages);
                $.fancybox.close();
            });
        });

    });

    // Summons modal for create and edit buttons
    $(".modal-summon").fancybox({
        type: 'ajax',
        ajax: {
            complete: function() {
                $("select").select2({width: "90%"});
            }
        }
    });

    // Send form via AJAX to Edit or Create
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
                    $modal.find('.modal-form').remove();
                    var $modal_forms = $(data).find('.modal-form');
                    $modal.find('.sapu-modal').append($modal_forms);
                } else {
                    var url = document.URL;
                    mainContent.empty();
                    mainContent.load(
                        url + " #main-content > *",
                        function() {
                            mainContent.prepend($messages);
                            $.fancybox.close();
                    });
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