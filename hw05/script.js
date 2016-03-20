var r_states = ['Samoa','Arizona','Utah','N Dakota','Wisconsin','New York','Conneticut','Delware','Maryland','Pennsylvania','Rhode Island','Indiana','Nebraska','W Virginia','Oregon','Washington','Caifornia','Montana','New Jersey','New Mexico','South Dakota'];
var r_count = [9,58,40,28,42,95,28,16,38,71,19,57,36,34,28,44,172,27,51,24,29];
var d_states = ['Arizona','Idaho','Utah','Arkansas','Hawaii','Washington','Wisconsin','Wyoming','New York','Maryland','Conneticut','Delaware','Pennsylvania','Rhode Island','Indiana','Guam','West Virginia','Kentucky','Oregon','Virgin Islands','Puerto Rico','California','Montana','New Jersey','North Dakota','New Mexico','South Dakota','Washington DC'];
var d_count = [85,27,37,20,34,118,96,14,291,118,70,31,210,33,92,12,37,60,74,12,67,546,27,142,23,43,25,45];
var r = document.getElementById('r');
r.addEventListener('click', function(e){
  d3.select(".chart")
   .selectAll("div")
     .data(r_count)
   .enter().append("div")
    .style("width", function(d){
	     return ""+d*4+"px";
     })
     .text(function(d, i){
   	   return r_states[i]+": "+d;
  }).style("background", function(d) {
  return 'red';
});

});
var d = document.getElementById('d');
d.addEventListener('click', function(e){
  d3.select(".chart")
   .selectAll("div")
     .data(d_count)
   .enter().append("div")
    .style("width", function(d){
	     return ""+(25+(d*1.5)/1)+"px";
     })
     .text(function(d, i){
   	   return d_states[i]+": "+d;
  }).style("background", function(d) {
  return 'blue';
});
});
