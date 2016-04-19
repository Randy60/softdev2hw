var base = "long string thingy";
var base2 = "short string";
var f2 = function(){
  console.log("yet another string");
}

var f1 = {
  base : "thing to go with long string",
  base2 : "thing to go with short string",
  k : function() {
    console.log("a: "+base);
    console.log("b: "+f1.base);
    console.log("c: "+this.base);
  } ,
  a : f2 ,
};



var makeAdder = function(n){
  var i = 0;
    return function(){
      i+=n;
      return i;
    }
}
makeIncrementer = makeAdder(1);
inc = makeIncrementer;
