import random

# Step 1: Decorator for logging function calls
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Step 2: Class for Random Word Management
class WordManager:
    def __init__(self):
        self.subjects = ['The cat', 'A programmer', 'The elephant', 'An artist', 'The robot']
        self.verbs = ['eats', 'creates', 'jumps over', 'paints', 'analyzes']
        self.objects = ['a sandwich', 'a masterpiece', 'a fence', 'the code', 'the stars']
        self.connectors = ['while', 'because', 'although', 'if', 'whenever']
        self.adjectives = ['quickly', 'gracefully', 'lazily', 'meticulously', 'chaotically']

    @log_calls
    def get_random_subject(self):
        return random.choice(self.subjects)
    
    @log_calls
    def get_random_verb(self):
        return random.choice(self.verbs)

    @log_calls
    def get_random_object(self):
        return random.choice(self.objects)

    @log_calls
    def get_random_connector(self):
        return random.choice(self.connectors)

    @log_calls
    def get_random_adjective(self):
        return random.choice(self.adjectives)

# Step 3: Recursion for Complex Sentence Generation
@log_calls
def generate_sentence_complexity(word_manager, depth=3):
    if depth <= 0:
        # Base case: Simple sentence
        return f"{word_manager.get_random_subject()} {word_manager.get_random_verb()} {word_manager.get_random_object()} {word_manager.get_random_adjective()}."

    # Recursive case: Add complexity
    simple_sentence = generate_sentence_complexity(word_manager, depth - 1)
    return f"{word_manager.get_random_subject()} {word_manager.get_random_verb()} {word_manager.get_random_object()} {word_manager.get_random_connector()} {simple_sentence}"

# Step 4: Functional Programming for Random Sentence
@log_calls
def random_sentence():
    word_manager = WordManager()
    depth = random.randint(1, 5)  # Random complexity depth
    return generate_sentence_complexity(word_manager, depth)

# Step 5: Generate 3 random sentences
if __name__ == "__main__":
    for _ in range(3):
        print(random_sentence())
