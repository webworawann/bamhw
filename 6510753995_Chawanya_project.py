# compare gold trader with 31 jan 2023
# spacific with buying


def main():
    # type = int(input("input type you would like to compare: "))
    gold_bars = float(input("gold gold bars price: "))
    gold_ornament = float(input("gold gold ornament price: "))

    # use function calculated for calculate gold price
    answer = calculated(gold_bars, gold_ornament, type)
    print("-----------------------------")
    i = 0

    while i <= 2:
        ans = ""
        ans = answer[i] + answer[i + 1]
        i += 2
        print(ans)


def calculated(gold_bars, gold_ornament, type):
    # 1bathofgold
    x = 34000  # 1bathofgoldbar
    y = 33382.32  # 1bathofgoldornament
    buying_goldbars = gold_bars
    buying_goldornament = gold_ornament

    # gb = abs(buying_goldbars)
    # go = abs(buying_goldornament)

    ans = []

    # goldbar
    ans.append("goldbar price ")
    if buying_goldbars > x:
        ans.append("rise")

    if buying_goldbars < x:
        ans.append("goes down")

    if buying_goldbars == x:
        ans.append("does not change")

    # goldornament
    ans.append("goldornament price ")
    if buying_goldornament > y:
        ans.append("rise")

    if buying_goldornament < y:
        ans.append("goes down")

    if buying_goldornament == y:
        ans.append("does not change")

    # print(ans)
    return ans


main()
