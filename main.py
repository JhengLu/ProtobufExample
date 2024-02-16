import addressbook_pb2
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

# The add() function is a method provided by the Protocol Buffers library for Python to add a new element to a repeated field. 
phone_2 = person.phones.add()
phone_2.number = "555-6666"
phone_2.type = addressbook_pb2.Person.PHONE_TYPE_WORK
print(person.phones)

# [number: "555-4321"
# type: PHONE_TYPE_HOME
# , number: "555-6666"
# type: PHONE_TYPE_WORK
# ]