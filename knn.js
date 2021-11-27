

    data = require('./results/prelim_data.json')
        // .then(response => response.json())
        // .then(json => {



    getNProximal(data[0]);


function l2Distance(targetDoc) {


    dataDistances = JSON.parse(JSON.stringify(data)); //deep copy

    dataDistances.forEach(doc => {
        var xDif = targetDoc.x - doc['x'];
        var yDif = targetDoc.y - doc['y'];
        var zDif = targetDoc.z - doc['z'];
        if (targetDoc.document === doc.document){
            doc['distance'] = Number.MIN_VALUE;
        } else {
            doc['distance'] = Math.hypot(xDif, yDif, zDif); //returns sqrt(sum(x,y,z))
        }

    });


}

function getNProximal(targetDoc, n=10) {


    l2Distance(targetDoc);

    dataDistances.sort((i_1, i_2)=>
        i_1.distance - i_2.distance);

    const topN = dataDistances.slice(1,n+1); //ignore target element itself
    return topN;
}


