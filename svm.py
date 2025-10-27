from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

features = [
    [-3, -1, 2],
    [0, -2, 1],
    [-2.5, 2, -1],
    [-1, -1, 0],
    [3, .5, 3],
    [.5, 3, 2],
    [-3, -3, -2]
]

weights = [0, 1, 0, 1, 1, 0, 1]  # list of length len(features)

clf = svm.SVC(kernel="linear").fit(features, weights)
test_point = [-2, -2, -1]

# Print detailed information
print(f"Prediction for {test_point}: {clf.predict([test_point])}")
print(f"\nDecision function value: {clf.decision_function([test_point])[0]:.4f}")
print(f"  (Positive = Class 1, Negative = Class 0)")
print(f"\nPlane equation coefficients:")
print(f"  w = {clf.coef_[0]}")
print(f"  b = {clf.intercept_[0]:.4f}")
print(f"\nCalculation: w·{test_point} + b = {clf.decision_function([test_point])[0]:.4f}")

# Show all training points for reference
print(f"\nTraining data points:")
for i, (feat, weight) in enumerate(zip(features, weights)):
    decision_val = clf.decision_function([feat])[0]
    print(f"  {feat} → Class {weight} (decision value: {decision_val:.4f})")

# Visualize the 3D data
features_array = np.array(features)
weights_array = np.array(weights)

# Create 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot training points (actual 3D coordinates)
colors = ['blue' if w == 0 else 'red' for w in weights_array]
ax.scatter(features_array[:, 0], features_array[:, 1], features_array[:, 2],
           c=colors, s=150, edgecolors='black', linewidth=1.5, alpha=0.8,
           label='Training Data')

# Plot support vectors
sv = clf.support_vectors_
ax.scatter(sv[:, 0], sv[:, 1], sv[:, 2],
           s=300, facecolors='none', edgecolors='green', linewidth=3, 
           label='Support Vectors')

# Plot the test point with prediction color
test_point_array = np.array([2, 4, 2])
test_prediction = clf.predict([test_point_array])[0]
test_color = 'blue' if test_prediction == 0 else 'red'
ax.scatter([test_point_array[0]], [test_point_array[1]], [test_point_array[2]], 
           c=test_color, s=400, marker='*', 
           edgecolors='yellow', linewidth=3, label=f'Test Point {test_point} → Class {test_prediction}')

# Create the decision boundary plane
# For linear SVM: w·x + b = 0, which defines a plane
# w[0]*x + w[1]*y + w[2]*z + b = 0
# Solve for z: z = -(w[0]*x + w[1]*y + b) / w[2]
w = clf.coef_[0]
b = clf.intercept_[0]

x_min, x_max = features_array[:, 0].min() - 1, features_array[:, 0].max() + 1
y_min, y_max = features_array[:, 1].min() - 1, features_array[:, 1].max() + 1

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 20),
                     np.linspace(y_min, y_max, 20))

if w[2] != 0:
    zz = -(w[0] * xx + w[1] * yy + b) / w[2]
    ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray')

ax.set_xlabel('Feature 1 (X)')
ax.set_ylabel('Feature 2 (Y)')
ax.set_zlabel('Feature 3 (Z)')
ax.set_title('3D SVM Classification with Linear Kernel\nGray plane = Decision Boundary')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# source .venv/bin/activate
# .venv/bin/python svm.py