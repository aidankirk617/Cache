#!/usr/bin/env python3

import fileinput    # Could potentially change this later?

file_name = "trace.dt"

for line in fileinput.input(files = file_name):    # Grabe each line of trace.dt
    print(line)
