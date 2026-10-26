"""Advanced Python assignments: files, dates, regex, exceptions, OOP."""
from pathlib import Path
from datetime import datetime, date, time, timedelta
from collections import Counter
import re, shutil, time as time_module

def read_entire_file(path): return Path(path).read_text(encoding="utf-8")
def file_counts(path):
    text=read_entire_file(path)
    return {"characters":len(text),"words":len(text.split()),"lines":len(text.splitlines())}
def append_and_display(path, text):
    with open(path,"a",encoding="utf-8") as f: f.write(text)
    return read_entire_file(path)
def lines_reversed(path): return [line.rstrip("\n")[::-1] for line in Path(path).read_text(encoding="utf-8").splitlines()]
def first_n_lines(path,n): return Path(path).read_text(encoding="utf-8").splitlines()[:n]
def last_n_lines(path,n): return Path(path).read_text(encoding="utf-8").splitlines()[-n:]
def words_frequency_file(path): return Counter(re.findall(r"\b[\w']+\b",read_entire_file(path).lower()))
def longest_words(path):
    words=re.findall(r"\b\w+\b",read_entire_file(path))
    max_len=max(map(len,words),default=0)
    return [w for w in words if len(w)==max_len]
def copy_file(src,dst): shutil.copyfile(src,dst)
def combine_lines(path1,path2,out):
    a=Path(path1).read_text().splitlines(); b=Path(path2).read_text().splitlines()
    Path(out).write_text("\n".join(f"{x} {y}" for x,y in zip(a,b)),encoding="utf-8")
def remove_newlines(path):
    return Path(path).read_text(encoding="utf-8").replace("\n","")
def current_time(): return datetime.now().strftime("%H:%M:%S")
def current_date_time(): return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def yesterday_today_tomorrow():
    today=date.today()
    return today-timedelta(days=1),today,today+timedelta(days=1)
def time_12_to_24(value): return datetime.strptime(value,"%I:%M %p").strftime("%H:%M")
def date_string_timestamp(value, fmt="%Y-%m-%d"):
    return datetime.strptime(value,fmt).timestamp()
def day_occurrences(year):
    c=Counter(date(year,1,1)+timedelta(days=i) for i in range((date(year+1,1,1)-date(year,1,1)).days))
    return Counter(d.strftime("%A") for d in c.elements())

# Regex practice
def lowercase_underscore_sequences(text): return re.findall(r"\b[a-z]+(?:_[a-z]+)+\b",text)
def only_defined_chars(text, allowed): return all(ch in set(allowed) for ch in text)
def alnum_underscore(text): return bool(re.fullmatch(r"\w+",text))
def remove_duplicate_words(text):
    return " ".join(dict.fromkeys(re.findall(r"\S+",text)))
def keep_letters_numbers(text): return re.sub(r"[^A-Za-z0-9]+","",text)
def char_counts(text):
    return {"uppercase":len(re.findall(r"[A-Z]",text)),"lowercase":len(re.findall(r"[a-z]",text)),
            "digits":len(re.findall(r"\d",text)),"special":len(re.findall(r"[^A-Za-z0-9\s]",text))}
def most_common_number(text):
    nums=re.findall(r"\d+",text); return Counter(nums).most_common(1)[0] if nums else None
def max_number(text):
    nums=[int(x) for x in re.findall(r"\d+",text)]; return max(nums) if nums else None
def split_capitals(text): return re.sub(r"(?<=[a-z])(?=[A-Z])"," ",text)
def same_first_last(text): return bool(text) and text[0]==text[-1]
def uppercase_then_lowercase(text): return re.findall(r"\b[A-Z][a-z]+\b",text)
def ends_alphanumeric(text): return bool(re.search(r"[A-Za-z0-9]$",text))
def starts_vowel(text): return bool(re.match(r"^[aeiouAEIOU]",text))
def starts_substring(text, sub): return text.startswith(sub)
def valid_email(text): return bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text))
def valid_ipv4(text):
    parts=text.split(".")
    return len(parts)==4 and all(p.isdigit() and 0<=int(p)<=255 and (p=="0" or not p.startswith("0")) for p in parts)
def valid_password(text):
    return len(text)>=8 and bool(re.search(r"[A-Z]",text)) and bool(re.search(r"[a-z]",text)) and bool(re.search(r"\d",text)) and bool(re.search(r"[^A-Za-z0-9]",text))
def files_with_extension(folder, ext):
    return [p.name for p in Path(folder).iterdir() if p.is_file() and p.suffix.lower()==ext.lower()]

# Exceptions
def demonstrate_exceptions():
    results=[]
    for fn in [lambda: 1/0, lambda: int("abc"), lambda: [1][4]]:
        try: fn()
        except Exception as e: results.append(type(e).__name__)
    return results

# OOP tasks
class Vehicle:
    def __init__(self, name="", mileage=0, capacity=0): self.name=name; self.mileage=mileage; self.capacity=capacity
    def fare(self): return self.capacity*100
class Bus(Vehicle):
    def fare(self): return self.capacity*110

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id=emp_id; self.emp_name=emp_name; self.emp_salary=emp_salary; self.emp_department=emp_department
    def calculate_emp_salary(self, hours=0):
        return self.emp_salary if hours<=40 else self.emp_salary+(hours-40)*(self.emp_salary/40)*1.5
    def emp_assign_department(self, department): self.emp_department=department
    def print_employee_details(self): return vars(self).copy()

class Restaurant:
    def __init__(self): self.menu_items={}; self.booked_tables=[]; self.customer_orders=[]
    def add_item_to_menu(self,item,price): self.menu_items[item]=price
    def book_tables(self,table_no): self.booked_tables.append(table_no)
    def customer_order(self,item,qty=1): self.customer_orders.append((item,qty))
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number; self.balance=balance; self.date_of_opening=date_of_opening; self.customer_name=customer_name
    def deposit(self,amount):
        if amount<=0: raise ValueError("Amount must be positive")
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=0 or amount>self.balance: raise ValueError("Invalid amount or insufficient funds")
        self.balance-=amount
    def check_balance(self): return self.balance
class Inventory:
    def __init__(self): self.items={}
    def add_item(self,item_id,item_name,stock_count,price): self.items[item_id]={"item_name":item_name,"stock_count":stock_count,"price":price}
    def update_item(self,item_id,stock_count=None,price=None):
        if item_id not in self.items: raise KeyError(item_id)
        if stock_count is not None: self.items[item_id]["stock_count"]=stock_count
        if price is not None: self.items[item_id]["price"]=price
    def check_item_details(self,item_id): return self.items.get(item_id)
