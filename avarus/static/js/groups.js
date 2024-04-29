var groups = [
    {
        name: "LOCATIONS",
        style: "islands#darkBlueCircleDotIcon",
        items: [
            {
                center: [75.542377, 105.377932],
                name: "34. Taymyr dataset (Elena and Igor Pospelovy)",
                ContentHeader:['<a>Taymyr dataset</a><br>' +
                '<span class="description">(Elena and Igor Pospelovy)</span><hr class="hr1"/>'],
                ContentBody:['<a href="#">\n' + '\n' + 'Location Map</a><br/>' + '<img src="../media/pictures/Photonone.png" height="150" width="200"> <br/> ' +
                '<br/> <a type="button" class="btn btn-info"  href=\'javascript: document.location.href = "/taymyr/";\' style="color:white">Open</a>',],
                ContentFooter:['Number of Plots:<br/>470 plots'],
                hint: ['<div class="map__hint">','Taymyr dataset','</div>']
            },
            {
                center: [70.768143, 149.118690],
                name: "35. Indigirka dataset (Mikhail Telyatnikov and Elena Troeva)",
                ContentHeader:['<a>Indigirka dataset</a><br>' +
                '<span class="description">(Mikhail Telyatnikov, Elena Troeva)</span><hr class="hr1"/>'],
                ContentBody:['<a href="#">\n' + '\n' + 'Location Map</a><br/>' + '<img src="../media/pictures/Indigirka.JPG" height="150" width="200"> <br/> ' +
                '<br/> <a type="button" class="btn btn-info"  href=\'javascript: document.location.href = "/indigirka-dataset/";\' style="color:white">Open</a>',],
                ContentFooter:['Number of Plots:<br/>133 plots'],
                hint: ['<div class="map__hint">','Indigirka dataset','</div>']
            },
        ]},
]

let places = document.getElementById('map-locations').value;
let obj = JSON.parse(places);

groups[0]['items'] = groups[0]['items'].concat(obj);
groups[0]['items'].pop();
