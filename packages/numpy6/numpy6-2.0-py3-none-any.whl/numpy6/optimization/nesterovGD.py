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


def nestrov_gradient_decent():
  w,b,lr,epochs = 2,-2,0.1,100
  errors = []
  print(X,Y)
  prev_v_w, prev_v_b , gamma = 0,0,0.9
  print(f"Error before updating weights: {error(w,b,X,Y)}")
  for i in range(epochs):
    dw,db = 0,0
    errors.append(error(w,b,X,Y))
    for x,y in zip(X,Y):
      dw+=grad_w(w - gamma * prev_v_w,b - gamma * prev_v_b,x,y)
      db+=grad_b(w - gamma * prev_v_w,b - gamma * prev_v_b,x,y)
    v_w = gamma * prev_v_w + lr*dw
    v_b= gamma * prev_v_b + lr*db

    w = w - v_w
    b = b - v_b
    prev_v_w = v_w
    prev_v_b = v_b

  print(f"Error after updating weights: {error(w,b,X,Y)} weight : {w} bias : {b} ")

  return errors


list_error = nestrov_gradient_decent()

plts(list_error)


