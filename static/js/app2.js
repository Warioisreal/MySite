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
function menuBtnChange(a, b) {
	if (a) {
		a.addEventListener("click", function () {
		if (b.type === "password") {
			b.type = "text";
			a.textContent = "H";
			a.classList.remove("show-password");
			a.classList.add("hide-password");
		} else {
			b.type = "password";
			a.textContent = "S";
			a.classList.remove("hide-password");
			a.classList.add("show-password");
		}
	});
	}
}
menuBtnChange(togglePasswordButton, passwordInput);
menuBtnChange(togglePasswordButton1, passwordInput1);
menuBtnChange(togglePasswordButton2, passwordInput2);