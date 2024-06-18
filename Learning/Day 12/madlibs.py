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
