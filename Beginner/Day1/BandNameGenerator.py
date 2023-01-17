
City_Input = input("What's the name of the city you grew up in? " )

Pet_Input = input("What's the name of your first pet? " )

def band_name_generator(City, Pet):
    print(f'Your band name is \"{City} {Pet}"')
    #print(City + " " + Pet)
    
# Main function:
if __name__ == "__main__":
    band_name_generator(City_Input, Pet_Input)