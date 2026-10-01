function getDate() {
    const day = Number(document.getElementById("day").value)
    const month = Number(document.getElementById("month").value)
    const year = Number(document.getElementById("year").value)
    return {day,month,year};
}

function xuatThu()
{
    const {day,month,year} = getDate();
    const options={
        weekday: 'long'
    };
    let myDate = (new Date(year, month-1, day)).toLocaleDateString('vi-VN', options);
    document.getElementById("res").innerHTML = `${myDate} Ngày ${day} tháng ${month} năm ${year}`;
}