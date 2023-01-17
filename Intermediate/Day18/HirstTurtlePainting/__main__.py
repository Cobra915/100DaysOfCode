if __name__ == '__main__':
    
    import Functions
    from pprint import pprint

    file = input('Please input a local file name: ')
    rgb_colors = Functions.extract_colors(file)
    pprint(rgb_colors)

    height = int(input('Please input a height: '))
    width = int(input('Please input a width: '))

    height_list = []
    for item in range(1,height+1):
        height_list.append(item*50)

    width_list = []
    for item in range(1,width+1):
        width_list.append(item*50)

    Functions.draw_stupid_art(height_list, width_list)