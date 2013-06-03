yt.recipe.shell
===============

yt.recipe.shell is a recipe to add shell scripts as executables under the bin folder. E.G.:


    [shell]
    recipe = yt.recipe.shell
    script = echo 'hello world!'
    name = hello

Will generate a 'bin/hello' executable that echos hello world!
