# Project Chat Bot
Python chat bot (discord.py) that can be invited to a Discord Server by the admin.

Project was based on the this(https://github.com/Habchy/BasicBot/wiki) tutorial by Habchy.

## Features:
Bot can respond to user posts if the admin sets a specific trigger.

The Bot searches every word of the post and responds with a custom response, setup by the admin,
for whatever is the first trigger that it comes across.

## Setting up a trigger:
Anyone in the Discord Server can set up a custom Trigger and a Response.

The user just need to use the set prefix (! for now) and use the addTrigger command.
```
Eg: !addTrigger "Trigger" "Response"
```

Similarly, the user can also remove Triggers using the rmTrigger command.
```
Eg: !rmTrigger "Trigger"
```