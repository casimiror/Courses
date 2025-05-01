create 
(D:Person{name:"Dan"}),
(A:Person{name:"Alice"}),
(B:Person{name:"Bob"}),
(C:Person{name:"Carol"}),
(F:Person{name:"Frank"}),
(G:Person{name:"Grace"}),
(H:Person{name:"Hank"}),
(I:Person{name:"Ivy"}),
(D)-[:Married]->(A)-[:Married]->(D),
(D)-[:Parent]->(B)<-[:Parent]-(A),
(D)-[:Parent]->(C)<-[:Parent]-(A),
(D)-[:Parent]->(F)<-[:Parent]-(A),
(F)-[:Married]->(G)-[:Married]->(F),
(F)-[:Parent]->(I)<-[:Parent]-(G),
(F)-[:Parent]->(H)<-[:Parent]-(G)
return * 