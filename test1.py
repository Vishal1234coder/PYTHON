import time

current_time= int(time.strftime("%H"))
if current_time>=00 and current_time<12:
    print("GOOD MORNING SIR")
elif current_time>=12 and current_time<16:
    print("GOOD AFTERNOON SIR")
elif current_time>=16 and current_time<20:
    print("GOOD EVENING SIR")
else:
    print("GOOD NIGHT SIR")




