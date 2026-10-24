# Classes
classes = ["Person", "Student", "Professor", "Course"]

# Properties
properties = ["studies", "teaches", "enrolled_in"]

# Individuals
individuals = {
    "Student": ["Arun", "Ravi"],
    "Professor": ["Dr_Kumar"],
    "Course": ["Python", "Java"]
}

print("University Ontology")
print("\nClasses:")
for c in classes:
    print(c)

print("\nProperties:")
for p in properties:
    print(p)

print("\nIndividuals:")
for category, names in individuals.items():
    for name in names:
        print(name, "is a", category)
