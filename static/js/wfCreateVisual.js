// URL for the data source
const urlGDP            = 'Resource/gdp.json';
const urlBRT            = 'Resource/birth_rate.json';
const urlPOP            = 'Resource/population.json';
                           
function getYear() {
  // first table and graph
  d3.json(urlGDP).then (function(GDPdata) { 
    var parmYear            = 0;
    var i                   = 0;
    var j                   = 0;
    var countryCodes        = [];
    var countryNames        = [];
    var countryGDP          = [];
    var graphTable          = [];
    d3.select("yearGraph1").dispatch("change");
    parmYear = d3.select("#yearGraph1").property("value");
    console.log('get year: ' + parmYear);
    for (i = 0; i < GDPdata.length; i++) {
      if (GDPdata[i].Year == parmYear) {
          countryCodes[j]        = GDPdata[i].Country_Code;
          countryNames[j]        = GDPdata[i].Country;
          countryGDP[j]          = GDPdata[i].GDP;
          graphTable[j]          = {"Country" : countryCodes[j], "GDP" : countryGDP[j] };
          j                      += 1;
      }
    }
    if (j > 0 ) {
      d3.select("#div2").selectAll("table").remove();
      tabulate('#div2',graphTable, ['Country', 'GDP']);
      let barGraph = [{
        x           : countryCodes,
        y           : countryGDP,
        text        : countryNames,
        name        : "GDP/World",
        type        : "bar",
        orientation : "v",
        marker      : { color         : "blue"}}];
        let layout  = { title        : "World GDP " + parmYear  , 
                        xaxis         : { linecolor: 'black', linewidth: 1, mirror: true },
                        yaxis         : { linecolor: 'black', linewidth: 1, mirror: true },
                        plot_bgcolor  : "Lightskyblue", 
                        paper_bgcolor : "Lightskyblue"
                      };
      Plotly.newPlot("div4", barGraph, layout);
    };
  });
}

