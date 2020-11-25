male(james_potter).
female(lily_potter).
male(harry_potter).
male(lucius_malfoy).
male(draco_malfoy).
male(andre).
male(luis).
female(annie).
parent(james_potter,harry_potter).
parent(lily_potter,harry_potter).
parent(andre,james_potter).
parent(luis,lily_potter).
parent(annie,lucius_malfoy).
parent(lucius_malfoy,draco_malfoy).
father(Parent,Child) :- parent(Parent,Child), male(Parent).
mother(Parent,Child) :- parent(Parent,Child), female(Parent).
grandparent(GrandPa,GrandChi) :- parent(GrandPa,GrandSon), parent(GrandSon,GrandChi).
grandfather(GrandPa,GrandChi) :- grandparent(GrandPa,GrandChi), male(GrandPa).

