//script the navbar ready state.
var kol_skip_font_awesome = true;
$(document).ready(function () {
  //Hover menus.
  function toggleDropdown(e) {
    const _d = $(e.target).closest(".dropdown"),
      _m = $(".dropdown-menu", _d);
    setTimeout(
      function () {
        const shouldOpen = e.type !== "click" && _d.is(":hover");
        _m.toggleClass("show", shouldOpen);
        _d.toggleClass("show", shouldOpen);
        $('[data-toggle="dropdown"]', _d).attr("aria-expanded", shouldOpen);
      },
      e.type === "mouseleave" ? 100 : 0
    );
  }

  $("body")
    .on("mouseenter mouseleave", ".dropdown", toggleDropdown)
    .on("click", ".dropdown-menu a", toggleDropdown);

  //set specific link active.
  $("#primary-top-nav a, #primary-top-nav li").removeClass("active");

  if (location.pathname.length > 1) {
    $('#primary-top-nav a[href="' + location.pathname + '"]')
      .addClass("active")
      .closest("li")
      .addClass("active");
    var picked = $('#primary-top-nav a[href="' + location.pathname + '"]');

    //only do a match if there is just one.
    if (
      picked.length == 0 &&
      $('#primary-top-nav a[href^="/' + location.pathname.split("/")[1] + '"]')
        .length == 1
    ) {
      $('#primary-top-nav a[href^="/' + location.pathname.split("/")[1] + '"]')
        .addClass("active")
        .closest("li")
        .addClass("active");
    }

    //otherwise try and pick a top level menu.
    if (
      picked.length == 0 &&
      $('#primary-top-nav a[href^="/' + location.pathname.split("/")[1] + '"]')
        .length > 1
    ) {
      $('#primary-top-nav a[href^="/' + location.pathname.split("/")[1] + '"]')
        .closest("li")
        .addClass("active");
    }
  }
});
jQuery(function ($) {
  console.log("got here");
  //actions on signup modal
  $("#signup-free").on("shown.bs.modal", function () {
    $("#email").focus();
  });

  // //image modal
  // $('#imagemodal').on('show.bs.modal', function (event) {
  // 	var button = $(event.relatedTarget) ;// Button that triggered the modal
  // 	var imageSrc = button.attr('href'); // Extract info from data-* attributes

  // 	console.log("heroic image");
  // 	console.log(imageSrc);
  // 	// If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // 	// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  // 	var modal = $(this)
  // 	modal.find('#image-modal-image').attr('src', imageSrc);
  // });
  //   $('#imagemodal').on('hide.bs.modal', function (event) {
  // 		var modal = $(this)
  // 		modal.find('#image-modal-image').attr('src', '')
  // 	});

  //actions for video MODAL

  //   $('#video-modal').on('show.bs.modal', function (event) {
  //    var button = $(event.relatedTarget) // Button that triggered the modal
  //    var frameSrc = button.data('video-frame-src') // Extract info from data-* attributes
  //    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  //    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  //    var modal = $(this)
  //    modal.find('#video-frame-src').attr('src', frameSrc + "?autoplay=true")
  //  });
  //  $('#video-modal').on('hide.bs.modal', function (event) {
  //   var modal = $(this)
  //   modal.find('#video-frame-src').attr('src', '')
  // });
});
