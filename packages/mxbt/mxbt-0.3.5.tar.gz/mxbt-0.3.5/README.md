# mxbt 

Yet another Matrix bot library, built on [matrix-nio](https://github.com/matrix-nio/matrix-nio).

## Feauters

- [x] Simple and powerfull bots creating
- [ ] Custom emojis support
    - [x] Getting
    - [x] Sending
    - [ ] Creating
- [x] Files sending
    - [x] External files
    - [x] Internal files
- [x] Native mentions
- [x] Access to `matrix-nio` features
- [x] Event filters
- [x] Bot modules support
- [ ] Wait for event system
- [ ] Full e2ee support

## Installation

**With pip:**

```sh
$ pip install mxbt
```

**With git and python:**

```sh
$ git clone https://codeberg.org/librehub/mxbt
$ cd mxbt
$ python -m pip install . 
```

## Getting started

More examples [here](examples/) or in [docs](https://librehub.codeberg.page/mxbt/).

```python
from mxbt import Bot, Context, Creds, Filter, Listener
import asyncio

bot = Bot(
    prefix="!",          # Standart command prefix, commands can setup it own prefix
    creds=Creds.from_json_file("credits.json")
)
lr = Listener(bot)

@lr.on_command(prefix="?", aliases=["test", "t"])
@Filter.from_users(['@username:homeserver'])    # Event works only with this senders
async def ctx_echo(ctx: Context) -> None:       # Context object contains main info about event
    await ctx.reply(ctx.body)                   # Reply message to event room

if __name__ == "__main__":
    asyncio.run(lr.start_polling())
```

**credits.json** structure
```json
{
    "homeserver" : "https://matrix.org",
    "user_id" : "user",
    "password" : "password"
}
```

## Built with mxbt

| Project                                               | Description                       |
| :---                                                  | :---                              |
| [sofie](https://codeberg.org/librehub/sofie)          | A simple selfbot                  |
| [cryptomx](https://codeberg.org/librehub/cryptomx)    | A crytpocurrency notification bot | 

## Special thanks

* [simplematrixbotlib](https://codeberg.org/imbev/simplematrixbotlib) for base parts of API, Listener and Callbacks code ideas. 
Code from simplematrixbotlib is included under the terms of the MIT license - Copyright (c) 2021-2023 Isaac Beverly
* [matrix-nio](https://github.com/poljar/matrix-nio) for cool client library.

## Support

Any contacts and crytpocurrency wallets you can find on my [profile page](https://warlock.codeberg.page).


