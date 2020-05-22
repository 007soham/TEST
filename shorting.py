def sort(let):
    for i in range(len(let) -1, 0, -1):
        for j in range(i):
            if let[j] > let[j+1]:
                temp = let[j]
                let[j] = let[j+1]
                let[j+1] = temp


let = ['a','b','k','y','w','v','s','k','m','s','f','j','w','y','a','l','s','d','m','b','s','d','f','j','h','g','s','k','l','m','d','f','s']
sort(let)
print("With duplicate letters : "+ str(let))

alpha = []
[alpha.append(x) for x in let if x not in alpha]
print("Without duplicate letters : " + str(alpha))
