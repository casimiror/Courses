CREATE
(d:Person {name: 'David'}),
(c:Vehicle {name: 'Car'}),
(a:Person {name: 'Alice'}),
(b:Person {name: 'Bob'}),
(dg:Animal {name: 'Dog'}),
(l:Location {name: 'AB street'}),
(cr:Crime {type: 'killing'}),
(d)-[:Participated_in]->(cr)<-[:Used_in]-(c),
(a)-[:Participated_in]->(cr)<-[:Investigated_by]-(b),
(dg)-[:Victim_of]->(cr)<-[:Occurred_at]-(l),
(dg)-[:Murdered_at]->(l)
return *