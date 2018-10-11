#!/bin/bash
for i in {3..6}
do
  python cli.py --ssport 10${i}0 --kcpport 40${i}0 --vpsip 103.29.68.34 --dest 40${i}0
done

