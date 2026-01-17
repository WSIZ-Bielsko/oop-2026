from faker import Faker
import sys
from dataclasses import dataclass
from typing import Dict, Any
import time

fake = Faker('pl_PL')

@dataclass(frozen=True)
class UserData:
    user_id: int
    department: str

def get_dict_size(dictionary: Dict) -> int:
    """Oblicza rozmiar słownika w bajtach"""
    return sys.getsizeof(dictionary) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in dictionary.items())

print("=" * 70)
print("TEST 1: Słownik z kluczami typu string (user1, user2, ...)")
print("=" * 70)

dict_string_keys = {}
start_time = time.time()

for i in range(1_000_000):
    key = f"user{i}"
    value = fake.name()
    dict_string_keys[key] = value

creation_time = time.time() - start_time
size_bytes = get_dict_size(dict_string_keys)
size_mb = size_bytes / (1024 * 1024)

print(f"Liczba elementów: {len(dict_string_keys):,}")
print(f"Czas tworzenia: {creation_time:.2f} s")
print(f"Rozmiar w pamięci: {size_bytes:,} bajtów ({size_mb:.2f} MB)")
print(f"Przykładowe dane: {list(dict_string_keys.items())[:3]}")
print()

del dict_string_keys

print("=" * 70)
print("TEST 2: Słownik z kluczami typu tuple (1,2), (3,4), ...")
print("=" * 70)

dict_tuple_keys = {}
start_time = time.time()

for i in range(1_000_000):
    key = (i, i+1)
    value = fake.name()
    dict_tuple_keys[key] = value

creation_time = time.time() - start_time
size_bytes = get_dict_size(dict_tuple_keys)
size_mb = size_bytes / (1024 * 1024)

print(f"Liczba elementów: {len(dict_tuple_keys):,}")
print(f"Czas tworzenia: {creation_time:.2f} s")
print(f"Rozmiar w pamięci: {size_bytes:,} bajtów ({size_mb:.2f} MB)")
print(f"Przykładowe dane: {list(dict_tuple_keys.items())[:3]}")
print()

del dict_tuple_keys

print("=" * 70)
print("TEST 3: Słownik z kluczami typu frozenset {1,2,3}, {4,5,6}, ...")
print("=" * 70)

dict_frozenset_keys = {}
start_time = time.time()

for i in range(1_000_000):
    key = frozenset({i, i+1, i+2})
    value = fake.name()
    dict_frozenset_keys[key] = value

creation_time = time.time() - start_time
size_bytes = get_dict_size(dict_frozenset_keys)
size_mb = size_bytes / (1024 * 1024)

print(f"Liczba elementów: {len(dict_frozenset_keys):,}")
print(f"Czas tworzenia: {creation_time:.2f} s")
print(f"Rozmiar w pamięci: {size_bytes:,} bajtów ({size_mb:.2f} MB)")
print(f"Przykładowe dane: {list(dict_frozenset_keys.items())[:3]}")
print()

del dict_frozenset_keys

print("=" * 70)
print("TEST 4: Słownik z kluczami typu @dataclass (frozen=True)")
print("=" * 70)

dict_dataclass_keys = {}
start_time = time.time()

departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales']

for i in range(1_000_000):
    key = UserData(user_id=i, department=departments[i % len(departments)])
    value = fake.name()
    dict_dataclass_keys[key] = value

creation_time = time.time() - start_time
size_bytes = get_dict_size(dict_dataclass_keys)
size_mb = size_bytes / (1024 * 1024)

print(f"Liczba elementów: {len(dict_dataclass_keys):,}")
print(f"Czas tworzenia: {creation_time:.2f} s")
print(f"Rozmiar w pamięci: {size_bytes:,} bajtów ({size_mb:.2f} MB)")
print(f"Przykładowe dane: {list(dict_dataclass_keys.items())[:3]}")
print()

print("=" * 70)
print("PODSUMOWANIE")
print("=" * 70)
print("Wszystkie testy zakończone pomyślnie!")
print("\nUwaga: Set {1,2,3} nie może być kluczem (unhashable).")
print("Użyto frozenset zamiast set - frozenset jest niezmienny i hashable.")