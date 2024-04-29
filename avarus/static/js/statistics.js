$('.mobile-menu').on('click', function (e){
    e.preventDefault();
    $('.menu-btn').toggleClass('menu-active')
    $('.nav-panel').toggleClass('menu-active')
})


$('.map-box').on('click', function (e){
    e.preventDefault();
    $('.map-box-btn').toggleClass('map-active')
    $('.resize').toggleClass('map-active')
})
$('.subItem .button').on('click', function (e){
    e.preventDefault();
    $('.resize').toggleClass('map-move')
})
document.querySelector('#elastic_statistics').oninput = function () {
    let val = this.value.trim();
    let elasticItems = document.querySelectorAll('.list-group-item__statistics-column');
    if (val) {
        elasticItems.forEach(function (elem) {
            if (elem.innerText.search(val) == -1) {
                elem.style.display = "none";
                // elem.innerHTML = elem.innerText;
            } else {
                elem.style.display = "block";
                let str = elem.innerText;
            }
        });
    } else {
        elasticItems.forEach(function (elem) {
                elem.style.display = "block";
            }
        );
    }
}

document. getElementById('select-all'). onclick = function() {
    var checkboxes = document. querySelectorAll('input[name="columns"]');
    for (var checkbox of checkboxes) {
        checkbox. checked = this. checked;
    }}

document. getElementById('select-all-env'). onclick = function() {
    var checkboxes = document. querySelectorAll('input[name="columns_env"]');
    for (var checkbox of checkboxes) {
        checkbox. checked = this. checked;
    }}