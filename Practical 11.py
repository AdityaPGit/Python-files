# Define predicates
males = ['Rahul', 'Amit', 'Ravi', 'Suresh', 'Vikram', 'Rajesh', 'Anil']  # List of males
females = ['Meera', 'Priya', 'Neha', 'Sita', 'Deepa', 'Rani', 'Geeta']  # List of females

# Define parent relationships as facts (clauses)
parents = [('Rahul', 'Meera'), ('Rahul', 'Priya'), ('Meera', 'Neha'),
           ('Meera', 'Ravi'), ('Amit', 'Priya'), ('Amit', 'Neha'),
           ('Priya', 'Sita'), ('Priya', 'Suresh'), ('Suresh', 'Vikram'),
           ('Suresh', 'Neha'), ('Ravi', 'Deepa'), ('Sita', 'Anil')]

# Define rules for family relationships using predicates and facts
# Rules for father, mother, grandfather, grandmother, brother, sister, uncle, aunt, nephew, niece, cousin

def father(x, y):
    return (x in males) and ((x, y) in parents)

def mother(x, y):
    return (x in females) and ((x, y) in parents)

def grandfather(x, y):
    for z in males:
        if father(x, z) and father(z, y):
            return True
        elif father(x, z) and mother(z, y):
            return True
    return False

def grandmother(x, y):
    for z in females:
        if mother(x, z) and father(z, y):
            return True
        elif mother(x, z) and mother(z, y):
            return True
    return False

def brother(x, y):
    for z in males:
        if (father(z, x) and father(z, y)) or (mother(z, x) and mother(z, y)):
            return True
    return False

def sister(x, y):
    for z in females:
        if (father(z, x) and father(z, y)) or (mother(z, x) and mother(z, y)):
            return True
    return False

def uncle(x, y):
    return (brother(x, z) and (father(z, y) or mother(z, y))) or \
           (husband(x, z) and sister(z, w) and (father(w, y) or mother(w, y)))

def aunt(x, y):
    return (sister(x, z) and (father(z, y) or mother(z, y))) or \
           (wife(x, z) and brother(z, w) and (father(w, y) or mother(w, y)))

def nephew(x, y):
    return (male(y) and (uncle(z, y) or aunt(z, y)))

def niece(x, y):
    return (female(y) and (uncle(z, y) or aunt(z, y)))

def cousin(x, y):
    return (parent(z, x) and parent(w, y) and (brother(z, w) or sister(z, w)))

# Main code for testing the predicates and rules
if __name__ == "__main__":
    # Test the predicates and rules
    print(f"Rahul is a father of Neha: {father('Rahul', 'Neha')}")
    print(f"Meera is a mother of Ravi: {mother('Meera', 'Ravi')}")
    print(f"Suresh is a grandfather of Deepa: {grandfather('Suresh', 'Deepa')}")
    print(f"Meera is a grandmother of Anil: {grandmother('Meera', 'Anil')}")
    print(f"Ravi is a brother of Sita: {brother('Ravi', 'Sita')}")
    print(f"Priya is a sister of Deepa: {sister('Priya', 'Deepa')}")
    # print(f"Amit is an uncle of Deepa: {uncle('Amit', 'Deepa')}")
    # print(f"Meera is an aunt of Anil: {aunt('Meera', 'Anil')}")
    # print(f"Vikram is a nephew of Priya: {nephew('Vikram', 'Priya')}")
    # print(f"Sita is a niece of Neha: {niece('Sita', 'Neha')}")
    # print(f"Neha and Anil are cousins: {cousin('Neha', 'Anil')}")
