import random

story_with_blanks = """

Once upon a time, there was a(n) [adjective] [noun] who loved to [verb]. Every day, the [noun] would go to the [place] to [verb] with friends. One day, they found a [adjective] [noun] and had the best [noun] ever!

"""
Collected_Words = {
    "adjective": ["funny","shiny"],
    "noun": ["cat","treasure", "day"],
    "Verb": "dance"
}

def madlibs(story, words):
    for key, value in words.items():
        if isinstance(value, list):
            replacement = random.choice(value)
        else:
            replacement = value
        story = story.replace(f"[{key}]".lower(), replacement)
    return story

print(madlibs(story_with_blanks, Collected_Words))

# adj = input("Adjective: ")
# verb1 = input("verb1")

# madlib = f"Once upon a time, there was a(n) {adj} {adj} who loved to {verb1}. Every day, the [noun] would go to the {verb1} to {adj} with friends. One day, they found a {adj} {adj} and had the best {verb1} ever!"

# print(madlib)

