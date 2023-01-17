if __name__ == '__main__':

    # import csv

    # with open('weather_data.csv') as file:
    #     data = csv.reader(file)
    #     print(data)
    #     temperatures = []
    #     for row in data:
    #         if row[1] == 'temp':
    #             continue
    #         temperatures.append(int(row[1]))

    #     print(temperatures)


    import pandas

    data = pandas.read_csv('weather_data.csv')

    # print(data['temp'])

    # data_dict = data.to_dict()
    # print(data_dict)

    # temp_list = data['temp'].to_list()
    # print(temp_list)
    # average_temp = (sum(temp_list)/len(temp_list))
    # print(average_temp)
    
    # # User series calls to manipulate data
    # temp_mean = print(data['temp'].mean())
    # temp_max = print(data['temp'].max())
    # temp_min = print(data['temp'].min())

    # # Get Data in columns
    # print(data['condition'])
    # print(data.condition)

    # # Get Data in Row
    # print(data[data.day == 'Monday'])

    # # Find the day on which the max temp fell
    # data['temp'].max()
    # # or
    # data.temp.max()

    # # construct the equival
    # data.temp == data.temp.max()

    # # insert into index
    # print(data[data.temp == data.temp.max()])

    # define an object using data index
    # monday = data[data.day == "Monday"]
    # print(monday.condition)

    # # # Take Monday's temp and convert it to F
    # Monday_FTemp = (monday.temp * 9/5) + 32
    # print(Monday_FTemp)

    # Create a dataframe from scratch
    data_dict = {
        'students' : ['Amy', 'James', 'Angela'],
        'scores' : [76, 56, 65]
    }

    data_2 = pandas.DataFrame(data_dict)

    print(data_2)

    data_2.to_csv('new_data.csv')

