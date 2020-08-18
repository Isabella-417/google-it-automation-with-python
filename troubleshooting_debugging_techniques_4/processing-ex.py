#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import subprocess
import os

src = "prod/"
dest= "prod_backup/"
directories = []


def dirList(source):
    return [os.path.join(source, f) for f in os.listdir(source)]

def run(task):
  # Do something with task here
    subprocess.call(['rsync', '-arq', task, dest])


if __name__ == '__main__':

    files_in_dir = dirList(src)
  # Create a pool of specific number of CPUs
    p = Pool(len(files_in_dir))
  # Start each task within the pool
    p.map(run, files_in_dir)

