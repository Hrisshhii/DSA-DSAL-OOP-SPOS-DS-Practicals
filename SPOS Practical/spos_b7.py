def fifo_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    next_replace_index = 0

    print("\nFIFO Page Replacement Process:")
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[next_replace_index] = page
                next_replace_index = (next_replace_index + 1) % frame_size
            page_faults += 1
        print(f"Page {page} -> Frames: {frames}")
    print(f"Total Page Faults (FIFO): {page_faults}\n")


def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    recent_usage = {}

    print("\nLRU Page Replacement Process:")
    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                lru_page = min(recent_usage, key=recent_usage.get)
                lru_index = frames.index(lru_page)
                frames[lru_index] = page
                del recent_usage[lru_page]
            page_faults += 1
        recent_usage[page] = i
        print(f"Page {page} -> Frames: {frames}")
    print(f"Total Page Faults (LRU): {page_faults}\n")


def optimal_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    print("\nOptimal Page Replacement Process:")
    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                future_uses = []
                for fpage in frames:
                    if fpage in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(fpage))
                    else:
                        future_uses.append(float('inf'))
                index_to_replace = future_uses.index(max(future_uses))
                frames[index_to_replace] = page
            page_faults += 1
        print(f"Page {page} -> Frames: {frames}")
    print(f"Total Page Faults (Optimal): {page_faults}\n")


if __name__ == "__main__":
    ref_str_input = input("Enter the reference string (space-separated page numbers): ")
    pages = list(map(int, ref_str_input.strip().split()))
    frame_size = int(input("Enter the number of frames: "))

    fifo_page_replacement(pages, frame_size)
    lru_page_replacement(pages, frame_size)
    optimal_page_replacement(pages, frame_size)

