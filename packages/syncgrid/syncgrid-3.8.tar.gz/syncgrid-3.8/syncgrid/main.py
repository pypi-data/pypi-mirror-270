"""
NumPy  for data science
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://numpy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `numpy` has been imported as ``np``::

  >>> import numpy as np

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help.  This is
particularly true if you see the line "Help on ufunc object:" at the top
of the help() page.  Ufuncs are implemented in C, not Python, for speed.
The native Python help() does not know how to view their help, but our
np.info() function does.

To search for documents containing a keyword, do::

  >>> np.lookfor('keyword')
  ... # doctest: +SKIP

General-purpose documents like a glossary and help on the basic concepts
of numpy are available under the ``doc`` sub-module::

  >>> from numpy import doc
  >>> help(doc)
  ... # doctest: +SKIP

Available subpackages
---------------------
lib
    Basic functions used by several sub-packages.
random
    Core Random Tools
linalg
    Core Linear Algebra Tools
fft
    Core FFT routines
polynomial
    Polynomial tools
testing
    NumPy testing tools
distutils
    Enhancements to distutils with support for
    Fortran compilers support and more  (for Python <= 3.11).

Utilities
---------
test
    Run numpy unittests
show_config
    Show numpy build configuration
matlib
    Make everything matrices.
__version__
    NumPy version string

Viewing documentation using IPython
-----------------------------------

## Multi threading in JAVA
```
class MultithreadingDemo extends Thread {
	public void run()
	{
		try {
			// Displaying the thread that is running
			System.out.println(
				"Thread " + Thread.currentThread().getId()
				+ " is running");
		}
		catch (Exception e) {
			// Throwing an exception
			System.out.println("Exception is caught");
		}
	}
}

// Main Class
public class Multithread {
	public static void main(String[] args)
	{
		int n = 8; // Number of threads
		for (int i = 0; i < n; i++) {
			MultithreadingDemo object
				= new MultithreadingDemo();
			object.start();
		}
	}
}

```


## Inter process communication Python
### Client Code: 
```
# IPCClient.py
import socket

HOST = 'localhost'
PORT = 1200

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('\n ************* CLIENT PROCESS STARTED ********************** \n')
    print('\n ********* PLEASE ENTER THE VALUES OF Number 1 AND Number 2 TO PASS THEM TO SERVER PROCESS******** \n')

    num1 = input("Enter Number 1: ")
    print(f"Number 1 ====> {num1}")
    s.sendall(num1.encode())

    num2 = input("Enter Number 2: ")
    print(f"Number 2 ====> {num2}")
    s.sendall(num2.encode())

    result = s.recv(1024).decode()
    print('\n CLIENT PROCESS HAS RECEIVED RESULT FROM SERVER. \n')
    print(f"THE ADDITION OF {num1} AND {num2} IS {result}")

print('\n CLIENT PROCESS EXITING \n')

```

### Server code:
```
# IPCServer.py
import socket

HOST = 'localhost'
PORT = 1200

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print('\n **** INTERPROCESS COMMUNICATION ****\n')
    print('\n *** SERVER PROCESS STARTED ***\n')
    print(f'\n * SERVER IS READY AND WAITING TO RECEIVE DATA FROM CLIENT PROCESS ON PORT {PORT}')

    conn, addr = s.accept()
    print(f'\n * Client is connected with IP address {addr[0]} and port Number {addr[1]}')

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            num1 = int(data.decode())
            print('\n SERVER RECEIVED')
            print(f'\n Number 1 ====> {num1}')

            data = conn.recv(1024)
            num2 = int(data.decode())
            print(f'\n Number 2 ====> {num2}')

            result = num1 + num2
            conn.sendall(str(result).encode())
            print(f'\n SERVER PROCESS HAS EXECUTED REQUESTED PROCESS AND SENT RESULT {result} TO THE CLIENT \n')

    print('\n SERVER PROCESS EXITING \n')

```

-------------------------------------------

## 3: Bully Election Algorithm

```
processes = {
    "1":1,
    "2":1,
    "3":1,
    "4":1,
    "5":1
}

coordinator = len(processes)

def election():
  global coordinator
  coordinator=coordinator-1

def crash(process_number):
  processes[process_number]= 0

def recover(process_number):
  processes[process_number]= 1

while(True):
  print("Enter 1:Crash\n 2:recover\n 0:exit\n")
  number = int(input("Enter your choice := \n"))
  if(number==1):
    crashProcessIndex = int(input("Enter process number that you want to crash = "))
    processes[f"{crashProcessIndex}"] = 0
    if(crashProcessIndex==coordinator):
      election()
    print(processes)
    print(f"coordinator = {coordinator}")

  if(number==2):
    recoverProcessIndex = int(input("Enter process number that you want to recover = "))
    processes[f"{recoverProcessIndex}"] = 1
    if(recoverProcessIndex > coordinator):
      coordinator = recoverProcessIndex
    print(processes)
    print(f"coordinator = {coordinator}")

  if(number==0):
    break
```

-----------------------------------
### 7. Load Balancing algorithm

```
def print_load(servers, processes):
    each = processes // servers
    extra = processes % servers
    for i in range(servers):
        total = each + 1 if extra > 0 else each
        extra -= 1 if extra > 0 else 0
        print(f"Server {chr(65 + i)} has {total} Processes")

def main():
    servers, processes = map(int, input("Enter the number of servers and Processes: ").split())
    while True:
        print_load(servers, processes)
        choice = int(input("1. Add Servers 2. Remove Servers 3. Add Processes 4. Remove Processes 5. Exit: "))
        if choice == 1:
            servers += int(input("How many more servers?: "))
        elif choice == 2:
            servers -= int(input("How many servers to remove?: "))
        elif choice == 3:
            processes += int(input("How many more Processes?: "))
        elif choice == 4:
            processes -= int(input("How many Processes to remove?: "))
        elif choice == 5:
            return


if __name__ == "__main__":
    main()
```

-----------------------------------
### 8. Berkley Clock Synchronization

```
from datetime import datetime,timedelta
server_time = datetime.now().time().replace(microsecond=0)
print(server_time)

node1_string_time = input("Enter node 1 time as H:M:S = ")
node1_time = datetime.strptime(node1_string_time, '%H:%M:%S').time()

node2_string_time = input("Enter node 2 time as H:M:S = ")
node2_time = datetime.strptime(node2_string_time, '%H:%M:%S').time()

server_time = datetime.combine(datetime.today(), server_time)
node1_time = datetime.combine(datetime.today(), node1_time)
node2_time = datetime.combine(datetime.today(), node2_time)

node1_difference = int((server_time - node1_time).total_seconds())
node2_difference = int((server_time - node2_time).total_seconds())

print("\ndifference of node1 and server node in seconds = ",node1_difference)
print("difference of node1 and server node in seconds = ",node2_difference)

averageOfDifference = int((node1_difference+node2_difference+0)/3)

print("\nAverage of difference = ",averageOfDifference)

def calculateSecondsForNodeTime(nodes_time):
  hour,minute,seconds = nodes_time.split(":")
  hour = int(hour)*60*60
  minute = int(minute)*60
  seconds = int(seconds)
  return hour+minute+seconds

node1TimeInseconds = calculateSecondsForNodeTime(node1_string_time)
node2TimeInseconds = calculateSecondsForNodeTime(node2_string_time)

node1CorrectedTime = str(timedelta(seconds=(averageOfDifference+node1_difference)+node1TimeInseconds))
node2CorrectedTime = str(timedelta(seconds=(averageOfDifference+node2_difference)+node2TimeInseconds))

print("\nBalanced time")
print(f"node1 time = {node1CorrectedTime}")
print(f"node2 time = {node2CorrectedTime}")
```

-----------------------------------
## 9: Deadlock management

```
def printMatrix(mat):
    for row in mat:
        print(row)

n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))

# Allocation Matrix
print("Enter the Allocation Matrix:")
alloc = []
for i in range(n):
    row = list(map(int, input().split()))
    alloc.append(row)

# Max Matrix
print("Enter the Max Matrix:")
max = []
for i in range(n):
    row = list(map(int, input().split()))
    max.append(row)

# Available Resources
print("Enter the Available matrix:")
avail = list(map(int, input().split()))

print("\nAllocation matrix =")
printMatrix(alloc)

print("\nMax matrix =")
printMatrix(max)

print("\nAvailable matrix =", avail, "\n")

# finish array
finish = [0] * n
ans = [0] * n
ind = 0

need = [[0 for i in range(m)] for i in range(n)]

# calculation of need matrix
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j] - alloc[i][j]

y = 0
for k in range(n):
    for i in range(n):
        if finish[i] == 0:
            flag = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    flag = 1
                    break

            if flag == 0:
                ans[ind] = i
                ind += 1
                for y in range(m):
                    avail[y] += alloc[i][y]
                finish[i] = 1

print("SAFE Sequence is ")

for i in range(n - 1):
    print(" P", ans[i], " ->", sep="", end="")
print(" P", ans[n - 1], sep="")

```
Output: 
```

Enter the number of processes: 5  
Enter the number of resources: 3
Enter the Allocation Matrix:
0 1 0
2 0 0
3 0 0
2 1 1
0 0 2
Enter the Max Matrix:
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3
Enter the Available matrix:
3 3 2

Available matrix = [3, 3, 2]

SAFE Sequence is
 P1 -> P3 -> P4 -> P0 -> P2
```

----------------------------------
## 10. Ring Mutual Exclusion algorithm

### Server code:
```
import socket
import threading

class MutualServer:
    def __init__(self, new_socket):
        self.socket = new_socket

    def run(self):
        try:
            while True:
                message = self.socket.recv(1024).decode()
                print(message)
        except Exception as e:
            print(e)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 7000))
    server_socket.listen(5)
    print("Server Started")
    
    while True:
        client_socket, _ = server_socket.accept()
        server = MutualServer(client_socket)
        server_thread = threading.Thread(target=server.run)
        server_thread.start()

if __name__ == "__main__":
    main()

```

### Client one code
```
import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 7000))
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 7001))
        server_socket.listen(1)
        s1, _ = server_socket.accept()
        
        while True:
            str = "Token"
            if str.lower() == "token":
                print("Do you want to send some data?")
                print("Enter Yes or No")
                str = input().strip()
                if str.lower() == "yes":
                    print("Enter the data")
                    data = input()
                    client_socket.send(data.encode())
                s1.send("Token".encode())

            print("Waiting for Token")
            str = s1.recv(1024).decode()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

```

### client two code:
```
import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 7000))

        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect(('localhost', 7001))

        while True:
            print("Waiting for Token")
            str = s2.recv(1024).decode()
            if str.lower() == "token":
                print("Do you want to send some data?")
                print("Enter Yes or No")
                str = input().strip()
                if str.lower() == "yes":
                    print("Enter the data")
                    data = input()
                    client_socket.send(data.encode())
                s2.send("Token".encode())

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

```

-----------------------------------

Start IPython and import `numpy` usually under the alias ``np``: `import
numpy as np`.  Then, directly past or use the ``%cpaste`` magic to paste
examples into the shell.  To see which functions are available in `numpy`,
type ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use
``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow
down the list.  To view the docstring for a function, use
``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view
the source code).

Copies vs. in-place operation
-----------------------------
Most of the functions in `numpy` return a copy of the array argument
(e.g., `np.sort`).  In-place versions of these functions are often
available as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.
Exceptions to this rule are documented.

"""

def calculateSecondsForNodeTime(nodes_time):
  hour,minute,seconds = nodes_time.split(":")
  hour = int(hour)*60*60
  minute = int(minute)*60
  seconds = int(seconds)
  return hour+minute+seconds
