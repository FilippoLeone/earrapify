function setAudioLabel(){
    var audioLevel = document.querySelector('#audioLevel').valueAsNumber;
    document.querySelector('#audioLevelText').innerText = "Boost level: " + audioLevel + " dB.";
}

function setFileName(){
    var fileName = document.querySelector('#inputGroupFile01').files[0].name || "Choose file";
    document.querySelector('#fileLabel').innerText = fileName;
}

function uploadFile(file) {
    let formData = new FormData();
    let musicFile = file.files[0];      
         
    formData.append("file", musicFile);
    formData.append("volume", document.querySelector('#audioLevel').valueAsNumber);

    var xhr = new XMLHttpRequest();
    xhr.open('post', '/process', true);

    xhr.onreadystatechange = function () {
          if (xhr.status === 200 && xhr.readyState == 4) {
            let response = JSON.parse(xhr.responseText);
            showDownloadButton(response);
          }
      };
      xhr.send(formData);
}

function showDownloadButton(filename) {
    document.querySelector("#download-block").style = 'display:block;';
    document.querySelector('#downloadButton').href = '/download?filename=' + filename['filename'];
}