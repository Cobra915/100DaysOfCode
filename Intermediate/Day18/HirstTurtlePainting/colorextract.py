###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
def extract_colors(file : str):
    colors = colorgram.extract(file, 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    if (255, 255, 255) in rgb_colors:
        rgb_colors.remove((255, 255, 255))
    return rgb_colors