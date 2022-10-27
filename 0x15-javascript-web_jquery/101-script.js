$('document').ready(() => {
  const item = '<li>item</li>';
  const toAppend = $('UL.my_list');
  $('DIV#add_item').click(() => {
    toAppend.append(item);
  });
  $('DIV#remove_item').click(() => {
    $('LI')[$('LI').length - 1].remove();
  });
});
