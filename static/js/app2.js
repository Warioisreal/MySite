let messages = document.querySelectorAll(".messages li");
setTimeout(function() {
	messages.forEach(function(message) {
		message.remove();
	});
}, 5000);

const togglePasswordButton = document.getElementById("togglePassword");
const togglePasswordButton1 = document.getElementById("togglePassword1");
const togglePasswordButton2 = document.getElementById("togglePassword2");
const passwordInput = document.getElementById("id_password");
const passwordInput1 = document.getElementById("id_password1");
const passwordInput2 = document.getElementById("id_password2");

if (togglePasswordButton) {
	togglePasswordButton.addEventListener("click", function () {
		if (passwordInput.type === "password") {
			passwordInput.type = "text";
			togglePasswordButton.textContent = "H";
			togglePasswordButton.classList.remove("show-password");
			togglePasswordButton.classList.add("hide-password");
		} else {
			passwordInput.type = "password";
			togglePasswordButton.textContent = "S";
			togglePasswordButton.classList.remove("hide-password");
			togglePasswordButton.classList.add("show-password");
		}
	});
}
if (togglePasswordButton1) {
	togglePasswordButton1.addEventListener("click", function () {
		if (passwordInput1.type === "password") {
			passwordInput1.type = "text";
			togglePasswordButton1.textContent = "H";
			togglePasswordButton1.classList.remove("show-password");
			togglePasswordButton1.classList.add("hide-password");
		} else {
			passwordInput1.type = "password";
			togglePasswordButton1.textContent = "S";
			togglePasswordButton1.classList.remove("hide-password");
			togglePasswordButton1.classList.add("show-password");
		}
	});
}
if (togglePasswordButton2) {
	togglePasswordButton2.addEventListener("click", function () {
		if (passwordInput2.type === "password") {
			passwordInput2.type = "text";
			togglePasswordButton2.textContent = "H";
			togglePasswordButton2.classList.remove("show-password");
			togglePasswordButton2.classList.add("hide-password");
		} else {
			passwordInput2.type = "password";
			togglePasswordButton2.textContent = "S";
			togglePasswordButton2.classList.remove("hide-password");
			togglePasswordButton2.classList.add("show-password");
		}
	});
}