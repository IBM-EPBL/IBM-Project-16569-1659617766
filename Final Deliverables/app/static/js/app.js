'use strict';

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

const sidePanelToggler = document.getElementById('sidepanel-toggler'); 
const sidePanel = document.getElementById('app-sidepanel');  
const sidePanelDrop = document.getElementById('sidepanel-drop'); 
const sidePanelClose = document.getElementById('sidepanel-close'); 

window.addEventListener('load', function(){
	responsiveSidePanel(); 
});

window.addEventListener('resize', function(){
	responsiveSidePanel(); 
});


function responsiveSidePanel() {
    let w = window.innerWidth;
	if(w >= 1200) {
		sidePanel.classList.remove('sidepanel-hidden');
		sidePanel.classList.add('sidepanel-visible');
		
	} else {
	    sidePanel.classList.remove('sidepanel-visible');
		sidePanel.classList.add('sidepanel-hidden');
	}
};

sidePanelToggler.addEventListener('click', () => {
	if (sidePanel.classList.contains('sidepanel-visible')) {
		console.log('visible');
		sidePanel.classList.remove('sidepanel-visible');
		sidePanel.classList.add('sidepanel-hidden');
		
	} else {
		console.log('hidden');
		sidePanel.classList.remove('sidepanel-hidden');
		sidePanel.classList.add('sidepanel-visible');
	}
});

sidePanelClose.addEventListener('click', (e) => {
	e.preventDefault();
	sidePanelToggler.click();
});

sidePanelDrop.addEventListener('click', (e) => {
	sidePanelToggler.click();
});

var fileAppended = false;
function checkFileSize(file) {
	let files = file.files;
	if(files.length > 0) {		
		if(files[0].size / 1000000 < 2){ 			
			return true;
		} else{
			return false;
		}
	}	
}


var fileurl = "";

function encodeImageFileAsURL(file) {	
	if (checkFileSize(file)){
		var filesSelected = file.files;
		if (filesSelected.length > 0) {
			var fileToLoad = filesSelected[0];
			var fileReader = new FileReader();
			fileReader.onload = function(fileLoadedEvent) {					 		
				const form = new FormData();
				form.append('image', fileLoadedEvent.target.result.split(',')[1]);
				fetch('https://api.imgbb.com/1/upload?key=f19a785a22fe470efbda931120335907', {
    				method: 'POST',
    				body: form
				}).then(response => response.json())
				.then(data => {
					fileurl = data.data.url;					
					document.getElementById("fileattachmentLabel").innerHTML = `Attached(${data.data.title})`;
				});
			}
			fileReader.readAsDataURL(fileToLoad);
		}
	} else {
		Swal.fire({
			icon: 'error',
			text: 'File Size Greater than 2 MB',
		});
	}
}

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {				
		JSON.parse(this.responseText).data.forEach(element => {
			var opt = document.createElement('option');
			opt.value = element[0];
			opt.innerHTML = `${element[1]} [${element[2]}]`;
			document.getElementById("wallet").append(opt);			
		});
	}
};
xhttp.open("POST", "/get/wallet?wid=all", true);
xhttp.send();

document.getElementById("ttype").addEventListener("change", function () {	
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {	
			document.getElementById("category").innerHTML = '';						 
			JSON.parse(this.responseText).categories.forEach(element => {
				var opt = document.createElement('option');
				opt.value = element.value;
				opt.innerHTML = element.text;
				document.getElementById("category").append(opt)
			});
			;
		}
	};
	xhttp.open("GET", `/static/data/${this.value}.json`, true);
	xhttp.send();
})

document.getElementById("IncExpForm").addEventListener("submit", function (e) {
	e.preventDefault();	
	var form = new FormData(this);
	form.append("attachment", fileurl);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {	
			if (JSON.parse(this.responseText).status == "success") {
				Swal.fire({
					icon: 'success',
					text: 'Added Transaction Successfully',
				}).then((_) => {
					window.location.reload();
				})				
			}
		}
	};
	xhttp.open("POST", `/add/transaction`, true);
	xhttp.send(form);	
})