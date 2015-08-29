#!/usr/bin/env python

import sys
from data.foods import foods_cade_can_eat, foods_cade_can_not_eat

if len(sys.argv) != 2:
    sys.stderr.write("usage: python cade_can_eat.py <food>\n")
    sys.exit()

query = sys.argv[1]
if query in foods_cade_can_eat:
    print("Can.")
elif query in foods_cade_can_not_eat:
    print("No can.")
else:
    print("Not sure :/")
