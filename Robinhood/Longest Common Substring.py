# Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
# Output : 5 or Geeks
# The longest common substring is “Geeks” and is of length 5.
X = "zxabcdezy"
Y = "yzabcdezx"


# Initialize a matrix of size (|X|+1)*(|Y|+1) to store
# the length of current substring. Expand the sizes of
# row and column by 1 to smooth the first column
# computations.
def longestSubstring(X, Y):
    maxLength = 0
    lstString = ""
    # Initialize a matrix of size (|X|+1)*(|Y|+1) to store
    # the length of current substring. Expand the sizes of
    # row and column by 1 to smooth the first column
    # computations.
    # counter = [[0] * (len(Y) + 1)] * (len(X) + 1)
    counter = [[0 for i in range(len(Y) + 1)] for j in range(len(X) + 1)]
    for i in range(len(Y)):
        for j in range(len(X)):
            if X[j] == Y[i]:
                newLength = counter[j][i] + 1
                if maxLength <= newLength:
                    maxLength = newLength
                    lstString = X[j-newLength+1:j+1]
                counter[j+1][i+1] = newLength
                print(lstString, newLength)
    return lstString

print(longestSubstring(X, Y))
