def avg_time(customers):
    present_time=0
    total_time=0

    for arrival_time, time_required in customers:
        if present_time<arrival_time:
            present_time=arrival_time

        finish_time=present_time+time_required
        waiting_time=finish_time-arrival_time
        total_time+=waiting_time
        present_time=finish_time

    average_time=total_time/len(customers)
    return average_time

customers=[(5,2), (5,4), (10,3), (20,1)]
print(avg_time(customers))
        
