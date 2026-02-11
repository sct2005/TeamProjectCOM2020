Alister
Sam
Ollie
Oli
Chase
Ed
Ted
John Ball
MOP

Admin (A)
Curator (C)
Journalist (J)
User (U)

Database (DB)
Main Pages (MP)

(Admin, Admin)
(Admin, Curator)
(Curator, Curator)
(Curator, Journalist)
(Journalist, Journalist)
(Journalist, User)

read_DB
write_DB
read_MP
write_MP

(Alister, Admin)
(Chase, Admin)
(Ollie, Admin)
(Oli, Admin)
(Sam, Admin)
(Ed, Admin)
(John Ball, User)
(MOP, User)

Admin:
  read  → DB
  write → DB
  

Journalist:
  write → MP

User:
  read → MP

Via inhertiance from hierachy:
Admin: read / write → DB , read / write → MP
Curator: read / write → MP
Journalist: read / write → MP
User: read → MP

