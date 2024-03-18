class PredicateDerivation:
    def __init__(self):
        self.predicates = {}  # Dictionary to store predicates

    def add_predicate(self, subject, predicate):
        """
        Add a predicate to the dictionary
        """
        if subject not in self.predicates:
            self.predicates[subject] = set()  # Initialize set if subject not found
        self.predicates[subject].add(predicate)

    def derive_predicate(self, subject):
        """
        Derive predicate using transitive inference
        """
        if subject not in self.predicates:
            return None  # Subject not found

        derived_predicates = set()  # Initialize set for derived predicates
        stack = list(self.predicates[subject])  # Stack for DFS traversal

        while stack:
            current_predicate = stack.pop()
            derived_predicates.add(current_predicate)
            if current_predicate in self.predicates:
                # Add predicates related to current_predicate to the stack
                stack.extend(self.predicates[current_predicate])

        return derived_predicates

# Example usage:
if __name__ == "__main__":
    # Create an instance of PredicateDerivation
    predicate_derivation = PredicateDerivation()
    # Add predicates
    predicate_derivation.add_predicate("Sachin", "batsman")
    predicate_derivation.add_predicate("batsman", "cricketer")
    # Derive predicate for Sachin
    derived_predicates = predicate_derivation.derive_predicate("Sachin")
    # Print derived predicates
    print("Derived predicates for Sachin:", derived_predicates)
