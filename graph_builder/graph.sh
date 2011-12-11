#!/bin/bash
python graph.py
awk '!x[$0]++' graph.dot > graph2.dot
dot -Tpng graph2.dot > graph.png
