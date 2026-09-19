LAST_NAME = "FABIA"

SEED_NUM = 6

FAVORITE_ARTIST = "LUKE CHIANG"



calls = 0





def trace_fault(fault_code):

    global calls



    calls += 1



    print(f"Fault Code: {fault_code}")



    if fault_code <= 1:

        return fault_code



    return trace_fault(fault_code // 2)





generated_fault = (

    len(LAST_NAME) * SEED_NUM

) + len(FAVORITE_ARTIST)



print("Generated Fault Data:", generated_fault)



result = trace_fault(generated_fault)



print("\nRecursive Trace Complete")

print("Final Result:", result)

print("Number of Recursive Calls:", calls)