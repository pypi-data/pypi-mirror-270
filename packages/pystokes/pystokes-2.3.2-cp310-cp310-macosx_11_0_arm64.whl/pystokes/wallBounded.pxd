cimport cython
from libc.math cimport sqrt, exp, pow, erfc, sin, cos
from cython.parallel import prange
import numpy as np
cimport numpy as np
cdef double PI = 3.14159265359

@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class Rbm:

    cdef readonly int Nx, Ny, Nz, N
    cdef readonly np.ndarray Mobility
    cdef readonly double Lx, Ly, Lz, a, facx, facy, facz, eta, mu, muv, mur


    cpdef mobilityTT(self, double [:] v, double [:] r, double [:] F)


    cpdef mobilityTR(   self, double [:] v, double [:] r, double [:] T)


    cpdef propulsionT2s(self, double [:] v, double [:] r, double [:] S)


    cpdef propulsionT3t(self, double [:] v, double [:] r, double [:] D)



    cpdef mobilityRT(self, double [:] o, double [:] r, double [:] F)


    cpdef mobilityRR(self, double [:] o, double [:] r, double [:] T)
    
    cpdef propulsionR2s(self, double [:] o, double [:] r, double [:] S)
    
    cpdef propulsionR3t(self, double [:] o, double [:] r, double [:] D)


    cpdef propulsionR3a(self, double [:] o, double [:] r, double [:] M)


    cpdef propulsionR4a(self, double [:] o, double [:] r, double [:] M)


    cpdef noiseTT_old(self, double [:] v, double [:] r)


    cpdef noiseRR_old(self, double [:] o, double [:] r)
    
    cpdef noiseTT(self, double [:] v, double [:] r)
    
    cpdef noiseTR(self, double [:] v, double [:] r)
    
    cpdef noiseRT(self, double [:] o, double [:] r)
    
    cpdef noiseRR(self, double [:] o, double [:] r)


## Flow at given points
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
@cython.wraparound(False)
cdef class Flow:
    cdef readonly double a, eta
    cdef readonly int Nt, N


    cpdef flowField1s(self, double [:] vv, double [:] rt, double [:] r, double [:] F)

    cpdef flowField2a(  self, double [:] vv, double [:] rt, double [:] r, double [:] T)

    cpdef flowField2s(self, double [:] vv, double [:] rt, double [:] r, double [:] S)

    cpdef flowField3t(self, double [:] vv, double [:] rt, double [:] r, double [:] D)
    

@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.nonecheck(False)
cdef class PD:

    cdef readonly int Nx, Ny, Nz, N
    cdef readonly np.ndarray Mobility
    cdef readonly double Lx, Ly, Lz, a, facx, facy, facz, eta, gammaT, gammaR, mu, muv, mur


    cpdef frictionTT(self, double depsilon, double [:] v, double [:] r)


    cpdef frictionTR(self, double depsilon, double [:] v, double [:] o, double [:] r)


    cpdef frictionT2s(self, double depsilon, double [:] V1s, double [:] S, double [:] r)


    cpdef frictionT3t(self, double depsilon, double [:] V1s, double [:] D, double [:] r)



    cpdef frictionRT(self, double depsilon, double [:]v, double [:] o, double [:] r)


    cpdef frictionRR(self, double depsilon, double [:] o, double [:] r)
