$( document ).ready(function() {
    $('.project-table').DataTable( {
        paging: false,
        searching: false,
        infoCallback: function(){}
    } );

    $("#institution-info").click(function() {
        $("#institution-collapse").slideToggle('slow');
    });
});