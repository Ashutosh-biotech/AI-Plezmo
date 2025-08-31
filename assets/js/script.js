let i = 1;
let max_val = i + 5;
let add_image = () => {
    if (i < 175) {
        for (i; i < max_val; i++) {
            document.querySelector("#img-row ").innerHTML += `<div class="col-md-6 col-lg-4 item">
                <img class="img-thumbnail img-fluid image mb-2" src="/assets/img/img/img (${i}).jpg" />
              <div class="btn-group" role="group">
                <a class="btn btn-primary" href="/assets/img/img/img (${i}).jpg" download="background~image-${i}_AI-plezmo.png">
                  <i class="fas fa-download"></i>
                </a>
                <a class="btn btn-outline-primary" href="/assets/img/img/img (${i}).jpg" download="AI_plezmo~${i}.jpg" >Download</a>
              </div>
            </div>`;
        }
        max_val = i + 5;
    } else {
        document.querySelector("#load_bg_images").classList.add("hide");
        document.querySelector("#load_bg_images").style.display = "none";
    }
};

function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", "demo_get.asp", true);
    xhttp.send("POST");
}

function load_search_image(image_url) {
    document.querySelector("#load").setAttribute("alt", "Loading...");
    if (navigator.onLine) {
        document
            .querySelector("#load")
            .setAttribute(
                "src",
                `https://source.unsplash.com/1600x900/?${image_url}`
            );
    } else {
        document.querySelector("#load").setAttribute("alt", `You are offline`);
    }
}