ymaps.ready(init);

function init() {

    // Создание экземпляра карты.
    var map = new ymaps.Map('map',
        {
            center: [70.385555, 68.410034],
            zoom: 5,
            controls: ['zoomControl'],
            behaviors: ['drag', 'scrollZoom'],
            type: 'yandex#satellite',
        },
        {
            searchControlProvider: 'yandex#search',
        }),

        // Контейнер для меню.

        menu = $('<ul class="menu"></ul>');
    for (var i = 0, l = groups.length; i < l; i++) {
        createMenuGroup(groups[i]);
    }

    function createMenuGroup(group) {
        // Пункт меню.
        var menuItem = $('<li class="menuItem"><a type="button">' + group.name + '</a></li>'),
            collection = new ymaps.GeoObjectCollection(null, {preset: group.style}),
            submenu = $('<ul class="submenu list-group"></ul>');

        // Добавляем коллекцию на карту.
        map.geoObjects.add(collection);
        // Добавляем подменю.
        menuItem.append(submenu).appendTo(menu)

        for (var j = 0, m = group.items.length; j < m; j++) {
            createSubMenu(group.items[j], collection, submenu);
        }
    }

    function createSubMenu(item, collection, submenu) {
        // Пункт подменю.
        var submenuItem = $('<li class="subItem list-group-item"><a type="button">' + item.name + '</a></li>'),
            // Создаем метку.
            placemark = new ymaps.Placemark(item.center, {
                    balloonContentHeader: item.ContentHeader.join(''),
                    // Зададим содержимое основной части балуна.
                    balloonContentBody: item.ContentBody.join(''),
                    // Зададим содержимое нижней части балуна.
                    balloonContentFooter: item.ContentFooter.join(''),
                    // Зададим содержимое всплывающей подсказки.
                    hintContent: item.hint.join(''),
                },{
                balloonPane: 'outerBalloon',
                balloonShadowPane: 'shadows'
                }
            );

        // Добавляем метку в коллекцию.S
        collection.add(placemark)
        // Добавляем пункт в подменю.
        submenuItem
            .appendTo(submenu)
            // При клике по пункту подменю открываем/закрываем баллун у метки.
            .bind('click', function () {
                map.panTo([item.center[0], item.center[1]], {flying: true, duration: 800})
                return false;
            })
            .bind('click', function () {
                if (!placemark.balloon.isOpen()) {
                    placemark.balloon.open();
                }
            })
    }

    $(menu).appendTo("#menu_list");

}
