LAST_NAME = "FABIA"

SEED_NUM = 6

FAVORITE_ARTIST = "LUKE CHIANG"





def logger(func):

    def wrapper(*args, **kwargs):

        print(f"[LOG] Running {func.__name__}")

        return func(*args, **kwargs)

    return wrapper





def validate_readings(readings):

    valid = []



    for value in readings:

        try:

            value = float(value)



            if value < 0:

                raise ValueError("Negative value")



            valid.append(value)



        except ValueError:

            print(f"Invalid reading: {value}")



    return valid





def calculate_average(readings):

    return sum(readings) / len(readings)





def classify_equipment(avg):

    if avg >= 80:

        return "NORMAL"

    elif avg >= 50:

        return "WARNING"

    else:

        return "CRITICAL"





@logger

def main():

    readings = [

        len(LAST_NAME) * 10,

        SEED_NUM * 12,

        len(FAVORITE_ARTIST) * 5,

        -5

    ]



    print("Generated Equipment Data:", readings)



    valid_data = validate_readings(readings)



    avg = calculate_average(valid_data)



    status = classify_equipment(avg)



    print("Validation Results:", valid_data)

    print("Diagnostic Results:", status)



    print("\nFinal Output")

    print("Average Reading:", round(avg, 2))

    print("Equipment Status:", status)





main()