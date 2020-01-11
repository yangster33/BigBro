import datetime

from django.contrib.auth.models import User


def which_week(date, which_one):
    # 输入当前日期"datetime.datetime.now(),0"生成本周首尾两天的日期列表
    oneday = datetime.timedelta(days=1)
    date = date + oneday*(6 - date.weekday())
    date = date + which_one * oneday * 7
    return (date - oneday * 6, date)


def yangster_no1(mylist):
    # 输入用sorted(dict.items,key=lambda x:x[1])函数排序的list 返回排名 可并列 并列不占名次
    mydict = {}
    num = 1
    last_i = 0
    for i in mylist:
        # 排除admin账号
        if i[0] != 'admin':
            # last_i!=0说明不是第循环第一次
            if last_i != 0:
                if last_i[1] == i[1]:
                    mydict[i[0]] = num
                    last_i = i
                else:
                    num += 1
                    mydict[i[0]] = num
                    last_i = i
            else:
                mydict[i[0]] = num
                last_i = i
        else:
            continue
    mydict.update({'admin': 0})
    return mydict


def startandenddays(date, year_add, month):
    # 输入datetime.datetime.now()返回去年month
    last_year = int(date.replace(year=date.year+year_add).strftime('%Y'))
    oneday = datetime.timedelta(days=1)
    date = datetime.date(last_year, month, 1)
    if date.month == 12:
        return (date, date.replace(day=31))
    else:
        return (date, date.replace(month=date.month+1)-oneday)


def which_season(date, season_add):
    this_year = date.year
    this_month = date.month + season_add * 3

    if this_month <= 0:
        date = date.replace(year=(this_year + this_month // 12))
        date = date.replace(month=this_month % 12)
    elif this_month > 12:
        date = date.replace(year=this_year + this_month // 12)
        date = date.replace(month=this_month % 12)
    else:
        date = date.replace(month=this_month)

    oneday = datetime.timedelta(days=1)

    if date.month in (1, 2, 3):
        return (datetime.date(date.year, 1, 1), datetime.date(date.year, 4, 1) - oneday)
    elif date.month in (4, 5, 6):
        return (datetime.date(date.year, 4, 1), datetime.date(date.year, 7, 1) - oneday)
    elif date.month in (7, 8, 9):
        return (datetime.date(date.year, 7, 1), datetime.date(date.year, 10, 1) - oneday)
    else:
        return (datetime.date(date.year, 10, 1), datetime.date(date.year+1, 1, 1) - oneday)