function greet() {
    let name = document.querySelector('#name').value;

    if (name === '') {
        name = 'stranger';
    }
    else {
        document.querySelector('#result').innerHTML = 'Hello, '+ name +'! Have a cookie. 🍪';
    }   
}