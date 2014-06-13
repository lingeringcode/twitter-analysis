// load the external data
d3.json("assets/data/cwconCountProper.json", function(error, data) {

  var mouse;
  var margin = {top: 20, right: 10, bottom: 30, left: 50},
    width = 1180 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  var x = d3.scale.ordinal()
      .rangePoints([0,width])
      .domain(data.map(function(d) { 
        // console.log(d.id);
        return d.id; 
      }));

  var y = d3.scale.linear()
      .range([height, 0])
      .domain(d3.extent(data, function(d) { return d.count; }));

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  var line = d3.svg.line()
      .x(function(d) { 
        return x(d.id); 
      })
      .y(function(d) { 
        return y(d.count); 
      });

  var svg = d3.select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".80em")
      .style("text-anchor", "end")
      .text("Word Count");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

  // Want to add an x-axis marker
  // var marker = svg.append('rect')
  //   .attr('width', 2)
  //   .attr('height', height)
  //   .style('display', 'none')
  //   .style('fill', '#FFFFFF')
  //   .style('pointer-events', 'all')
  //   .style('stroke', '#FB5050')
  //   .style('stroke-width', '2px');

  /*=======================================
    Event listeners/handlers
    mouse events for markers not finished
    =======================================*/
  svg.on('mouseover', function() {
      theKey.style('display', 'inherit');
    })
    .on('mouseout', function() {
      mouse = 0;
    })
    .on('mousemove', function() {
      mouse = d3.mouse(this);
      theKey.attr("transform", "translate(" + data[mouse[0]].id + "," + mouse[1] + ")");
      theKey.select("text").text(data[mouse[0]].word + ", " + data[mouse[0]].count);
    });

  var theKey = svg.append("g")
    .attr("class", "theKey")
    .style("display", "none");

  theKey.append("text")
    .attr("x", -35)
    .attr("y", 30)
    .attr("dy", ".55em");

  svg.append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height)
    .on("mouseover", function() { 
      theKey.style("display", null); 
    })
    .on("mouseout", function() {
      theKey.style("display", "none"); 
    });
});