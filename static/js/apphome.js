let messages = document.querySelectorAll(".messages li");
setTimeout(function() {
	messages.forEach(function(message) {
		message.remove();
	});
}, 5000);