cities = str(input()) # input = 3 10 12 5
arr = cities.split()  # separate by every space to isolate distances

# convert str input to ints w/ list comp
distances = [int(city) for city in arr]

# create a 2D array (more like a martix) filled with zeros in a 5*5 "Grid", where n = 5 (total # of outputs per line)
n = len(distances) + 1
distance_matrix = [[0] * n for _ in range(n)]

"""
For context, this is how it'd look at this point:

City0 City1 City2 City3 City4
City0   0    0    0    0    0
City1   0    0    0    0    0
City2   0    0    0    0    0
City3   0    0    0    0    0
City4   0    0    0    0    0

Where City0 is the 0th index of the distances list, and so on.
"""

# insane matrix calculation logic
for i in range(n): # iterate over all cities
    for j in range(i + 1, n): 
        distance_matrix[i][j] = distance_matrix[i][j - 1] + distances[j - 1] # cumulative distance between nodes/cities, massive explanation below of logic

        """ 
        In the matrix, we'd say i = 0, and j = 1. Since j = i + 1 in accordance to the for loop logic. 
        distance_matrix[0][1] is equal to distance_matrix[0][0] + distances[j-1], where j = 1, so it's distances = [0].

        In the first iteration of the first array, where distances[0] = 3, we can say the distance from City0 to City1 is 3.

        For later iterations, say when going from City0 to City2, it'd look something like this:

        --> distance_matrix[0][2] = distance_matrix[0][1] + distances[1] 

        We can say this is basically: distance_matrix[0][2] is equal to --> 3 + 10, WHICH IT IS!!!
        
        """

        """

        Now let's say that we reach the point where we want to find the distance between City1 to City1. This would equal 0, as the distance between them is the same value, and they'd subtract from each other.
        In the matrix, it'd look something like --> distance_matrix[1][2]

        "Hol' up, that's not right. J can never equal 1 anyways, so how do we go to City1 from City1?"

        YOU DON'T LMAO. The logic is set up to avoid dup cities, so those matrix indices will be left as 0, which is what we want.
        
        """

        """
        And as the comment below says, the bottom line is to assert that the distance between both cities. Since distance is a symmetric property here, it will be the same between the two same nodes even if they're swapped.

        If anything, the bottom line below is an assignment section, so this line is really just good practice to ensure the output is consistent and correct.
        
        The funny thing is though is that, without this line, our final matrix is broken. This line actually makes the opposite diagonal of the matrix filled to match the other half. And if you look closely, our calculations will in fact fit this rule of symmetry, since they basically reflect along the center diagonal, which is what we want!
        
        """

        distance_matrix[j][i] = distance_matrix[i][j] # the distance between both nodes will be the same!!

# Print the distance matrix
for row in distance_matrix:
    print(" ".join(map(str, row)))

"""

The above logic looks at each row of the matrix, which is the arrays inside the matrix. To make it simpler, assume this structure internally:

[ 2nd layer (2D array/matrix layer)

    [0  3  13  25  30] 1st layer (arrays)
    [3  0  10  22  27]
    [13 10  0  12  17]
    [25 22  12  0   5]
    [30 27  17  5   0]

]

Each line is it's own array, and if you look long enough at the above calculation logic, it's literally replacing the values in the row [i] and column [j] that is called.
So in the end, we're just printing the inputs of each array on seperate lines. More specifically, we extract and map the integers in the rows to be strings, then output them all with spaces at the end to separate them accordingly.

"""