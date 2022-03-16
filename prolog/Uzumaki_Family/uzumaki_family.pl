/*
	Basic Artificial Intelligence - HCMUS
		Lab02 - Logic

	exercise 2: prolog
	topic: uzumaki family tree in anime series: "naruto" & "naruto shippuden"
<<<<<<< Updated upstream
=======
	image source: https://www.pinterest.es/pin/631066966525657798/
>>>>>>> Stashed changes
*/


/*gender*/
male(uzumaki_kenta).
male(uzumaki_hayata).
male(uzumaki_ren).
male(uzumaki_sichiro).
male(senju_hashirama).
male(uzumaki_kiku).
male(kesu_miku).
male(senju_shigeko).
male(namikaze_minato).
male(ise).
male(uzumaki_nagato).
male(uzumaki_naruto).
male(kesu_bagheera).
male(nara).
male(senju_nawaki).
male(uzumaki_yuto).

female(akane).
female(araki_kouta).
female(chiko).
female(uzumaki_matami).
female(yuna).
female(uzumaki_mito).
female(yasu).
female(uzumaki_mio).
female(masaru).
female(kesu_mimi).
female(senju_tsunade).
female(uzumaki_mito).
female(uzumaki_kushina).
female(uzumaki_fuso).

/*marital status*/
spouse(akane, uzumaki_kenta).
spouse(uzumaki_kenta, akane).
spouse(uzumaki_hayata, araki_kouta).
spouse(araki_kouta, uzumaki_hayata).
spouse(uzumaki_ren, chiko).
spouse(chiko, uzumaki_ren).
spouse(yuna, uzumaki_sichiro).
spouse(uzumaki_sichiro, yuna).
spouse(uzumaki_mito, senju_hashirama).
spouse(senju_hashirama, uzumaki_mito).
spouse(uzumaki_kiku, yasu).
spouse(yasu, uzumaki_kiku).
spouse(uzumaki_mio, kesu_miku).
spouse(kesu_miku, uzumaki_mio).
spouse(senju_shigeko, masaru).
spouse(masaru, senju_shigeko).
spouse(kesu_mimi, nara).
spouse(nara, kesu_mimi).
spouse(namikaze_minato, uzumaki_kushina).
spouse(uzumaki_kushina, namikaze_minato).
spouse(ise, uzumaki_fuso).
spouse(uzumaki_fuso, ise).

/*parent-child relationship*/
parent(ise, uzumaki_nagoto).
parent(uzumaki_fuso, uzumaki_nagoto).
parent(namikaze_minato, uzumaki_naruto).
parent(uzumaki_kushina, uzumaki_naruto).
parent(yasu, uzumaki_kushina).
parent(uzumaki_kiku, uzumaki_kushina).
parent(chiko, uzumaki_kiku).
parent(uzumaki_ren, uzumaki_kiku).
parent(akane, uzumaki_ren).
parent(uzumaki_kenta, uzumaki_matami).
parent(akane, uzumaki_matami).
parent(uzumaki_matami, uzumaki_mio).
parent(uzumaki_mio, kesu_mimi).
parent(uzumaki_mio, kesu_bagheera).
parent(kesu_miku, kesu_mimi).
parent(kesu_miku, kesu_bagheera).
parent(uzumaki_hayata,uzumaki_sichiro).
parent(uzumaki_hayata, uzumaki_mito).
parent(araki_kouta, uzumaki_sichoro).
parent(araki_kouta, uzumaki_mito).
parent(yuna, uzumaki_yuto).
parent(uzumaki_sichiro, uzumaki_yuto).
parent(uzumaki_yuto, uzumaki_fuso).
parent(uzumaki_yuto, ise).
parent(ise, uzumaki_nagato).
parent(uzumaki_fuso, uzumaki_nagato).
parent(uzumaki_mito, senju_shigeko).
parent(senju_hashirama, senju_shigeko).
parent(senju_shigeko, senju_tsunade).
parent(masaru, senju_tsunade).
parent(senju_shigeko, senju_nawaki).
parent(masaru, senju_nawaki).

/*Rule:*/
/*
GP: grandparent
GM: grandmother
GF: grandfather
GC: grandchild
GS: grandson
GD: granddaughter
P: parent
*/
grandparent(GP,GC) :- parent(GP,P), parent(P,GC).
grandmother(GM,GC) :- grandparent(GM,GC), female(GM).
grandfather(GF,GC) :- grandparent(GF,GC), male(GF).

greatgrandparent(GGP, GGC) :- parent(GGP, GP), grandparent(GP, GGC).
greatgrandfather(GGF, GGC) :- greatgrandparent(GGF, GGC), male(GGF).
greatgrandmother(GGM, GGC) :- greatgrandparent(GGM, GGC), female(GGM).

grandchild(GC,GP) :- grandparent(GP,GC).
grandson(GS,GP) :- grandchild(GS,GP),male(GS).
granddaughter(GD,GP) :- grandchild(GD,GP), female(GD).

greatgrandchild(GGC, GGP) :- greatgrandparent(GGP, GGC).
greatgrandson(GGS, GGP) :- greatgrandparent(GGP, GGS), male(GGS).
greatgranddaughter(GGD, GGP) :- greatgrandparent(GGP, GGD), female(GGD).
/*
P: parent
C: child
Per: person
W: wife
H: husband
*/

husband(Per,W) :- spouse(Per,W), male(Per).
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
wife(Per,H) :- spouse(Per,H), female(Per).

father(P,C) :- male(P), parent(P,C).
fatherinlaw(F, Per) :- father(F, Mate), spouse(Mate, Per).
mother(P,C) :- female(P), parent(P,C).
motherinlaw(M, Per) :- mother(M, Mate), spouse(Mate, Per).

child(C,P) :- parent(P,C).
son(C,P) :- child(C,P), male(C).
soninlaw(C,P) :- child(Mate, P), husband(C, Mate).
daughter(C,P) :- child(C,P), female(C).
daughterinlaw(C, P) :- child(Mate, P), wife(C, Mate).

/*
S: sibling
A: aunt
U: uncle
AU: aunt/uncle
*/
sibling(Per_A, Per_B) :- parent(P, Per_A), parent(P, Per_B), Per_A \= Per_B.
cousin(Per_A, Per_B) :-  parent(P_A, Per_A), parent(P_B, Per_B), sibling(P_A, P_B), Per_A \= Per_B.
siscousin(Per_A, Per_B) :- cousin(Per_A, Per_B), female(Per_A), Per_A \= Per_B.
brocousin(Per_A, Per_B) :- cousin(Per_A, Per_B), male(Per_A), Per_A \= Per_B.

brother(Per, S) :- male(Per), sibling(Per, S).
sister(Per, S) :- female(Per), sibling(Per, S). 

brotherinlaw(Per_A, Per_B) :- sibling(Per_B, Mate), husband(Per_A, Mate).
sisterinlaw(Per_A, Per_B) :- sibling(Per_B, Mate), wife(Per_A, Mate).

aunt(A, Per) :- female(A), sibling(A, P), parent(P, Per).
greataunt(GA, Per) :- grandfather(GF, Per), sister(GA, GF).

uncle(U, Per) :- male(U), sibling(U, P), parent(P, Per).
greatuncle(GU, Per) :- grandfather(GF, Per), brother(GU, GF).

niece(Per, AU) :- female(Per), parent(P, Per), sibling(P, AU).
nephew(Per, AU) :- male(Per), parent(P, Per), sibling(P, AU).
