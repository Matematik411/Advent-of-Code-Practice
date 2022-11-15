captcha = input()
l = len(captcha)

same = sum([int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[(i+1) % l]])

same_b = sum([int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[(i+(l//2)) % l]])


print("a: ", same)
print("b: ", same_b)
