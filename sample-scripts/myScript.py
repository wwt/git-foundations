#! /usr/bin/env python

# This script says hello and requires Python version 3.x
import myFunction as m

def main():

    name = input('What is your name: ')
    print(f'\nWell hello, {name}.  It is nice to meet you.\n')

    upperName = m.myFunction(name)
    print(upperName)

if __name__ == '__main__':
    main()