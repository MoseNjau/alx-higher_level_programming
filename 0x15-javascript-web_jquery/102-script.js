$(document).ready(() => {
  const url = "https://www.fourtonfish.com/hellosalut/?";
  $("INPUT#btn_translate").click(() => {
    const lang = $("INPUT#language_code").val();
    $.getJSON(url + $.param({ lang: lang }), (data) => {
      $("DIV#hello").text(data.hello);
    });
  });
});
