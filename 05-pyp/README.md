# pyp

> Easily run Python at the shell

https://github.com/hauntsaninja/pyp

    poetry add pypyp

(Note: package is called `pypyp` not `pyp`)

Provides a command-line application `pyp` that can apply python snippets to input files and output the results.

Can iterate over lines in a file by referencing the magic `line` variable:

    type demo1.txt | pyp "len(line)"

Or can apply to the whole array of input lines by referencing the magic `lines` variable:

    type demo1.txt | pyp "len(line)" | pyp "sum(map(int, lines))"

Automatically imports modules you reference, eg:

    dir /B | pyp "pathlib.Path(line).suffix"

In fact, for certain modules like `pathlib`, `math` and a few others, you don't even need to mention the module:

    type demo1.txt | pyp "sqrt(len(line))"

Can filter lines from the output by returning `None`:

    type demo1.txt | pyp "line if 'the' in line else None"

Also has a nice feature to output a script to explain what it is doing:

    pyp --explain "line if 'the' in line else None"

And lots more features - read the github page.

It also lists a number of alternatives like:

* `pyped`
* `mario`
* `xonsh`
* etc...
