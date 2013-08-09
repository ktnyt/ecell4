from ecell4.reaction_reader.decorator2 import species_attributes, reaction_rules
from ecell4.reaction_reader.species import generate_reactions

@species_attributes
def attributegen():
    Null()                                       | 1
    gTetR(lac!1,lac!2).pLacI(tet!1).pLacI(tet!2) | 1
    gCI(tet!1,tet!2).pTetR(cI!1).pTetR(cI!2)     | 1
    gLacI(cI!1,cI!2).pCI(lac!1).pCI(lac!2)       | 1
    mTetR()             |          3163
    mCI()               |          6819
    mLacI()             |          129
    pTetR(cI)           |          183453
    pCI(lac)            |          2006198
    pLacI(tet)          |          165670

@reaction_rules
def rulegen():
    gTetR(lac,lac) + pLacI(tet) == gTetR(lac^1,lac).pLacI(tet^1)     |  (c0/Na/V*tF/pF, c1*tF)
    gTetR(lac^_,lac) + pLacI(tet) == gTetR(lac^_,lac^1).pLacI(tet^1) |  (c0/Na/V*tF/pF, c2*tF)
    gTetR(lac,lac) > gTetR(lac,lac) + mTetR()                        |  c3*rF
    gTetR(lac^_) > gTetR(lac^_) + mTetR()                            |  c4*rF
    mTetR() > mTetR() + pTetR(cI)                                    |  c5/rF*pF
    mTetR() + Null() > Null()                                        |  c6
    pTetR(cI) + Null() > Null()                                      |  c7
    #
    gCI(tet,tet) + pTetR(cI) == gCI(tet^1,tet).pTetR(cI^1)           |  (c0/Na/V*tF/pF, c1*tF)
    gCI(tet^_,tet) + pTetR(cI) == gCI(tet^_,tet^1).pTetR(cI^1)       |  (c0/Na/V*tF/pF, c2*tF)
    gCI(tet,tet) > gCI(tet,tet) + mCI()                              |  c3*rF
    gCI(tet^_) > gCI(tet^_) + mCI()                                  |  c4*rF
    mCI() > mCI() + pCI(lac)                                         |  c5/rF*pF
    mCI() + Null() > Null()                                          |  c6
    pCI(lac) + Null() > Null()                                       |  c7
    #
    gLacI(cI,cI) + pCI(lac) == gLacI(cI^1,cI).pCI(lac^1)             |  (c0/Na/V*tF/pF, c1*tF)
    gLacI(cI^_,cI) + pCI(lac) == gLacI(cI^_,cI^1).pCI(lac^1)         |  (c0/Na/V*tF/pF, c2*tF)
    gLacI(cI,cI) > gLacI(cI,cI) + mLacI()                            |  c3*rF
    gLacI(cI^_) > gLacI(cI^_) + mLacI()                              |  c4*rF
    mLacI() > mLacI() + pLacI(tet)                                   |  c5/rF*pF
    mLacI() + Null() > Null()                                        |  c6
    pLacI(tet) + Null() > Null()                                     |  c7

if __name__ == "__main__":
    newseeds = []
    for i, (sp, attr) in enumerate(attributegen()):
        print i, sp, attr
        newseeds.append(sp)
    print ''

    rules = rulegen()
    for i, rr in enumerate(rules):
        print i, rr
    print ''

    generate_reactions(newseeds, rules)

