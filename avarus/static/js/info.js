

var feedback = document.querySelector('.feedback');
var open = document.querySelector('.open');
feedback.style.display = 'none'


open.addEventListener("click",      function() {

    if(feedback.style.display == 'none') feedback.style.display = 'block';
    else feedback.style.display = 'none'

  });


function checkParams() {
    const name = $('#Name1').val();
    const name_space = $('#Name_space1').val();
    const login = $('#Login1').val();
    const organization = $('#Organization1').val();
    const position = $('#Position1').val();
    const email = $('#Email1').val();
    const description = $('#Description1').val();


    if(name.length !== 0 && email.length !== 0 && name_space.length !== 0 && login.length !== 0
    && organization.length !== 0 && position.length !== 0 && description.length !== 0) {
        $('#submit').removeAttr('disabled');
    } else {
        $('#submit').attr('disabled', 'disabled');
    }
}