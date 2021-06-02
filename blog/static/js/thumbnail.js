
document.getElementById("id_thumbnail").addEventListener('change', 

function preview(event) {
    var input = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function() {
        var result = reader.result;
        const img = document.getElementById("img");
        img.setAttribute("src",this.result)
    }
    reader.readAsDataURL(input);
}

);
      

function chooseFile() {
    document.getElementById("id_thumbnail").click();
 }


$("div").contents().filter(function() {
    return this.nodeType === 3;
}).wrap("<p>"); 