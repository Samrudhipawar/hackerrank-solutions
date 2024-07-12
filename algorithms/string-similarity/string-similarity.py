def z_algorithm(s):
    """Compute the Z-array of a string s."""
    n = len(s)
    Z = [0] * n
    l, r, K = 0, 0, 0
    for i in range(n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            K = i - l
            if Z[K] < r - i + 1:
                Z[i] = Z[K]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    return Z

def sum_of_similarities(s):
    """Compute the sum of similarities of a string s with each of its suffixes."""
    Z = z_algorithm(s)
    return sum(Z) + len(s)  # + len(s) accounts for the similarity of the string with itself

# Read the number of test cases
t = int(input().strip())

for _ in range(t):
    s = input().strip()
    print(sum_of_similarities(s))
