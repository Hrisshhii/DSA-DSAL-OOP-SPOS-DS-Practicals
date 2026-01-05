# FCFS Scheduling without classes

# Input number of processes
n = int(input("Enter the number of processes: "))

processes = []

# Input arrival time and burst time for each process
for i in range(n):
    arrival = int(input(f"Enter arrival time for P{i}: "))
    burst = int(input(f"Enter burst time for P{i}: "))
    processes.append({
        "id": i,
        "arrival": arrival,
        "burst": burst,
        "completion": 0,
        "waiting": 0,
        "turnaround": 0,
        "response": 0
    })

# Display input table
print("\n| PID | Arrival | Burst |")
for p in processes:
    print(f"| P{p['id']}  |   {p['arrival']}     |  {p['burst']}   |")

# FCFS calculation
current_time = 0
print("\nProcess Execution Order: ", end="")

for p in processes:
    # If CPU is idle before process arrives
    if current_time < p["arrival"]:
        while current_time < p["arrival"]:
            print("NULL ", end="")
            current_time += 1

    print(f"P{p['id']} ", end="")
    p["response"] = current_time - p["arrival"]
    current_time += p["burst"]
    p["completion"] = current_time
    p["turnaround"] = p["completion"] - p["arrival"]
    p["waiting"] = p["turnaround"] - p["burst"]

# Display results
print("\n\n| PID | Completion | Waiting | Turnaround | Response |")
totalCT = totalWT = totalTAT = 0

for p in processes:
    print(f"| P{p['id']}  |     {p['completion']}      |   {p['waiting']}     |     {p['turnaround']}     |    {p['response']}     |")
    totalCT += p["completion"]
    totalWT += p["waiting"]
    totalTAT += p["turnaround"]

# Calculate averages
print(f"\nAverage Completion Time: {totalCT / n:.2f}")
print(f"Average Waiting Time   : {totalWT / n:.2f}")
print(f"Average Turnaround Time: {totalTAT / n:.2f}")
