import pickle
from Class_point2D import Point2D

point1 = Point2D(1,1)
# Сериализация
# data = {'1': (1,2),
#         '2': 'volvo',
#         '3': True,
#         '4': point1}

f = open('point.pkl', 'wb')
pickle.dump(point1, f)
f.close()

# Десериализация

f = open('point.pkl', 'rb')

point_new = pickle.load(f)

print(point1)
print(point_new)

f.close()

