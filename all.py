{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d6cac71",
   "metadata": {},
   "outputs": [],
   "source": [
    "l = ['a',6,9.15]\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b048dc9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2 = list (l)\n",
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e672e841",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks = [38, 98, 55, 86, 75, 49]\n",
    "marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46b2676c",
   "metadata": {},
   "outputs": [],
   "source": [
    "copy_marks=list(marks)\n",
    "copy_marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfa54fb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "list('Ramanujam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9a2f897",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee= ['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha']\n",
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ae90d02",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee.append('Vishnu')\n",
    "print(employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7534033",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee.insert(3, 'Sunil')\n",
    "print(employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5737b93e",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36822f96",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee[5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dd0fb3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee[0]= 'Sudheer'\n",
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a14e37b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee[3]= 'Sapna'\n",
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff0c6857",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee[0]= 'Sudheer'\n",
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5831b36",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary=[25000, 51000, 45000, 26000, 60000, 85000, 49000, 68000, 77000, 82000, 100000]\n",
    "emp_salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "551721ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary[1: ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56a61cdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary[ :8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8476b515",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary [1:11]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e8dbf36",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary = emp_salary +[28000]\n",
    "emp_salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bdc9721",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_salary *2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6f223de0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==========================================================================================\n",
      "                           Niraj Mishra                    \n",
      "==========================================================================================\n"
     ]
    }
   ],
   "source": [
    "print('=' * 90)\n",
    "print('                           Niraj Mishra                    ')\n",
    "print('=' * 90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d71ff1e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks = [88, 68, 48, 52, 48, 74, 55, 78, 74, 67, 68, 42, 49, 49, 48, 88, 92, 88,74, 55, 68, 58]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "84644ce6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marks.count(68)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0f090a0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marks.index(68)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b20b0b83",
   "metadata": {},
   "outputs": [],
   "source": [
    "employee= ['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "26fb0392",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employee"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0934c475",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha', ['Farhan', 'Sachin']]\n"
     ]
    }
   ],
   "source": [
    "employee.append(['Farhan', 'Sachin'])\n",
    "print(employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a5ffd7a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha', 'Farhan', 'Sachin']\n"
     ]
    }
   ],
   "source": [
    "employee= ['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha']\n",
    "employee.extend(['Farhan', 'Sachin'])\n",
    "print(employee)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ee068765",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ramesh',\n",
       " 'Deepak',\n",
       " 'Rakesh',\n",
       " 'Dhirendra',\n",
       " 'Suraj',\n",
       " 'Minakshi',\n",
       " 'Radha',\n",
       " 'Farhan',\n",
       " 'Sachin']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students = ['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha', 'Farhan', 'Sachin']\n",
    "students"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7dd5a674",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_last =students.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6de96304",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sachin'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_last"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "cf45370e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ramesh',\n",
       " 'Deepak',\n",
       " 'Rakesh',\n",
       " 'Dhirendra',\n",
       " 'Suraj',\n",
       " 'Minakshi',\n",
       " 'Radha',\n",
       " 'Farhan']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b889d29e",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_index =students.pop(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "18babe9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Dhirendra'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "31bb0353",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ramesh', 'Deepak', 'Rakesh', 'Suraj', 'Minakshi', 'Radha', 'Farhan']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d67a9e8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number = [100,101,102,103,104,105,104,106,107,108,109,110,111,112,113]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "72dc261f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 101, 102, 103, 104, 105, 104, 106, 107, 108, 109, 110, 111, 112, 113]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roll_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0f5e66c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number.remove(104)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "864fabc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 101, 102, 103, 105, 104, 106, 107, 108, 109, 110, 111, 112, 113]\n"
     ]
    }
   ],
   "source": [
    "print(roll_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e727d916",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst=[1,2,3,4,5,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d3ac748a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "31cb3f13",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f1b388ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6, 5, 4, 3, 2, 1]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4165ac4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks = [28,37,15,24,36,75,82,14,35,15,72]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e7fe094c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[28, 37, 15, 24, 36, 75, 82, 14, 35, 15, 72]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "cadf0988",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "176ab4ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[14, 15, 15, 24, 28, 35, 36, 37, 72, 75, 82]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e63cb8a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "marks.sort(reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8951f75f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[82, 75, 72, 37, 36, 35, 28, 24, 15, 15, 14]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "marks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "8389abca",
   "metadata": {},
   "outputs": [],
   "source": [
    "li = [1,2,3, 'a', 'b', 'c']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "8230fd14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 'a', 'b', 'c']"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "5aaaa8b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tuples - Tuples is a immutable variable thats mean you can not edit, add, delete "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "0d35b2dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "work_location = ('Bangaluru', 'Noida', 'Chennai', 'Delhi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "5a4d0d6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Bangaluru', 'Noida', 'Chennai', 'Delhi')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d7e507b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(work_location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "57b292e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "work_location = list(work_location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "9d9ab1d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Bangaluru', 'Noida', 'Chennai', 'Delhi']"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "7ccac77b",
   "metadata": {},
   "outputs": [],
   "source": [
    "work_location.append('Hayderabad')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "35ded32b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Bangaluru', 'Noida', 'Chennai', 'Delhi', 'Hayderabad']"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4267f53d",
   "metadata": {},
   "outputs": [],
   "source": [
    "work_location[1] = 'Kolkata'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "4abbeb11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Bangaluru', 'Kolkata', 'Chennai', 'Delhi', 'Hayderabad']"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "51ba3eee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Bangaluru', 'Kolkata', 'Chennai', 'Delhi', 'Hayderabad')"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple(work_location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "9edc896e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(work_location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "008adb86",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Kolkata'"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "752a55c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Delhi'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work_location[-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "0d9852ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Ramesh', 28),\n",
       " ('Deepak', 37),\n",
       " ('Rakesh', 15),\n",
       " ('Dhirendra', 24),\n",
       " ('Suraj', 36),\n",
       " ('Minakshi', 75),\n",
       " ('Radha', 82),\n",
       " ('Farhan', 14),\n",
       " ('Sachin', 35)]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students = ['Ramesh', 'Deepak', 'Rakesh', 'Dhirendra', 'Suraj', 'Minakshi', 'Radha', 'Farhan', 'Sachin']\n",
    "marks = [28,37,15,24,36,75,82,14,35]\n",
    "[*zip(students, marks)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "44a5b60f",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number = set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "372470e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(roll_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "c37fd931",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number.add(120)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "3b659c4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{120}"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roll_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "3a7aba19",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number.add(121)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "c9f6baac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{120, 121}"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roll_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "3936b12e",
   "metadata": {},
   "outputs": [],
   "source": [
    "roll_number = [100,101,102,101,103,104,105,104,106,107,108,109,110,109,111,112,113]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "f3c092a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100,\n",
       " 101,\n",
       " 102,\n",
       " 101,\n",
       " 103,\n",
       " 104,\n",
       " 105,\n",
       " 104,\n",
       " 106,\n",
       " 107,\n",
       " 108,\n",
       " 109,\n",
       " 110,\n",
       " 109,\n",
       " 111,\n",
       " 112,\n",
       " 113]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "roll_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "4782f09a",
   "metadata": {},
   "outputs": [],
   "source": [
    "remove_dups = [100,101,102,101,103,104,105,104,106,107,108,109,110,109,111,112,113]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "c3d59597",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113}"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(remove_dups)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ed509f92",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "9508ed5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "cc70b472",
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "cb21584d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1}"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "566952f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "26f0ced3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2}"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "4dadc6c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "stng = ['Prakash', 'Yash', 'Vinay', 'Vijay', 'Niraj', 'Niraj']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "3547dd3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Niraj', 'Prakash', 'Vijay', 'Vinay', 'Yash'}"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(stng)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "efac6c60",
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [12,14,12,48,14,16,18,16,18,48]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "5d75b2b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{12, 14, 16, 18, 48}"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "e0f7f470",
   "metadata": {},
   "outputs": [],
   "source": [
    "#map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "213e8c28",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cube(y):\n",
    "    return y*y*y\n",
    "lambda_cube = lambda y: y*y*y\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "576bee92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3375"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "db2cdcb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "format_numeric = lambda num: f\"{num:e}\" if isinstance(num, int) else f\"{num:,.2f}\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "664f5e76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Int formatting: 1.000000e+06\n"
     ]
    }
   ],
   "source": [
    "print(\"Int formatting:\", format_numeric(1000000))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "f34f362d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Lambda Functions or Anonymous Functions "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "c9ea582f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Branching if, elif, else"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "57c51f11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "less than 6\n"
     ]
    }
   ],
   "source": [
    "i=5\n",
    "if i<4:\n",
    "    print('less than 4')\n",
    "elif i <6:\n",
    "    print('less than 6')\n",
    "else:\n",
    "    print('6 or more')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "bcec76d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i is the greater than j\n"
     ]
    }
   ],
   "source": [
    "i = 88\n",
    "j = 56\n",
    "if i>j: print('i is the greater than j')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "d02847c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=\n"
     ]
    }
   ],
   "source": [
    "a = 556\n",
    "b=556\n",
    "print(\"A\") if a>b else print(\"=\") if a==b else print (\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "32d79c85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Both conditions are True\n"
     ]
    }
   ],
   "source": [
    "a = 500\n",
    "b = 300\n",
    "c = 200\n",
    "if a > b and c < a:\n",
    "    print(\"Both conditions are True\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "acdf0179",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "At least one of the conditions is True\n"
     ]
    }
   ],
   "source": [
    "a = 500\n",
    "b = 300\n",
    "c = 200\n",
    "if a > b or c < a:\n",
    "    print(\"At least one of the conditions is True\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "a3f02ff7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Above ten,\n",
      "But not above 20.\n"
     ]
    }
   ],
   "source": [
    "x=65\n",
    "if x>60:\n",
    "    print(\"Above ten,\")\n",
    "    if x < 50:\n",
    "        print(\"And also above 20!\")\n",
    "    else:\n",
    "        print(\"But not above 20.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "48e70e6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    " a = True + True + True + 2 - False\n",
    "\n",
    " b = 5*(True) + False\n",
    "\n",
    " print(\"A\") if a > b else print(\"None\") if a == b else print(\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "011d9747",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logging on to geeksforgeeks...\n",
      "All set !\n"
     ]
    }
   ],
   "source": [
    "site = 'gfg'\n",
    "\n",
    "if site == 'gfg':\n",
    "    print('Logging on to geeksforgeeks...')\n",
    "else:\n",
    "    print('retype the URL.')\n",
    "print('All set !')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "e14b5a93",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (Temp/ipykernel_10672/1461022206.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\niraj\\AppData\\Local\\Temp/ipykernel_10672/1461022206.py\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    b = 5*(True) + False\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "a = True + True + True + 2 - False\n",
    "\n",
    " b = 5*(True) + False\n",
    "\n",
    " print(\"A\") if a > b else print(\"None\") if a == b else print(\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "2132a4fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "eec27b78",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fahrenheit(T):\n",
    "    return ((float(9)/5)*T + 32)\n",
    "    \n",
    "def celsius(T):\n",
    "    return(float(5)/9)*(T-32)\n",
    "\n",
    "temp = [0, 22.5, 40, 100]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "1b0eb943",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[32.0, 72.5, 104.0, 212.0]"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "F_temps = list(map(fahrenheit, temp))\n",
    "F_temps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "f0c6421d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.0, 22.5, 40.0, 100.0]"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(celsius, F_temps))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "b2c068ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.0, 22.5, 40.0, 100.0]"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(lambda x: (5.0/9)*(x-32),F_temps))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "69c649fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "fe0934d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "11\n",
      "19\n",
      "33\n",
      "49\n",
      "69\n",
      "88\n",
      "94\n",
      "112\n",
      "159\n",
      "The sum is 159\n"
     ]
    }
   ],
   "source": [
    "number = [5,6,8,14,16,20,19,6,18,47]\n",
    "sum = 0\n",
    "for val in number:\n",
    "    sum = sum+val\n",
    "    print(sum)\n",
    "print(\"The sum is\", sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c4e1820",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop with wlse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "6f798025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "5\n",
      "6\n",
      "No items left\n"
     ]
    }
   ],
   "source": [
    "digits = [0, 5, 6]\n",
    "for i in digits:\n",
    "    print(i)\n",
    "else:\n",
    "    print(\"No items left\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "9840ef63",
   "metadata": {},
   "outputs": [],
   "source": [
    "#while loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "f6d36b1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum 1\n",
      "i 2\n",
      "sum 3\n",
      "i 3\n",
      "sum 6\n",
      "i 4\n",
      "sum 10\n",
      "i 5\n",
      "sum 15\n",
      "i 6\n",
      "sum 21\n",
      "i 7\n",
      "sum 28\n",
      "i 8\n",
      "sum 36\n",
      "i 9\n",
      "sum 45\n",
      "i 10\n",
      "sum 55\n",
      "i 11\n"
     ]
    }
   ],
   "source": [
    "n = 10\n",
    "sum = 0\n",
    "i = 1\n",
    "while i <= n:\n",
    "    sum = sum+i\n",
    "    i = i +1\n",
    "    print('sum', sum)\n",
    "    print('i', i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "72cbb503",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "110\n"
     ]
    }
   ],
   "source": [
    "marks = 100\n",
    "sum = 0\n",
    "x =10\n",
    "\n",
    "\t\n",
    "while x <= marks:\n",
    "\n",
    "    x += 10\n",
    "\n",
    "print (x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "6e2b3edc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "x= [10,20,30,40]\n",
    "\n",
    "\n",
    "for i in x:\n",
    "\n",
    "    if i == 30:\n",
    "\n",
    "        print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "55d01d47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "\t\n",
    "x = [1,2,3,4]\n",
    "\n",
    "for i in x:\n",
    "\n",
    "    if i > 3:\n",
    "\n",
    "        print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "18426a04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(0, 10)\n"
     ]
    }
   ],
   "source": [
    "print(range(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "db4cc8f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "print(list(range(10)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "a1ce2594",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4, 5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "print(list(range(2, 8)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "d40f9292",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n"
     ]
    }
   ],
   "source": [
    "print(list(range(2, 21, 1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "afcba822",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want laptop\n",
      "I want mobile\n",
      "I want redio\n",
      "I want tv\n"
     ]
    }
   ],
   "source": [
    "device = ['laptop', 'mobile', 'redio', 'tv']\n",
    "for i in range(len(device)):\n",
    "    print(\"I want\", device[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "9318a512",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "radio\n",
      "xyz\n",
      "aa\n"
     ]
    }
   ],
   "source": [
    "genre = ['laptop', 'mobile', 'radio', 'tv', 'xyz', 'abc', 'aa', 'bb']\n",
    "\n",
    "for i in range(2, len(genre), 2):\n",
    "\n",
    "        print(genre[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "f86a6e38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[21, 31, 41, 51, 61]\n"
     ]
    }
   ],
   "source": [
    "generate_numbers = [21,31,41,51,61]\n",
    "print(list(range(21, 71, 10)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "f7b20b73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s\n",
      "t\n",
      "r\n"
     ]
    }
   ],
   "source": [
    "for val in \"string\":\n",
    "    if val == \"i\":\n",
    "        break\n",
    "    print(val)     \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "9d0bcc45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for val in [10, 20, 30, 25, 45, 60]:\n",
    "    if val > 25:\n",
    "        break\n",
    "    print(val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "bbfd3b01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s\n",
      "s\n",
      "t\n",
      "t\n",
      "r\n",
      "r\n",
      "g\n",
      "g\n",
      "e\n",
      "e\n",
      "The end\n"
     ]
    }
   ],
   "source": [
    "for val in \"strigexample\":\n",
    "    if val == \"i\":\n",
    "        continue\n",
    "    else:\n",
    "        if val == 'x':\n",
    "            break\n",
    "        print(val)\n",
    "    print(val)\n",
    "    \n",
    "print(\"The end\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea141d36",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
