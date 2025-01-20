let adrese = window.location.hash;
adrese = decodeURI(adrese);
adrese = adrese.replace('#', '');
adrese = adrese.split(",");
let vards = adrese[0];
let klikski = adrese[1];
let laiks = adrese[2];

let datums = new Date();
let datumsVirkne = datums.getDate() + '.' + (datums.getMonth() + 1) + '.' + datums.getFullYear() + '.';

async function iegutDatusNoApi(url) {
    try {
        let datiNoServera = await fetch(url);
        if (!datiNoServera.ok) {
            throw new Error("Servera atbilde nav veiksmīga: " + datiNoServera.status);
        }
        let datiNoServeraJson = await datiNoServera.json();
        return datiNoServeraJson;
    } catch (error) {
        console.error("Kļūda iegūstot datus no API:", error);
        return [];
    }
}

async function atlasitTop() {
    let topsJson = await iegutDatusNoApi('../result.json'); // Pārliecinies, ka ceļš ir pareizs.
    let tabula = document.querySelector(".tops");

    topsJson.forEach((item) => {
        let rinda = document.createElement('tr');
        rinda.id = item['id'];

        rinda.innerHTML = `
            <td>${item['vards']}</td>
            <td>${item['klikski']}</td>
            <td>${item['laiks']}</td>
            <td>${item['datums']}</td>
        `;
        tabula.appendChild(rinda);
    });
}

atlasitTop();

function pievienotTop() {
    let tabula = document.querySelector('.tops');
    let rinda = document.createElement('tr');
    rinda.id = 'jauns';

    rinda.innerHTML = `
        <td>${vards}</td>
        <td>${klikski}</td>
        <td>${laiks}</td>
        <td>${datumsVirkne}</td>
    `;
    tabula.appendChild(rinda);
}
