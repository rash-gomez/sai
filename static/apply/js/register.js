window.onload = function() {
  let level = document.querySelector("#id_level");
  let bts1 = document.querySelector("#id_bts1");
  let bts2 = document.querySelector("#id_bts2");
  let bachelor = document.querySelector("#id_bachelor");

  // dynamic selections with respect to the "level field" and removing the required attribute
  level.addEventListener("change", item => {
    if (level.options[level.selectedIndex].value == "bts1") {
      bts1.style.display = "none";
      bts1.querySelector("input").removeAttribute("required");
      bts2.style.display = "none";
      bts2.querySelector("input").removeAttribute("required");
      bachelor.style.display = "none";
      bachelor.querySelector("input").removeAttribute("required");
    } else if (level.options[level.selectedIndex].value == "bts2") {
      bts2.style.display = "none";
      bts1.style.display = "block";
      bts2.querySelector("input").removeAttribute("required");
      bachelor.style.display = "none";
      bachelor.querySelector("input").removeAttribute("required");
    } else if (level.options[level.selectedIndex].value == "bachelor") {
      bts1.style.display = "block";
      bts2.style.display = "block";
      bachelor.style.display = "none";
      bachelor.querySelector("input").removeAttribute("required");
    }
  });

};


// this is for a date picker
//$(function () {
//    $("#id_expiry_date").datepicker({
//        format: 'yyyy-mm-dd',
//    });
//});