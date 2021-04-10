function header() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}


count = 0;
function myFunction(obj) {
  var value = obj.value;
  if (value == "classification") {
    document.getElementById("classimodel").style.display = "block";
    document.getElementById("regmodel").style.display = "none";
    document.getElementById("n").style.display = "block";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";
  }
  else {
    document.getElementById("classimodel").style.display = "none";
    document.getElementById("regmodel").style.display = "block";
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";
  }
  
}

function myFunction2(obj) {
  var value = obj.value;
  console.log(value);
  if (value =="Naive Bayes") {
    document.getElementById("n").style.display = "block";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";

  }
  else if (value == "Knn") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "block";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";
  }
  else if (value == "Decision Trees") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "block";
    document.getElementById("dr").style.display = "block";
    document.getElementById("r").style.display = "none";
  }
  else if (value == "Random Forest") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "block";
    document.getElementById("r").style.display = "block";
  }
}
 
function myFunction3(obj) {
  var value = obj.value;
  console.log(value);

  if (value == "Linear Regression") 
  {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";
  }
  else if (value == "Knn Regression") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "block";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "none";
    document.getElementById("r").style.display = "none";
  }
  else if (value == "Decision Tree Regression") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "block";
    document.getElementById("dr").style.display = "block";
    document.getElementById("r").style.display = "none";
  }
  else if (value == "Random Forest Regression") {
    document.getElementById("n").style.display = "none";
    document.getElementById("k").style.display = "none";
    document.getElementById("d").style.display = "none";
    document.getElementById("dr").style.display = "block";
    document.getElementById("r").style.display = "block";
  }
  
}
