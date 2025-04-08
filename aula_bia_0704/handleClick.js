export function handleClick() {
    if (img.src.includes('l1.png')) {
        img.src = "./l2.png";
        btn.textContent = "apagar"
    } else {
        img.src = "./l1.png";
        btn.textContent = "ascender"
    };
};