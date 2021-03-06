$( document ).ready(function() {

    $(".fancybox").fancybox({
        autoSize : false,
        width: 500
    });

    $(".select-container select").select2({width: "15%"});

    var options = {
        valueNames: [
            'table-state',
            'table-creation',
            'table-name',
            'table-id',
            'table-type',
            'table-description',
            'table-deadline',
            'table-image',
            'table-actions' ],
        page: 10,
        plugins: [ ListPagination({}) ]
    };

    var projectList = new List('projects-container', options);

    $(document).on("click", "#filter-ontime", function() {
        projectList.filter(function(values) {
            if(values.elm.className == "En tiempo") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $(document).on("click", "#filter-complete", function() {
        projectList.filter(function(values) {
            if(values.elm.className == "Terminado") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $(document).on("click", "#filter-late", function() {
        projectList.filter(function(values) {
            if(values.elm.className == "Retrasado") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $(document).on("click", "#filter-cancelled", function() {
        projectList.filter(function(values) {
            if(values.elm.className == "Cancelado") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $(document).on("click", "#filter-paused", function() {
        projectList.filter(function(values) {
            if(values.elm.className == "Congelado") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    // Selectors reutilized throughout the script
    var modalDeleteSummon = $(".modal-delete-summon");
    var mainContent = $(".main-content");
    var listContent = $("#list-content");

    // Data Table creation on projects view
    /*$('.project-table').DataTable( {
        paging: false,
        searching: false,
        infoCallback: function(){}
    } );*/

    // Changes delete button URL on click
    $(document).on("click", ".modal-delete-summon", function() {
        var _href = $(this).attr("href");
        _href = _href.substr(1);
        var targetModal = document.getElementById(_href);
        var modal_href = $(targetModal).children("a.submit-delete").attr("href");
        $(targetModal).children("a.submit-delete").attr("href", modal_href + $(this).attr("id"));
    });

    // Return delete button URL back to default, add fancybox
    modalDeleteSummon.fancybox({
       'afterClose' : function() {
            var _href = $(this).attr("href");
            _href = _href.substr(1);
            var targetModal = document.getElementById(_href);
            var modal_href = $(targetModal).children("a.submit-delete").attr("href");
            while(modal_href.charAt(modal_href.length - 1) != '/')
                modal_href = modal_href.substr(0, modal_href.length - 1);
            $(targetModal).children("a.submit-delete").attr("href", modal_href);
        }
    });

    // Makes AJAX deletion
    $(document).on("click", ".submit-delete", function(event) {
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
                $(".select-container select").select2({width: "15%"});
                projectList = new List('projects-container', options);
                $.fancybox.close();
            });
        });
    });

    // Summons modal for create and edit buttons
    $(".modal-summon").fancybox({
        margin: 50,
        minWidth: 500,
        scrolling: 'auto',
        type: 'ajax',
        ajax: {
            complete: function() {
                $(".sapu-modal select").select2({width: "90%"});
                $(".datetime-field").datepicker();
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
                    $(".sapu-modal select").select2({width: "90%"});
                    projectList = new List('projects-container', options);
                    $(".datetime-field").datepicker();
                } else {
                    var url = document.URL;
                    mainContent.empty();
                    mainContent.load(
                        url + " #main-content > *",
                        function() {
                            mainContent.prepend($messages);
                            $(".select-container select").select2({width: "15%"});
                            projectList = new List('projects-container', options);
                            $.fancybox.close();
                    });
                }
            })
            .fail(function(data){
                var $alert = $('<div class="error message form-error error"/>')
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

    // Close fancybox on click
    $(document).on(
        'click',
        '.modal-footer a.cancel-button[href="#"]',
        function(event) {
            event.preventDefault();
            $.fancybox.close();
    });

    // Close delete fancybox on click
    $(document).on(
        'click',
        '.delete-modal a[href="#"]',
        function(event) {
            event.preventDefault();
            $.fancybox.close();
    });

    // Check and uncheck tasks with AJAX
    $(document).on("click", ".check-click", function(event) {
        event.preventDefault();

        if ($(this).hasClass("fa-check-square")) {
            $(this).removeClass("fa-check-square");
            $(this).addClass("fa-square-o");

        } else {
            $(this).removeClass("fa-square-o");
            $(this).addClass("fa-check-square");
        }

        var _href = $(this).parent().attr("href");

        $(this).load(_href);
        $(".select-container select").select2({width: "15%"});
    });

    // Hover on image upload icon
    $(".image-upload-container").hover(function() {
        $(this).children("a").addClass("image-button-hover");
    }, function() {
        $(this).children("a").removeClass("image-button-hover");
    });

});