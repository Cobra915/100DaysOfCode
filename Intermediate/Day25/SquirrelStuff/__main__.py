if __name__ == '__main__':
    
    import pandas

    data = pandas.read_csv('./SquirrelStuff/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
    
    Fur_Colors = data['Primary Fur Color']

    Black = Fur_Colors.str.count('Black').sum()
    Gray = Fur_Colors.str.count('Gray').sum()
    Cinnamon = Fur_Colors.str.count('Cinnamon').sum()

    data_dict = {
        'Colors' : ['Black', 'Gray', 'Cinnamon'],
        'Values' : [Black, Gray, Cinnamon]
    }

    df = pandas.DataFrame(data_dict)


    df.to_csv('./SquirrelStuff/Squirrel_Colors.csv')