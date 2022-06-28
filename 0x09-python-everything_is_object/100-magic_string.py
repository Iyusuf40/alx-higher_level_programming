#!/usr/bin/python3
def magic_string():
    magic_string.a = 0 if "a" not in magic_string.__dict__ else (magic_string.a + 1)
    return "BestSchool" if not magic_string.a else "BestSchool, " * magic_string.a + "BestSchool"
