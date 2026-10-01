const thienCan = {
    0: "Canh",
    1: "Tân",
    2: "Nhâm",
    3: "Quý",
    4: "Giáp",
    5: "Ất",
    6: "Bính",
    7: "Đinh",
    8: "Mậu",
    9: "Kỷ"
};

const diaChi = {
    0: "Thân",
    1: "Dậu",
    2: "Tuất",
    3: "Hợi",
    4: "Tý",
    5: "Sửu",
    6: "Dần",
    7: "Mão",
    8: "Thìn",
    9: "Tỵ",
    10: "Ngọ",
    11: "Mùi"
};

function getYear() {
    let inputYear = Number(document.getElementById("year").value);
    return inputYear;
}

function yearValidate(year) {
    return year <=0;
}

function tinhCanChi() {
    let inputYear = getYear();
    if (yearValidate(inputYear)) {
        alert("Vui lòng nhập lại năm!");
        return;
    }

    const ThienCan = thienCan[inputYear % 10];
    const DiaChi = diaChi[inputYear % 12];
    const CanChi = ThienCan + " " + DiaChi;
    document.getElementById("can-chi").value = CanChi;


}

