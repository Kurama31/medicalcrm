function first_01() {
        document.getElementById("second_hide_01").setAttribute("style", "opacity:1; transition: 1s; height: 100%;");
        document.getElementById("first_01").setAttribute("style", "display: none");
        document.getElementById("first_yelloy_01").setAttribute("style", "display: block");
        document.getElementById('status_value_id_01').value = '1';
    }

function first_yelloy_01() {
    document.getElementById("second_hide_01").setAttribute("style", "display: none");
    document.getElementById("first_yelloy_01").setAttribute("style", "display: none");
    document.getElementById("first_01").setAttribute("style", "display: block");
    document.getElementById('status_value_id_01').value = '0';
    }