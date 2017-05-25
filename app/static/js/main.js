$( document ).ready(function() {

    $( "#month_hours" ).blur(function() {
      var num1 = $('#month_hours').val();
      var num2 = $('#hc').val();
      var result = parseInt(num1) + parseInt(num2);
      $('available').val(result);
    });
});
