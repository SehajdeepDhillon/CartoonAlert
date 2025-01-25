document.addEventListener("DOMContentLoaded", function () {
    const phoneInputField = document.querySelector("#phone");
    const phoneInput = window.intlTelInput(phoneInputField, {
        initialCountry: "ca",
        onlyCountries: ["ca"],
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.12/js/utils.js"
    });

    const form = document.getElementById("phone-form");
    form.addEventListener("submit", function(event) {
        const phoneNumber = phoneInput.getNumber();
        phoneInputField.value = phoneNumber;
    });
});