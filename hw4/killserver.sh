#!/bin/sh
ps | grep 'python' | awk '{print $1}' | xargs kill
