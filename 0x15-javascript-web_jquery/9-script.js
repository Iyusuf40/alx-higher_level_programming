$('document').ready(() => {
  const tag = $('DIV#hello');
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    tag.text(data.hello);
  });
});
