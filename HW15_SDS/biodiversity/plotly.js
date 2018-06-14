function PopulateNames(){
    url="/names";
    Plotly.d3.json(url, function(error, response)
     {
         console.log("PopulateNames:Got Response")
        var select = document.getElementById('selDataset')
        for(var i=0;i<response.length;i++)
        {
        var option = document.createElement('option');
        option.value = response[i];
        option.text=response[i];
        select.appendChild(option)
        }
        Initialize();
    });
    console.log("PopulateNames:End")
}
PopulateNames();