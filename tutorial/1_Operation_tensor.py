import tensorflow as tf

# 3 * 2 + 1 을 텐서플로우로 계산

# tf.constant 함수를 사용하여 계산에 사용할 값 3개를 위한 오퍼레이션을 생성합니다.
# name 아규먼트의 값은 오퍼레이션을 구분을 위해 붙인 이름입니다.

a = tf.constant(3, name="a")
b = tf.constant(2, name="b")
c = tf.constant(1, name="c")

# 텐서플로우는 계싼을 한번에 하지않고 단계에 나눠서합니다.
d = a * b
e = d + c

# <tf.Operation 'a' type=Const>, <tf.Operation 'b' type=Const>, <tf.Operation 'c' type=Const>, <tf.Operation 'mul' type=Mul>, <tf.Operation 'add' type=Add>]
print(tf.get_default_graph().get_operations())

# Tensor("a:0", shape=(), dtype=int32) shape()인것은 a:0이 상수텐서라는것을 의미한다.
print(a)

# 텐서객체를 출력하는 오퍼레이션에 접근할수있다.
print(a.op)

# a는 오퍼레이션같지만 텐서객체이다. 19번줄에도 Tensor 라고 명시
print(isinstance(a,tf.Operation)) #False
print(isinstance(a.op,tf.Operation)) #True
print(isinstance(a,tf.Tensor)) #True

# a:0 텐서의 이름은 오퍼레이션이름 : 출력텐서인덱스로 구성되어있다.
print(a.name)
# a 아까 name 아규먼트로 설정한값으로 나온다.
print(a.op.name)

#오퍼레이션의 입력값 확인
print(d.op.inputs)
print(d.op.inputs[0])
print(d.op.inputs[1])

print(e.op.inputs[0])
print(e.op.inputs[1])

# 텐서객체(Tf.Tensor)는 오퍼레이션 객체가 실행될때 오퍼레이션 객체간에 전달되는 단위데이터이다.

print("\n\n",d.op)
print(d.op.inputs[0],d.op.inputs[1])
print(a.op.inputs)


