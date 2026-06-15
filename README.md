EcoFriend is a Discord bot created with Python. The purpose of this bot is to help users learn about recycling, eco-friendly habits, environmental challenges, and personal progress in a fun and interactive way.

The bot can classify objects, give approximate decomposition times, share ecological tips, suggest daily challenges, provide craft ideas using reusable materials, and track the user's progress.

FEATURES:

Classifies items for recycling, trash, or e-waste.
Gives approximate decomposition times for different objects.
Sends random eco-friendly tips.
Suggests daily environmental challenges.
Allows users to mark challenges as completed.
Gives ideas for crafts and reusing materials.
Tracks user progress with a simple text-based progress bar.
Commands
!saludo - Greets the user.
!ayuda - Shows the list of available commands.
!reciclar <objeto> - Tells the user where an item should go.
!tiempo <objeto> - Shows the approximate decomposition time of an item.
!tip - Sends a random ecological tip.
!reto - Gives the user an environmental challenge.
!listo - Registers a completed challenge.
!manualidad - Gives a craft or reuse idea.
!progreso - Shows the user's progress.

EXAMPLES:

!saludo
!reciclar botella plastico
!tiempo bateria
!tip
!reto
!listo
!manualidad
!progreso

PROJECT STRUCTURE:

ecofriend-discord-bot/
│
├── main.py
├── eco_logic.py
└── README.md

main.py contains the Discord bot commands and connects the bot to Discord.
eco_logic.py contains the logic used by the bot, such as recycling classification, decomposition times, random tips, challenges, craft ideas, and progress bars.

HOW TO RUN:

First, install the required library:
pip install discord.py
Then add your Discord bot token in the code:
EcoFriend.run("TOKEN_GOES_HERE")
After that, run the bot:
python main.py

If your main file has a different name, use that file name instead. For example:

python app.py
Important Note

The real Discord bot token should not be uploaded to GitHub. For safety, the repository should use a placeholder like this:

EcoFriend.run("TOKEN_GOES_HERE")

LAST BUT NOT LEAST, PURPOSE:

This project was created as part of a programming assignment to practice creating Discord bots, using commands, organizing code into multiple files, and making a useful interactive project.

EcoFriend is designed to encourage users to make better environmental decisions and learn more about how everyday objects affect the planet. I hope you enjoy it. :)
