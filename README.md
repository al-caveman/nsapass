# what is `nsapass`?
it's the simplest, most secure, passwords manager that i know of, for these
reasons:

- **advanced tag-based hierarchical search!**  _only_ minimum typing is
  needed to identify an entry — so fast even a _sloth_ would feel like a
  fox!
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
  made of _only_ about ~`500` lines of code!  no separate config file.  the
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

  also your _password_, which you use to decrypt the passwords database,
  never goes into `nsapass`.  you just talk to the external
  encryption/decryption app of your choice which you use (by default
  `scrypt`).

- **looks pretty:**  look at the beautiful colors!

# alternatives to `nsapass`
i didn't use much alternatives, but recently i've been using `keepassxc`.
it sucks, because, look at their github page.  loads of C++, CMake, C,
Shell, Objective-C++, etc. extreme complexity!

<p align="center">
    <img src="pics/comparision.png">
</p>

how can _you_ know that funny memory bugs don't exist in `keepassxc`!?
would _you_ put _faith_ in keepassxc's devs that their app is free of
segfaults?  _no way!_ no thanks sir! _keep_ your keepass to yourself.
i'm going to rather rely on the _many_ highly skilled monkeys at _python_
by coding an alternative in ~`500` lines of python code.

to be more exact, i used to use the command `keepassxc-cli` to load
passwords into my clipboard, then paste them manually in password fields as
i want.  i just never liked having fancy browser-integration where
username-password fields get populated automatically by mere press of some
shortcut key.  imo totally not worth the extra complexity.  our passwords
are very _dear_ to us, and the web is like a big toilet full of disease.
just imagine how horrible browsers are?  imagine the javascript?  imagine
the html5?  layers of horror upon horror.  so yeah, browser integration?
nothx!

so, yeah, i just used `keepassxc-cli`, and then kept suffering until i
decided to finally write ~`500` lines of python (i.e. `nsapass`) to end this
misery and it ended.  and now it's _your_ time, do _you_ want to end your
misery too?  it's easy!  just `git clone` this enjoy the taste of liberty!

# how to use?

## installation and configuration
permanent configs are stored in `nsapass` itself; just edit it.  for
run-time configs run `nsa -h` and follow along.  you can get further
help from the subcommands by, say, `nsa get -h`.

## general guidelines

1. you're highly encouraged to take advantage of the easy audit-ability of
   `nsapass` by reading it yourself.  
2. then, after reading it, you create your own fork of the thing that
   you've reviewed and hopefully use it forever.
3. if at any point you wish to update your version to take advantage of new
   changes in upstream, you should go back to step (1) again.  but, again,
   since `nsapass` is small, written in an easy language (python), such
   audit is simple.

this auditing is really worth it.  would you blindly trust the developers
of your passwords manager?  fortunately you don't have to with `nsapass`,
so don't blindly trust when you can verify.

to speed up your auditing, you may start reading `nsapass` from near the
end where it says `# part where stuff start happening`.  from there, you
will see the functions that it uses, and which values are passed to them,
and move forward.

all the `nsapass` commands keep reusing of the same basic functions over
and over.  so, once you review the functionality of a single `nsapass`
command, such as, say, `nsa get`, you will not see much new functions
for the other commands.

<p align="center">
    <img src="pics/screenshotconfigs.png">
</p>

# mini tutorial
let's create a passwords database with a new entry!
<p align="center">
    <img
    src="pics/screenshot_1.png">
</p>

that's _so_ pretty indeed.  let's repeat with `-z` flag to see the
passwords with _even_ more colors!
<p align="center">
    <img
    src="pics/screenshot_z_1.png">
</p>

oh boy it gets even better!  let's add a _super_ secure generated pass
shall we?
<p align="center">
    <img
    src="pics/screenshot_2.png">
</p>

let's see how _that_ looks under `-z`!
<p align="center">
    <img
    src="pics/screenshot_z_2.png">
</p>

mkay, that's so _much_ fun already.  how about list what we've done to see
what _beauty_ we have just crafted?
<p align="center">
    <img
    src="pics/screenshot_3.png">
</p>

aand all the way with the `-z`, too!
<p align="center">
    <img
    src="pics/screenshot_z_3.png">
</p>

let's load a password into clipboard to use it!
<p align="center">
    <img
    src="pics/screenshot_4.png">
</p>

wow!  did you just see how _smart_ the search is?  you don't _need_ to type
full tags!  suffices to _minimally_ type tag _parts_ until one entry is
unique!  _`-z`eeee_ it!

<p align="center">
    <img
    src="pics/screenshot_z_4.png">
</p>

moar commands await you! this is just the _beginning_!
<p align="center">
    <img
    src="pics/morecommands.png">
</p>

# dependencies

- python.
- any encryption/decryption app (by default
  [`scrypt`](https://github.com/Tarsnap/scrypt)).
- any clipboard management app (by default
  [`xclip`](https://github.com/astrand/xclip)).

# message from founder
despite _all_ my engineering excellence and finesse, i'm still a maximally
humble and a down-to-earth guy.  so, if you like some features, i'd like to
see your patch.  if they it is sensible i'll merge it.  if i like your
idea, i may even implemented it _myself_, by my very own hands, for _free_
and _git commit-pull-merge-push_ it or me _and_ for you!  because i also
care about _you_ and i want _you_ to be happy as well.
