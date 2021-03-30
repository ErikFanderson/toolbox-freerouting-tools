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
    export MYPYPATH=$PWD/toolbox_freerouting_tools
else
    export MYPYPATH=$PWD/toolbox_freerouting_tools:$MYPYPATH
fi

# Set TOOLBOX_FREEROUTING_TOOLS_HOME variable
export TOOLBOX_FREEROUTING_TOOLS_HOME=$PWD
