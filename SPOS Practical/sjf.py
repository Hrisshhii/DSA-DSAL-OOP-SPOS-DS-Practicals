def get_input():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        arrival = int(input(f"\nEnter arrival time for process P{i}: "))
        burst = int(input(f"Enter burst time for process P{i}: "))
        processes.append({
            "id": i,
            "arrival": arrival,
            "burst": burst,
            "original_burst": burst,
            "completion": 0,
            "turnaround": 0,
            "waiting": 0
        })
    return processes, n


def compute(processes, n):
    time = 0
    completed = 0
    print("\nProcess execution order:")

    while completed < n:
        shortest = -1
        min_burst = float("inf")

        for i in range(n):
            if processes[i]["arrival"] <= time and processes[i]["burst"] > 0:
                if processes[i]["burst"] < min_burst:
                    min_burst = processes[i]["burst"]
                    shortest = i

        if shortest != -1:
            print(f"P{processes[shortest]['id']}", end=" ")
            processes[shortest]["burst"] -= 1
            time += 1

            if processes[shortest]["burst"] == 0:
                processes[shortest]["completion"] = time
                processes[shortest]["turnaround"] = time - processes[shortest]["arrival"]
                processes[shortest]["waiting"] = (
                    processes[shortest]["turnaround"] - processes[shortest]["original_burst"]
                )
                completed += 1
        else:
            print("IDLE", end=" ")
            time += 1


def display(processes, n):
    total_completion = 0
    total_turnaround = 0
    total_waiting = 0

    print("\n\n| PID | Arrival | Burst | Completion | Turnaround | Waiting |")
    print("---------------------------------------------------------------")

    for p in processes:
        print(
            f"| P{p['id']}   |   {p['arrival']:<6} |  {p['original_burst']:<4} |"
            f"     {p['completion']:<6} |     {p['turnaround']:<6} |   {p['waiting']:<6} |"
        )
        total_completion += p["completion"]
        total_turnaround += p["turnaround"]
        total_waiting += p["waiting"]

    print(f"\nAverage Completion Time: {total_completion / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")
    print(f"Average Waiting Time   : {total_waiting / n:.2f}")


if __name__ == "__main__":
    processes, n = get_input()
    compute(processes, n)
    display(processes, n)
