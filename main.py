import sys

'''
Input: A sorted array, A, wehre one unique value appears once and every other value appears twice (no more or less).
Output: The single unique value.
'''
def binary_search(a, start, end):
    if (start == end):
        return a[start]
    mid = (start + end) // 2

    if mid % 2 != 0:
        mid -= 1
    
    if a[mid] == a[mid+1]:
        return binary_search(a, mid+2, end)
    else:
        return binary_search(a, start, mid)
    

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("usage: python3 find_unique.py <path-to-input>\n")
        return

    path = sys.argv[1]
    with open(path, "r") as f:
        a = [int(x) for x in f.read().split()]

    print(binary_search(a, 0, len(a) - 1))


if __name__ == "__main__":
    main()
