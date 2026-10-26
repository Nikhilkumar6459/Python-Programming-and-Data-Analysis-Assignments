"""Basics & Intermediate Python Assignments — worked solutions.
Run this file with Python 3. Uses only the standard library.
"""
from math import factorial
import random

# Assignment 1 — Strings
def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

def is_symmetric(text):
    mid = len(text) // 2
    return text[:mid] == text[(mid if len(text) % 2 == 0 else mid + 1):]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def remove_ith_character(text, i):
    return text[:i] + text[i+1:] if 0 <= i < len(text) else text

def max_of_three(a, b, c):
    return max(a, b, c)

def sum_list(values):
    return sum(values)

def reverse_string(text):
    return text[::-1]

def even_length_words(text):
    return [word for word in text.split() if len(word) % 2 == 0]

def contains_all_vowels(text):
    return set('aeiou').issubset(set(text.lower()))

def matching_characters(a, b):
    return len(set(a) & set(b))

def unique_list(values):
    return list(dict.fromkeys(values))

def is_prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, int(n**0.5) + 1))

def is_perfect(n):
    return n > 1 and sum(d for d in range(1, n) if n % d == 0) == n

# Assignment 2 — fundamentals
def triangle_area(base, height): return base * height / 2
def swap(a, b): return b, a
def random_integer(low=1, high=100): return random.randint(low, high)
def sign(n): return "positive" if n > 0 else "negative" if n < 0 else "zero"
def odd_even(n): return "even" if n % 2 == 0 else "odd"
def is_armstrong(n):
    digits = str(abs(n)); return n >= 0 and sum(int(d)**len(digits) for d in digits) == n
def km_to_miles(km): return km * 0.621371
def celsius_to_fahrenheit(c): return c * 9/5 + 32
def is_leap_year(year): return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
def primes_in_range(start, end): return [n for n in range(start, end+1) if is_prime(n)]
def fibonacci(count):
    a, b, result = 0, 1, []
    for _ in range(max(0, count)): result.append(a); a, b = b, a+b
    return result
def armstrong_in_range(start, end): return [n for n in range(start, end+1) if is_armstrong(n)]
def sum_natural(n): return n*(n+1)//2
def append_items(target, items): target.extend(items); return target
def substring_present(text, sub): return sub in text
def word_frequency(text):
    from collections import Counter
    import re
    return Counter(re.findall(r"\b\w+\b", text.lower()))
def snake_to_pascal(text): return ''.join(part.capitalize() for part in text.split('_'))
def factorial_nonnegative(n):
    if n < 0: raise ValueError("n must be non-negative")
    return factorial(n)
def in_range(n, low, high): return low <= n <= high
def count_case(text):
    return sum(c.isupper() for c in text), sum(c.islower() for c in text)
def remove_duplicate_chars(text): return ''.join(dict.fromkeys(text))
def sorted_hyphen_words(text): return '-'.join(sorted(text.split('-')))
def local_variable_count():
    example = 1
    label = "local"
    return len(locals()) - 1  # exclude the locals() result itself

# Assignment 4 — lists, tuples, sets, dictionaries
def list_sum(xs): return sum(xs)
def list_product(xs):
    result = 1
    for x in xs: result *= x
    return result
def sort_tuples_by_last(xs): return sorted(xs, key=lambda item: item[-1])
def tuple_contains(t, value): return value in t
def set_difference(a, b): return set(a) - set(b)
def dict_sorted_by_value(d, reverse=False): return dict(sorted(d.items(), key=lambda kv: kv[1], reverse=reverse))
def remove_duplicates(xs): return list(dict.fromkeys(xs))
def list_is_empty(xs): return len(xs) == 0
def list_to_tuple(xs): return tuple(xs)
def tuple_remove(t, value): return tuple(x for x in t if x != value)
def tuple_slice(t, start, end): return t[start:end]
def set_is_subset(a, b): return set(a).issubset(set(b))
def number_square_dict(n): return {x: x*x for x in range(1, n+1)}
def merge_dicts(a, b): return {**a, **b}
def largest(xs): return max(xs)
def smallest(xs): return min(xs)
def count_same_first_last(words): return sum(len(w) >= 2 and w[0] == w[-1] for w in words)
def tuple_add(t, item): return t + (item,)
def tuple_to_string(t): return ''.join(map(str, t))
def tuple_copy(t): return tuple(t)
def add_set_members(s, values): s.update(values); return s
def set_intersection(a, b): return set(a) & set(b)
def set_union(a, b): return set(a) | set(b)
def map_lists(keys, values): return dict(zip(keys, values))
def sort_dict_by_key(d): return dict(sorted(d.items()))
def dict_min_max(d): return min(d.values()), max(d.values())
def copy_list(xs): return xs.copy()
def words_longer_than(words, n): return [w for w in words if len(w) > n]
def unzip_tuples(pairs): return tuple(map(list, zip(*pairs))) if pairs else ([], [])
def reverse_tuple(t): return t[::-1]
def tuples_to_dict(pairs): return dict(pairs)
def symmetric_difference(a, b): return set(a) ^ set(b)
def is_superset(a, b): return set(a).issuperset(set(b))
def disjoint(a, b): return set(a).isdisjoint(set(b))
def remove_intersection(a, b): return set(a) - set(b)
def remove_duplicate_dict_values(d): return {k:v for k,v in d.items() if v not in (seen := set()) and not seen.add(v)}
def dict_key_exists(d, key): return key in d
def dict_sum(d): return sum(d.values())
def dict_product(d):
    result=1
    for value in d.values(): result *= value
    return result
def dict_without_key(d, key): return {k:v for k,v in d.items() if k != key}

if __name__ == "__main__":
    print("Palindrome:", is_palindrome("Never odd or even"))
    print("Prime numbers 1-30:", primes_in_range(1, 30))
    print("Fibonacci:", fibonacci(10))
    print("Dictionary squares:", number_square_dict(5))
