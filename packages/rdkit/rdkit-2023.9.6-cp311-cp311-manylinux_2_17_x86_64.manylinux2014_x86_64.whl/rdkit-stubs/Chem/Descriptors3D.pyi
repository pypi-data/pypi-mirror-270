"""
 Descriptors derived from a molecule's 3D structure

"""
from __future__ import annotations
from rdkit.Chem.Descriptors import _isCallable
from rdkit.Chem import rdMolDescriptors
__all__ = ['CalcMolDescriptors3D', 'descList', 'rdMolDescriptors']
def CalcMolDescriptors3D(mol, confId = None):
    """
    
        Compute all 3D descriptors of a molecule
        
        Arguments:
        - mol: the molecule to work with
        - confId: conformer ID to work with. If not specified the default (-1) is used
        
        Return:
        
        dict
            A dictionary with decriptor names as keys and the descriptor values as values
    
        raises a ValueError 
            If the molecule does not have conformers
        
    """
def _setupDescriptors(namespace):
    ...
descList: list  # value = [('PMI1', <function <lambda> at 0x7fe7476bb1a0>), ('PMI2', <function <lambda> at 0x7fe738569580>), ('PMI3', <function <lambda> at 0x7fe7385696c0>), ('NPR1', <function <lambda> at 0x7fe738569760>), ('NPR2', <function <lambda> at 0x7fe738569800>), ('RadiusOfGyration', <function <lambda> at 0x7fe7385698a0>), ('InertialShapeFactor', <function <lambda> at 0x7fe738569940>), ('Eccentricity', <function <lambda> at 0x7fe7385699e0>), ('Asphericity', <function <lambda> at 0x7fe738569a80>), ('SpherocityIndex', <function <lambda> at 0x7fe738569b20>), ('PBF', <function <lambda> at 0x7fe738569bc0>)]
