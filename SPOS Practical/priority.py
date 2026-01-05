def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    processes=[]
    
    for i in range (n):
        arrival = int(input("Enter the arrival time : "))
        burst = int(input("Enter the burst time: "))
        priority = int(input("Enter the priority: "))
        
        processes.append({
            'id': i + 1,
            'arrival': arrival,
            'burst': burst,
            'priority': priority,
            'completion': 0,
            'waiting': 0,
            'turnaround': 0,
            'response': -1,
            'done': False})
            
    time = 0
    completed = 0
    
    while( completed < n):
        idx = -1
        highest_priority = float('inf') 
        
        for i, p in enumerate(processes): 
            if not p['done'] and p['arrival'] <= time and p['priority'] < highest_priority:
                highest_priority = p['priority']
                idx = i
                
        if idx != -1:
            p = processes[idx]
            if p['response'] == -1:
                p['response'] = time - p['arrival']
            time += p['burst']
            p['completion'] = time
            p['turnaround'] = p['completion'] - p['arrival']
            p['waiting'] = p['turnaround'] - p['burst']
            p['done'] = True
            completed += 1
        else:
            time += 1
            
            
            
            
    total_waiting = sum(p['waiting'] for p in processes)
    total_turnaround = sum(p['turnaround'] for p in processes)
    total_completion = sum(p['completion'] for p in processes)

    print("\nProcess | Completion | Waiting | Turnaround | Response")
    for p in processes:
        print(f"P{p['id']}      | {p['completion']}          | {p['waiting']}       | {p['turnaround']}          | {p['response']}")

    print(f"\nAverage completion time: {total_completion / n}")
    print(f"Average waiting time: {total_waiting / n}")
    print(f"Average turnaround time: {total_turnaround / n}")

if __name__ == "__main__":
    priority_scheduling()
           
       
        
