from setuptools import setup, find_packages

# Define setup parameters for each package
setup_params = [
    {
        "name": "cipher_decipher",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["koushik katakam"],
        "description": "A Spy's Whisper: Encryption & Decryption Of Messages Using Python",
        "long_description": open(r'C:\Users\koush\Downloads\Demo\cipherdecipher_module\cipher-and-decipher\cipherdecipher.md', encoding='utf-8').read()
    },
    {
        "name": "lc_programs",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["Adarsh Reddy"],
        "description": "lc_programs"
    },
    {
        "name": "for_patterns",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["G.Sai Jyothi"]
    },
    {
        "name": "while_patterns",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["G.Sai Jyothi"]
    },
    {
        "name": "sdkm",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["Bhargav Naik"],
        "description": 'sdkm',
        "long_description": open(r'C:\Users\koush\Downloads\Demo\Python-Snake_Game-main\Snake-game\ReadMe.md', encoding='utf-8').read()
    },
    {
        "name": "String_methods",
        "version": "1.0",
        "packages": find_packages(),
        "author": ["Meghana"]
    }
]

# Extract all author names
all_authors = []
for params in setup_params:
    all_authors.extend(params["author"])

# Combine all authors into a single string
combined_author = ', '.join(all_authors)

# Merge setup parameters for all packages
merged_setup_params = {}
for params in setup_params:
    name = params.pop("name")  # Remove 'name' to avoid conflicts
    merged_setup_params[name] = params

# Call setup() function with combined author name, name, and version
setup(name="python_coding_playground", version="1.0 ",author=combined_author, **merged_setup_params)



