from telemetry_utils import telemetry_generator
from telemetry_utils import recursive_abnormal

from telemetry_analysis import log_process

LAST_NAME = "FABIA"
SEED_NUM = 6
FAVORITE_ARTIST = "LUKE CHIANG"


@log_process
def process_data():

    telemetry = [
        len(LAST_NAME) * 8,
        SEED_NUM * 10,
        len(FAVORITE_ARTIST) * 9,
        120,
        -10
    ]

    print("Generated:", telemetry)

    valid = []
    invalid =[]

    for value in telemetry:

        try:

            if value < 0:
                raise ValueError()

            valid.append(value)

        except ValueError:
            invalid.append(value)

    stream = telemetry_generator(valid)

    processed = list(
        map(lambda x: x * 1.1, stream)
    )

    abnormal = recursive_abnormal(processed)

    print("\nValid Results:", valid)
    print("Invalid Results:", invalid)

    print("Processed Results:", processed)

    print("\nRecursive Analysis:")
    print("Abnormal Readings:", abnormal)

    print("\nFinal Diagnostic Summary")
    print("Processed Count:", len(processed))
    print("Invalid Count:", len(invalid))
    print("Overall Status:", 
          "NORMAL" if abnormal < 2 else "WARNING")


process_data()