# Operating System Sallybus

# Phase 1: OS Fundamentals

- [ ] What is an Operating System?
- [ ] OS Goals and Responsibilities
- [ ] Kernel vs User Space
- [ ] System Programs
- [ ] System Calls
- [ ] OS Structures
- [ ] Monolithic Kernel
- [ ] Microkernel
- [ ] Hybrid Kernel
- [ ] Boot Process
- [ ] Interrupts
- [ ] Traps & Exceptions
- [ ] Privileged vs Unprivileged Mode

---

# Phase 2: Processes

- [ ] Program vs Process
- [ ] Process States
- [ ] Process Control Block (PCB)
- [ ] Process Creation
- [ ] Process Termination
- [ ] Parent & Child Processes
- [ ] Process Context
- [ ] Context Switching
- [ ] Inter-Process Communication (IPC)
- [ ] Pipes
- [ ] Signals
- [ ] Shared Memory
- [ ] Message Passing

---

# Phase 3: Threads & Concurrency

- [ ] Process vs Thread
- [ ] User-Level Threads
- [ ] Kernel-Level Threads
- [ ] Multithreading
- [ ] Thread Lifecycle
- [ ] Concurrency vs Parallelism
- [ ] Race Conditions
- [ ] Critical Sections
- [ ] Mutual Exclusion
- [ ] Atomic Operations
- [ ] Locks
- [ ] Mutex
- [ ] Semaphores
- [ ] Condition Variables
- [ ] Monitors
- [ ] Thread Pools

---

# Phase 4: CPU Scheduling

- [ ] Scheduling Concepts
- [ ] Preemptive vs Non-Preemptive Scheduling
- [ ] FCFS
- [ ] SJF
- [ ] SRTF
- [ ] Priority Scheduling
- [ ] Round Robin
- [ ] Multilevel Queue
- [ ] Multilevel Feedback Queue
- [ ] Scheduling Metrics
- [ ] Throughput
- [ ] Turnaround Time
- [ ] Waiting Time
- [ ] Response Time
- [ ] Linux Scheduling Basics

---

# Phase 5: Synchronization

- [ ] Critical-Section Problem
- [ ] Peterson's Algorithm
- [ ] Mutex Synchronization
- [ ] Semaphore Synchronization
- [ ] Producer-Consumer Problem
- [ ] Readers-Writers Problem
- [ ] Dining Philosophers Problem
- [ ] Deadlock vs Starvation
- [ ] Livelock
- [ ] Priority Inversion

---

# Phase 6: Deadlocks

- [ ] What is Deadlock?
- [ ] Four Necessary Conditions
- [ ] Resource Allocation Graph
- [ ] Deadlock Prevention
- [ ] Deadlock Avoidance
- [ ] Banker's Algorithm
- [ ] Deadlock Detection
- [ ] Deadlock Recovery

---

# Phase 7: Memory Management

- [ ] Memory Hierarchy
- [ ] Logical vs Physical Address
- [ ] Address Binding
- [ ] Memory Allocation
- [ ] Contiguous Allocation
- [ ] Fragmentation
- [ ] Internal Fragmentation
- [ ] External Fragmentation
- [ ] Paging
- [ ] Page Tables
- [ ] Multilevel Page Tables
- [ ] Translation Lookaside Buffer (TLB)
- [ ] Segmentation
- [ ] Segmentation with Paging

---

# Phase 8: Virtual Memory

- [ ] Virtual Memory
- [ ] Demand Paging
- [ ] Page Faults
- [ ] Page Replacement
- [ ] FIFO
- [ ] Optimal Page Replacement
- [ ] LRU
- [ ] Clock Algorithm
- [ ] Thrashing
- [ ] Working Set
- [ ] Copy-on-Write
- [ ] Memory-Mapped Files

---

# Phase 9: File Systems

- [ ] File Concepts
- [ ] File Attributes
- [ ] File Operations
- [ ] File Descriptors
- [ ] Directory Structures
- [ ] File Allocation
- [ ] Inodes
- [ ] Hard Links
- [ ] Symbolic Links
- [ ] File Permissions
- [ ] Mounting
- [ ] Journaling
- [ ] Virtual File System (VFS)

---

# Phase 10: Storage & I/O

- [ ] I/O Hardware
- [ ] Device Controllers
- [ ] Device Drivers
- [ ] Interrupt-Driven I/O
- [ ] Direct Memory Access (DMA)
- [ ] Buffering
- [ ] Caching
- [ ] Spooling
- [ ] HDD Architecture
- [ ] SSD Architecture
- [ ] Disk Scheduling
- [ ] Storage Performance

