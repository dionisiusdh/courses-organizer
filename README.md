# Course Organizer
> Organize college courses plan using Topological Sort and Decrease &amp; Conquer Algorithm

![](https://img.shields.io/badge/Made%20with-Python-blue)

## Author
Dionisius Darryl H. / 13519058 / K02
         
## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [How to use](#how-to-use)

## General info
A python program to organize courses plan using topological sort and decrease &amp; conquer algorithm.
How the algorithm works:
1. Find the vertex with lowest in-degree
2. Split the graph into two sub-section: One is the vertex with the lowest in-degree, and the rest is simply all the other vertex
3. Delete the vertex from the graph and remove all the edges that are corresponding do it
4. Repeat step 2 to 4 until the graph is empty

## Requirements
* Python 3

## How to Use
1. Make sure that you have ```Python``` and its compiler installed
2. Clone this repository into your local computer
3. Run ```main.py``` inside ```./bin/``` directory
4. Input your file name for example ```3``` (without file extension or path). Make sure that the file is in ```./test/``` directory
5. The program will show the corresponding output

## Thank you
