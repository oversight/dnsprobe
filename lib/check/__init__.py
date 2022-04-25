from .checkA import CheckA
from .checkAAAA import CheckAAAA
from .checkCAA import CheckCAA
from .checkCNAME import CheckCNAME
from .checkDS import CheckDS
from .checkMX import CheckMX
from .checkNS import CheckNS
from .checkPTR import CheckPTR
from .checkSOA import CheckSOA
from .checkSRV import CheckSRV
from .checkTXT import CheckTXT


CHECKS = {
    'CheckA': CheckA,
    'CheckAAAA': CheckAAAA,
    'CheckCAA': CheckCAA,
    'CheckCNAME': CheckCNAME,
    'CheckDS': CheckDS,
    'CheckMX': CheckMX,
    'CheckNS': CheckNS,
    'CheckPTR': CheckPTR,
    'CheckSOA': CheckSOA,
    'CheckSRV': CheckSRV,
    'CheckTXT': CheckTXT
}
