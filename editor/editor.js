// Lists IDs of the fields that can be modified with .html() or .css()
// ids with underscore means it will update the css attribute following it
var fields_list = [
  'header-logo',
  'header_color',
  'header_background-color',
  'footer_background-color',
  'header-title',
  'content-above-video',
  'content-above-etherpad',
  'content-above-irc',
  'content-below-irc',
  'youtube-iframe',
  'etherpad-iframe',
  'irc-iframe',
  'style'
];
// List of checkboxes. Each id should be 'check-' + the id of the iframe that needs to be hid
var checkbox_list = [
  'check-youtube-iframe',
  'check-etherpad-iframe',
  'check-irc-iframe'
];


var update_field_helper = function(e) {
  // e: event
  var editor_id = e.target.id;
  var field_id = $(e.target).data('field');
  update_field(editor_id, field_id);
}


var update_field = function(editor_id, field_id) {
  var editor = $('#'+editor_id);

  // console.log(editor_id + ' ' + field_id);

  var css_attr = '';
  // if there's colon in the field_id, should update css
  if (field_id.indexOf('_') != -1) {
    css_attr = field_id.substr(field_id.indexOf('_')+1);
    field_id = field_id.substr(0, field_id.indexOf('_'));
  }
  var field = $('#'+field_id);

  // console.log(field);
  if (css_attr) {
    field.css(css_attr, editor.val());
  } else if (field.is('img')) {
    // update src
    // field.css('display', 'inline'); // show image first
    field.removeClass('hidden');
    field.attr('src', editor.val()); // update the url. if the link is broken, image will be hidden
  } else if (field.is('iframe')) {
    // update src
    field.attr('src', editor.val());
  } else if (field.is('div') || field.is('h1') || field.is('style')) {
    // update html content
    field.html(editor.val());  
  } else {
    console.log('!!! nothing is updated !!!');
  }
}

var clean_up_dom = function() {
  $('.hidden').remove();
  $('.remove').remove();
  var html_str = $('#wrapper').wrap('<div>').parent().html();
  var encoded_str = 'data:text/html;base64,' + $.base64.encode(html_str);
  // console.log('redirecting...');
  window.location.href = encoded_str;
}


$(document).ready(function() {
  // go thru the fields
  for (var i = 0; i < fields_list.length; i ++) {
    var field_id = fields_list[i];
    var editor_id = field_id + '-input';
    // console.log(field_id);
    // console.log(editor_id);

    // register event listener
    $('#'+editor_id).data('field', field_id)
      .change(update_field_helper)
      .keyup(update_field_helper)
      .change();
  }

  // go thru the checkboxes
  for (var i = 0; i < checkbox_list.length; i ++) {
    var checkbox_id = checkbox_list[i];
    
    $('#'+checkbox_id).change(function(e) {
      var iframe_id = e.target.id.substr(6); // remove 'check-'
      if (e.target.checked) {
        $('#'+iframe_id).removeClass('hidden');
      } else {
        $('#'+iframe_id).addClass('hidden');
      }
    }).change();
  }

  // hide broken images
  $('img').error(function() {
    $(this).addClass('hidden');
  });

  // toggle button
  $('#editor-toggle').click(function(){
    $('#editor').slideToggle();
  });

  // save button
  $('#save-button').click(clean_up_dom);
});
