def print_perm_time_call(msc_time):
    hours_msc = int(msc_time[:2])
    minutes = msc_time[-2:]
    hours_perm = hours_msc + 2
    if hours_perm < 10:
        hours_perm = '0' + str(hours_perm)
    print(f"Созвон будет в {hours_perm}:{minutes}.")


msc_time = input()
print_perm_time_call(msc_time)
