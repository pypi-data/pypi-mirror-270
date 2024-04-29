def andGate(inputs):
    threshold = 2
    return 1 if sum(inputs) >= threshold else 0

def orGate(inputs):
    threshold = 1
    return 1 if sum(inputs) >= threshold else 0

def notGate(inputs):
    threshold = 1
    return 0 if inputs >= threshold else 1

def norGate(inputs):
    threshold = 1
    return 0 if sum(inputs) >= threshold else 1

inputs = []
inputs.append(int(input("Input 1: ")))
inputs.append(int(input("Input 2: ")))

print("ADD:", andGate(inputs))
print("OR:", orGate(inputs))
print("NOR:", norGate(inputs))
print("NOT:", notGate(inputs[0]))
