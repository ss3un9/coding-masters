money = int(input())

coupons = [50000, 10000, 5000, 1000, 500, 100, 50, 10] 
count = 0 
for coupon in coupons:
    count += money // coupon 
    money %= coupon 

print(count)