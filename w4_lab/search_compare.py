'''temps = [23.5, 28.1, 31.4, 26.8, 24.2, 29.5, 27.0,
         22.3, 35.6, 30.1, 25.4, 23.9, 28.7, 26.2,
         32.0, 24.8, 29.3, 27.5, 22.8, 31.8, 25.7,
         26.1, 28.4, 33.2, 24.5, 27.8, 29.1, 30.6,
         25.3, 26.9]
def linear_search_count(lst, target):


    count = 0
    
    for i in range(len(lst)):

        count += 1          # 计数器：每次比较前加 1
        
        if lst[i] == target:
            
            return i, count
    return -1,count
idx, comparisons = linear_search_count(temps, 29.5)
print(f"线性查找：索引={idx}, 比较次数={comparisons}")
def binary_search_count(lst, target):
    left, right = 0, len(lst) - 1
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid, count
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, count

sorted_temps = sorted(temps)
idx, comparisons = binary_search_count(sorted_temps, 29.5)
print(f"二分查找：排序后索引={idx}, 比较次数={comparisons}")
temp_dict = {}
for i, temp in enumerate(temps):
    temp_dict[temp] = i
idx = temp_dict[29.5]
print(f"字典查找：索引={idx}, 比较次数=1") 
f = open("fox.txt", "r")
c = 0
for line in f:
    for word in line.split():
        if word == "fox":
            c += 1
print(f"文件中 'fox' 的出现次数: {c}")
from pyecharts.charts import Line
line = Line()
line.add_xaxis(["USA", "China", "India", "Germany", "UK"])
line.add_yaxis("GDP", [21.43, 14.34, 2.87, 3.86, 2.83])
line.render("gdp_line_chart.html")'''
x, n = map(int, input().split())
num = 1
for i in range(1,n +1):
    num += num * x
print(num)
    