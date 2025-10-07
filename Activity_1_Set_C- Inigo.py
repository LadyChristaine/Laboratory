print("Task 1")
def count_vowels(v):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in v if ch in vowels)
    return vowel_count

words = input("Enter Words: ")
results = count_vowels(words)
print("Number of Vowels:", results)

print("\n")
print("Task 2")
def make_shirt(size="Large", message="I Love Python"):
    
    print(f"Ordered a {size} shirt with the message: '{message}'.")
make_shirt()

print("\n")
print("Task 3")
def merge_strings(*args):
    return " ".join(args)
   
print(merge_strings("Hello", ",", "sir", "Benedict", "Viba", "Yamat!"))

print("\n")
print("Task 4")
def setup_application(app_name, version, **kwargs):

    config = {
        "app_name": app_name,
        "version": version
    }
    config.update(kwargs)
    return config

result = setup_application("MyApp", "1.0", debug=True, port=3000, environment="production")
print(result)

