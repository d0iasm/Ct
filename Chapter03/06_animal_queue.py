import unittest


class Animal(object):
    def __init__(self, type, order, name="hoge", next=None):
        # 0: dog, 1: cat
        self.type = type
        self.order = order
        self.name = name
        self.next = next


class AnimalQueue(object):
    def __init__(self):
        self.dogs = None
        self.cats = None
        self.order = 0

    def enqueue(self, type, name="hoge"):
        animal = Animal(type, self.order, name)
        self.order += 1

        if type == 0:
            animal.next = self.dogs
            self.dogs = animal
        else:
            animal.next = self.cats
            self.cats = animal

    def dequeue_any(self):
        if self.dogs is None:
            return self.dequeue_cat()
        if self.cats is None:
            return self.dequeue_dog()

        dog = self.dogs
        dog_prev = dog
        while dog.next:
            dog_prev = dog
            dog = dog.next
        
        cat = self.cats
        cat_prev = cat
        while cat.next:
            cat_prev = cat
            cat = cat.next

        if dog.order < cat.order:
            dog_prev.next = None
            if dog is dog_prev:
                self.dogs = None
            return dog
        else:
            cat_prev.next = None
            if cat is cat_prev:
                self.cats = None
            return cat

    def dequeue_dog(self):
        dog = self.dogs
        if dog is None:
            return None
        prev = dog
        while dog.next:
            prev = dog
            dog = dog.next
        if prev is not None:
            prev.next = None
        if prev is dog:
            self.dogs = None
        return dog

    def dequeue_cat(self):
        cat = self.cats
        if cat is None:
            return None
        prev = cat
        while cat.next:
            prev = cat
            cat = cat.next
        if prev is not None:
            prev.next = None
        if prev is cat:
            self.cats = None
        return cat


class Test(unittest.TestCase):
    def test_animal_queue(self):
        animal_queue = AnimalQueue()
        animal_queue.enqueue(0, "dog1")
        animal_queue.enqueue(1, "cat1")
        animal_queue.enqueue(0, "dog2")

        self.assertEqual("dog1", animal_queue.dequeue_any().name)
        self.assertEqual("cat1", animal_queue.dequeue_any().name)
        self.assertEqual("dog2", animal_queue.dequeue_any().name)
        self.assertIsNone(animal_queue.dequeue_any())
        
    def test_animal_queue_alldogs(self):
        animal_queue = AnimalQueue()
        animal_queue.enqueue(0, "dog1")
        animal_queue.enqueue(0, "dog2")
        animal_queue.enqueue(0, "dog3")

        self.assertEqual("dog1", animal_queue.dequeue_any().name)
        self.assertEqual("dog2", animal_queue.dequeue_any().name)
        self.assertEqual("dog3", animal_queue.dequeue_any().name)
        self.assertIsNone(animal_queue.dequeue_any())

    def test_animal_queue_dequeue_dogs(self):
        animal_queue = AnimalQueue()
        animal_queue.enqueue(0, "dog1")
        animal_queue.enqueue(1, "cat1")
        animal_queue.enqueue(0, "dog2")

        self.assertEqual("dog1", animal_queue.dequeue_dog().name)
        self.assertEqual("dog2", animal_queue.dequeue_dog().name)
        self.assertIsNone(animal_queue.dequeue_dog())

    def test_animal_queue_dequeue_mix(self):
        animal_queue = AnimalQueue()
        animal_queue.enqueue(0, "dog1")
        animal_queue.enqueue(1, "cat1")
        animal_queue.enqueue(0, "dog2")

        self.assertEqual("cat1", animal_queue.dequeue_cat().name)
        self.assertEqual("dog1", animal_queue.dequeue_dog().name)
        self.assertEqual("dog2", animal_queue.dequeue_any().name)
        self.assertIsNone(animal_queue.dequeue_dog())


if __name__ == '__main__':
    unittest.main()
