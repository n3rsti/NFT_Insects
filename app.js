let list = document.querySelectorAll(".explore-palette_colors");
for (let i = 0; i < list.length; i++) {
    let arr = [];
    let in_list = list[i].querySelectorAll("div")
    if (in_list.length < 5) {
        continue;
    }
    for (let z = 0; z < in_list.length; z++) {
        arr.push(in_list[z].style.background.toString().replace("rgb", ""))
    }
    let reverse = arr.reverse()
    console.log(`[${reverse[0]}, ${reverse[1]}, ${reverse[2]}, ${reverse[3]}, ${reverse[4]}, ${reverse[5]}],`)
}