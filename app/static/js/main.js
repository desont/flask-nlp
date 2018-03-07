
document.write("<script type='text/javascript' src='/static/js/Chart.js'></script>")

function getjiebadata(){
    var input = document.querySelector("#content").value

    $.post("/jieba",{content:input})
    .done(function(data){

        loadChart(data)
        maxnum = Math.min(30,data.length)
        let atx =''
        for(let i = 0; i < maxnum; i++) {
            u=data[i][0]
            n=data[i][1]
            atx = atx + u+":"+n+ "<br>"

        }

        document.querySelector("#nh1").innerHTML = atx
    })
    .fail(function(){
        alert("jieba error")
    })
}

function loadChart(rawData) {

    const ctxRef = document.querySelector('#data-chart');

    let labels = [];
    let counts = [];
    let colors = [];
    maxnum = Math.min(30,rawData.length)
    for(let i = 0; i < maxnum; i++) {
      labels.push(rawData[i][0]);
      counts.push(rawData[i][1]);
      colors.push(getRandomColor())
    }


    const data = {
        labels: labels,
        datasets: [{
            data: counts,
            backgroundColor: colors,
        }]
    };

    const myPieChart = new Chart(ctxRef, {
    type: 'pie',
        data: data,
    });

}

function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}