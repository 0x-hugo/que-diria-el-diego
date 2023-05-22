document.getElementById('ask-button').addEventListener('click', function() {
    var prompt = encodeURIComponent(document.getElementById('prompt').value);
    let localhost = 'http://localhost:5005';
    let path = '/ask';
    let query = `prompt=${prompt}`;
    fetch(`${localhost}${path}?${query}`)
        .then(function(response) { return response.json(); })
        .then(function(json) {
            console.log(json);
            document.getElementById('response').innerText = json.data;
        });
});
