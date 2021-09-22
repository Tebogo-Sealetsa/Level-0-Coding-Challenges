def convert_to_hours_and_minutes(minutes):
    hours= minutes // 60
    mins = minutes % 60
    if hours ==1:
        print(str(hours)+" hour, "+str(mins)+" minutes")
    elif hours > 1:
        print(str(hours)+" hours, "+str(mins)+" minutes")
    return hours, mins
convert_to_hours_and_minutes(80)
convert_to_hours_and_minutes(148)
