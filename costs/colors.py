def myrgb(r, g, b, nums):

    outputnum = [100 - 100 / nums * i for i in range(nums)]

    minrbg = min(r, g, b,)
    maxrbg = max(r, g, b,)

    gradient_r = (r - minrbg) / (maxrbg - minrbg)
    gradient_g = (g - minrbg) / (maxrbg - minrbg)
    gradient_b = (b - minrbg) / (maxrbg - minrbg)

    for i,j in enumerate(outputnum):
        now_minrbg = minrbg * j /100
        outputnum[i] = [(j / 100 * 255 - now_minrbg) * gradient_r + now_minrbg,
                        (j / 100 * 255 - now_minrbg) * gradient_g + now_minrbg,
                        (j / 100 * 255 - now_minrbg) * gradient_b + now_minrbg, ]
    
    for i,color in enumerate(outputnum):
        color_hex = '#'
        for rgb in color:
            color_hex += hex(int(rgb))[2:]
        outputnum[i] = color_hex



    return outputnum

if __name__ == "__main__":
    r = 110
    g = 144
    b = 255
    nums = 10
    print(myrgb(r, g, b, nums))

