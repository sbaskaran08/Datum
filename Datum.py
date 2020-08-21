days={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
month={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
result=17
month_date=list(map(int,input().split()))
result=result+month_date[0]+month[month_date[1]]
result=result%7
print(days[result])
