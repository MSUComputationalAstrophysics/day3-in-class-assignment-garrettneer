I think the only way to break the bisection method would be to use a function that never changes sign. For example, the function (x-c)^(2n) has one root at c but never changes sign.
Functions that have divergent derivatives at the root will break Newton's Method (|x^n| where n < 1/2). Apparently, this will break Brent's Method too. It breaks bisection method because it doesn't cross y=0.
I would say that bisection method and Brents method are equally robust. The bisection method is guaranteed to converge if your function crosses y=0 and you choose a range with one root.
Apparently, Newtons Method can get stuck in a saddle point. I spent most of the class trying to do this, but was unsucessful unless you guess the exact value of a local minima. 

