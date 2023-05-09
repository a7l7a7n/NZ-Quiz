"""v1_Welcome_screen
This program is the first and hopefully the only version that welcomes the user
for the start of the quiz
"""


# Allows the welcome screen to have characters around the welcome text
def formatter(symbol, text):
    sides = symbol * 5
    formatter_text = f"{sides}, {text}, {sides}"
    top_bottom = symbol * len(formatter_text)
    return f"{top_bottom}\n{formatter_text}\n{top_bottom}"


# Main routine
print(formatter("🥝", "Welcome to The NZ QUIZ for Kiwis"))
print()
