#!/usr/bin/env bash

# Set PYTHONPATH accordingly
if [ -z "$PYTHONPATH" ]
then
    export PYTHONPATH=$PWD
else
    export PYTHONPATH=$PWD:$PYTHONPATH
fi

# Set MYPYPATH accordingly
if [ -z "$MYPYPATH" ]
then
    export MYPYPATH=$PWD/toolbox-freerouting-tools
else
    export MYPYPATH=$PWD/toolbox-freerouting-tools:$MYPYPATH
fi

# Set TOOLBOX-FREEROUTING-TOOLS_HOME variable
export TOOLBOX-FREEROUTING-TOOLS_HOME=$PWD
