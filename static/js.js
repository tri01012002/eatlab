// script.js

document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault(); 
 
    var fileInput = document.querySelector("input[type='file']");
    var file = fileInput.files[0];
    if (!file) {
        alert("choose file!");
        return;
    }

    var formData = new FormData();
    formData.append("file", file);


    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())  
    .then(data => {
        console.log("result:", data);

      
        if (data.message) {
            alert(data.message);  
        }

        
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = '';  
        if (data.output_file) {
            const video = document.createElement("video");
            video.src = data.output_file;
            video.controls = true;
            video.width = 640;
            resultDiv.appendChild(video);
        } else {
            
            const img = document.createElement("img");
            img.src = data.output_file;
            img.width = 640;
            resultDiv.appendChild(img);
        }
    })
    .catch(error => {
        console.error("Có lỗi xảy ra:", error);
        alert("error");
    });
});
