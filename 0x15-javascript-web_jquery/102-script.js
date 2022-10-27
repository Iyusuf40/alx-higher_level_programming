$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    const tag = $('DIV#hello');
    const lang = $('INPUT#language_code').val();
    const url = 'https://stefanbohacek.com/hellosalut/?lang=' + lang;
    const settings = {
      method: 'GET',
      success: (data, stat, xml) => {
        tag.text(data.hello);
      }
    };
    $.ajax(url, settings);
  });
});
