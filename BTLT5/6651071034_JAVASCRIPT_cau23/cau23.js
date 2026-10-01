function tinhLuong()
{
    const luong = document.getElementById("salary").value;
    const heSoLuong = document.getElementById("he-soLuong").value;
    const res = luong*heSoLuong;
    document.getElementById("res").innerHTML = `${res}`;
}