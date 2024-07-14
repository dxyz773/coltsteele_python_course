// def sum_all_values(*args):
//     print(args)
//     print(sum(x for x in args))

function sumAllValues(...args) {
  console.log(args);
}
const test = [3, 3, 4, 5, 6];
sumAllValues(...test);
