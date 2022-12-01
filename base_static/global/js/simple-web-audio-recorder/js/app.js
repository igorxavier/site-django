//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var recorder; 						//WebAudioRecorder object
var input; 							//MediaStreamAudioSourceNode  we'll be recording
var encodingType; 					//holds selected encoding for resulting audio (file)
var encodeAfterRecord = true;       // when to encode

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext; //new audio context to help us record

var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");

//add events to those 2 buttons
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
stopButton.classList.toggle("hidden")

function startRecording() {
	console.log("startRecording() called");

	/*
		Simple constraints object, for more advanced features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/
    
    var constraints = { audio: true, video:false }

    /*
    	We're using the standard promise based getUserMedia() 
    	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
	*/

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {

		/*
			create an audio context after getUserMedia is called
			sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
			the sampleRate defaults to the one set in your OS for your playback device

		*/
		audioContext = new AudioContext();

		//assign to gumStream for later use
		gumStream = stream;
		
		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);

		recorder = new WebAudioRecorder(input, {
		  workerDir: "js/", // must end with slash
		  encoding: 'mp3',
		  numChannels:2, //2 is the default, mp3 encoding supports only 2
		  onEncoderLoading: function(recorder, encoding) {
		    // show "loading encoder..." display
		  },
		  onEncoderLoaded: function(recorder, encoding) {
		    // hide "loading encoder..." display
		  }
		});

		recorder.onComplete = function(recorder, blob) { 
			createDownloadLink(blob,recorder.encoding);
		}

		recorder.setOptions({
		  timeLimit:120,
		  encodeAfterRecord:encodeAfterRecord,
	      ogg: {quality: 0.5},
	      mp3: {bitRate: 160}
	    });

		//start the recording process
		recorder.startRecording();

	}).catch(function(err) {
	  	//enable the record button if getUSerMedia() fails
    	recordButton.disabled = false;
		recordButton.classList.toggle("hidden")
    	stopButton.disabled = true;
		stopButton.classList.toggle("hidden")

	});

	//disable the record button
    recordButton.disabled = true;
	recordButton.classList.toggle("hidden")
    stopButton.disabled = false;
	stopButton.classList.toggle("hidden")
}

function stopRecording() {
	console.log("stopRecording() called");
	
	//stop microphone access
	gumStream.getAudioTracks()[0].stop();

	//disable the stop button
	stopButton.disabled = true;
	stopButton.classList.toggle("hidden")
	recordButton.disabled = false;
	recordButton.classList.toggle("hidden")
	
	//tell the recorder to finish the recording (stop recording + encode the recorded audio)
	recorder.finishRecording();
}

function createDownloadLink(blob,encoding) {

	recordedAudio.src = URL.createObjectURL(blob);                   
	recordedAudio.controls = true;
	recordedAudio.autoplay = true;

	let file = new File([blob], 'audio.mp3', {
		type: blob.type,
		lastModified: Date.now()
	});

	let container = new DataTransfer(); 
	container.items.add(file);
	audio_field.files = container.files;
	
}
