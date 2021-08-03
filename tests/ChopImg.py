def chopImg(captchaImg):
    # Chop img into pieces
    NUMBER_OF_CHOPS = 4
    arrayImg = []
    width, height = captchaImg.size
    chopsize = int(width/NUMBER_OF_CHOPS)

    for x0 in range(0, width, chopsize):
        for y0 in range(0, height, chopsize):
            box = (x0, y0,
                   x0+chopsize if x0+chopsize < width else width - 1,
                   y0+chopsize if y0+chopsize < height else height - 1)
            arrayImg.append(captchaImg.crop(box))

    return arrayImg