function getCountryCode() {
  // GDP DATA AND GRAPH STARTS HERE
  d3.json(urlGDP).then (function(GDPdata) { 
    var parmCountry         = 0;
    var i                   = 0;
    var j                   = 0;
    var countryCode         = "";
    var countryName         = "";
    var countryYears        = [];
    var countryGDP          = [];
    var countryBRT          = [];
    var countryPOP          = [];
    var countryPOPG100      = [];
    var countryF15_T64      = [];
    var countryE01          = [];
    var graphTable          = [];
    d3.select("countryCodeGraph1").dispatch("change");
    parmCountry = d3.select("#countryCodeGraph2").property("value");
    console.log('get country code: ' + parmCountry);
    for (i = 0; i < GDPdata.length; i++) {
        countryCode = GDPdata[i].Country_Code;
        if (countryCode == parmCountry) {
            countryName            = GDPdata[i].Country;
            countryYears[j]        = GDPdata[i].Year;
            countryGDP[j]          = GDPdata[i].GDP;
            graphTable[j]          = {"Year" : countryYears[j], "GDP" : countryGDP[j] };
            j                      += 1;
        }
    }

    if (j > 0 ) {
      d3.select("#div6").selectAll("table").remove();      
      tabulate('#div6',graphTable, ['Year', 'GDP']);
      let barGraph = [{
        x           : countryYears,
        y           : countryGDP,
        text        : countryYears,
        name        : "GDP/Year",
        type        : "line",
        orientation : "v",
        marker      : { color          : 'blue'}}];
        let layout  = { title          : countryName + " GDP"  , 
                         xaxis         : { linecolor: 'black', linewidth: 1, mirror: true },
                         yaxis         : { linecolor: 'black', linewidth: 1, mirror: true },
                         plot_bgcolor  : "Lightskyblue", 
                         paper_bgcolor : "Lightskyblue"
                      };
      Plotly.newPlot("div8", barGraph, layout);
      // BIRTH RATE DATA AND GRAPH STARTS HERE
      d3.json(urlBRT).then (function(BRTdata) { 
        i                   = 0;
        j                   = 0;
        countryCode         = "";
        countryName         = "";
        countryYears        = [];
        countryBRT          = [];
        graphTable          = [];
        for (i = 0; i < BRTdata.length; i++) {
            countryCode = BRTdata[i].Country_Code;
            if (countryCode == parmCountry) {
                countryName           = BRTdata[i].Country;
                countryYears[j]       = BRTdata[i].Year;
                countryBRT[j]         = BRTdata[i].Birth_Rate;
                graphTable[j]         = {"Year" : countryYears[j], "Birth_Rate" : countryBRT[j] };
                j                    += 1;
            }
        }
        if (j > 0 ) {
          d3.select("#div10").selectAll("table").remove();
          tabulate('#div10',graphTable, ['Year', 'Birth_Rate']);
          let barGraph = [{
            x           : countryYears,
            y           : countryBRT,
            text        : countryYears,
            name        : "Birth Rate/Year",
            type        : "line",
            orientation : "V",
            marker      : { color : "red"}}];
            let layout = { title : countryName + " Birth Rate"  , 
                            xaxis : { linecolor: 'black', linewidth: 1, mirror: true },
                            yaxis : { linecolor: 'black', linewidth: 1, mirror: true },
                            plot_bgcolor : "Lightskyblue", 
                            paper_bgcolor: "Lightskyblue"
                          };
          Plotly.newPlot("div12"   ,    barGraph, layout);
        };
        // POPULATION DATA AND GRAPH STARTS HERE
        d3.json(urlPOP).then (function(POPdata) { 
          i                   = 0;
          j                   = 0;
          countryYears        = [];
          countryPOP          = [];
          countryPOPG100      = [];
          countryF15_T64      = [];
          countryF60_T69      = [];
          countryE01          = [];
          graphTable          = [];
          for (i = 0; i < POPdata.length; i++) {
              Country = POPdata[i].Country;
              if (Country == countryName) {
                  countryYears[j]   = POPdata[i].Year;
                  countryPOP[j]     = POPdata[i].pop;
                  countryE01[j]     = POPdata[i].pop_e01;
                  countryF15_T64[j] = POPdata[i].pop_f15_t64;
                  countryF60_T69[j] = POPdata[i].pop_f60_t69; //pop_f60_t69
                  countryPOPG100[j] = POPdata[i].pop_g100;
                  graphTable[j]    = {'Year'       : countryYears[j], 
                                       'Population' : countryPOP[j], 
                                       'POPE01'     : countryE01[j],
                                       'POPF15_T64' : countryF15_T64[j],
                                       'POPF60_T69' : countryF60_T69[j],
                                       'POPG100'    : countryPOPG100[j]
                                       };
                  j                    += 1;
              }
          }
          if (j > 0 ) {
            d3.select("#div14").selectAll("table").remove();
            tabulate('#div14',graphTable, ['Year', 
                                            'Population', 
                                            'POPE01',
                                            'POPF15_T64',
                                            'POPF60_T69',
                                            'POPG100']);
            var Population = {
              x      : countryYears,
              y      : countryPOP,
              type   : 'line',
              mode   : 'lines',
              name   : 'Population',
              marker : { color : "lightgreen"}
            };
            var PopulationE01 = {
              x      : countryYears,
              y      : countryE01,
              type   : 'line',
              mode   : 'lines',
              name   : 'Population exact 1',
              marker : { color : "magenta"}
            };
            var PopulationF15T64 = {
              x      : countryYears,
              y      : countryF15_T64,
              type   : 'line',
              mode   : 'lines',
              name   : 'Population from 15 to 64',
              marker : { color : "cyan"}
            };
            var PopulationF60T69 = {
              x      : countryYears,
              y      : countryF60_T69,
              type   : 'line',
              mode   : 'lines',
              name   : 'Population from 60 to 69',
              marker : { color : "darkblue"}
            };
            var PopulationG100 = {
              x      : countryYears,
              y      : countryPOPG100,
              type   : 'line',
              mode   : 'lines',
              name   : 'Population over 100',
              marker : { color : "red"}
            };
            var data   = [Population, PopulationE01, PopulationF15T64, PopulationF60T69, PopulationG100, ] ;
            var layout = {
              grid          : {rows: 1, columns: 1 , pattern: 'independent'},
              title         : countryName + " Population by Age Range",
              plot_bgcolor  : "Lightskyblue", 
              paper_bgcolor : "Lightskyblue",
              xaxis: { type : 'log',autorange: true, linecolor: 'black', linewidth: 1, mirror: true },
              yaxis: { type : 'log',autorange: true, linecolor: 'black', linewidth: 1, mirror: true },
            };
            Plotly.newPlot('div18', data, layout);
          };
        });
      });
    }
  });
}

function tabulate(div,data, columns) {
  var table = d3.select(div).append('table')
  var thead = table.append('thead')
  var tbody = table.append('tbody').style('border', '1px solid #FFFFFF');;
  // append the header row
  thead.append('tr').selectAll('th').data(columns).enter().append('th').text(function (column) { return column; });
  // create a row for each object in the data
  var rows = tbody.selectAll('tr').data(data).enter().append('tr');
  // create a cell in each row for each column
  var cells = rows.selectAll('td').data(function (row) {
      return columns.map(function (column) {
        return {column: column, value: row[column]};
      });
    }).enter()
      .append('td')
      .text(function (d) { return d.value; })
      .style('border', '1px solid #FFFFFF');
    d3.selectAll('td').style('text-align', 'right');
  return table;
}
