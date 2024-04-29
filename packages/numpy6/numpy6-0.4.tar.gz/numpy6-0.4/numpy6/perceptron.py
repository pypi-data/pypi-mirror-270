import numpy as np

X = np.array([[5,8],[3,6],[7,9],[2,4],[6,7]]) # hours studied and slept
Y = np.array([1, 0, 1, 0, 1])

# X = np.array([[0,0],[0,1],[1,0],[1,1]]) # AND gate
# Y = np.array([0, 0, 0, 1])

weights = np.random.randn(X.shape[1])

epoch = 1000
learning_rate = 0.002

error = 0

print("Initial weights:",weights)

for i in range(epoch):
    # print(f"Epoch {i+1}")
    for x,y in zip(X,Y):
        # predict
        y_pred = np.dot(x,weights)

        # convert predict to binary
        y_pred = 1 if y_pred > 0.5 else 0

        # calculate error
        error = y - y_pred

        # Update weights
        weights += learning_rate * error * x

print("Error: ", error)
print("Final weights:",weights)

def predict(inputs,weights):
    y_pred = np.dot(inputs,weights)
    return "PASS" if y_pred > 0.5 else "FAIL"


hours_studied = int(input("No of hours studied: "))
hours_slept = int(input("No of hours slept: "))

print(predict([hours_studied,hours_slept], weights))
