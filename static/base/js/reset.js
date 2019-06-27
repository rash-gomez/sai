$(document).ready(function () {

    let country = document.querySelector('#countryId');
    let state = document.querySelector('#stateId');
    let city = document.querySelector('#cityId');
    let dob = document.querySelector('#id_dob');
    let mode = document.querySelector('#id_mode');
    let level = document.querySelector('#id_level');
    let field = document.querySelector('#id_field');
    let speciality = document.querySelector('#id_speciality');
    let session = document.querySelector('#id_session');
    let gender = document.querySelector('#id_gender');

    dob.setAttribute('autocomplete', 'off');

    country_option = document.createElement('option');
    state_option = document.createElement('option');
    city_option = document.createElement('option');
    // mode_option = document.createElement('option');
    // level_option = document.createElement('option');
    // field_option = document.createElement('option');
    // speciality_option = document.createElement('option');
    // session_option = document.createElement('option');
    // gender_option = document.createElement('option');

    country_option.innerHTML = 'Select Country';
    state_option.innerHTML = 'Select State';
    city_option.innerHTML = 'Select City';

    mode.firstElementChild.innerHTML = 'Select Mode';
    level.firstElementChild.innerHTML = 'Select level';
    field.firstElementChild.innerHTML = 'Select Field';
    speciality.firstElementChild.innerHTML = 'Select Speciality';
    session.firstElementChild.innerHTML = 'Select Session';
    gender.firstElementChild.innerHTML = 'Select Gender';

    country.append(country_option)
    state.append(state_option)
    city.append(city_option)



    // toggle display on level select

    let student_level = document.querySelector("#id_level");
    let bts1 = document.querySelector("#id_bts1");
    let bts2 = document.querySelector("#id_bts2");
    let bachelor = document.querySelector("#id_bachelor");

    // dynamic selections with respect to the "level field" and removing the required attribute
    student_level.addEventListener("change", item => {
        if (level.options[level.selectedIndex].value == "BTS1") {
            bts1.parentElement.style.display = "none";
            bts1.parentElement.querySelector("input").removeAttribute("required");
            bts2.parentElement.style.display = "none";
            bts2.parentElement.querySelector("input").removeAttribute("required");
            bachelor.parentElement.style.display = "none";
            bachelor.parentElement.querySelector("input").removeAttribute("required");
        } else if (level.options[level.selectedIndex].value == "BTS2") {
            bts2.parentElement.style.display = "none";
            bts1.parentElement.style.display = "block";
            bts2.parentElement.querySelector("input").removeAttribute("required");
            bachelor.parentElement.style.display = "none";
            bachelor.parentElement.querySelector("input").removeAttribute("required");
        } else if (level.options[level.selectedIndex].value == "LICENCE") {
            bts1.parentElement.style.display = "block";
            bts2.parentElement.style.display = "block";
            bachelor.parentElement.style.display = "none";
            bachelor.parentElement.querySelector("input").removeAttribute("required");
        }
    });

})