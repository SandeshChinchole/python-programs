
# accessing last item using index

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
length = len(smoothies)
last = smoothies[length-1]
print('Last item using index: ', last)

# accessing last item using negative index (take the last three smoothies on our list and print them)

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
last = smoothies[-1]
second_last = smoothies[-2]
third_last = smoothies[-3]
print('last item: ', last + ', ' + 'second last: ' + second_last + ', ' + 'third_last: ' + third_last)
