Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Write a checkpoint that takes under five minutes and survives a cold start. Include: **state, intent, next action, authority record, stop condition**. Test it by giving only the checkpoint to a fresh agent. If the fresh agent cannot take the first correct action without guessing, the checkpoint failed.

FIXTURE:
*(describe your multi-session workstream: what work was done in the prior session, what remains, and what authorization the human operator granted)*
````
