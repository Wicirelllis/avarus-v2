var groups = [
    {
        name: "LOCATIONS",
        style: "islands#darkBlueCircleDotIcon",
        items: [],
    },
]

let places = document.getElementById('map-locations').value;
let obj = JSON.parse(places);

groups[0]['items'] = groups[0]['items'].concat(obj);
