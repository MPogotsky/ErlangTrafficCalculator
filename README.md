# ErlangTrafficCalculator
A program for determining the blocking factor in systems with loss of messages described by the Erlang model.

# Basic concepts
**Erlang model** - stochnistic model used for traffic analysis in queuing systems.
The model allows you to estimate the probability (or factor) of a lock, a situation where the client can not be served at the given parameters of the model.

The program uses a recursive formula to calculate the lock factor:

![image](https://user-images.githubusercontent.com/60144533/140714471-1c885024-bb55-4d85-b664-98b58b41cb62.png)

Where:
* P(A,N) - probability of blockage
* A - is a number representing the average traffic value (in Erlang).
* N - is the number of channels.

# Model assumptions
* Independent generation of requests by sources (subscribers do not decide that they will call together at a fixed time),
* Request handling time (e.g. phone call) is exponential,
* The service is FIFO (first in first out) – requests are handled in the order they arrive.

Literature:
1. [EN] Wikipedia.org, Erlang(unit): Erlang B formula, from 23.09.2021.
    https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_B_formula
2. [PL] Wikipedia.org, Model Erlanga: Model Erlang B, from 07.07.2018.
    https://pl.wikipedia.org/wiki/Model_Erlanga
