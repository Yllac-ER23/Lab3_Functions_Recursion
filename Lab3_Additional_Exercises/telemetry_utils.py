def telemetry_generator(data):

    for item in data:

        yield item





def recursive_abnormal(data, index=0):



    if index >= len(data):

        return 0



    if data[index] > 70:

        return 1 + recursive_abnormal(data, index + 1)



    return recursive_abnormal(data, index + 1)