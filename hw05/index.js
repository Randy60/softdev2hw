var r_states = ['Iowa','New Hampshire','South Carolina','Nevada','Alabama','Alaska','Arkansas','Georgia','Massachusets','Minnesota','Oklahoma','Tennessee','Texas','Vermont','Virginia','Kansas','Kentucky','Louisiana','Maine','Puerto Rico','Hawaii','Idaho','Michigan','Mississippi',
'Virgin Islands','Washington D.C.','Guam','Florida','Illinois','Montana', 'North Carolina','Marianas','Ohio',
'Samoa','Arizona','Utah','N Dakota','Wisconsin','New York','Conneticut','Delware','Maryland','Pennsylvania','Rhode Island','Indiana','Nebraska','W Virginia','Oregon','Washington','Caifornia','Montana','New Jersey','New Mexico','South Dakota'];
var r_count = [30,23,50,30,50,28,40,76,42,38,43,58,155,16,49,40,46,46,23,23,19,32,59,40,9,19,9,99,69,52,72,9,66,9,58,40,28,42,95,28,16,38,71,19,57,36,34,28,44,172,27,51,24,29];
//if i<32, delegates allocated
var democrats = [
    {state: "Iowa", count: 44, allocated: 1},
    {state: "New Hampshire", count: 24, allocated: 1},
    {state: "Nevada", count: 35, allocated: 1},
    {state: "South Carolina", count: 53, allocated: 1},
    {state: "Alabama", count: 53, allocated: 1},
    {state: "Arkansas", count: 32, allocated: 1},
    {state: "Colorado", count: 66, allocated: 1},
    {state: "Georgia", count: 102, allocated: 1},
    {state: "Massachusetts", count: 91, allocated: 1},
    {state: "Minnesota", count: 77, allocated: 1},
    {state: "Oklahoma", count: 38, allocated: 1},
    {state: "Tennessee", count: 67, allocated: 1},
    {state: "Texas", count: 222, allocated: 1},
    {state: "Vermont", count: 16, allocated: 1},
    {state: "Virginia", count: 95, allocated: 1},
    {state: "Louisiana", count: 51, allocated: 1},
    {state: "Nebraska", count: 25, allocated: 1},
    {state: "Kansas", count: 33, allocated: 1},
    {state: "Maine", count: 25, allocated: 1},
    {state: "Mississippi", count: 36, allocated: 1},
    {state: "Michigan", count: 130, allocated: 1},
    {state: "Florida", count: 214, allocated: 1},
    {state: "Illinois", count: 156, allocated: 1},
    {state: "Missouri", count: 71, allocated: 1},
    {state: "North Carolina", count: 107, allocated: 1},
    {state: "Ohio", count: 143, allocated: 1},
    {state: "Arizona", count: 75, allocated: 0},
    {state: "Idaho", count: 23, allocated: 0},
    {state: "Utah", count: 33, allocated: 0},
    {state: "Alaska", count: 16, allocated: 0},
    {state: "Hawaii", count: 25, allocated: 0},
    {state: "Washington", count: 101, allocated: 0},
    {state: "Wisconsin", count: 86, allocated: 0},
    {state: "Wyoming", count: 14, allocated: 0},
    {state: "New York", count: 247, allocated: 0},
    {state: "Maryland", count: 95, allocated: 0},
    {state: "Connecticut", count: 55, allocated: 0},
    {state: "Delaware", count: 21, allocated: 0},
    {state: "Pennsylvania", count: 189, allocated: 0},
    {state: "Rhode Island", count: 24, allocated: 0},
    {state: "Indiana", count: 83, allocated: 0},
    {state: "West Virginia", count: 29, allocated: 0},
    {state: "Kentucky", count: 55, allocated: 0},
    {state: "Oregon", count: 61, allocated: 0},
    {state: "California", count: 475, allocated: 0},
    {state: "Montana", count: 21, allocated: 0},
    {state: "New Jersey", count: 126, allocated: 0},
    {state: "North Dakota", count: 18, allocated: 0},
    {state: "New Mexico", count: 34, allocated: 0},
    {state: "South Dakota", count: 20, allocated: 0},
    {state: "District of Columbia", count: 20, allocated: 0}
];
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
  }).style("background", function(d,i) {
  return 'rgb('+255+','+70*(i>32)+','+100*(i>32)+')';
});

});
var d = document.getElementById('d');
d.addEventListener('click', function(e){
  d3.select(".chart")
   .selectAll("div")
     .data(democrats)
   .enter().append("div")
    .style("width", function(d){
	     return ""+(20+(d.count*1.5)/1)+"px";
     })
     .text(function(d, i){
   	   return d.state+": "+d.count;
  }).style("background", function(d) {
  return 'rgb('+(!d.allocated)*70+','+(!d.allocated)*100+','+(255)+')';
});
});
