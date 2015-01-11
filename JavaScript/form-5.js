// Companion code to form-5.html

// Set up function, to attach to onLoad
function setup () {
    formElement = document.getElementById('text');
    writeElement = document.getElementById('write');
    formElement.addEventListener('input', handler);
}
// Handler function, to provide to addEventListener
handler = function (e) {
    writeElement.innerHTML = formElement.value;
};
