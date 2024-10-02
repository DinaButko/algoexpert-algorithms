def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.

    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'

    for index in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[index]
        blueShirtHeight = blueShirtHeights[index]

        if shirtColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True