---

# Phase 11: Linux & Practical OS Engineering

- [ ] Linux Architecture
- [ ] Linux Shell & CLI
- [ ] Processes in Linux
- [ ] Threads in Linux
- [ ] fork()
- [ ] exec()
- [ ] wait()
- [ ] Signals
- [ ] File Descriptors
- [ ] Pipes
- [ ] /proc
- [ ] /sys
- [ ] Linux Permissions
- [ ] Users & Groups
- [ ] Environment Variables
- [ ] Linux Services
- [ ] Process Monitoring
- [ ] Resource Monitoring
- [ ] ps
- [ ] top / htop
- [ ] lsof
- [ ] strace
- [ ] df
- [ ] du
- [ ] free

---

# Phase 12: Security & Protection

- [ ] Authentication vs Authorization
- [ ] Protection Domains
- [ ] Access Control
- [ ] File Permissions
- [ ] Privilege Separation
- [ ] Least Privilege
- [ ] Sandboxing
- [ ] Process Isolation
- [ ] Memory Protection
- [ ] Kernel Security
- [ ] OS-Level Attack Surfaces

---

# Phase 13: Advanced OS Concepts

- [ ] Kernel Architecture
- [ ] System Call Path
- [ ] Interrupt Handling
- [ ] Context Switching Internals
- [ ] CPU Cache
- [ ] Memory Locality
- [ ] NUMA Basics
- [ ] Multicore Systems
- [ ] CPU Affinity
- [ ] Kernel Scheduling
- [ ] Virtualization
- [ ] Containers
- [ ] Linux Namespaces
- [ ] cgroups
- [ ] Container Isolation
- [ ] OS Interaction with Docker

---

# Phase 14: OS + Backend Engineering

- [ ] How Node.js Uses the OS
- [ ] Event Loop vs OS Threads
- [ ] Async I/O
- [ ] File I/O
- [ ] Network Sockets
- [ ] Connection Handling
- [ ] Process Management
- [ ] Worker Threads
- [ ] Child Processes
- [ ] Memory Usage
- [ ] CPU Usage
- [ ] Backpressure
- [ ] Resource Limits

---

# Phase 15: OS + Performance Engineering

- [ ] CPU Bottlenecks
- [ ] Memory Bottlenecks
- [ ] I/O Bottlenecks
- [ ] Disk Bottlenecks
- [ ] Network Bottlenecks
- [ ] Context-Switch Overhead
- [ ] CPU Cache Effects
- [ ] Memory Leaks
- [ ] CPU Profiling
- [ ] Memory Profiling
- [ ] Performance Monitoring
- [ ] Benchmarking

---

# Phase 16: Practical OS Projects

- [ ] Build a Linux Process Monitor
- [ ] Build a Mini Shell
- [ ] Implement Producer-Consumer
- [ ] Implement a Thread Pool
- [ ] Implement an IPC Example
- [ ] Experiment with Process Scheduling
- [ ] Experiment with Page Replacement
- [ ] Explore Linux /proc
- [ ] Debug a Process with strace
- [ ] Analyze CPU Bottlenecks
- [ ] Analyze Memory Bottlenecks
- [ ] Analyze I/O Bottlenecks
- [ ] Run and Analyze Docker Containers

---

# Phase 17: Senior Engineer Understanding

- [ ] Explain what happens when a program starts
- [ ] Explain what happens during a system call
- [ ] Explain context switching
- [ ] Explain process vs thread trade-offs
- [ ] Explain concurrency vs parallelism
- [ ] Diagnose race conditions
- [ ] Diagnose deadlocks
- [ ] Explain virtual memory
- [ ] Explain page faults
- [ ] Explain file descriptors
- [ ] Explain how Linux manages processes
- [ ] Explain how Docker uses OS primitives
- [ ] Diagnose CPU bottlenecks
- [ ] Diagnose memory bottlenecks
- [ ] Diagnose I/O bottlenecks
- [ ] Connect OS concepts to backend systems
- [ ] Connect OS concepts to distributed systems

---

#  Highest-Priority Topics

If time is limited, prioritize these:

- [ ] Processes & Threads
- [ ] Concurrency & Synchronization
- [ ] CPU Scheduling
- [ ] Memory Management
- [ ] Virtual Memory
- [ ] File Systems
- [ ] I/O & Storage
- [ ] Linux Internals
- [ ] System Calls
- [ ] Kernel vs User Space
- [ ] Virtualization & Containers
- [ ] OS Performance
- [ ] OS + Backend Integration
