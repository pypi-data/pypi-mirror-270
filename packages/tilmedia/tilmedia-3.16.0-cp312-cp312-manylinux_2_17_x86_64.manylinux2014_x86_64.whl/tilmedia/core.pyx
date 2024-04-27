from libcpp cimport bool
from libcpp.string cimport string
import numpy as np

ctypedef int (__stdcall* TPrintFormatMessageFunction)(const char* _Format, ...) noexcept
ctypedef int (__stdcall* TCustomErrorMessageFunction)(const char*, int, void*) noexcept


cdef extern from "Message_C.h":

    ctypedef struct CallbackFunctions:
        TPrintFormatMessageFunction ModelicaFormatMessage
        TPrintFormatMessageFunction ModelicaFormatError
        TCustomErrorMessageFunction TILMedia_globalCustomMessageFunction
        void* messageUserData
        const double *time
        char *cacheInstanceName
        int isTopLevelInstance

        int lock_gas
        int lock_liq
        int lock_vle
        int lock_realmixture
        int lock_modelmap
        int lock_ntu
        int lock_modelmap_ntu
        int lock_lic_new
        int lock_AddOnLicenseCheck
        int lock_refprop
        int lock_multiflash

    cdef CallbackFunctions* CallbackFunctions_construct() nogil


include "c_externalobject.pxi"

include "c_batchcaller.pxi"

include "c_general.pxi"

include "c_liquid.pxi"

include "c_gas.pxi"

include "c_vlefluid.pxi"

