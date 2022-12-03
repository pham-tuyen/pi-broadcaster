window.onload = () => {
    //Clock module:index.html
    const displayDate = () => {
        setInterval(() => {
            time = new Date();
            document.getElementById("clock").innerText = time;
        }, 1000)
    }
    displayDate();
}