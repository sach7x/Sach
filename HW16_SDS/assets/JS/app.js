// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

var svgWidth = 1000;
var svgHeight = 750;

var margin = {
    top: 50,
    right: 50,
    bottom: 100,
    left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// create SVG wrapper
var svg = d3
.select('.chart')
.append('svg')
.attr('width', svgWidth)
.attr('height', svgHeight);

// append SVG group
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// initial params
var chosenXAxis = "disability";
// append tooltip
d3.select('.chart')
  .append('div')
  .attr('class', 'tooltip');

// // retrieve data from CSV file and execute everything below
d3.csv('./../../data/data.csv', function(wellnessData) {
    // if (err) throw err;
console.log(wellnessData);
//parse data
wellnessData.forEach(function(data) {
    data.disability = +data.disability;
    data.depression = +data.depression;
});

// function used for updating x-scale var upon click on axis label
function xScale(depression, chosenXAxis) {
    // create scales
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(depression, d => d[chosenXAxis]) * 0.8,
        d3.max(depression, d => d[chosenXAxis]) * 1.2
      ])
      .range([0, width]);
  
    return xLinearScale;
  
  }
// xLinearScale function above csv import
var xLinearScale = xScale(wellnessData, chosenXAxis);

// create y scale function
var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(wellnessData, d => d.depression)])
    .range([height, 0]);

// create initial axis functions
var bottomAxis = d3.axisBottom(xLinearScale);
var leftAxis = d3.axisLeft(yLinearScale);

//append x axis
chartGroup.append("g")
.classed("x-axis", true)
.attr("transform", `translate(0, ${height})`)
.call(bottomAxis);

// append x axis labels..can use orient bottom?
chartGroup.append("text")
//    .attr("transform", "translate(" + (chartWidth/3) + "," + (chartHeight + margin.top + 30) + ")") 
    .attr("transform", `translate(${width / 1.5}, ${height + 20})`)    
    .attr("class", "axisText")
    .text("Percentage of the Population with a Disability");

// append y axis
chartGroup.append("g")
    .call(leftAxis);

// append y axis labels..can also use orient left?
chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height/1.5))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Percentage of the Population with Depression");

// make tooltip functional
var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(data) {
        var state = data.state;
        var disabilityRate = +data.disability;
        var depressionRate = +data.depression;
        return (state + "<br> Disability Rate: " + disabilityRate + "%" + "<br> Percentage of population suffering from depression: " + depressionRate + "%");
    })

chartGroup.call(toolTip);

// append all datapoints as circles to chart
var circlesGroup = chartGroup.selectAll("circle")
.data(wellnessData)
.enter()
.append("circle")
//.attr("cx", d=> xLinearScale(d.disability)) <--same?
.attr("cx", d => xLinearScale(d[chosenXAxis]))
.attr("cy", d => yLinearScale(d.depression))
.attr("r", 20)
.attr("fill", "blue")
.attr("opacity", ".5")
.on("click", function(data) {
    toolTip.show(data);
})

// mousout event
.on("mousout", function(data, index) {
    toolTip.hide(data);
});

});

