// Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// Displays the value of hello from that fetch in the HTML tag DIV#hello

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
