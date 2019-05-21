import tensorflow as tf

# tf.get_default_graph() 함수를 사용하여 디폴트그래프 객체를 참조하여 접근하고
# 편의상 변수 graph로 사용, 단 graph 구성이 바뀐다면 이코드를 다시실행해줘야합니다.
graph = tf.get_default_graph()
print(graph)

#그래프 객체는 tf.Graph 클래스의 인스턴스 (객체)입니다.
print(isinstance(graph,tf.Graph))

# 그래프 객체에 대한 프로토콜 버퍼를 출력해볼수있습니다.
# 프로토컬 버퍼에는 그래프 객체에 추가되어있는 모든 오퍼레이션의 정보가 포함되어 있습니다.

print(graph.as_graph_def()) #현재는 그래프에 추가된 노드가없기 대문에 프로토콜 버전만 출력됩니다.

print(type(graph.as_graph_def()))

# 새로운 오퍼레이션 객체를 생성하는 함수를 호출하면
tensor_a = tf.constant('안녕하세여',name="Hi")
tensor_b = tf.constant(1234,name="nuber")
#디폴트 그래프객체에 오퍼레이션 객체가 추가됩니다 [] -> [오퍼레이션 값s]
print(graph.get_operations())

print(graph.as_graph_def())


print("tensor_a.op ==\n",tensor_a.op.node_def)

print(id(tensor_a.op.outputs[0]))
print(id(tensor_a))