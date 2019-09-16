def reshapeColor(colorEightBit):
    # Transforming 0/255 BGR to 0/1 RGB 
    colors = list(colorEightBit)
    colors.reverse()
    return [i / 255 for i in colors]

def upscaleColor(color):
    return [i * 255 for i in color]

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))
