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
descList: list  # value = [('PMI1', <function <lambda> at 0xffff9f8f3100>), ('PMI2', <function <lambda> at 0xffff930a54e0>), ('PMI3', <function <lambda> at 0xffff930a5620>), ('NPR1', <function <lambda> at 0xffff930a56c0>), ('NPR2', <function <lambda> at 0xffff930a5760>), ('RadiusOfGyration', <function <lambda> at 0xffff930a5800>), ('InertialShapeFactor', <function <lambda> at 0xffff930a58a0>), ('Eccentricity', <function <lambda> at 0xffff930a5940>), ('Asphericity', <function <lambda> at 0xffff930a59e0>), ('SpherocityIndex', <function <lambda> at 0xffff930a5a80>), ('PBF', <function <lambda> at 0xffff930a5b20>)]
