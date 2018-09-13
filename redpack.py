# 1、9.17-9.23   380个认证红包（红包数量上限）
# 2、红包总额2800元。尽量接近，不用精确发完
# 3、每50个出现一个大包50元；其余10% 在10-20元，50%在5-10元，30%在2-5元，8%在1-2元。精确到分
import random
from math import floor

def redpack(totalMoney, totalNum):
	res = []

	fiftycount = 8
	# zeroTwoPartTotal = 380 * 0.08 * 100 = 30400
	zeroTwoPartTotal = 30400
	zeroTwoMax = 199
	zeroTwoCount = 30
	# twoFivePartToal = 380 * 0.3 * 350 = 39900
	twoFivePartToal = 39900
	twoFiveMax = 499
	twoFiveCount = 114
	# fiveTenpartTotal = 380 * 0.5 * 750 = 142500
	fiveTenpartTotal = 142500
	fiveTenMax = 999
	fiveTenCount = 190
	# tenTwentypartTotal = 380 * 0.1 * 1500 = 57000
	tenTwentypartTotal = 57000
	tenTwentyMax = 2000
	tenTwentyCount = 38

	randomList = [i for i in range(1, 101)]
	random.shuffle(randomList)
	i = 0
	while totalNum > 0 and totalMoney > 0 and i < len(randomList):
		randomNum = randomList[i]
		i += 1
		if randomNum >= 1 and randomNum <= 2 and fiftycount > 0:
			print(fiftycount)
			red = 5000
			fiftycount -= 1
		if randomNum >= 3 and randomNum <= 10 and zeroTwoPartTotal > 0 and zeroTwoCount > 0:
			try:
				red = random.randrange(100, math.floor(zeroTwoMax))
				zeroTwoMax = zeroTwoMax * (1- red/zeroTwoPartTotal)
				zeroTwoPartTotal -= red
				# zeroTwoMax = (zeroTwoPartTotal / zeroTwoCount) * 2
				zeroTwoCount -= 1
			except Exception:
				pass
		if randomNum >= 11 and randomNum <= 40 and twoFivePartToal > 0 and twoFiveCount > 0:
			try:
				red = random.randrange(200, math.floor(twoFiveMax))
				twoFiveMax = twoFiveMax * (1 - red/twoFivePartToal)
				twoFivePartToal -= red
				twoFiveCount -= 1
			except Exception:
				pass
		if randomNum >= 41 and randomNum <= 90 and fiveTenpartTotal > 0 and fiveTenCount > 0:
			try:
				red = random.randrange(500, math.floor(fiveTenMax))
				fiveTenMax = fiveTenMax * (1 - red/fiveTenpartTotal)
				fiveTenpartTotal -= red
				fiveTenCount -= 1
			except Exception:
				pass
		if randomNum >= 91 and randomNum <= 100 and tenTwentypartTotal > 0 and tenTwentyCount > 0:
			try:
				red = random.randrange(1000, math.floor(tenTwentyMax))
				tenTwentyMax = tenTwentyMax * (1 - red/tenTwentypartTotal)
				tenTwentypartTotal -= red
				tenTwentyCount -= 1
			except Exception:
				pass

		totalMoney -= red
		totalNum -= 1
		res.append(red)
	print(len(res))
	count = 0
	for i in range(len(res)):
		if res[i] == 5000:
			count += 1
	print(count)
	# while totalNum > 0 and totalMoney > 0:
	# 	redpack(totalMoney, totalNum)


# total 总金额
# num 红包数
# min 最低金额
# max 最高金额
def randBonus(total, num, min, max):
    total = float(total)
    num = int(num)
     
    if num < 1:
        return
    if num == 1:
        print("第%d个人拿到红包数:%.2f" % (num,total))
        ret.append(round(total, 2))
        return
    i = 1
    totalMoney = total
    ret = []
    while(i < num):
        maxnum = totalMoney - min*(num- i)
        #k = int(num - i)
        #k为系数 可以控制红包平均大小分部和总花费金额
        #此处若k不除以2，总花费2400，除以2，总花费2800，可随意调节

        #思路，对剩下的红包，先保证每个红包至少有最小值，减去这个最小值，剩下的money总额算是额外的，可以除以一个系数，比如剩下的红宝数，得到剩下的每个红包
        #可以得到的额外金额，加上最低金额，即为剩下的每个红包的随机上限，再比较下跟原来的最高上限的大小，保证不超过每个红包最高上限
        k = int(num-i)
        if num -i <= 2:
            k = num - i
        maxnum = maxnum/k + min
        max = maxnum if maxnum < max else max
        money = random.randint(int(min*100), int(max*100))
        money = float(money)/100
        totalMoney = totalMoney - money
        print("第%d个人拿到红包为:%.2f, 余额:%.2f"%(i,money,totalMoney))
        ret.append(round(money, 2))
        i += 1
 	
    lastBonus = totalMoney if totalMoney < max else max
    ret.append(round(lastBonus,2))
    remain = float(totalMoney - lastBonus)
    print("第%d个人拿到红包为:%.2f, 余额:%.2f"%(i,lastBonus,remain))
    return ret


if __name__ == "__main__":
	list = []
	#50红包
	list50 = [50.00] * 8
	#1-2块红包
	list1 = randBonus(45, 30, 1, 2)
	#2-5块红包
	list2 = randBonus(399, 114, 2, 5)
	#5-10块红包
	list5 = randBonus(1425, 190, 5, 10)
	#10-20块红包
	list10 = randBonus(570, 38, 10, 20)

	for i,val in enumerate(list50):
		list.append(val)
	for i,val in enumerate(list1):
		list.append(val)
	for i,val in enumerate(list2):
		list.append(val)
	for i,val in enumerate(list5):
		list.append(val)
	for i,val in enumerate(list10):
		list.append(val)

	for i in range(len(list)):
		list[i] *= 100
		list[i] = int(list[i])
	random.shuffle(list)
	print(sum(list))
	print(list)


