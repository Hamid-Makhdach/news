let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick=()=>{
  menu.classList.toggle('bx-x');
  navbar.classList.toggle('open');
} ;


$(document).ready(function() {
  $("#toggleList").click(function() {
    $(".page-list").toggleClass("hidden");
  });
})





$readMoreJS.init({
  target: '.dummy p',           // Selector of the element the plugin applies to (any CSS selector, eg: '#', '.'). Default: ''
  numOfWords: 55,               // Number of words to initially display (any number). Default: 50
  toggle: true,                 // If true, user can toggle between 'read more' and 'read less'. Default: true
  moreLink: 'read more...',    // The text of 'Read more' link. Default: 'read more ...'
  lessLink: 'read less'         // The text of 'Read less' link. Default: 'read less'
});