def solution(enroll, referral, seller, amount):
    answer = []

    benefit = dict()
    ref = dict()
    for i in range(len(enroll)):
        name = enroll[i]
        benefit[name] = 0
        ref[name] = referral[i]
    benefit['-'] = 0
    for i in range(len(seller)):
        sellerName = seller[i]
        cost = 100 * amount[i]
        while True:
            if sellerName != '-':
                if cost == 0:
                    break
                fees = int(cost*0.1)
                benefit[sellerName] += cost - fees  # 0.9 몫을 가져옴
                sellerName = ref[sellerName]
                cost = fees
            else:
                break
    benefit.pop('-')
    return list(benefit.values())


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	, ["-", "-", "mary",
         "edward", "mary", "mary", "jaimie", "edward"]	, ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]	)
