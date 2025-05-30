import sys

def min_subseq_all_letters(a, k):

    cnt = [0] * (k + 1)  
    have = 0             
    best = len(a) + 1
    l = 0
    for r, x in enumerate(a):
        if 1 <= x <= k:
            if cnt[x] == 0:
                have += 1
            cnt[x] += 1
        
        while have == k:
            curr_len = r - l + 1
            if curr_len < best:
                best = curr_len
            y = a[l]
            cnt[y] -= 1
            if cnt[y] == 0:
                have -= 1
            l += 1
    return best if best <= len(a) else None

def main():
    
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = 'data_prog_contest_problem_2.txt'
    
    with open(infile, 'r') as f:
        parts = f.read().split()
    if len(parts) < 2:
        print("Неверный формат входного файла")
        return
    n, k = map(int, parts[:2])
    seq = list(map(int, parts[2:2+n]))
    
    result = min_subseq_all_letters(seq, k)
   
    print(result if result is not None else "NONE")

if __name__ == "__main__":
    main()