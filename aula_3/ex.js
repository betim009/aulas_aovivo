const array = [
    {name: "Rocco"},
    {name: "Rocco"},
    {}
];

const filterByName = array.filter((e) => e?.name === "Rocco")
console.log(filterByName)

console.log(filterByName.length)