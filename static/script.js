$(document).ready(function() { 
  $(".Month").change(function() {
    if ($('.Month:checked').length == $('.Month').length) {
      $("#map").replaceWith("<p id='map'>All Checked</p>")
    }
    else if ($('.Month:checked').length === 0) {
      $("#map").replaceWith("<p id='map'>All Not Checked</p>")
    }
  });
  //$("#monthSelection").click(function() {
  //  if($("input.Month").not(":checked").length === 0)
  //  {
  //    $("#map").replaceWith("<p>All Checked</p>")
  //  }
  //  else if($("input.Month").not(":checked").length === 12)
  //  {
  //    $("#map").replaceWith("<p>All Not Checked</p>")
  //  }
  //  if($("#Jan").is(":checked"))
  //  {
  //  }
  //}); 
});
