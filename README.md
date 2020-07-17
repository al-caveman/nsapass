# what is `nsapass`?
it's the simplest, most secure, passwords manager that i know of, for these
reasons:

- **minimum segfaults and funny bugs:**  written _entirely_ in python.  you
  can be pretty sure that undefined behaviour due to improper memory access
  is _pretty_ minimum.  in a sense `nsapass` takes advantage of the _many_
  highly skilled python monkeys to ensure that this app does not have funny
  memory bugs.

  sensitive parts concerning encryption, decryption or access to clipboard,
  is entirely offloaded into other external apps of your choice in the
  _true_ spirit of the UNIX philosophy!  by default, the configuration
  makes a _great_ choice by using `scrypt` for encryption and decryption.
  `scrypt` is _super_ hard to bruteforce and other attacks!

- **super _ultra_ easy to audit:**  written in a _single_ python script
  made of _only_ `404` lines of code!  no separate config file.  the
  configs are done in a _sucklessy_ kind of approach where you edit some
  variables in the `nsapass` file itself.

  the passwords database itself is a simple json text file!  of course,
  this entire json file is encrypted, but thanks to the _extreme_
  simplicity of this, you may decrypt it manually to see by _yourself_ how
  simple and awesome and _occam-razory_ this is!

- **flexible:**  yup.  just look at the configs part of `nsapass` file.

- **common sense:** your passwords database never touches the disk in plain
  text form.  i know this is common sense, but i just listed it in case it
  helps lowering your resting heart beat rate, so that hopefully your heart
  attack is postponed.  in a sense `nsapass` also helps in prolonging your
  lifespan.

  also your _password_, which you use to decrypt the passwrods database,
  never goes into `nsapass`.  you just talk to the external
  encryption/decription app of your choice which you use (by default
  `scrypt`).

# alternatives to `nsapass`
i didn't use much alternatives, but recently i've been using `keepassxc`.
it sucks, because, look at their github page.  loads of C++, CMake, C,
Shell, Objective-C++, etc. extreme complexity!

<p align="center">
    <img src="https://github.com/Al-Caveman/nsapass/blob/master/pics/comparision.png">
</p>

how can _you_ know that funny memory bugs don't exist in `keepassxc`!?
would _you_ put _faith_ in keepassxc's devs that their app is free of
segfaults?  _no way!_ no thanks sir! _keep_ your keepass to yourself.
i'm going to rather rely on the _many_ highly skilled monkeys at _python_
by coding an alternative in `404` lines of python code.

to be more exact, i used to use the command `keepassxc-cli` to load
passwords into my clipboard, then paste them manually in password fields as
i want.  i just never liked having fancy browser-integration where
username-password fields get populated automatically by mere press of some
shortcut key.  imo totally not worth the extra complexity.  our passwords
are very _dear_ to us, and the web is like a big toilet full of disease.
just imagine how horrible browsers are?  imagine the javascript?  imagine
the html5?  layers of horror upon horror.  so yeah, brwoser integration?
nothx!

so, yeah, i just used `keepassxc-cli`, and then kept suffering until i
decided to finally write `404` lines of python (i.e. `nsapass`) to end this
misery and it ended.  and now it's _your_ time, do _you_ want to end your
misery too?  it's easy!  just `git clone` this enjoy the taste of liberty!

# how to use?
permanent configs are stored in `nsapass` itself; just edit it.  for
run-time configs run `nsapass -h` and follow along.  you can get further
help from the subcommands by, say, `nsapass get -h`.

# dependencies

- python.
- any encryption/decription app (by default `script`).
- any clipboard management app (by default `xclip`).

# message from founder
despite _all_ my engineering excellence and finesse, i'm still a maximally
humble and a down-to-earth guy.  so, if you like some features, i'd like to
see your patch.  if they it is sensible i'll merge it.  if i like your
idea, i may even implemented it _myself_, by my very own hands, for _free_
and _git commit-pull-merge-push_ it or me _and_ for you!  because i also
care about _you_ and i want _you_ to be happy as well.
