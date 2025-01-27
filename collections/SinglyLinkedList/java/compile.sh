#!/bin/bash
javac -Xlint -d bin ./src/*.java
cd bin
java Main
cd..
