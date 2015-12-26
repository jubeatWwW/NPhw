#!/bin/sh
ps auxww | grep cwlin | grep python | awk '{print $2}' | xargs kill -9
