"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person:
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
        self.relation=[]

    def add_relationship(self,name,relationship):
        self.relation.append({"Name":name,"Relationship":relationship})

#if _name_ == "_main_":

Jill=Person("Jill",26,"biologist")
Zalika=Person("Zalika",  28, "artis")
John=Person("John", 27, "writer")
Nash=Person("Nash", 34, "chef")

Jill.add_relationship("Zalika","friend")
Jill.add_relationship("John","partner")
Zalika.add_relationship("Jill","friend")
print(Jill.relation)
        
