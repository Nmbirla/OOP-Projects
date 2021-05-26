# OOP-Projects
Object Oriented Programming (OOP) Projects:
1. Blackjack Simulator
  Create a Blackjack game model that has options for Hit, and Stand.
  Use 6 decks, and run until the shoe ( 6 decks all together ) gets to 52 cards or less, then reshuffle.
  Part 1 - Create the blackjack classes so you can play.

  Part 2 - Write unit tests to ensure your classes work.

  Part 3 - Run 100,000 simulations to build a strategy sheet like ( do this by tracking how often a given starting hand is dealt, and take the various actions and record results ) https://en.wikipedia.org/wiki/Blackjack#Basic_strategy


2. Maze Solver
  Backtracking Maze Solver program.

  Create a maze class that accepts a 2d list as the 'maze' to solve.

  Use backtracking recursion to solve the maze.

3. Unloading and Merchandise Delivery
  Unloading Merchandise and Delivery (UMD) is in carge of loading air planes and trains from containers that have been unloaded from ships. The material from the dock is stacked (up to 5 containers high) if it to be sent by train. The materials destined to be sent by planes are unpacked and placed on an assembly line. Each item is labeled either a train number or plane number (which is its destination). Items destined for trains are placed in a stack until it reaches 5 items high, then a new stack is begun behind the original. Items are planes are placed on a long assembly line (there is only 1 assembly line). You can assume 1 worker is loading trains and 1 worker is loading the planes at the same time. The trains (planes) closer to the dock have the smaller train (plane) numbers Each worker requires 2 minutes x train number to move an item from the dock to a train and return. Each worker required 10 minutes x the plane number to move an item from the dock to a plane and return. Given the order that items are unloaded from the ship, your job is write a program to determine the total time it will take to load all the materials.

  Input
  All input will be from the keyboard. The ﬁrst line of input will be 4 integers (t,p and nt and np) (0 <= t < 100, 0 <= p < 10,0 <= nt,0 <= np) (each separated by a single space), which represent the total number of trains , the total number of planes and the total number of to be loaded into trains and the total number of items to be loaded into planes. The second line will contain t integers (again separated by a single space) representing the number of items to be loaded to each train. The third line will contain p integers (again separated by a single space) representing the number of items to be loaded to each plane. The fourth line will contain nt representing the destination of each item being sent by a train. The last line will contain np representing the destination of each item being sent by a plane.

  Output
  Output will be on the screen in 2 lines. The ﬁrst line contains nt integers each separated by 1 space. The ith integer represents the time the ith train ﬁnished loading. The second line contains np integers each separated by 1 space. The ith integer represents the time the ith plane ﬁnished loading.

  Sample Input
  3 2 10 5

  2 7 1

  3 2

  2 2 2 1 3 2 2 2 1 2

  2 1 1 2 1

  Corresponding Output
  25 36 3

  65 50

4. Polynomial

  write the implementation for a class of polynomial operations. Your will write the code for: addition, multiplication , differentiation and integration of polynomials. The polynomials will be linked lists of TermNodes

  class TermNode
   exponent : int
   coefficient : float
   next : TermNode
   __eq__(other: TermNode) : bool
   __ne__(other: TermNode) : bool 

  class Polynomial
   _first_node : TermNode 
  __init__( exp, coef ) 
   __add__ (Polynomial) : Polynomial 
   __mul__(Polynomial) : Polynomial
   differentiate() : Polynomial
   integrate() : Polynomial #(with 0 as the constant) 
  __str__ : string # in descending exponential order - clean up anything x^0 
  - coefficient to 2 decimal places 
  __eq__(other: Polynomial ) : bool
  __ne__(other: Polynomial ) : bool

  Examples:

  poly2 = Polynomial(2,3) # makes the polynomial 2.00x^3 
  poly3 = Polynomial(3,4) # makes the polynomial 3.00x^4 
  poly1 = poly2 + poly3; # makes poly1 = 3.00x^4 + 2.00x^3 
  print(poly1) # prints out 3.0x^4 + 2.00x^3 
  poly3 = poly2*poly1 # sets poly3 to 6.00x^7+4.00x^6 
  poly4 = poly3.differentiate() # sets poly4 to 42.00x^6+24.00x^5 
  poly5 = poly1.integrate() # sets poly5 to .60x^5+.50x^4 

