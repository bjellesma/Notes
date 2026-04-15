## General

* When the context window fills up, this is when the AI starts hallucinating. Hallucinating may be when it loses track of what step it's on.
  * Code quality may degrade because it forgets where it is in the steps
  * A good way to guard against that is to compact the conversation when the context window gets large
* You can control context
  * press escape to redirect claude
  * compact the conversation to help claude stay focused. Most AI can auto compact but this can still be useful. For example, if you're about

* There are different locations that you can put your AI files
<img width="1181" height="433" alt="image" src="https://github.com/user-attachments/assets/6867e60d-b1ba-4d19-bd4f-916741b89ec5" />

## Tips

* Max thinking is useful if the task is more complicated. It's not useful to always do that
* When you start a new chat, you may need to be vigilant that claude may decide to regenerate a function because it doesn't have context that it created that function already
* Plan mode is useful so that claude doesn't go off and start coding the wrong this
* If you spin up new agents, they will have their own context windows.
<img width="463" height="428" alt="image" src="https://github.com/user-attachments/assets/e36cb042-ea85-43ee-9393-9bbbaa7e6a16" />
* It's better to keep a running chat for similar tasks rather than to clear and open new chats

## Generating claude.md

* Use your CV when generating a claude.md file
  * It'll understand things like if you're an expert in something, it won't waste tokens explaining something. If you're an expert, it'll try to actually give you a better algorithm.
  * If claude recognizes you as a novice, you can ask it to be more verbose
* When using claude on the web, I can use my user settings for a claude.md like interface 
