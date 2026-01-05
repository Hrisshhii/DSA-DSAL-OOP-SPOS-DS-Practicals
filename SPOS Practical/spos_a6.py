def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    memory = blocks[:] 

    for i, process in enumerate(processes):
        for j in range(len(memory)):
            if memory[j] >= process:                                                                        
                allocation[i] = j
                memory[j] -= process
                break
    return allocation, memory
    

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    memory = blocks[:]

    for i, process in enumerate(processes):
        best_idx = -1
        for j in range(len(memory)):
            if memory[j] >= process:
                if best_idx == -1 or memory[j] < memory[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            memory[best_idx] -= process
    return allocation, memory
    
    
def next_fit(blocks, processes):
    allocation = [-1] * len(processes)
    memory = blocks[:]
    start_idx = 0

    for i, process in enumerate(processes):
        count = 0
        j = start_idx
        while count < len(memory):
            if memory[j] >= process:
                allocation[i] = j
                memory[j] -= process
                start_idx = j
                break
            j = (j + 1) % len(memory)
            count += 1
    return allocation, memory
    
    
def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    memory = blocks[:]

    for i, process in enumerate(processes):
        worst_idx = -1
        for j in range(len(memory)):
            if memory[j] >= process:
                if worst_idx == -1 or memory[j] > memory[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            memory[worst_idx] -= process
    return allocation
    
def print_allocation(processes, allocation, memory, blocks):
    print("Process No. | Process Size | Block Allocated | Remaining Fragment")
    for i, block in enumerate(allocation):
        if block != -1:
            remaining = memory[block]
            print(f"{i+1:<11} | {processes[i]:<12} | {block+1:<15} | {remaining}")
        else:
            print(f"{i+1:<11} | {processes[i]:<12} | Not Allocated   | -")

  
def main():
    blocks = list(map(int, input("Enter memory block sizes (space separated): ").strip().split()))
    processes = list(map(int, input("Enter process sizes (space separated): ").strip().split()))

    print("\nMemory blocks:", blocks)
    print("Processes:", processes)
    print()

    print("First Fit Allocation:")
    allocation, memory = first_fit(blocks, processes)
    print_allocation(processes, allocation, memory, blocks)
    print()
    
    print("Best Fit Allocation:")
    allocation, memory = best_fit(blocks, processes)
    print_allocation(processes, allocation, memory, blocks)
    print()
    
    print("Next Fit Allocation:")
    allocation, memory = next_fit(blocks, processes)
    print_allocation(processes, allocation, memory, blocks)
    print()
    
    print("Worst Fit Allocation:")
    allocation = worst_fit(blocks, processes)
    print_allocation(processes, allocation, memory, blocks)
    print()
    
if __name__ == "__main__":
    main()

