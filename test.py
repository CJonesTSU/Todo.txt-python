# TODO.TXT-CLI-python test script
# Copyright (C) 2011  Sigmavirus24
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# TLDR: This is licensed under the GPLv3. See LICENSE for more details.

# Common functions for test_*_todo.py
import todo
import sys
import re
from os import unlink

todotxt = todo.CONFIG["TODO_FILE"] = "test_todo.txt"
donetxt = todo.CONFIG["DONE_FILE"] = "test_done.txt"

def count_matches(regexp):
	count = 0
	for line in todo.iter_todos():
		if re.match(regexp, line):
			count += 1
	return count


def redirect_stdout():
	sys.stdout = open("/dev/null", "w")


def reset_stdout():
	sys.stdout = sys.__stdout__


def _print(title_string, x, y):
	string = "Test [{function}]: {x} of {y} passed.".format(
			function=title_string, x=x, y=y)
	if x < y:
		string = ''.join([string, " FAILED\n"])
	else:
		string = ''.join([string, " PASSED\n"])
	print(string)


def test_lines(num):
	return ["Test {0}".format(i) for i in range(0, num)]


def create_truncate():
	open(todotxt, "w+").close()
	open(donetxt, "w+").close()

def cleanup():
	unlink(todotxt)
	unlink(donetxt)
