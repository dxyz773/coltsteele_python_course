alphabet = ("a", "b", "c", "d")
# print("a" in alphabet)

months = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

locations = {
    (35.3244, 39.5832): "Toyko Office",
    (40.7123, 74.0002): "New York Office",
    (36.7734, 122.4194): "San Francisco Office",
}

cat = dict(name="biscuit", age=" 0.5", favorite_toy="my chapstick")

# print(cat.items())

for x in range(-1, -len(months) - 1, -1):
    print(months[x])