#begin model
#begin parameters
#    Na    6.022e23    # Avogadro's [mol^-1]
#    V      1.4e-15    # Cell volume [L]
#    #
#    c0    1e9         # M^-1 s^-1 
#    c1    224         # s^-1
#    c2    9           # s^-1
#    c3    0.5         # s^-1
#    c4    5e-4        # s^-1
#    c5    0.167       # s^-1
#    c6    ln(2)/120  # s^-1
#    c7    ln(2)/600  # s^-1
#    #
#    tF    1e-4        # telegraph factor
#    rF    1000        # rna factor
#    pF    1000        # protein factor
#end parameters
#
#begin molecule types
#    Null()
#    gTetR(lac,lac)
#    gCI(tet,tet)
#    gLacI(cI,cI)
#    mTetR()
#    mCI()
#    mLacI()
#    pTetR(cI)
#    pCI(lac)
#    pLacI(tet)
#end molecule types
#
#begin seed species
#    Null()                                          1
#    gTetR(lac!1,lac!2).pLacI(tet!1).pLacI(tet!2)    1
#    gCI(tet!1,tet!2).pTetR(cI!1).pTetR(cI!2)        1
#    gLacI(cI!1,cI!2).pCI(lac!1).pCI(lac!2)          1
#    mTetR()                        3163
#    mCI()                          6819
#    mLacI()                        129
#    pTetR(cI)                      183453
#    pCI(lac)                       2006198
#    pLacI(tet)                     165670
#end seed species
#
#begin observables 
#    Molecules    pTetR    pTetR(cI)
#    Molecules    pCI      pCI(lac)
#    Molecules    pLacI    pLacI(tet)
#    Molecules    NULL     Null()
#end observables
#
#begin reaction rules
#    gTetR(lac,lac) + pLacI(tet) <-> gTetR(lac!1,lac).pLacI(tet!1)        c0/Na/V*tF/pF, c1*tF
#    gTetR(lac!+,lac) + pLacI(tet) <-> gTetR(lac!+,lac!1).pLacI(tet!1)    c0/Na/V*tF/pF, c2*tF
#    gTetR(lac,lac) -> gTetR(lac,lac) + mTetR()                           c3*rF
#    gTetR(lac!+) -> gTetR(lac!+) + mTetR()                               c4*rF
#    mTetR() -> mTetR() + pTetR(cI)                                       c5/rF*pF
#    mTetR() + Null() -> Null()                                           c6
#    pTetR(cI) + Null() -> Null()                                         c7
#    #
#    gCI(tet,tet) + pTetR(cI) <-> gCI(tet!1,tet).pTetR(cI!1)              c0/Na/V*tF/pF, c1*tF
#    gCI(tet!+,tet) + pTetR(cI) <-> gCI(tet!+,tet!1).pTetR(cI!1)          c0/Na/V*tF/pF, c2*tF
#    gCI(tet,tet) -> gCI(tet,tet) + mCI()                                 c3*rF
#    gCI(tet!+) -> gCI(tet!+) + mCI()                                     c4*rF
#    mCI() -> mCI() + pCI(lac)                                            c5/rF*pF
#    mCI() + Null() -> Null()                                             c6
#    pCI(lac) + Null() -> Null()                                          c7
#    #
#    gLacI(cI,cI) + pCI(lac) <-> gLacI(cI!1,cI).pCI(lac!1)                c0/Na/V*tF/pF, c1*tF
#    gLacI(cI!+,cI) + pCI(lac) <-> gLacI(cI!+,cI!1).pCI(lac!1)            c0/Na/V*tF/pF, c2*tF
#    gLacI(cI,cI) -> gLacI(cI,cI) + mLacI()                               c3*rF
#    gLacI(cI!+) -> gLacI(cI!+) + mLacI()                                 c4*rF
#    mLacI() -> mLacI() + pLacI(tet)                                      c5/rF*pF
#    mLacI() + Null() -> Null()                                           c6
#    pLacI(tet) + Null() -> Null()                                        c7
#end reaction rules
#end model
#
#generate_network({overwrite=>1})
#simulate({method=>"ode",t_end=>4e4,n_steps=>4e2,verbose=>1,atol=>1e-12,rtol=>1e-12})
##simulate({method=>"pla",t_end=>4e4,n_steps=>4e2,verbose=>1,pla_config=>"fEuler|sb|pre:post|eps=0.03"})
