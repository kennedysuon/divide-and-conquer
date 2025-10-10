import sys

'''
Binary Search based approach
Input: A sorted array, A, wehre one unique value appears once and every other value appears twice (no more or less).
Output: The single unique value.
'''
def binary_search(a, start, end):
    if (start == end):
        return a[start]
    mid = (start + end) // 2

    if (mid-start) % 2 != 0:
        mid -= 1
    
    if a[mid] == a[mid+1]:
        return binary_search(a, mid+2, end)
    else:
        return binary_search(a, start, mid)
    

'''
Merge Sort based approach
Input: A sorted array, A, wehre one unique value appears once and every other value appears twice OR MORE.
Output: The single unique value.
'''
def merge_based(a, start, end):
    if start > end:
        return None
    
    if start == end:
        return a[start]
    
    mid = (start + end) // 2
    val = a[mid]

    # Search the left of the middle value until it stops repeating.
    i = mid
    while i > start and a[i-1] == val:
        i -= 1
    
    # Search the right of the middle value until it stops repeating.
    j = mid 
    while j < end and a[j+1] == val:
        j += 1
    
    # If i and j only ran once then we found our unique value.
    if i == j:
        return a[i]
    
    # Search the left sublist
    result = merge_based(a, start, i-1)
    if result is not None:
        return result
    # Search the right sublist
    else:
        return merge_based(a, j+1, end)


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("usage: python3.10 main.py <path-to-input>\n")
        return

    path = sys.argv[1]
    with open(path, "r") as f:
        a = [int(x) for x in f.read().split()]

    print("Binary:", binary_search(a, 0, len(a) - 1))
    print("Merge:", merge_based(a, 0, len(a)-1))


if __name__ == "__main__":
    main()
