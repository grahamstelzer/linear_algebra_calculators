The general goal is to write things that the user can customize and find relevant information
based on differing vector spaces, inner products etc. Ex. A calculator online might give the
result of a dot product, but the user may want to see what is actually getting multiplied
together.


=======================
Gram-Schmidt process:==
=======================

Methodology is to build classes for different vector spaces that are customizable. The user
should be able to specify a vector space and inner product which will carry out slightly
different GS processes for different vector spaces.

Unfinished work:
- need other vector spaces for C, R, M
- need to implement other inner products, but currently I am trying to figure out if it would
be easier to write different inner product classes or just have a single modifiable one.
- need to implement the GS process for the other vector spaces


========================
Orthog_proj_calculator:=
========================
Simple calculator that takes in a vector and a basis and returns the orthogonal projection of
the vector onto the basis.