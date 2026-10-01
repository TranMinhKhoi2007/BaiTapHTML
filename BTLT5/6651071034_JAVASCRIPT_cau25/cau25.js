const List = {
    // Món ăn
    "Bún bò": 20000,
    "Hủ tiếu": 18000,
    "Bánh canh": 17000,
    "Phở bò": 19000,
    Nuôi: 15000,
    "Bánh mì thịt": 12000,
    "Bánh cuốn": 15000,
    // Thức uống
    "Cà phê đá": 12000,
    "Cà phê sữa": 15000,
    "Chanh dây": 13000,
    "Chanh muối": 12000,
    "Xí muội": 14000,
    "Sữa tươi": 13000,
    "Cam vắt": 17000,
};

function getFood() {
    const selectedFood = document.querySelectorAll("#thuc-an option:checked");
    const foodList={}
    selectedFood.forEach(function(item){
        if(item.selected){
            let tenMon = item.value;
            foodList[tenMon] = true;
        }
    })

    return foodList;
}

function getDrink() {
    const selectedDrink = document.querySelectorAll("#thuc-uong option:checked");
    const drinkList={};
    selectedDrink.forEach(function(item){
        if(item.selected){
            let tenMon = item.value;
            drinkList[tenMon] = true;
        }
    })
    return drinkList;
}

function tinhTien() {
    let tableOutput = `<table border="1" style="border-collapse: collapse; background-color: cyan;">
        <thead style="color: blue;">
            <tr>
                <th>Các món đã dùng</th>
                <th>Giá Tiền</th>
            </tr>
        </thead>
        <tbody>
        `;

    const foods = getFood(),
        drinks = getDrink();
    let tongTien = 0;
    const chosenList = { ...foods, ...drinks };
    for (let tenMon in chosenList) {
        let cost = List[tenMon];
        tongTien += cost;
        tableOutput += `
    <tr>
        <td>${tenMon}</td>
        <td>${cost.toLocaleString("vi-VN")}</td>
    </tr>
    `; 
    }
    let time = document.getElementsByName("thời điểm");
    time.forEach(function(option){
        if(option.value == "Ban đêm" && option.checked){
            tongTien *= 1.1;
        }
    });
    tableOutput += `
            <tr>
                <td>Tổng cộng</td>
                <td>${tongTien.toLocaleString("vi-VN")}</td>
            </tr>
        </tbody>
    </table>
    `;
    document.getElementById("output-table").innerHTML = tableOutput;
}
