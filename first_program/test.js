console.log([] && "hi");

const test = { name: "wow" };
console.log(test.name);

for (const item in Object.entries(test)) {
  console.log(item);
}
