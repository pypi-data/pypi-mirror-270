import numpy as np
import matplotlib.pyplot as plt

X = [0.3,0.5,0.7,0.4]
Y = [0.2,0.6,0.9,0.3]

def sigmoid(w,x,b):
  return (1.0/(1.0+np.exp(-(w*x + b))))

def error(w,b,X,Y):
  errors = 0.0
  for x,y in zip(X,Y):
    y_pred = sigmoid(w,x,b)
    errors += 0.5*(y_pred - y)**2

  return errors

def grad_w(w,b,X,Y):
  y_pred = sigmoid(w,X,b)
  return ((y_pred - Y)*y_pred*(1-y_pred)*X)


def grad_b(w,b,X,Y):
  y_pred = sigmoid(w,X,b)
  return ((y_pred - Y)*y_pred*(1-y_pred))


def plts(errors:list):
  index = [i for i in range(len(errors))]
  plt.plot(index , errors)
  plt.xlabel("epoch")
  plt.ylabel("Error")
  plt.show()

# Gradient decent vanialla
def gradient_decent():
  w, b, lr, epoch = 2,-2,1,100
  errors = []
  print(X,Y)
  print(f"Error before updating weights: {error(w,b,X,Y)}")

  for i in range(epoch):
    errors.append(error(w,b,X,Y))
    dw,db = 0,0
    for x,y in zip(X,Y):
      # print(x,y)
      dw+=grad_w(w,b,x,y)
      db+=grad_b(w,b,x,y)

    w = w - lr*dw
    b = b - lr*db

  print(f"Error after updating weights: {error(w,b,X,Y)} weight : {w} bias : {b} ")
  return errors


list_error = gradient_decent()

plts(list_error)


