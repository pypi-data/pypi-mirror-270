# ------------------------------------------------------------------------------------#
#  Distributed Multidisciplinary Design Optimization - DMDO                           #
#                                                                                     #
#  Author: Ahmed H. Bayoumy                                                           #
#  email: ahmed.bayoumy@mail.mcgill.ca                                                #
#                                                                                     #
#  This program is free software: you can redistribute it and/or modify it under the  #
#  terms of the GNU Lesser General Public License as published by the Free Software   #
#  Foundation, either version 3 of the License, or (at your option) any later         #
#  version.                                                                           #
#                                                                                     #
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY    #
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A    #
#  PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.   #
#                                                                                     #
#  You should have received a copy of the GNU Lesser General Public License along     #
#  with this program. If not, see <http://www.gnu.org/licenses/>.                     #
#                                                                                     #
#  You can find information on simple_mads at                                         #
#  https://github.com/Ahmed-Bayoumy/DMDO                                              #
# ------------------------------------------------------------------------------------#

from .DMDO import USER, MDO, main

from ._globals import *
from ._common import *
from .SP import *
from .MDA import *
from .DA import *
from .preprocess import *

__all__ = ['USER', 'double_precision', 'VAR_TYPE', 'VALIDATOR', 'BARRIER_TYPE', 'PSIZE_UPDATE', 'w_scheme', 'MODEL_TYPE', 'COUPLING_STRENGTH', 'COUPLING_TYPE', 'MDO_ARCHITECTURE', 'variableData', 'Process_data', 'coordinationData', 'coordinator', 'process', 'search', 'DA_Data', 'optimizationData', 'DA', 'MDA_data', 'MDA', 'ADMM', 'ADMM_data', 'partitionedProblemData', 'SubProblem', 'MDO_data', 'MDO', 'problemSetup', 'main']