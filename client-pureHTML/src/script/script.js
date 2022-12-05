setInterval(() => {
    time = new Date();
    document.getElementById("clock").innerText = time;
}, 1000)

var total_index = 0;

const data = document.getElementsByClassName("data");
const tog = document.getElementsByClassName("toggle");
const del = document.getElementsByClassName("del");

const toggle = (n) => {
    tog[n].addEventListener("click", () => {
        if(tog[n].innerHTML === "Sử dụng file cục bộ"){
            tog[n].innerHTML = "Sử dụng danh sách phát trên YouTube";
            document.getElementsByClassName("input")[n].innerHTML = "<input type='file' accept='.mp3'/>"
        }
        else if(tog[n].innerHTML === "Sử dụng danh sách phát trên YouTube"){
            tog[n].innerHTML = "Sử dụng file cục bộ";
            document.getElementsByClassName("input")[n].innerHTML = '<input type="url" placeholder="Nhập liên kết YouTube">';
        }
    })
}

const deleter = (n) => {
    del[n].addEventListener("click", () => {
        data[n].remove();
    })
}

toggle(0);
deleter(0);

document.getElementById("add").addEventListener("click", () => {
    document.getElementById("config").innerHTML += '<tr class="data"><td class="input"><input type="url" class="url" placeholder="Nhập liên kết YouTube"></input></td>    <td>        <input type="time" class="time" placeholder="Nhập giờ">       </td>    <td>        <button class="toggle">Sử dụng file cục bộ</button>        <button class="del">Xoá</button>    </td></tr>';
    ++total_index;
    for(var i = 0; i <= total_index; i++) {
        toggle(i);
        deleter(i);
    }
})