// URL for the data source in USGS
const url            = 'Resource/gdp.json';
var row              = [];
var countryTableYear = [];
var countryTableGDP  = [];
var tableData        = [];
var j                = 0;
const colorGradient  = ['rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)',
                       'rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)',
                       'rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)',
                       'rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)',
                       'rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)',
                       'rgb(250, 250, 110)', 'rgb(196, 236, 116)', 
                       'rgb(146, 220, 126)', 'rgb(100, 201, 135)', 
                       'rgb(057, 180, 142)', 'rgb(008, 159, 143)',
                       'rgb(000, 137, 138)', 'rgb(008, 115, 127)', 
                       'rgb(033, 093, 110)', 'rgb(042, 072, 088)',
                       'rgb(042, 052, 066)', 'rgb(033, 033, 033)'];
d3.json(url).then (function(GDPdata) { 

    for (var i = 0; i < GDPdata.length; i++) {
        Country = GDPdata[i].Country;
        if (Country == "United States") {
            countryTableYear[j] = GDPdata[i].Year;
            countryTableGDP[j]  = GDPdata[i].GDP;
            tableData[j]        = {"Year" : countryTableYear[j], "GDP" : countryTableGDP[j] };
            j                   = j + 1;
        }
    }
    console.log('tabeData.length',tableData.length);
    console.log(tableData);
    tabulate('#div1',tableData, ['Year', 'GDP']);
    tabulate('#div3',tableData, ['Year', 'GDP']);
    tabulate('#div5',tableData, ['Year', 'GDP']);

    let barGraph = [{
      x           : countryTableYear,
      y           : countryTableGDP,
      text        : countryTableYear,
      name        : "GDP/Year",
      type        : "bar",
      orientation : "v",
      transforms  : [{ type : 'sort', target : 'y', order : 'descending'}],
      marker      : { color : colorGradient}}];
      let layout1 = { title        : "USA GDP"  , 
                      plot_bgcolor : "Lightskyblue", 
                      paper_bgcolor: "Lightskyblue"};
      Plotly.newPlot("div2"   ,    barGraph, layout1);
      Plotly.newPlot("div4"   ,    barGraph, layout1);
      Plotly.newPlot("div6"   ,    barGraph, layout1);
});

function tabulate(div,data, columns) {
      var table = d3.select(div).append('table')
      var thead = table.append('thead')
      var tbody = table.append('tbody').style('border', '1px solid #000000');;
  
      // append the header row
      thead.append('tr').selectAll('th').data(columns).enter().append('th').text(function (column) { return column; });
  
      // create a row for each object in the data
      var rows = tbody.selectAll('tr').data(data).enter().append('tr');
  
      // create a cell in each row for each column
      var cells = rows.selectAll('td').data(function (row) {
          return columns.map(function (column) {
            return {column: column, value: row[column]};
          });
        })
        .enter()
        .append('td')
          .text(function (d) { return d.value; })
          .style('border', '1px solid #000000');
        d3.selectAll('td').style('text-align', 'right');
    return table;
  }
  


