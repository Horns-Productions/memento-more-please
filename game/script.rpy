# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narinder", color="#333333")
define h = Character("Heket", color="#ff0000")
define s = Character("Shamura", color="#9900ff")
define l = Character("Leshy", color="#009b00")


# The game starts here.

transform midright:
    xalign 0.7

transform midleft:
    xalign 0.3

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show narinder at left

    n "I'm a gayass cat."

    show heket at midleft

    h "Forg"

    show shamura at midright

    s "Shamura moment"

    show leshy at right

    l "AAAAAAAAAAA"

    menu:
        "Who should I breakdance with?"
        "Narinder":
            "I breakdanced with Narinder."
        "Heket":
            "I breakdanced with Heket."
        "Shamura":
            "I breakdanced with Shamura."
        "Leshy":
            "I breakdanced with Leshy."

    "Wahoo."

    # This ends the game.

    return
