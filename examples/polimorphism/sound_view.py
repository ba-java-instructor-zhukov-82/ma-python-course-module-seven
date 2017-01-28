from examples.polimorphism.bears import Bear
from examples.polimorphism.dogs import Dog
from examples.polimorphism.planes import Plane

for source in [Bear(), Dog(), Plane()]:
    source.sound()
